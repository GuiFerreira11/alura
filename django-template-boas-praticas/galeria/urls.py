from django.urls import path
from .views import index, imagem

urlpatterns = [
    path("", index),
    path("imagem/", imagem),
]
