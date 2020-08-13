from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Store,Product
from django.shortcuts import get_object_or_404

# Create your views here.

class StoreView(ListView):
    model = Store
    context_object_name = 'all_stores'
    def get_queryset(self):
        return Store.objects.all()

class StoreDetailView(DetailView):
    model = Store
    template_name = "home/store_details.html"
    context_object_name = 'store'
    
class ProductView(ListView):
    model = Store
    

