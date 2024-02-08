#t this code in  myapp/models.py, not directly in the notebook
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    usbn=models.CharField(max_length=100)
   #when you call string itcales __str__
    def __str__(self):
        return self.title