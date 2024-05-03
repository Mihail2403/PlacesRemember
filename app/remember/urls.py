from django.urls import path

from . import views


urlpatterns = [
    path("new/", views.new_remember, name="new_remember"),
    path("<int:id>/", views.full_remember),
]
