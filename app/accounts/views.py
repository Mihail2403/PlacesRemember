import requests
from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from social_django.models import UserSocialAuth

from remember.decorators import is_not_admin
from remember.models import Remember
from .models import Image


@is_not_admin
@login_required(login_url="/accounts")
def profile(request):
    """Profile view login required"""
    if request.user.is_staff:
        print(
            "Вам необходимо войти от имени автоирзованного через \
                вк пользователя (не root - выйдете с его аккаунта)"
        )
        return redirect("/admin")

    user = request.user

    # if user has no image in db, get it from VK.com
    img = Image.objects.filter(user=user).first()
    if not img:
        user_social_auth = UserSocialAuth.objects.filter(user=user).first()
        params = {
            "fields": "photo_max",
            "access_token": user_social_auth.access_token,
            "v": 5.131,
        }
        r = requests.get("https://api.vk.com/method/users.get", params=params)
        photo_link = r.json().get("response")[0].get("photo_max")
        img = Image.objects.create(
            user=user,
            img=photo_link,
        )
    remembers = Remember.objects.filter(user=user)
    ctx = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "photo_link": img.img,
        "remembers": remembers,
        "remembers_for_json": serializers.serialize("json", remembers),
    }
    return render(request, "account/profile.html", ctx)


def start(request):
    """Page with btn to auth with VK.com"""
    if request.user.is_authenticated:
        return redirect("profile/")
    return render(request, "account/login.html")


def logout(request):
    auth_logout(request)
    return redirect("/accounts")
