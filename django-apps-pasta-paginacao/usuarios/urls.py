from django.urls import path
from . import views

urlpatterns = [
    path("cadastro", views.cadastro, name="cadastro"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("criar/receita", views.criar_receita, name="criar_receita"),
    path(
        "deletar/receita/<int:receita_id>",
        views.deletar_receita,
        name="deletar_receita",
    ),
]
