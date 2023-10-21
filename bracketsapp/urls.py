from django.urls import path
from bracketsapp import views

urlpatterns = [
    path('', views.check, name='index')
]
