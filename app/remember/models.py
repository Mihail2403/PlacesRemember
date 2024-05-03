from django.db import models
from django.contrib.auth.models import User


class Remember(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    lat = models.FloatField()
    long = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
