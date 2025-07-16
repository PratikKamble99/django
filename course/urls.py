from django.urls import path

from . import views

# URL config
urlpatterns = [
    path('php/', views.php), # this is same as router in nodejs
]