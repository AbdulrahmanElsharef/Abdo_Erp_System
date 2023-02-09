from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeItemView.as_view(), name='home'),
    path('items', views.ItemList.as_view(), name='items'),
    path('Categories', views.CategoryList.as_view(), name='Categories'),
    path('add', views.ItemCreate.as_view(), name='add'),
    path('<slug:slug>/update', views.ItemUpdate.as_view(), name='update'),
    path('<slug:slug>/del', views.ItemDelete.as_view(), name='delete'),
]
