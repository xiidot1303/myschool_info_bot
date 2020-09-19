from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    group = models.CharField(max_length=100)

class dt(models.Model):
    w = models.CharField(max_length=100)

class message(models.Model):
    name = models.BooleanField(primary_key=False)
    surname = models.BooleanField(primary_key=False)
    group = models.BooleanField(primary_key=False)