from django.shortcuts import render
from django.views.generic.list import ListView 
from .models import Store
# Create your views here.

class StoreView(ListView):
    model = Store
    #template_name = "templates/stores.html"