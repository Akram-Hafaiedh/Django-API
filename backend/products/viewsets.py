from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):
    """
    get-> list -> Queryset
    get-> retreive -> Product instnace Detail view
    post->create -> New instance
    put -> Update
    patch -> partial Update
    delete -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'