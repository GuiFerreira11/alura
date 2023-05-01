from django.shortcuts import render
from receitas.models import Receita

def busca(request):
    receitas = Receita.objects.filter(publicada=True).order_by("-data_receita")
    if "search" in request.GET:
        nome_receita = request.GET["search"]
        if nome_receita:
            receitas = receitas.filter(nome_receita__icontains=nome_receita)
    lista_de_receitas = {"receitas": receitas}
    return render(request, "receitas/buscar.html", lista_de_receitas)
