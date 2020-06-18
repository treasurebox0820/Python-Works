from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"), 
    path("/temple', views.formtest, name='formtest’),
]