from django.db import models
from django.forms import CharField, IntegerField
import urllib,json

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    region=models.CharField(max_length=200)
    postalzip=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    alphanumeric = models.IntegerField()

