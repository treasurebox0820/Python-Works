from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=200,default="")
    lastname = models.CharField(max_length=200,default="")
    old = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
