from urllib import response
from django.http import Http404
from rest_framework import generics,authentication, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from ..api.permissions import IsStaffEditorPermission




class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     authentication.TokenAuthentication
    # ]
    # permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        # print(serializer)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
        #! send a django signal if its not Model related

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    # lookup_field = 'pk'
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_update(self, serializer):
        instance  = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_destroy(self, instance):
        #instance 
        return super().perform_destroy(instance)

# class ProductListAPIView(generics.ListAPIView):
#     """
#     Not gonna use this view
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#! CLASS BASED VEIW
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self,request,*args, **kwargs): #* HTTP ->GET
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs): #* HTTP ->POST
        return self.create(request,*args, **kwargs)


#! FUNCTION BASED VIEW
@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args, **kwargs):
    if request.method =="GET":
        if pk is not None:
            #detail view
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj, many=False).data
            # qs= Product.objects.filter(pk=pk)
            # if not qs.exists():
            #     raise Http404
            return Response(data)
        # list view
        # url_args
        # get request->detail view
        qs= Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        return Response(data)
    if request.method =="POST":
        # create item
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            # instance = serializer.save()
            # instance = form.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)