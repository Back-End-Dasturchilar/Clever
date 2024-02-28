from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser):
    phone = models.CharField(max_length=200)
    site = models.URLField()

    REQUIRED_FIELDS = ['phone','site']

    def __str__(self) -> str:
        return self.username


class Teacher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    img = models.ImageField(upload_to='teacher/')
    job = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name 
    

class Cours(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='cours/')
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    desc = models.TextField()
    view = models.PositiveIntegerField(blank=True, default=0)
    price = models.CharField(max_length=255)
    likes = models.ManyToManyField(Customer, related_name='likes')
    like_count = models.PositiveIntegerField(blank=True, default=0)
    like = models.FloatField(blank=True, default=0.0)
    total = models.FloatField(blank=True, default=0.0)


    def __str__(self) -> str:
        return self.title
      

class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    msg = models.TextField()


    def __str__(self) -> str:
        return self.name
    



class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='blog/')
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    desc = models.TextField()
    view = models.PositiveIntegerField(blank=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title
      
