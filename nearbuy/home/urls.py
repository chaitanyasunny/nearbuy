from rest_framework import routers
from .api import StoreViewSet

router = routers.DefaultRouter()
router.register('storeapi', StoreViewSet, 'store_api')

urlpatterns = router.urls