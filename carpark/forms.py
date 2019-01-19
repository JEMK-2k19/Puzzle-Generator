from django import forms
from . import models

class RouteForm(forms.ModelForm):
    class Meta:
        model = models.Route
        fields = ["start", "destination"]