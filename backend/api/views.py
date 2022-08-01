from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET","POST"])
def api_home(request,*args, **kwargs):
    """
    Django Rest Framework API View
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        # data = model_to_dict(model_data,fields=['id','title','price'])
        #* serialization: model instance(model_data) -> Python dic -> return Json to client
    return Response(data)

