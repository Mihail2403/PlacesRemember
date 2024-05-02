from django import forms


class Remember(forms.Form):
    title = forms.CharField(max_length=100)
    lat = forms.FloatField()
    long = forms.FloatField()
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 30}),
        max_length=160,
    )
