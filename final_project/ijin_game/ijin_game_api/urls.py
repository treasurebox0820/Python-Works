
from django.urls import path
from . import views

urlpatterns = [
    path('syntactic_analysis/', views.SyntacticAnalysis.as_view(),
         name='syntactic_analysis'),
]

# viewsetではない場合はRoutersに登録不可
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'', ImageAnalysis)
