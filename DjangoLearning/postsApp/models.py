from django.db import models

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=75)
    body= models.TextField()
    city= models.CharField(max_length=75)
    date= models.DateTimeField(auto_now_add=True)