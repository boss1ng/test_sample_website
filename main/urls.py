from django.urls import path
from . import views


urlpatterns = [
    path("",            views.base,         name = "Base Template"),
    path("<int:id>",    views.list_view,    name = "Specific List View"),
    path("home/",       views.home,         name = "Home Page"),
    path("create/",     views.create,       name = "Create New List"),
    path("view/",       views.view,         name = "List View of Logged User"),
    
    #path("",            views.list_view,        name = "List View"),
    #path("<int:id>",    views.index_manipulate,     name = "index"),
    
]
