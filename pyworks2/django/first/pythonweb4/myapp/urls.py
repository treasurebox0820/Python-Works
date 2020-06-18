from django.urls import path
from . import views
urlpatterns = [
    path("index", views.index, name="index"), 
    path("formtest", views.formtest, name="formtest"),
    path("temple",views.index_template, name = "temple")
]
