from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/2.2/ref/models/fields/
# https://docs.djangoproject.com/en/2.2/topics/db/sql/

class Company(models.Model):
    id = models.AutoField
    id_parent = models.IntegerField(default=0)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    born = models.DateField()
    address = models.CharField(max_length=200)

class Articles(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    public_date = models.DateField() 