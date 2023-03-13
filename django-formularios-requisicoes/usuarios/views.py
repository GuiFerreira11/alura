from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def cadastro(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        senha1 = request.POST["password"]
        senha2 = request.POST["password2"]
        if not nome.strip():
            print("O campo 'nome' está em branco")
            return render(request, "usuarios/cadastro.html")
        if senha1 != senha2:
            print("As senhas são diferentes")
            return render(request, "usuarios/cadastro.html")
        if User.objects.filter(email=email).exists():
            print("Usuário já cadastrado")
            return render(request, "usuarios/cadastro.html")
        user = User.objects.create(username=nome, email=email)
        user.set_password(senha1)
        user.save()
        print("Usuário criado com sucesso!")
        return redirect("login")
    else:
        return render(request, "usuarios/cadastro.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        senha = request.POST["senha"]
        if not email.strip() or not senha.strip():
            print("Os campos de e-mail e senha não podem ficar em branco")
            return render(request, "usuarios/login.html")
        if User.objects.filter(email=email).exists():
            username = (
                User.objects.filter(email=email)
                .values_list("username", flat=True)
                .get()
            )
            user = auth.authenticate(request, username=username, password=senha)
            if user is not None:
                auth.login(request, user)
                print("Login realizado com sucesso")
                return redirect("dashboard")
        else:
            print("Usuário não cadastrado")
            return render(request, "usuarios/login.html")
    else:
        return render(request, "usuarios/login.html")


def logout(request):
    auth.logout(request)
    return redirect("index")


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "usuarios/dashboard.html")
    else:
        return redirect("index")
