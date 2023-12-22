from django.shortcuts import render


def index(request):
    return render(request, 'galeria/index.html', context={})


def imagem(request):
    return render(request, 'galeria/imagem.html')