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

## All commands of Django Project
- install django
  ```bash
    pip3 install django
  ```

- check version
  ```bash
    python  -m  django  --version
  ```

- Command To Check all the versions of installed modules:
  ```bash
    pip freeze  
  ```
    
- create django project
    ```bash
    django-admin startproject <project_name> ./ --> ./ means create project in same dir
    ```
    
- Create app in project
    ```bash
    python manage.py startapp <app_name>
    ```
    
- run server on port
    ```bash
    python manage.py runserver <port> / <ip>:<port>
    ```

- create migration
    - Migration in Django is to make changes to our models like deleting a model, adding a field, etc. into your database schema.

    ```bash
    python manage.py makemigrations
    ```

- migrate
    ```bash
    python manage.py migrate
    ```

- Show migrations of app 
    ```bash
    python manage.py showmigrations <app_name> # to show all migration remove app name
    ```

- To see raw SQL query executing behind applied migration
    ```bash
    python  manage.py  sqlmigrate  <app_name>  <migration_name>
    ```

- create superuser
    ```bash
    python manage.py createsuperuser
    ```

- iew a database schema of an existing (or legacy) database
    ```bash
    python manage.py inspectdb
    ```

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

It helps us with working with data in a more object-oriented way.

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
# INTERVIEW QUESTIONS
## Combine multiple querysets from different models
1. If both querysets belong to the same model, you can use the union().
```python
qs1 = Course.objects.filter(name="PHP")
qs2 = Course.objects.filter(name="PHP-2")
qs = qs1.union(qs2)
```

2. Using Itertools.chain()
```python
from itertools import chain 
combined_list = list(chain(query_set_1,query_set_2))
```

## Django Architecture
Django follows a software design pattern called as MVT (Model View Template) Architecture.

- Model: It helps in handling the database (Models). They provide the options to create, edit and query data records in the database.
- View: It handles the business logic and user interactions.
- Template: It manages the presentation layer and user interface.

## How A Request Is Processed In Django
`Manage.py >> Setting.py >> urls.py >> views.py >> models.py >> templates`

1. Django first determines which root URLconf or URL configuration module is to be used
2. Then, that particular Python module urls is loaded and then Django looks for the variable urlpatterns
3. Then check each URL patterns in urls.py file, and it stops at the first match of the requested URL
4. Once that is done, the Django then imports and calls the given view.
5. In case none of the URLs match the requested URL, Django invokes an error-handling view
6. If URL maps, a view is called that interact with model and template, it renders a template.
Django responds back to the user and sends a template as a response.

## Difference Between A Project And An App In Django
A Project is the entire Django application and an App is a module inside the project that deals with one specific use case.

## Why Is Django Called A Loosely Coupled Framework?
- Django is called a loosely coupled framework because of its `MVT architecture`, which is a variant of the MVC architecture. 
- `MVT helps in separating the server code from the client-related code`. 
- Django’s Models and Views are present on the client machine and only templates return to the client, which are essentially HTML, CSS code and contains the required data from the models.
- These components are totally independent of each other and therefore, front-end developers and backend developers can work simultaneously on the project as these two parts changing will have little to no effect on each other when changed

## Set Up The Database In Django
To set up a database in Django, you can find its configurations in setting.py  file that representing Django settings.
Engines: you can change database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql_psycopg2’, ‘django.db.backends.oracle’ and so on

`'ENGINE'`: 'django.db.backends.postgresql_psycopg2',

Now we should replace the above code with our connection credentials to Mysql. The updated code should look like the code below.

```python   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'helloworld',
        'USER': '<yourname>',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

## What do you mean by the CSRF Token
CSRF Token is a security feature in Django that helps prevent `Cross-Site Request Forgery` (CSRF) attacks. 

It is a `unique value that is generated for each user session and is used to verify that the request is coming from the same use`r who made the request.

## What Is A QuerySet In Django
QuerySet is a collection of database records that match a specified set of conditions.

```python
qs = Course.objects.filter(name="PHP")
qs2 = users.objects.get(id=3) 

```

## Difference Between select_related & prefetch_related
1. `select_related`:
- is used for `one-to-one` and `foreign key` relationships
- performs a SQL join and retrieves the related objects in a single query

2. `prefetch_related`:
- is used for `many-to-many` and `reverse foreign key` relationships. 
- performs separate queries and uses Python to combine the results. 

## How Static Files Are Defined In Django
1. Websites generally need to serve additional files such as images. Javascript or CSS. In Django, these files are referred to as “static files”, Apart from that Django provides django.contrib.staticfiles to manage these static files.
2. These files are created within the project app directory by creating a subdirectory named as static.
3. Static files are stored in the folder called static in the Django app.

```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

## Explain Django Admin & Django Admin Interface.
- The application Django admin is imported from the `django.contrib package`
- This imported application is also expected to get control by the corresponding organization hence it does not require an additional front end.

    The Django admin interface provides a number of advanced features like:

- Authorization access
- Managing multiple models
- Content management system

## What is django.shortcuts.render function?
- Render function is a shortcut function that lets the developer easily pass the data dictionary with the template. 
```python
    render(request, template_name, context=None, content_type=None, status=None, using=None)
```

## Q objects in Django ORM
Q objects are used to perform complex queries as in filter() functions just "AND" the conditions while if you want to "OR" the conditions you can use Q objects. 
```python
from django.db.models import Q

Course.objects.get( Q(name__startswith='php'), Q(author__startswith='prakash')  | Q(author__startswith='Atul') )

# Equivalent to
SELECT * FROM Model WHERE name LIKE ‘php%’ And (author="prakash%" OR author="Atul%")
```

## include” Function In The urls.py File
- As in Django there can be many apps, each app may have some URLs that it responds to. 
- Rather than `registering all URLs for all apps in a single urls.py file, each app maintains its own urls.py file`, and in the project’s urls.py file we use each individual urls.py file of each app by using the include function.

## What Does “{% include %}” Does In Django
- {% include %} is a template tag in Django that allows you to include the content of another template within the current template.

## Django Rest Framework(DRF)
- DRF is a `web framework` that makes it easy to build `APIs`.
- DRF provides a `RESTful API` for your models, which can be used to `access and modify data` in your database.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def api_view(request):
    return Response({'message': 'Hello, World!'}, status=status.HTTP_200_OK)
```

## Middleware In Django
- Middleware is something that executes between the request and response. 
- Django provides various built-in middleware and also allows us to write our own middleware. 

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewares.middleware.CustomMiddleware',
]
```

```python
# middlewares/middleware.py
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
```

### usage
1. Session management,
2. Use authentication
3. Cross-site request forgery protection(CSRF)
4. Content Gzipping

## Django Signals
Signals are `events` that are sent by Django when certain actions occur. They are used to `connect` to these events and perform some action when the event occurs.

- Receiver: It specifies the callback function which connected to the signal.
- Sender: It specifies a particular sender from where a signal is received.

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Course)
def course_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"Course {instance.name} created successfully.")
    else:
        print(f"Course {instance.name} updated successfully.")
```

## Django Exceptions
Django provides a set of exceptions that can be used to handle errors in your application.
ex.
1. AppRegistryNotReady: This class raises for using models before loading the app process.
2. ObjectDoesNotExist: It’s a base class for DoesNotExist exceptions.
3. EmptyResultSet: This exception arises when the query fails to return results.
4. FieldDoesNotExist: When the requested file does not exist, this exception arises.
5. MultipleObjectsReturned: It raises by the query multiple objects returned when we expect only one object. 
6. SuspiciousOperation: It raises when the user has performed some operation, which is considered suspicious from a security perspective.
etc...

## Difference Between Django OneToOneField & ForeignKey Field
1. OneToOneField: It is used to create a one-to-one relationship between two models. It is similar to a ForeignKey, but ForeignKey with unique=True, but the “reverse” side of the relation will directly return a single object.
2. ForeignKey: It is used to create a many-to-one relationship between two models. It is similar to a OneToOneField, but it allows multiple instances of the related model to be associated with a single instance of the model it is related to.

## Serialization In Django?
Serialization is the process of converting Django models into other formats such as XML, JSON, etc.

## Generic Views
Generic views are a set of pre-built views that provide common functionality for handling HTTP requests.

```python
from django.views.generic import ListView, DetailView

class CourseListView(ListView):
    model = Course
    template_name = 'course/course_list.html'
    context_object_name = 'courses'
```
# use in urls.py
```python
from django.urls import path
from .views import CourseListView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
]
```
