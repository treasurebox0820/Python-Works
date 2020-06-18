from django.shortcuts import render

# Create your views here.
import django_filters
from rest_framework import viewsets, filters
from .models import Item
from .serializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    #print("たたたたたたったあたたたた",type(serializer_class))