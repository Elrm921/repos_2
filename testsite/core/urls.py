"""core app URL Configuration"""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:item_id>/', views.detail),
    path('<int:item_id>/_edit/', views.edit),
    path('<int:item_id>/_delete/', views.delete),
    path('new/', views.create_entry),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(next_page='/')),
    path('reg/', views.create_user),  
]
