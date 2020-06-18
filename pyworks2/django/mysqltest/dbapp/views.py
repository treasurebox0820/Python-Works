from django.http import HttpResponse
from .models import Member
from . import views
def index(request):
    
    Member.objects.create(firstname='Taro',lastname='Python')
    print("aaaa")
    return HttpResponse("TEST1")
