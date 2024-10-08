from django import forms
from .models import Product


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,  # NOTE assignment 1
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "search me if you can"}),
    )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category"]
