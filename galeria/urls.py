from galeria import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:id>', views.imagem, name='imagem'),
]