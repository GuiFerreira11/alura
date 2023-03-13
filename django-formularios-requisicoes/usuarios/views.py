from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from receitas.models import Receita


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
        id = request.user.id
        receita = Receita.objects.filter(pessoa=id).order_by("-data_receita")
        lista_receitas = {"receitas": receita}
        return render(request, "usuarios/dashboard.html", lista_receitas)
    else:
        return redirect("index")


def criar_receita(request):
    if request.method == "POST":
        nome_receita = request.POST["nome_receita"]
        ingredientes = request.POST["ingredientes"]
        modo_preparo = request.POST["modo_preparo"]
        tempo_preparo = request.POST["tempo_preparo"]
        rendimento = request.POST["rendimento"]
        categoria = request.POST["categoria"]
        foto_receita = request.FILES["foto_receita"]
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(
            pessoa=user,
            nome_receita=nome_receita,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            foto_receita=foto_receita,
        )
        receita.save()
        return redirect("dashboard")
    else:
        return render(request, "usuarios/criar_receita.html")
