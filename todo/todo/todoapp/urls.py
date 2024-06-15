from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('delete/<str:name>/', views.DeleteTask, name='delete'),
    path('update/<str:name>/', views.UpdateTask, name='update')
]
