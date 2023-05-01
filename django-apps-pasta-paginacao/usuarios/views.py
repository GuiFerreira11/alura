from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita


def cadastro(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        senha1 = request.POST["password"]
        senha2 = request.POST["password2"]
        if campo_em_branco(nome):
            messages.error(request, "O campo 'nome' está em branco")
            return render(request, "usuarios/cadastro.html")
        if senhas_diferentes(senha1, senha2):
            messages.error(request, "As senhas inseridas são diferentes")
            return render(request, "usuarios/cadastro.html")
        if exite_atributo_email(email) or exite_atributo_user(nome):
            messages.error(request, "Usuário já cadastrado")
            return render(request, "usuarios/cadastro.html")
        user = User.objects.create(username=nome, email=email)
        user.set_password(senha1)
        user.save()
        messages.success(request, "Usuário cadastrado com sucesso")
        return redirect("login")
    else:
        return render(request, "usuarios/cadastro.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        senha = request.POST["senha"]
        if campo_em_branco(email) or campo_em_branco(senha):
            messages.error(
                request, "Os campos de e-mail e senha não podem ficar em branco"
            )
            return render(request, "usuarios/login.html")
        if exite_atributo_email(email):
            username = (
                User.objects.filter(email=email)
                .values_list("username", flat=True)
                .get()
            )
            user = auth.authenticate(request, username=username, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
        else:
            messages.error(request, "Usuário não cadastrado")
            return render(request, "usuarios/login.html")
    else:
        return render(request, "usuarios/login.html")


def logout(request):
    auth.logout(request)
    return redirect("index")


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receita = Receita.objects.filter(pessoa=id).order_by("-data_receita")
        lista_receitas = {"receitas": receita}
        return render(request, "usuarios/dashboard.html", lista_receitas)
    else:
        return redirect("index")



def campo_em_branco(campo):
    return not campo.strip()


def senhas_diferentes(senha1, senha2):
    return senha1 != senha2


def exite_atributo_email(email):
    return User.objects.filter(email=email).exists()


def exite_atributo_user(user):
    return User.objects.filter(username=user).exists()
