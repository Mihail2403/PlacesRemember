from django import forms
from . import models


class Remember(forms.ModelForm):

    class Meta:
        model = models.Remember
        fields = ["title", "lat", "long", "description", "user"]
        exclude = ["user"]
