from rest_framework import routers
from .api import StoreViewSet
from django.urls import path 
from .views import StoreView 

router = routers.DefaultRouter()
router.register('storeapi', StoreViewSet, 'store_api')

urlpatterns = [
    path('stores', StoreView.as_view() ), 
    
]
urlpatterns += router.urls