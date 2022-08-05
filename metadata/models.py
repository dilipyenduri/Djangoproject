from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    created_on = models.CharField(max_length=100,blank=True,null=True)
    updated_on = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_on = models.CharField(max_length=100,blank=True,null=True)
    updated_on = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_on = models.CharField(max_length=100,blank=True,null=True)
    updated_on = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.CharField(max_length=100,blank=True,null=True)
    updated_on = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name