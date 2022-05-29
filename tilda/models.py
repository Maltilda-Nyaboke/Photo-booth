from email.mime import image
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=35,null=False,blank=False)
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, id):
        image = self.objects.get(id=id)
        image.update()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=35,null=False,blank=False)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete() 

    def update_location(self, id):
        image = self.objects.get(id=id)
        image.update()       


    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=30,blank=False,null=False)
    description = models.TextField(null=False,blank=False)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, id):
        image = self.objects.get(id=id)
        image.update()

    def get_image_by_id(self, id):
        image = self.objects.get(id=id)
        return image
    
    def __str__(self):
        return self.description


