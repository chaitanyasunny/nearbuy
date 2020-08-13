from rest_framework import routers
from .api import StoreViewSet
from django.urls import path
from django.conf.urls import url
from .views import StoreView,ProductView,StoreDetailView

router = routers.DefaultRouter()
router.register('storeapi', StoreViewSet, 'store_api')

urlpatterns = [
    path('stores', StoreView.as_view(), name='allstores'), 
    path('store/<int:pk>', StoreDetailView.as_view(), name='store-detail'),
    #path('stores/<int:id>', ProductView.as_view(), name='allproducts'),
    
]
urlpatterns += router.urls