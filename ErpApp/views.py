from django.shortcuts import render
from .models import *

from django.views.generic import ListView
from django.views.generic.edit import  CreateView,UpdateView,DeleteView


class ItemListView(ListView):
    model=Item
    # context_object_name = 'items'	

class ItemCreateView(CreateView):
    model=Item
    fields=['name','brand','item_img','brand_img','quantity','price','Color','details','category']
    success_url='list'
    
# Create your views here.
class ItemUpdateView(UpdateView):
    model=Item
    fields=['name','brand','item_img','brand_img','quantity','price','Color','details','category']
    success_url='list'
    context_object_name = 'update'	
    template_name_suffix = '_update'
    
    
class ItemDeleteView(DeleteView):
    model=Item
    success_url='/list'


