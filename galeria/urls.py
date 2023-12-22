from galeria import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/', views.imagem, name='imagem'),
]