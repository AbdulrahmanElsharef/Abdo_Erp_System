from django.urls import path
from . import views



urlpatterns = [
    path('',views.HomeItemView.as_view(),name='home'),
    path('',views.HomeCategoryView.as_view(),name='home'),
    path('list',views.ItemListView.as_view(),name='list'),
    path('add',views.ItemCreateView.as_view(),name='add'),
    path('<slug:slug>/update',views.ItemUpdateView.as_view(),name='update'),
    path('<slug:slug>/del',views.ItemDeleteView.as_view(),name='delete'),
]