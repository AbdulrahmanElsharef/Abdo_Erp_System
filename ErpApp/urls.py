from django.urls import path
from .views import *



urlpatterns = [
    path('list',ItemListView.as_view(),name='list'),
    path('add',ItemCreateView.as_view(),name='add'),
    path('<slug:slug>/update',ItemUpdateView.as_view(),name='update'),
    path('<slug:slug>/del',ItemDeleteView.as_view(),name='delete'),

]