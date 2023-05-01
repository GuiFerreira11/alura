from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("<int:receita_id>", receita, name="receita"),
    path("buscar/", busca, name="buscar"),
    path("criar/receita", criar_receita, name="criar_receita"),
    path(
        "editar/receita/<int:receita_id>", editar_receita, name="editar_receita"
    ),
    path(
        "deletar/receita/<int:receita_id>",
        deletar_receita,
        name="deletar_receita",
    ),
    path("atualizar_receita", atualizar_receita, name="atualizar_receita"),
]
