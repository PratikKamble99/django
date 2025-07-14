from django.db import models

""" 

    -- A model in Django is a Python class that represents a table in a database. 
    -- Each attribute in the model becomes a column in that table.
    -- Think of models as the blueprint for your database tables.

    -- Field Type	Use For
        CharField	    Short text like names, titles
        TextField	    Long text like descriptions
        IntegerField	Whole numbers
        FloatField	    Decimal numbers
        BooleanField	True/False
        DateTimeField	Date and time
        EmailField	    Email addresses
        ForeignKey	    One-to-many relationship
        ManyToManyField	Many-to-many relationship
        ImageField	    Images (requires Pillow)

 """

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image= models.ImageField(default='fallback.png', blank=True)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)