from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile),
    path("", views.start, name="start"),
    path("logout/", views.logout)
]
