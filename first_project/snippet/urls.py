from django.urls import path
from . import views

urlpatterns = [
    path('', views.snippet, name='snippet-page')
]