from django.contrib import admin
from django.urls import path
from.views import home

app_name='ErpApp'


urlpatterns = [
    path('home/',home, name='home'),
    # path('add',item_create, name='item_create'),
    # path('<slug:slug>',item_detail, name='item_detail'),
    # path('<slug:slug>/update',item_update, name='item_update'),
    # path('<slug:slug>/delete',item_delete, name='item_delete'),
]