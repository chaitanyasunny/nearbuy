from .models import Store
from rest_framework import viewsets, permissions
from .serializers import StoreSerializer

# Store Viewset

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = StoreSerializer