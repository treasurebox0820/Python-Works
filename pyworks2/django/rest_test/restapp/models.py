from django.db import models

# Create your models here.
from django.db import models
class Item(models.Model):
    item_name = models.CharField(max_length=32)
    price = models.IntegerField(default=0)