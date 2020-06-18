from django.urls import path
from . import views

urlpatterns = [
    # ログイン、ログアウトへの遷移はDjangoのログイン認証機能を使用する
    path('', views.top, name='top'),
    path('regist_member', views.RegistMemberView.as_view(), name='regist_member'),
    path('regist_photograph', views.regist_photograph, name='regist_photograph'),
    path('regist_image_file', views.regist_image_file, name='regist_image_file'),
    path('regist_photo_file', views.regist_photo_file, name='regist_photo_file'),
    path('mypage', views.mypage, name='mypage'),
    path('how_to_play', views.how_to_play, name='how_to_play'),
    path('recognize_ijin_image', views.recognize_ijin_image,
         name='recognize_ijin_image'),
    path('generate_ijin_sentence', views.generate_ijin_sentence,
         name='generate_ijin_sentence'),
    path('result', views.result, name='result'),
    path('ranking', views.ranking, name='ranking'),
    path('ajax_image_upload', views.ajax_image_upload, name='ajax_image_upload'),
]
