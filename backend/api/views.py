import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def api_home(request,*args, **kwargs):
    # request-> HttpRequest -> Django
    print(request.GET) #url query params
    print(request.POST) #url query params
    body = request.body  #string of JSON data  -> Python D ic
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
     #! not JSON , byte string of JSON data 
    print(data)
    print(request.headers)
    print(request.content_type)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)

