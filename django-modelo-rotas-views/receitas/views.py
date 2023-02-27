from django.shortcuts import render


def index(request):
    receitas = {
        1: "Lasanha",
        2: "Sopa de Legumes",
        3: "Sovete",
        4: "Bolo de chocolate",
    }
    lista_de_receitas = {"nome_das_receitas": receitas}
    return render(request, "receitas/index.html", lista_de_receitas)


def receita(request):
    return render(request, "receitas/receita.html")
