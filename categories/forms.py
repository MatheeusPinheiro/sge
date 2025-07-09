from django.forms import ModelForm
from categories.models import Category
from django import forms


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput({"class": "form-control"}),
            "description": forms.Textarea({"class": "form-control", "rows":3})
        }
        labels = {
            "name": "Nome",
            "description": "Descrição"
        }

    