import json
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from products.models import Product
# Create your views here.

def api_home(request,*args, **kwargs):

    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data = model_to_dict(model_data)
        data = model_to_dict(model_data,fields=['id','title','price'])
        # print(data)
        # json_data_str = json.dumps(data)
        # data['id']= model_data.id
        # data['title']= model_data.title
        # data['content']= model_data.content
        # data['price']= model_data.price
        #* serialization: model instance(model_data) -> Python dic -> return Json to client
    return JsonResponse(data)
    # return HttpResponse(json_data_str,headers={"content-type":"application/json"})

