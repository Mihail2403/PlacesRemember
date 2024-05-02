import requests
from django.shortcuts import redirect, render

from social_django.models import UserSocialAuth

from .models import Image


def profile(request):
    """Profile view login required"""
    if not request.user.is_authenticated:
        return redirect("/accounts")

    if request.user.is_staff:
        print(
            "Вам необходимо войти от имени автоирзованного через вк пользователя (не root - выйдете с его аккаунта)"
        )
        return redirect("/admin")

    user = request.user

    # if user has no image in db, get it from VK.com
    if not Image.objects.filter(user=user).first():
        user_social_auth = UserSocialAuth.objects.filter(user=user).first()
        params = {
            "fields": "photo_max",
            "access_token": user_social_auth.access_token,
            "v": 5.131,
        }
        r = requests.get("https://api.vk.com/method/users.get", params=params)
        photo_link = r.json().get("response")[0].get("photo_max")
        Image.objects.create(
            user=user,
            img=photo_link,
        )

    img = Image.objects.get(user=user)
    ctx = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "photo_link": img.img,
    }
    return render(request, "account/profile.html", ctx)


def start(request):
    """Page with btn to auth with VK.com"""
    if request.user.is_authenticated:
        return redirect("profile/")
    return render(request, "account/login.html")
