from django.shortcuts import render, redirect
from django.contrib.auth.models import User


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
        user = User.objects.create(username=nome, email=email, password=senha1)
        user.save()
        print("Usuário criado com sucesso!")
        return redirect("login")
    else:
        return render(request, "usuarios/cadastro.html")


def login(request):
    return render(request, "usuarios/login.html")


def logout(request):
    pass


def dashboard(request):
    pass
