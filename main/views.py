from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def base(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})

def list_view(response, id):
    ls = ToDoList.objects.get(id = id)

    # if ToDoList is IN the ToDoList of the User
    if ls in response.user.todolist.all():
        if response.method == "POST":
            #{"save": ["save"], "c1": ["clicked"]}
            print(response.POST) # prints in the command line
            
            if response.POST.get("saveButton"):
                for item in ls.item_set.all():
                    if response.POST.get("ItemNo." + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                
                    item.save()

            elif response.POST.get("addNewItemButton"):
                txt = response.POST.get("newItem")

                if len(txt) > 2: # hypothetical value
                    ls.item_set.create(text = txt, complete = False)
                else:
                    print("Invalid.") # prints in the command line
        
        return render(response, "main/list.html", {"ls": ls})

    else:
        return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
            response.user.todolist.add(t)

            # cleaned_data is unencrypting the input values
            # "name" is the variable name under the form class in forms.py

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

def view(response):
    return render(response, "main/view.html", {})

"""
def index_manipulate(response, id):
    ls = ToDoList.objects.get(id = id)
    return HttpResponse("<h1>%s</h1>" % ls.name)
"""

"""
"""
