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

1. But where’s our poll app? It’s not displayed on the admin index page. One more thing to do: we need to tell the admin that Question objects have an admin interface. To do this, open the polls/admin.py file, and edit it to look like this:

       from .models import Question
       admin.site.register(Question)

2. You can add and change the Models by clicking on the model name

<br>
<h1>Views</h1>