from django.shortcuts import redirect, render
from .models import Remember
from . import forms


def new_remember(request):
    """View creating new remember"""
    if not request.user.is_authenticated:
        return redirect("/accounts")
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


def full_remember(request, id: int):
    """Full info about the remember"""
    remember = Remember.objects.filter(user=request.user).filter(id=id).values_list()
    ctx = {"remember": remember, "is_true": len(remember) > 0}

    return render(request, "remember/full_remember.html", ctx)
