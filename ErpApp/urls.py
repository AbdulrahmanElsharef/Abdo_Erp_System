from django.urls import path
from .views import *



urlpatterns = [
    path('',ItemListView.as_view(),name='index')
]