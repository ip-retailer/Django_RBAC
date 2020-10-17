from django.db import models

# Create your models here.
    
class Permission(models.Model):
    permision = models.CharField(unique=True,max_length=10)
    description = models.CharField(unique=False,max_length=50)

    def __str__(self):
        return self.permision

class Group(models.Model):
    groupname = models.CharField(unique=True,max_length=15)
    permision = models.ManyToManyField(Permission)

    def __str__(self):
        return self.groupname

class User(models.Model):
    username = models.CharField(unique=True,max_length=10)
    firstname = models.CharField(unique=False,max_length=10)
    lastname = models.CharField(unique=False,max_length=10)
    group = models.ManyToManyField(Group)
    phonenumber = models.IntegerField()

    def __str__(self):
        return self.username
