from django.shortcuts import render
from .models import *

from django.views.generic import ListView
from django.views.generic.edit import  CreateView


class ItemListView(ListView):
    model=Item
    # context_object_name = 'items'	


# Create your views here.
