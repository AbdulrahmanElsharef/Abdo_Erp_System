from django import forms

from .models import Item,Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Item
        exclude=['id',]

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        exclude=['id','slug']
