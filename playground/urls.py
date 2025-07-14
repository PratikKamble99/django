from django.urls import path

from . import views

# URL config
urlpatterns = [
    path('hello/', views.say_hello), # this is same as router in nodejs
    path('add-product/', views.create_product) # this is same as router in nodejs
]