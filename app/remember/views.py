import json
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Remember
from . import forms


@login_required(login_url='/accounts')
def new_remember(request):
    """View creating new remember"""
    if request.user.is_staff:
        print(
            "Вам необходимо войти от имени автоирзованного через \
                вк пользователя (не root - выйдете с его аккаунта)"
        )
        return redirect("/admin")
    if request.method == "POST":
        user = request.user
        form = forms.Remember(request.POST)
        if form.is_valid():
            Remember.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                lat=form.cleaned_data["lat"],
                long=form.cleaned_data["long"],
                user=user,
            )
            return redirect("/accounts/profile")
    else:
        form = forms.Remember()
    return render(request, "remember/new_remember.html", {"form": form})


@login_required(login_url='/accounts')
def full_remember(request, id: int):
    """Full info about the remember"""
    if request.user.is_staff:
        print(
            "Вам необходимо войти от имени автоирзованного через \
                вк пользователя (не root - выйдете с его аккаунта)"
        )
        return redirect("/admin")
    rem = Remember.objects.filter(id=id).values_list()
    if request.method == "POST" and rem:
        user = request.user
        form = forms.Remember(request.POST)
        if form.is_valid():
            rem.update(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                lat=form.cleaned_data["lat"],
                long=form.cleaned_data["long"],
            )
            return redirect("/accounts/profile")
    else:
        form = forms.Remember()
    ctx = {
        "form": form,
        "is_true": len(rem)>0,
        "json_remember": json.dumps(list(rem), ensure_ascii=False)
    }
    return render(request, "remember/full_remember.html", ctx)
