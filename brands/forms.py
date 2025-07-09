from django.forms import ModelForm
from brands.models import Brand
from django import forms


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput({"class": "form-control"}),
            "description": forms.Textarea({"class": "form-control", "rows":3})
        }
        labels = {
            "name": "Nome",
            "description": "Descrição"
        }

    