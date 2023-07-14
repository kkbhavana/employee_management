from django.db import models


# Create your models here.
class Employee(models.Model):
    register_number = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    dept = models.CharField(max_length=250)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name
