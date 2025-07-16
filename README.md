# what is Django

    https://chatgpt.com/share/6874c523-e034-8012-8550-2c689c29f173
    Django is opensource framework or building web apps with python

## Django features

    admin site
    ORM ( Object relational mapper )
    Authentication
    Caching

## Why We Use venv in Python:

    Reason	Explanation
    1. Isolated Environment	Keeps dependencies separate for each project, avoiding conflicts.
    2. Avoids Global Pollution	Prevents you from installing packages globally (which can break other projects).
    3. Different Versions	Allows different projects to use different versions of the same package.
    4. Safer Development	Easy to recreate environments (e.g., via requirements.txt), reducing "it works on my machine" issues.
    5. Deployment Friendly	Your deployment server only installs what's in the venv, making builds faster and cleaner.

## create virtual ENV

    pip3 install virtualenv
    virtualenv venv -p python3 --> create virtual env
    source venv/bin/activate --> activate venv


    1. Use pipenv: If you’re working on Python applications (like web apps or scripts) and want pip + virtualenv with better dependency control.

    2. Use conda: If you’re doing data science or ML and want faster installation of heavy packages like numpy, pandas, tensorflow without dealing with system-level compilation issues.

    3. Use python -m venv or virtualenv: If you prefer lightweight, manual control, and are already using pip or requirements.txt—ideal for simple or small projects

## Pipfile

    The Pipfile is a modern replacement for the traditional requirements.txt file, used by pipenv to manage Python project dependencies and virtual environments more cleanly and securely.

## steps to create django project

    https://medium.com/@diwassharma/starting-a-python-django-project-on-mac-os-x-c089165cf010

## install Django

    pip3 install django
    django-admin startproject <project_name> ./ --> ./ means create project in same dir

## Debugging djando application

    Steps:
    1. Click on run and debug
    2. select django as env
    3. it will create new launch.json file in .vscode folder --> this is dibug conf file
    4. you can change debugger server port by adding port in args list
    5. now add breakpoint in your file and hit that function url in browser

## URL based debugger

    https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

    just change debug url import like in urlConf of main project

    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        # ... the rest of your URLconf goes here ...
    ] + debug_toolbar_urls()

    # above code not works
    path('__debug__/', include(debug_toolbar.urls)) # this will include your other apps urls in main project

## Models in Django

    -- A model in Django is a Python class that represents a table in a database.
    -- Each attribute in the model becomes a column in that table.
    -- Think of models as the blueprint for your database tables.

    Eg.
        from django.db import models

        class Product(models.Model):
            name = models.CharField(max_length=100)
            price = models.DecimalField(max_digits=10, decimal_places=2)
            in_stock = models.BooleanField(default=True)
            created_at = models.DateTimeField(auto_now_add=True)

    Common fields:
        Field Type	Use For
        CharField	Short text like names, titles
        TextField	Long text like descriptions
        IntegerField	Whole numbers
        FloatField	Decimal numbers
        BooleanField	True/False
        DateTimeField	Date and time
        EmailField	Email addresses
        ForeignKey	One-to-many relationship
        ManyToManyField	Many-to-many relationship
        ImageField	Images (requires Pillow)

## Migrating your models in DB

    1. python manage.py makemigrations
        -- Detects changes to your models.py
        -- Creates migration files inside the migrations/ folder
        -- These migration files describe what SQL operations Django should run to match your models with the database schema.

    2. python manage.py migrate
        -- To actually create or update the database tables

## Django ORM

Django `ORM lets you interact with the database using Python code instead of writing raw SQL`.

It maps Python classes to database tables, and class instances to table rows

Start shell with:
python manage.py shell

```python
from .models import Product

# Create and save
p1 = Product(name="Laptop", price=60000)
p1.save()

# Shortcut
Product.objects.create(name="Mouse", price=500)

# Get All Records
Product.objects.all()
```

## create admin in django

    python manage.py createsuperuser

## register your model in admin site

    add admin.site.register(models.Product) in your app admin.py file

## connect django with MYSQL

    install mysql client:- pip3 install mysql-connector-python

    # import clinet in settings.py file
    import mysql.connector.django

    # add database info
    DATABASES = {
            'default': {
                'ENGINE': 'mysql.connector.django',
                'NAME': 'db_name',  # Replace with your database name
                'USER': 'root',  # Replace with your MySQL username
                'PASSWORD': 'your_password',  # Replace with your MySQL password
                'HOST': 'localhost',  # Or the IP address/hostname of your MySQL server
                'PORT': '3306',  # Default MySQL port
            }
        }

    # follow migration steps

## Install packages in Django Peoject

    Notes: Missing Packages in `Pipfile` and Present in virtual Environment issue

---

## Problem

If a package is:

- Installed in the virtual environment (`venv`) but
- Not listed in the `Pipfile`,

then **your code will break** after deleting and recreating the environment.

## Why?

When you run:

```bash
pipenv install
```

It installs only the packages listed in the Pipfile and Pipfile.lock.
Any unlisted packages (e.g., mongoengine) will not be reinstalled.
and If you are using package in Project then you willl get erorr
`ModuleNotFoundError: No module named 'mongoengine'`

to prevent this
Always install packages using: `pipenv install <package-name>`  
Avoid using `pip install` inside the `pipenv` environment — it won't update the Pipfile.

## What is pipenv?

Instal pipenv : `pip3 install pipenv`
`pipenv` is a Python packaging and dependency management tool that aims to simplify working with Python projects by combining:

- pip (for installing packages)
- virtualenv (for creating isolated environments)

## Why pipenv

| Feature                 | What It Does                                             |
| ----------------------- | -------------------------------------------------------- |
| 🔒 `Pipfile`            | Tracks your project’s dependencies (like `package.json`) |
| 🔐 `Pipfile.lock`       | Ensures **exact same versions** are installed every time |
| 📦 Manages Virtual Envs | Automatically creates and manages a virtual environment  |
| ☁️ Easier Deployment    | Keeps dependencies isolated and predictable              |
| 🧪 Dev vs Prod Packages | Separates dev dependencies from production ones          |

## Project folder structure

**Packages:**

- if dir contains `__init__.py` file: It marks a directory as a Python package ( this is must file )

- `wsgi.py` file: WSGI stands for `Web Server Gateway Interface` — it's a specification that connects Python web frameworks (like Django or Flask) with web servers (like Gunicorn, uWSGI, Apache).

  WSGI is the bridge between Python web application and web server (e.g., Gunicorn, uWSGI, Apache with mod_wsgi)

  exposes the WSGI application callable, which the WSGI server uses to run your Django app

- `asgi.py` file: ASGI stands for `Asynchronous Server Gateway Interface`. It's the modern successor to WSGI and `allows asynchronous (non-blocking) communication between Python web apps and web servers`.

  - Why ASGI: HTTP (like WSGI), WebSockets (real-time apps), Background tasks, Long-lived connections

**manage.py**

- The manage.py file is a command-line utility that comes with every Django project.
- It helps you interact with your Django project — manage databases, run development servers, create apps, and more.

**\_\_pycache dir**

- The `__pycache__` folder is automatically created by Python when you run a script or import a module.
- It stores the compiled bytecode files (.pyc) for faster execution.

## load static files in in template

- `{% load static %}` add in template HTML file
- ```html
  <link rel="stylesheet" href="{% static '<path_of_static_file>' %}" />
  ```
