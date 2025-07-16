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

    # render( req, ≤template_path≥, context=dict)
    # return render(request, 'hello.html', {"name":"pratik"})

def create_product(request):
    if request.method == 'POST':
        # Using model form
        # form = ProductForm(request.POST, request.FILES)  # include request.FILES for images/files
        # if form.is_valid():
        #     form.save()
        #     return HttpResponse('Product saved')
        
        # Using Regular form
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            # EXTRACTING DATA FROM FORM
            name = data.get("name")
            price = data.get("price")
            image = data.get("image")
            in_stock = data.get("in_stock")

            # creating instance of Model
            product = Product(name=name, price=price, image=image, in_stock=in_stock)
            product.save()
            return HttpResponse('Product saved')


    else: 
        # form = ProductForm({'name':'Pratik'}) # setting by-default input value
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def direct_import_fn(request, **kwargs):
    print(kwargs)
    status = kwargs.get('status')
    return HttpResponse(f"direct import view {status}")