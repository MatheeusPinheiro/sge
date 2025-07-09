from django.forms import ModelForm
from suppliers.models import Supplier
from django import forms


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput({"class": "form-control"}),
            "description": forms.Textarea({"class": "form-control", "rows":3})
        }
        labels = {
            "name": "Nome",
            "description": "Descrição"
        }

    