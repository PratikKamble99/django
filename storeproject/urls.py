"""
URL configuration for storeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from . import views
from playground.views import direct_import_fn

# file upload import
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls), # pratik-k/123@kamble
    path('', views.home),
    # Import view from your app
    path('playground/direct', direct_import_fn, {'status':'OK'}), # 3rd paramater get passed to view function and you can access with **kwargs
    # Import urlConf from your app
    path('playground/', include('playground.urls'), name='say_hello' ) ,# this will include your other apps urls in main project
    path('__debug__/', include(debug_toolbar.urls)), # this will include your other apps urls in main project
    path('course/', include('course.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
