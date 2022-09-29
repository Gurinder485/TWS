from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("signup", views.signup, name='signup'),
    path("signin", views.signin, name='signin'),
    path("signout", views.signout, name='signout'),
]