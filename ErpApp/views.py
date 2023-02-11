from django.shortcuts import render
from .models import *

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HomeItemView(ListView):
    def get(self,request):
        items=Item.objects.all()
        categories=Category.objects.all()
        context={'items':items,'categories':categories}
        return render(request,'home.html',context)

class CategoryList(ListView):
    model = Category
        # context_object_name = 'items'
class ItemList(ListView):
    model = Item
    # context_object_name = 'items'
    


class ItemCreate(CreateView):
    model = Item
    fields = ['name', 'brand', 'item_img', 'brand_img',
              'quantity', 'price', 'Color', 'details', 'category']
    success_url = '/'
    template_name_suffix = '_create'

# Create your views here.


class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'brand', 'item_img', 'brand_img',
              'quantity', 'price', 'Color', 'details', 'category']
    success_url = '/'
    # context_object_name = 'update'
    template_name_suffix = '_update'


class ItemDelete(DeleteView):
    model = Item
    success_url = '/'
    template_name_suffix = '_delete'
