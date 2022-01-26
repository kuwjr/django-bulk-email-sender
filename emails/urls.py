from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('new', views.createNewBulkEmail, name='send_email'),
    path('<int:id>', views.viewSingleBulkEmail, name='single_email')
]