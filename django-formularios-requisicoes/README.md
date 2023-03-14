# Autenticação no Django: formulários, requisições e mensagens

Nesse curso vamos criar a funcionalidade de cadastro de usuários e um ambiente para os usuários publicarem suas receitas.

A primeira coisa a se fazer é criar um novo app de usuários dentro do nosso projeto django. Como já sabemos que vamos criar, pelo menos 4 páginas, a de cadastro, login, logout e dashboard, já podemos criar o arquivo `urls.py` com os `path` para esses endereços e funções em `views.py` para responder a essas chamadas com o comportamento `pass` por enquanto e conforme formos criando o comportamento de cada página vamos alterando essas funções.

Precisamos também registrar nossa nova aplicação no arquivo `settings.py` do nosso projeto, assim como incluir suas urls no arquivo `urls.py`. Podemos adicionar `usuarios` a nossa url, assim quando for entrar na página de login a url vai ficar [localhost:8000/usuarios/login](http://localhost:8000/usuarios/login) ao invés de localhost:8000/login.

Criei também um novo diretório dentro de templates para guardar os arquivos HTML que peguei de exemplo na aula.

Começando com o cadastro de usuários, vamos utilizar o método `POST` para fazer o envio das informações de cadastro, então devemos alterar no arquivo HTML o método que será utilizado, além de especificar quem ficará responsável pelo processamento dos dados, no caso será a própria função `cadastro`. Essa alteração seá feita na tag `<form>` do HTML

```html
<form action="{% url "cadastro" %}" method="POST">
```

Podemos verificar se o método de evnio dos dados realmente é o POST verificando o tipo de requisição, lá na nossa função `cadastro` em `views.py`, basta utilizar o método `.method` e comparar com a sting `"POST`. Se o método for o POST podemos realizar o cadastro e redirecionar o usuário para a página de login, utilizando a função `redirect("login")`, que precisa ser importada juto com a `render`, caso contrário, devemos renderizar novamente a página de cadastro.

O django implementa algumas ferramentas de segurança, como tokens CSRF, que são tokens utilizados para evitar ataques CSRF (Cross-site Request Forgery), um tipo de ataque muito comum que utiliza o fato de os navegadores sempre enviarem junto com a requisição para um site em que você já está autenticado o cookie de autenticação. Para utilizar essa ferramenta nos formulário que enviamos para páginas do django devemos incluir o seguinte código dentro do ambiente `<form>` do nosso HTML `{% csrf_token %}`.

```html
<form action="{% url "cadastro" %}" method="POST">
 {% csrf_token %}
 ...
</form>
```

Isso irá criar um campo escondido no nosso formulário que será preenchido com um token aleatório toda vez que carregarmos a página e esse token será comparado com o token armazenado no servidor.

Vamos agora acessar os valores inseridos no formulário. Como já verificamos que o tipo de método utilizado no envio do formulário é o POST, para acessar esses valores vamos utilizar `request.POST["nome_do_campo_do_formulario_no_html"]` e atribuir esses valores a variáveis. Devemos fazer algumas verificações nesses valores antes de criar o usuário de fato, como se o nome do usuário não foi preenchido com espaços em branco `if not nome.strip` e se a confirmação de senha é diferente da primeira senha digitada `if senha1 != senha2`. Como iremos utilizar o email como forma de entrada, devemos verificar se o email inserido no formulário já está cadastradono nosso banco de dados. Para isso vamos utilizar um `.filter` na classe `User` e verificar a existência com `.exists()` da seguinte maneira `if User.objects.filter(email=email).exists():`. Caso não tenha nenhum usuário podemos prosseguir com o cadastro.

Após as verificações podemos criar um objeto do tipo usuário, atribuí-lo a uma variável e salvar esse objeto no banco de dados. Vamos utilizar a tabela `auth_user` que o django já cria por padrão. Para isso vamos importar de `django.contrib.auth.models` a classe `User` e criar um objeto com `usuario = User.objects.create(parâmetros_para_a_criacao_do_objeto)`. A tabela `auth_user` do django tem como atributos:

- id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- date_joined

Iremos utilizar apenas `username`, `password` e `email`. O `username` e `email` podemos passar direto para o objeto, porém a senha precisa ser atribuida de outra forma, para garantir que ela será salva depois de passar pelo hash. Para isso utilizaremos o método `.set_password(senha)`. Após o objeto criado vamos enviar as informações para nosso banco de dados com o método `.save()` e redirecionar o usuário para a página de login.

Durante os teste na implementação da função de cadastro, para verificar as informações do formulário podemos utilizar a função `print` do python para imprimir mensagens no terminal que está rodando nossa aplicação.

```python
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
        user = User.objects.create(username=nome, email=email)
        user.set_password(senha1)
        user.save()
        print("Usuário criado com sucesso!")
        return redirect("login")
    else:
        return render(request, "usuarios/cadastro.html")

...
```

Para realizar o login dos usuários, devemos fazer as mesmas alterações no HTML da página de login, alterando a `action` e `method` da tag `<form>`, além de adicionar o token csrf `{% csrf_token %}`. No arquivo `views.py` o comportamento inicial da função `login` será paracido com a da função `cadastro`, onde vamos verificar o método da requisição, recuperar os valores dessa requisição e fazer alguns testes para validar esses valores

```python
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        senha = request.POST["senha"]
        if not email.strip() or not senha.strip():
            print("Os campos de e-mail e senha não podem ficar em branco")
            return render(request, "usuarios/login.html")
```

Apesar de nossa inteção ser utilizar o email para realizar o login, o módulo do django responsável pela autenticação e login utiliza o username, portanto precisamos, com a informação do email, acessar o username associado a ele no banco de dados. Para isso vamos primeiro verificar se o email digitado exite em nosso banco de dados e então com um `.filter(email)` utilizar o método `.values_list()` para acessar o username e `.get()` para poder capturar o valor e atribuí-lo a uma variável. O método `.values_list()` retorna uma lista com tuplas com os valores dos atributos passados como argumento para o método para cada objeto. Quando utilizamos só um argumento, podemos especificar a flag `flat=True`, assim os valores são passados diretamente para a lista, ao invés de tupla com um único elemento.

```python
if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list("username", flat=True).get()
```

Com a informação do username em mãos vamos agora utilizao o método `auth.authenticate()` passando como argumento o `request`, `username=` e `password=` para autenticar nosso usuário e armazenar seu conteúdo em uma variável. Basta então verificar se essa variável não é igual a `None` e utilizar o método `auth.login()` passando como argumento `request` e `user` para realizar a operação de login. Podemos então escrever uma mensagem confirmando o login e redirecionar para a pagina inicial após o login, no nooso caso para a dashboard. A utilização dos métodos de autenticação e login dependem da importação do módulo `from django.contrib import auth`.

```python
user = auth.authenticate(request, username=username, password=senha)
            if user is not None:
                auth.login(request, user)
                print("Login realizado com sucesso")
                return redirect("dashboard")
```

No final nossa função ficou

```python
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
            return redirect("login")
    else:
        return render(request, "usuarios/login.html")
```

Para manter a coerência entre as entre as páginas, vamos manter o visual da página index no nosso dashboard, porém vamos adicionar uma mensagem de saudação para o nosso usuário com seu nome. Para recuperar o nome do usuário utilizamos código python dentro do HTML da seguinte forma `{{ usuario.username }}`.

```html
<div class="contact-area section-padding-0-80">
   <div class="container">
       <div class="row">
           <div class="col-12">
               <div class="section-heading">
                   <h3>Olá {{ user.username }}</h3>
               </div>
           </div>
       </div>
   </div>
</div>
```

Alguns links do nosso menu não fazem sentido quando estamos logados, como cadastro e login, vamos então utilizar um condicional `if` dentro do HTML da partials `_menu.html` para verificar se o usuário está autenticado e então mudar o conteúdo do nosso menu. Essa verificação é geita com o método `.is_authenticated`

```html
<!-- Nav Start -->
            <div class="classynav">
              <ul>
                {% if user.is_authenticated %}
                    <li><a href="{% url "index" %}">Home</a></li>
                    <li><a href="{% url "dashboard" %}">Minhas Receitas</a></li>
                    <li><a href="{% url "logout" %}">Logout</a></li>
                {% else %}
                    <li><a href="{% url "index" %}">Home</a></li>
                    <li><a href="{% url "cadastro" %}">Cadastro</a></li>
                    <li><a href="{% url "login" %}">Login</a></li>
                {% endif %}
              </ul>
```

Agora que adicionamos um link para a página de logout precisamos adicionar um comportamento na função `views.logout`. Como só queremos realizar o logout e redirecionar o usuário para a página principal basta utilizar a função `auth.logout(request)` e depois um `return redirect("index")`.

A nossa página de dashboard pode ser acessível a qualquer um com o seu endereço, para evitar que pessoas sem autenticação acessem essa página, mesmo ela permanecendo em branco. Podemos fazer uma verificação se há algum usuário autenticado quando recebemos uma requisição para a página de dashboard, caso positivo renderizamos a página, caso negativo redirecionamos para a página inicial.

Vamos agora criar um formulário para o usuário cadastrar sua receita. Utilizei o template do curso para a parte do HTML. Para a url criamos um novo `path` para `criar/receita`. A função `views.criar_receita`, por enquanto apenas renderiza o arquivo HTML, que já possui tanto a `action` como o `method` corretos e o `csrf_token`.

Precisamos mudar o `models.py` do app de receitas para vincular as receitas com usuários agora e não mais com pessoas. Então importamos a classe `User` de `django.contrib.auth.models` e substituimos no campo `ForeignKey` de `Pessoa` para `User`. Preparamos e fazemos a migração. Agora precisamos capturar as informações passadas com o método `POST` em nosso formulário de criar receitas.

Agora precisamos criar um objeto do tipo `Receita` e salva-lo no banco de dados, para isso vamos precisar importar a classe `Receita` de `receita/models`. A criação de um objeto do tipo receita vai ser igual ao do usuário, basta atribuir as variáveis que recuperamos do formulário aos atributos do nosso objeto. Conseguimos recuperar quase todos os atributos só do formulário, porém  oatributo `pessoa` tem que ser igual ao usuário que está logado. Para recuperar a informação do `id` desse usuário vamos utilizar a função `get_object_or_404()`, que deve ser importada de `django.shortcuts`. Passamos como argumento para essa função primeiro o tipo de objeto que queremos recuperar, no nosso caso `User` e depois a `pk`, ou primary key, a chave que queremos recuperar. Com todos os atributos é só utilizar o método `receita = Receita.objects.create()` e depois `receita.save()` para salvar a receita do usuário no banco de dados e podemos agora redirecioná-lo para a página de dashboard.

```python
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
```

Na página de dashboard ainda não estamos exibindo nenhuma receita, precisamos buscar todos os objetos `Receita` do nosso banco de dados e filtrar pelo id do usuário. O id do usuário é acessivél com `id = request.user.id`. Após atribuir os objetos filtrados para uma variável criamos um dicionário com essa variável e passamos junto com os argumento da função `render()`.

```python
def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receita = Receita.objects.filter(pessoa=id).order_by("-data_receita")
        lista_receitas = {"receitas": receita}
        return render(request, "usuarios/dashboard.html", lista_receitas)
    else:
        return redirect("index")
```

As mensagens de erro e sucesso que inserimos durante a criação das nossas funções em `views.py` aparecem apenas no terminal onde estamos rodando o server da nossa aplicação. Para notificar o usuário com essas mensagens podemos utilizar o modulo de mensagens do próprio django. Como no projeto estamos utilizando o bootstrap vamos utilizar seu padrão de mensagens para exibir os recados para nosso usuário. Iremos utilizar as mensagens de `alert-danger` e `alert-success`.

```html
<div class="alert alert-danger" role="alert">
  Mensagem de erro
</div>
```

Para definir quando vamos usar cada tipo de mensagem, precisamos, no arquivo `settings.py` do nosso projeto definir os tipos de mensagem `ERROR` e `SUCCESS` do django como `danger` e `success`.

```python
# Messages
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: "danger",
    messages.SUCCESS: "success",
}
```

Como o trecho de código responsável por exibir os alertas em HTML é pequeno e será reutilizado vamos criar um arquivo dentro de partials para armazena-lo. Nesse arquivo precisamos primeiro verificar se existem mensagens para serem exibidas e então para cada mensagem utilizar o tipo de mensagem do bootstrap correto, assim como o conteúdo a ser exibido.

```html
{% if messages %}
{% for message in messages %}
<div class="alert alert-{{message.tags}}" role="alert">
  {{ message }}
</div>
{% endfor %}
{% endif %}
```

Podemos então substituir nossos `print` que utilizamos durante a criação do comportamento das funções por funções `messages`. Para isso precisamo importar, junto com `auth` a classe `messages` e para cada mensagem que queremos exibir utilizar o método correspondente. Como cadastramos em `settings.py` apenas mensagens de erro e de sucesso, vamos utilizar os métodos `.error(request, "mesagem a ser exibida")` e `.success(request, "mesagem a ser exibida")`.

Precisamos adicionar mais uma verificação no cadastro de usuários, pois como o django utiliza o `username` para fazer a autenticação devemos barrar o cadastro de novos usuários com o mesmo nome também.

Para finalizar o curso, algums comportamentos utilizados em `usuarios/views.py` foram transformados em funções separadas, permitindo que eles fossem reutilizados mais facilmente e aumento a legibilidade do código.