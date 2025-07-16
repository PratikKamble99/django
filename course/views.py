from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def php(request):
    # return HttpResponse('<h1>PHP course</h1>')
    return render(request, 'course/php.html')