from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Course
from playground.models import Product
from rest_framework.decorators import api_view
from itertools import chain
# Create your views here.
@api_view(['POST'])
def php(request):
    # return HttpResponse('<h1>PHP course</h1>')
    if request.method == 'POST':
        name = request.data.get('name')
        author = request.data.get('author')
        price = request.data.get('price')
        print(name, author, price)
        Course.objects.create(name=name, author=author, price=price)
        return JsonResponse({'message': 'Course created successfully'})

    return render(request, 'course/php.html')

@api_view(['GET'])
def php(request):

    # Combine multiple querysets

    # 1. Using union()
    # qs1 = Course.objects.filter(name="PHP")
    # qs2 = Course.objects.filter(name="PHP-2")
    # qs = qs1.union(qs2)
    # print(qs1)
    # print(qs2)
    # return JsonResponse(list(qs.values()), safe=False)

    # 2. Using Itertools.chain() ---> Combine multiple querysets from different models
    qs1 = Course.objects.filter(name="PHP")
    qs2 = Product.objects.all()
    print(qs1)
    print(qs2)
    combined_list = list(chain(qs1.values(),qs2.values()))


    return JsonResponse(combined_list, safe=False)


def mongo(request):
    return HttpResponse('<h1>mongo course</h1>')