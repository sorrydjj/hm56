from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Basket, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
        widgets = {
            "category": forms.RadioSelect
        }