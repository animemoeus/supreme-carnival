from django.forms import ModelForm, Select

from .models import Category


class CreateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            "country",
            "title",
            "price_per_kilo",
        ]
        widgets = {
            "country": Select(attrs={"class": "form-select"}),
        }


class UpdateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            "country",
            "title",
            "price_per_kilo",
        ]
        widgets = {
            "country": Select(attrs={"class": "form-select"}),
        }
