from django.forms import ModelForm
from outflows.models import Outflow
from django import forms
from django.core.exceptions import ValidationError

class OutflowForm(ModelForm):

    class Meta:
        model = Outflow
        fields = ["product", "quantity", "description"]
        widgets = {
            "product": forms.Select({"class": "form-control"}),
            "quantity": forms.NumberInput({"class": "form-control"}),
            "description": forms.Textarea({"class": "form-control", "rows":3})
        }
        labels = {
            "product": "Produto",
            "quantity": "Quantidade",
            "description": "Descrição",
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto: {product.title} é de {product.quantity} unidades.'
            )
        
        return quantity