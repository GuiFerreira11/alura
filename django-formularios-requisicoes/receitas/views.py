from django.shortcuts import render, get_object_or_404
from .models import Receita


def index(request):
    receitas = Receita.objects.filter(publicada=True).order_by("-data_receita")
    lista_de_receitas = {"receitas": receitas}
    return render(request, "receitas/index.html", lista_de_receitas)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {"receita": receita}
    return render(request, "receitas/receita.html", receita_a_exibir)


def buscar(request):
    receitas = Receita.objects.filter(publicada=True).order_by("-data_receita")
    if "search" in request.GET:
        nome_receita = request.GET["search"]
        if nome_receita:
            receitas = receitas.filter(nome_receita__icontains=nome_receita)
    lista_de_receitas = {"receitas": receitas}
    return render(request, "receitas/buscar.html", lista_de_receitas)
