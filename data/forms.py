from django import forms
from . import models

class LoadData(forms.ModelForm):
    class Meta:
        model = models.Data
        fields = ["text"]

class Transliterate(forms.ModelForm):
    class Meta:
        model = models.Transliterate
        fields = ["text", "src", "dst"]

class Random(forms.ModelForm):
    class Meta:
        #model = models.Transliterate
        #fields = ["text", "src", "dst"]
        model = models.Random
        fields = ["nouns", "verbs", "adj","verbs_i","adv","prep"]
