from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    img = models.TextField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
