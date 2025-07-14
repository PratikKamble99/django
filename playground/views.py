from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Product
import json
from django.core import serializers
from .forms import ProductForm



# Create your views here. same as contoller in nodejs
# request --> response
# request handler
# action

def calculate(a, b):
    return a+b

def say_hello(request):
    # pull data from DB
    # transform
    # Send email
    
    # Option 1: Recommended
    products = Product.objects.all().values('id', 'name', 'price', 'image') # choose fields you want

    return JsonResponse(list(products), status=201, safe=False, json_dumps_params={'indent': 2})

    # Option 2: Use Django's serializers.serialize
    # products = Product.objects.all()
    # data = serializers.serialize('json', products)
    # return HttpResponse(data, content_type='application/json', status=200)

    # return HttpResponse(products)
    x=calculate(2, 3)
    # return render(request, 'hello.html', {"name":"pratik"})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # include request.FILES for images/files
        if form.is_valid():
            form.save()
            return HttpResponse('Product saved')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})