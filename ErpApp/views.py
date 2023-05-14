from django.shortcuts import render,redirect,get_object_or_404
from .models import Item,Category
from .forms import ItemForm


def home(request):
    
    
    context={
        'items':Item.objects.all(),
        'Categories':Category.objects.all(),
    }
    return render (request,'ErpApp/home.html',context)