from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('auth1.html', views.auth1, name='auth1'),
    path('auth2.html', views.auth2, name='auth2'),
    path('auth3.html', views.auth3, name='auth3'),
    path('main1.html', views.main1, name='main1'),
    path('main1_1.html', views.main1_1, name='main1_1'),
    path('main2.html', views.main2, name='main2'),
    path('main2_1.html', views.main2_1, name='main2_1'),
    path('main3.html', views.main3, name='main3'),
    ]