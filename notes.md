<h1>Project and Apps</h1>  

<h2>Project</h2>
To create a project in django we do the following:

    $ django-admin startproject mysite

<h2>Apps</h2>
To create an app inside a project we do the following:
    
    $ python manage.py startapp polls

<h2>What’s the difference between a project and an app?</h2> 
An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. 
A project is a collection of configuration and apps for a particular website. 
A project can contain multiple apps. An app can be in multiple projects.
<br>
<br>
<h1>Create a new Project Steps:</h1>

1. $ python manage.py startapp polls

2. Create a new views.py file if not available and 

       from django.http import HttpResponse
3. Define your index
    
     <code>

       def index(request):
          return HttpResponse('Hello Silcharians, welcome to django')    
    </code>

4. Create a urls.py file and import your view.py
    
    <code>

        from django.urls import path
        from . import views
        urlpatterns = [
            path('', views.index, name='index')
        ]
    </code>


Add the url patterns in the <code>app/urls.py</code>

5. Add the path in your project(mysite)/urls.py
    path('silchar/', include('polls.urls'))
    
6. Run the project and redirect to the page
<br>
<br>
<h1>
Adding multiple pages under the same application</h1>

1. In your views.py
    add a new function which returns a new page
    
    <code>
    
       def homepageSilchar(request):
           return HttpResponse('This is the homepage of silcharians')
    </code>
2. Add the function in the urlpatterns of your urls.py of the application
    <code>
        
        urlpatterns = [
            path('', views.index, name='index'),
            path('home', views.homepageSilchar, name='homepage')
        ]
    </code>

3. Restart the server and redirect to the silchar/home


<h1>Migrations</h1>

<https://realpython.com/django-migrations-a-primer/>
1. Django is designed to work with a relational database, stored in a relational database management system like PostgreSQL, MySQL, or SQLite.

2. In a relational database, data is organized in tables. A database table has a certain number of columns, but it can have any number of rows. Each column has a specific datatype, like a string of a certain maximum length or a positive integer. The description of all tables with their columns and their respective datatypes is called a <b>database schema</b>.

3. All database systems supported by Django use the language SQL to create, read, update and delete data in a relational database. SQL is also used to create, change, and delete the database tables themselves.
Working directly with SQL can be quite cumbersome, so to make your life easier, Django comes with an object-relational mapper, or ORM for short. 

4. The ORM maps the relational database to the world of object oriented programming. Instead of defining database tables in SQL, you write Django models in Python. Your models define database fields, which correspond to the columns in their database tables.

5. But just defining a model class in a Python file does not make a database table magically appear out of nowhere. Creating the database tables to store your Django models is the job of a database migration. Additionally, whenever you make a change to your models, like adding a field, the database has to be changed too. Migrations handle that as well.

<h1>Advantages of using Migrations</h1>

1. Without migrations, you would have to connect to your database and type in a bunch of SQL commands or use a graphical tool like PHPMyAdmin to modify the database schema every time you wanted to change your model definition. In Django, migrations are primarily written in Python, so you don’t have to know any SQL unless you have really advanced use cases.

2. Creating a model and then writing SQL to create the database tables for it would be repetitive. Migrations are generated from your models, making sure you don’t repeat yourself.

3. With Django Migrations, you can easily keep multiple databases in sync with your models.

4. As migrations are plain Python in Django, you can put them in a version control system just like any other piece of code.

<h1>Creating Migrations</h1>

1. Create a new application "historical_data" which tracks the prices of Bitcoin

2. Do the necessary steps like previous to add the route

3. Add <b>historical_data</b> to <b>project/settings.py</b> in the installed app section

4. In the <b>historical_data/models.py</b> file create a new model which corresponds to multiple database fields 
<code>

       class PriceHistory(models.Model):
            date = models.DateTimeField(auto_now_add=True)
            price = models.DecimalField(max_digits=7, decimal_places=2)
            volume = models.PositiveIntegerField()
</code>

5. With the model created, the first thing you need to do is create a migration for it. You can do this with the following command:
    
       $ python3 manage.py makemigrations historical_data

6. Install sqlite

7. Apply Migrations

       $ python3 manage.py migrate

8. Check if the tables are created

       $ python3 manage.py dbshell
       
       This gives you an overview of all the tables available after migrations

9. The migration that you generated in the previous step has created the <b><i>historical_data_pricehistory</i></b> table. Let’s inspect it using the <b><i>.schema</i></b> command:

       $ sqlite> .schema --indent historical_data_pricehistory
         CREATE TABLE IF NOT EXISTS "historical_data_pricehistory"(
            "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            "date" datetime NOT NULL,
            "price" decimal NOT NULL,
            "volume" integer unsigned NOT NULL CHECK("volume" >= 0)
            );


10. List out all the available migrations
    
        $ python3 manage.py showmigrations

<br>
<h1>Creating Admin User</h1>

1. Go to your project and in your terminal

       $ python3 manage.py createsuperuser

2. Redirect to <b>http://localhost:8000/admin/</b>

3. Enter the username and password

<br>
<h1>Make my apps modifiable in admin sections</h1>

1. But where’s our poll app? It’s not displayed on the admin index page. One more thing to do: we need to tell the admin that Question objects have an admin interface. To do this, open the <b>polls/admin.py</b> file, and edit it to look like this:

       from .models import Question
       admin.site.register(Question)

2. You can add and change the Models by clicking on the model name

<br>
<h1>Use Your DbShell to see your Models</h1>

1. Open your terminal and open your dbshell

       $ python3 manage.py shell

2. Now import your Models and work on it

Import the model classes we just wrote.

    # No questions are in the system yet.
    >>> Question.objects.all()
    <QuerySet []>

    # Create a new Question.
    # Support for time zones is enabled in the default settings file, so
    # Django expects a datetime with tzinfo for pub_date. Use timezone.now()
    # instead of datetime.datetime.now() and it will do the right thing.
    >>> from django.utils import timezone
    >>> q = Question(question_text="What's new?", pub_date=timezone.now())

    # Save the object into the database. You have to call save() explicitly.
    >>> q.save()

    # Now it has an ID.
    >>> q.id
    1

    # Access model field values via Python attributes.
    >>> q.question_text
    "What's new?"
    >>> q.pub_date
    datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

    # Change values by changing the attributes, then calling save().
    >>> q.question_text = "What's up?"
    >>> q.save()

    # objects.all() displays all the questions in the database.
    >>> Question.objects.all()
    <QuerySet [<Question: Question object (1)>]>

3. <b><Question: Question object (1)></b> isn’t a helpful representation of this object. Let’s fix that by editing the Question model (in the polls/models.py file) and adding a __str__() method to both Question and Choice:
<br>
Open the <b>polls/models.py</b> 

       class Question(models.Model):
       # ...
            def __str__(self):
                return self.question_text

        class Choice(models.Model):
            # ...
            def __str__(self):
                return self.choice_text
<br>
<h1>Views</h1>
<b>Creating user interfaces</b>

To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.
<br>
<h3>Rendering a HTML page</h3>

1. Go to <b>app/views.py</b> and add a function

       from django.shortcuts import render

       def hello_world(request):
           return render(request, 'hello_world.html', {})

2. In the <b>app/urls.py</b> add the view created

       from django.urls import path, include
       from . import views

       urlpatterns = [
            path('blog', views.blog, name='blog')
        ]

3. In your <b>project/urls.py</b> add the route

        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('polls/', include('polls.urls')),
            path('silchar/', include('silchar.urls')),
            path('historicalData/', include('historical_data.urls'))
        ]

4. In your <b>project/settings.py</b> add the application in <b>INSTALLED_APPS</b>

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'historical_data',
            'polls',
            'silchar'
        ]

<br>
<br>
<br>
<h1>Django REST Framework</h1>
Django REST framework helps us to build RESTful Web Services flexibly.

<br>
<br>

1. Create a new Project

2. Install Django Rest Framework

       $ pip3 install djangorestframework

3. Install markdown and django filter
        
        $ pip install markdown 
        $ pip install django-filter

4. Go to <b>project/settings.py</b> and add the following

        INSTALLED_APPS = [
            ...
            'rest_framework',
        ]

<b>REST Framework has been added successfully</b>


<br>
<br>
<br>

<h1>Connect Django project to MongoDB database</h1>

1. Install Djongo
        
        $ pip3 install djongo

2. Integrate the Mongodb
    So open <i>settings.py</i> and change declaration of <b>DATABASES</b>:

        DATABASES = {
            'default': {
                'ENGINE': 'djongo',
                'NAME': 'bezkoder_db',
                'HOST': '127.0.0.1',
                'PORT': 27017,
            }
        }

<h1>Configure CORS and middleware</h1>

1. Install CORS Header     

       $ pip3 install django-cors-headers

2. Add CORS to settings.py

        INSTALLED_APPS = [
            ...
            # CORS
            'corsheaders',
        ]    

3. You also need to add a middleware class to listen in on responses:

        MIDDLEWARE = [
            ...
            # CORS
            'corsheaders.middleware.CorsMiddleware',
            'django.middleware.common.CommonMiddleware',
        ]
4. Set CORS_ORIGIN_ALLOW_ALL and add the host to CORS_ORIGIN_WHITELIST

        CORS_ORIGIN_ALLOW_ALL = False
        CORS_ORIGIN_WHITELIST = (
            'http://localhost:8081',
        )

5. Create a new model and create migrations
6. Go to the mongodb and check if your db was created or not

