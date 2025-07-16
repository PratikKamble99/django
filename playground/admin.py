from django.contrib import admin
from . import models
# Register your models here.

# @admin.register(models.Product)
admin.site.register(models.Product) # this registers yout Model in admin