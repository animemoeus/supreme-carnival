from django import forms

from .models import Country


class CreateCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ["name", "flag", "currency"]


class EditCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ["name", "flag", "currency"]
