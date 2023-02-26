from django.shortcuts import render


def index(request):
    return render(request, "receitas/index.html")


def receita(request):
    return render(request, "receitas/receita.html")
