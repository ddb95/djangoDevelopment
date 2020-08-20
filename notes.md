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

2. Create a new views.py file if not available and from django.http import HttpResponse
3. Define your index
    
     def index(request):
        return HttpResponse('Hello Silcharians, welcome to django')

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