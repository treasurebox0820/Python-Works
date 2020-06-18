from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"), 
    path("aaa/formtest", views.formtest, name="formtest"),
    path("aaa/temple",views.index_template, name = "temple")
]
