from email.mime import image
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=35,null=False,blank=False)


    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=35,null=False,blank=False)


    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=30,blank=False,null=False)
    description = models.TextField(null=False,blank=False)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.description


