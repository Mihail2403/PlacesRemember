from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core import serializers

from .decorators import is_not_admin
from .models import Remember
from . import forms


@is_not_admin
@login_required(login_url="/accounts")
def new_remember(request):
    """View creating new remember"""
    if request.method == "POST":
        user = request.user
        form = forms.Remember(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            return redirect("/accounts/profile")
    else:
        form = forms.Remember()
    return render(request, "remember/new_remember.html", {"form": form})


@is_not_admin
@login_required(login_url="/accounts")
def full_remember(request, id: int):
    """Full info about the remember"""
    rem = Remember.objects.filter(id=id).first()
    if request.method == "POST" and rem:
        form = forms.Remember(request.POST, instance=rem)
        if form.is_valid():
            form.save()
            return redirect("/accounts/profile")

    else:
        form = forms.Remember()
    ctx = {
        "id": id,
        "form": form,
        "rem_exists": bool(rem),
        "json_remember": serializers.serialize("json", [rem]) if rem else dict(),
    }
    return render(request, "remember/full_remember.html", ctx)


@login_required(login_url="/accounts")
def delete(request, id):
    """deleting remember url"""
    user = request.user
    remember = Remember.objects.filter(user=user).filter(id=id).first()
    if remember:
        remember.delete()
    return redirect("/accounts/profile")
