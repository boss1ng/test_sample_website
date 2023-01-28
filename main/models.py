from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="todolist", null=True)   # related_name="todolist" is the way to access to a related object, the user.
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
        # when queried, it will return a memory address, instead of the name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
        # on_delete=models.CASCADE ==> gets deleted as well once ToDoList has been deleted
    text = models.CharField(max_length = 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
        # when queried, it will return a memory address, instead of the name