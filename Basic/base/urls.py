from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.login, name='login'),
    path('getdata/<str:name>', views.get_data, name='getdata'),
]