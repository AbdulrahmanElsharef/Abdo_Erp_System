from django.shortcuts import render
from .models import *

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HomeItemView(ListView):
    model = Item
    context_object_name = 'items'

    def get_template_names(self):
        return ['ErpApp_home.html']


class ItemList(ListView):
    model = Item
    # context_object_name = 'items'


class CategoryList(ListView):
    model = Category
    # context_object_name = 'items'


class ItemCreate(CreateView):
    model = Item
    fields = ['name', 'brand', 'item_img', 'brand_img',
              'quantity', 'price', 'Color', 'details', 'category']
    success_url = 'list'

# Create your views here.


class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'brand', 'item_img', 'brand_img',
              'quantity', 'price', 'Color', 'details', 'category']
    success_url = 'list'
    context_object_name = 'update'
    template_name_suffix = '_update'


class ItemDelete(DeleteView):
    model = Item
    success_url = '/items'
