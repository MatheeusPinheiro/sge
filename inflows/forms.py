from django.forms import ModelForm
from inflows.models import Inflow
from django import forms


class InflowForm(ModelForm):

    class Meta:
        model = Inflow
        fields = ["supplier", "product", "quantity", "description"]
        widgets = {
            "supplier": forms.Select({"class": "form-control"}),
            "product": forms.Select({"class": "form-control"}),
            "quantity": forms.NumberInput({"class": "form-control"}),
            "description": forms.Textarea({"class": "form-control", "rows":3})
        }
        labels = {
            "supplier": "Fornecedor",
            "product": "Produto",
            "quantity": "Quantidade",
            "description": "Descrição",
        }
