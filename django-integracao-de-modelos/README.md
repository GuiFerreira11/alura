# Django: modelos rotas e views

Nesse curso vamos utilizar um ambiente virutal para desenvolver nossa aplicação, para que as bibliotecas que instalarmos fiquem restritas a esse projeto. A criação de um ambiente virtual pode ser feita com:

```bash
python3 -m venv ./venv
```

Precisamos ativar o ambiente virtual antes de instalar as bibliotecas/dependências, para isso precisamos dar um `source` no arquivo `activate` que esta dentro da pasta `venv/bin/`. Quando terminar o desenvolvimento da aplicação e quiser sair do ambiente virtual basta digitar o comando `deactivate`. 

Após entrar no ambiente virtual podemos utilizar o pip para instalar o framework django `python3 -m pip install django`.

O django possui varios comando acessíveis através do comando `django-admin`, podemos ver uma lista dos comandos disponíveis com `django-admin help`. O comando que devemos utilizar para iniciar um novo projeto é `django-admin startproject nome_do_projeto caminho_para_o_projeto`. O nome do projeto nós podemos definir de acordo com a finalidade do projeto, já o caminho para o projeto, se deixarmos em branco o django irá criar um diretório com o mesmo nome que demos ao nosso projeto e então irá criar os arquivos e subpastas com o mesmo nome do nosso projeto dentro desse diretório, já se utilizarmos a notação para o diretório atual `.`, ele criará esses arquivos no diretório que estamos. Por exemplo, ao criarmos nosso livro de receitas podemos inicializar nosso projeto com `django-admin startproject livroreceitas .`. Com isso o django criará os seguintes arquivos e diretórios:

- manage.py - arquivo utilizado para acessar algums comando do django e gerenciar nosso projeto
- livroreceitas
    - **init**.py - arquivo em branco que irá indicar para o python que a pasta atual é um pacote
    - settings.py - arquivo importante que contém as configurações relacionadas a nossa aplicação, é nele por exemplo que podemos tanto trocar a lingua de exibição da nossa aplicação de `en-us` para `pt-br` em `LANGUAGE_CODE =` e também trocar o `TIME_ZONE =` de `UTC` para `America/Sao_Paulo`.
    - urls.py - um arquivo com a declaração de todasa as URLs do nosso projeto, é como um índice dentro do django.
    - wsgi.py - é um ponto de integração com servidores web compatíveis com WSGI, porém essa parte não será aborada no curso.

Dentro do arquivo `settings.py` uma `SECURITY_KEY` é gerada. Essa chave é muito importante e não deve ser enviada junto com o restante do projeto para o github, mas ao mesmo tempo é necessário para que o django possa rodar corretamente. Uma alternativa para armazenar essa informação é em um arquivo `.env`.  Para isso devemos instalar o pacote `python-dotenv` com o `pip`. Podemos agora copiar a `SECURITY_KEY` para dentro do arquivo `.env` e importar da biblioteca `dotenv` o modulo `load_dotenv` dentro do arquivo `settings.py`. Após fazer essa importação precisamos de fato carregar essas variáveis de ambiente e atribui-las a variáveis do nosso código e isso é feito da seguinte forma:

Arquivo `.env`:

```
SECRET_KEY = sequencia_de_caracteres_gerado_pelo_django
```

Arquivo `settings.py`:

```python
...

import os
from dotenv import load_dotenv

load_dotenv()

...

SECRET_KEY = str(os.getenv("SECRET_KEY"))
```

Com o nosso projeto criado, já é possível subir nosso servidor e acessa-lo na web, para isso utilizamos o arquivo `manage.py` junto com o comando `runserver`. A porta padrão que o django irá utilizar é a `8000`, porém podemos alterar essea porta para a clássica `8080`, basta passar essa porta como argumento, logo após o `runserver`, assim o comando todo fica `python manage.py runserver 8008`. Podemos acessar agora essa página com [localhost:8080](http://localhost:8080) ou [http://127.0.0.1:8080](http://127.0.0.1:8080).

Podemos agora começar a criar nosso app, não um app mobile, mas um app no conceito do django, uma aplicação. O que criamos anteriormente foi um projeto. Um projeto nada mais é do que um conjunto de configurações e aplicações, assim um projeto pode conter várias aplicações. Uma aplicação por sua vez está encarregada de realizar determinada ação e/ou função.

Podemos manter um terminal aberto rodando nosso servidor e outro para criar nossa aplicação, pois o servidor possui um carregamento automático, asim não precisamos ficar reiniciando o servidor a acada alteração, salvo algumas exeções.

A criação de um app é parecida com a de um projeto, poré utilizamos o arquivo `manage.py` ao invés do `django-admin` e o comando `startapp` ao invés do `startproject`. Quando iniciamos um novo app, assim como quando iniciamos um novo projeto, o django irá criar um novo diretóriocom vários arquivos dentro. Por exemplo `python manage.py startapp receitas`

- receitas
    - **init**.py
    - admin.py
    - apps.py
    - models.py
    - tests.py
    - views.py
    - migrations
        - __init.py

Dentro do arquivo `apps.py` temos uma classe/objeto com algumas configurações do nosso app e uma variavel com o nome da nossa aplicação. Precisamos registrar esse nome no nosso projeto e esse registro é feito no arquivo settings.py, na lista `INSTALLED_APPS`.

Para poder acessar esse nosso app precisamos de uma URL para ele, como não temos o arquivo `urls.py` dentro do diretório do nosso app precisamos cria-lo. Dentro desse arquivo precisamos as urls do django e todas as views, para isso usamos:

```python
from django.urls import path
from . import views
```

Dentro desse arquivo criamos uma lista com os padrões de urls que utilizaremos

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

Onde o primeiro parâmetro, que está vazio, indica o caminho para a raiz da nossa aplicação, ou seja o caminho [localhost:8080/](http://localhost:8080/), o segundo é o responsável por atender a requisição quando ela for realizada para o caminho descrito anteriormente e por ultimo o namespace do aplicativo para essa entrada de url.

Como o nosso arquivo `views.py` ainda esta em branco, precisamos criar lá a função que irá responder a requisição definida no arquivo `urls.py`. No arquivo `views.py` precisamos importar o `HttpResponse` da biblioteca `django.http` e definir uma função com o nome `index`, já que foi esse o nome que especificamos no arquivo `urls.py`. Essa função terá como argumento `request` e retornará um `HttpResponde("codigo_html_a_ser_exibido")`.

```python
def index(request):
    return HttpResponse("<h1>Receitas</h1>")
```

Estamos quase conseguindo visualizar nossa applicação, mas antes disso precisamos incluir nosso arquivo `urls.py` dentro do arquivo de urls do nosso projeto. Para isso abrimos o arquivo `urls.py` do nosso projeto e dentro da lista `urlpatterns` criamos um novo `path` com o caminho vazio e damos un include em receitas.urls

```python
urlpatterns = [
    path("", include("receitas.urls")),
    path("admin/", admin.site.urls),
]
```

Agora basta salvar todos os arquivos e podemos atualizar nosso navegadro em [localhost:8080](http://localhost:8080) que iremos visualizar o conteúdo da nossa primeira view. Contudo não seria nada prático desenvolver todo o HTML da nossa aplicação dentro da função `index` da nossa view.

Então vamos utilizar o conceito de templates do django para armazenar nossos arquivos html que serão renderizados no navegador. Para isso criamos um diretório com o nome de `templates` dentro do diretório principal do projeto e registramos esse diretório lá no arquivo `settings.py` do nosso projeto. Esse registro deve ser feito dentro da lista `TEMPLATES = []` como valor da chave `"DIRS"` utilizando a estrutura de `os.path.join`

```python
TEMPLATES = [
    { ...
        "DIRS": [os.path.join(BASE_DIR, "templates)],
        ...
    }
]
```

Devemos também criar um diretório com o nome do nosso app para deixar a pasta de templates organizada e escrever nossos arquivo html dentro dela. Como não vamos mais responder diretamente ao `request` podemos deletar a importação do `HttpResponse`no arquivo `views.py`, pois agora é a função `render` que irá retornar o nosso arquivo html renderizado. Essa função recebe como primeiro parâmetro o request que é passado na definição da nossa função `index` e como segundo parâmetro o caminho para o arquivo HTML que queremos exibir. Como já registramos o diretório `templates` dentro do arquivo `settings.py` só precisamos indicar o caminho a partir dai.

```python
from django.shortcuts import render

def index(request):
    return render(request, "receitas/index.html")
```

O django trata os arquivos de imagens, CSS e JavaScript como arquivos estáticos e tem uma maneira certa de trabalhar com eles. Para isso precisaremos definir onde colocaremos esses arquivos estáticos para o djando acessar e para onde ele pode fazer uma cópia desses arquivos para a melhor manipulação deles. Essas duas definições são feitas no arquivo `settings.py`, no final do arquivo com as seguintes variáveis

```python
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "livroreceitas/static"),
]
```

Onde `STATIC_ROOT` é o diretório que o djano irá criar, na raiz do nosso projeto para copiar os arquivos estático que colocarmos dentro do diretório `static` que criaremos dentro de `livroreceitas`. Depois de adicionarmos os arquivos estáticos ao diretório `livroreceitas/static` precisamos “notificar”o django que adicionamos esses arquivos, para isso usamos o comando `python manage.py collectstatic`

Porém isso não basta para que o nosso arquivo HTML encontre a localização dos arquivos estáticos, para isso precisamos fazer algumas indicações ao longo do arquivo. A primeira indicação que precisamos fazer é adicionar a seguinte tag no começo do arquivo HTML, como primeira linha `{% load static %}`, isso irá indicar para o nosso arquivo que algumas dependências do HTML estão em arquivos estáticos. A segunda indicação que devemos fazer é, sempre que um arquivo estático for referenciado ao longo do código, como quando colocamos o caminho para uma figura, o caminho para o arquivo CSS ou para um script JavaScript, precisamos envolver o caminho com a seguinte tag `{% static "caminho_para_o_recurso" %}`. Por exemplo

```python
Antes
<a class="nav-brand" href="index.html"><img src="img/core-img/logo.png" alt=""></a>

Depois
<a class="nav-brand" href="index.html"><img src="{% static "img/core-img/logo.png" %}" alt=""></a>
```

Além da tag para demarcar conteúdos estáticos, outra tag muito importante. usada ao longo do HTML é a tag para fazer referência a outras páginas HTML. Quando temos um link para uma subpagina da nossa aplicação, devemos primeiro definir uma nova função no arquivo `views.py` para renderizar o conteúdo dessa nova página, registrar uma nova url, no arquivo `urls.py`, que utilizará a função definida anteriormente no arquivo `views.py` e durante o HTML usar a seguinte tag `{% url "nome_da_url" %}`, sendo que esse `nome_da_url` é aquele definido com a variável `name=` ao se adicionar uma nova url. Então, por exemplo, para exibir o conteúdo da página de receita ao clicar em um link na nossa pagina principal devemos fazer:

Arquivo `views.py`:

```python
from django.shortcuts import render

...

def receita(request):
    return render(request, "receitas/receita.html")
```

Arquivo `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("receita/", views.receita, name="receita"),
]
```

Arquivo HTML:

```html
...

<a href="{% url "receita" %}">Receitas</a>

...
```

Uma vez que repetimos uma grande quantidade de código quando estamos fazendo o HTML, principalmente no que se trata do `<head></head>` uma boa prática para não precisar repetir esse código e facilitar futuras manutenções é criar um arquivo com essa parte do código que será a base para a construção das outras páginas. Assim caso seja necessário alterar alguma coisa, só precisaremos alterar em um lugar.. Essa separação do conteúdo repetido é feita criando um arquivo HTML que normalmente recebe o nome de `base.html` e nele coloamos o cósigo que servirá de base para todas as nossas páginas. Precisamos então indicar onde o código de cada página será inserido, o que ocorre normalmente no começo da tag `<body></body>`. As tags django que usamo para isso são `{% block content %} {% endblock %}`. Já nos arquivos que representam as nossas páginas, precisamos adicionar a seguinte tag logo no começo do arquivo, antes mesmo da tag de `{% load static %}` é a tag `{% extends "caminho_para_o_arquivo_base.html" %}`. Por exemplo, caso o meu arquivo `base.html` fique junto dos meus outros arquivos HTML em `/templates/receitas/base.html`, devmos indicar o caminho `receitas/base.html`. Além disso precisamos também indicar onde começa e onde termina o çodigo que será adicionado no nosso arquivo `base.html`. Essa indicação é feita com as mesmas tags `{% block content %} {% endblock %}`, porém a primeira ficará no começo do arquivo e a segunda no final.

Outros trechos de códigos que também são muito repetidos, são aqueles responsáveis por menus a parte superior das páginas e aqueles responsáveis pelo rodapé, pelo footer da página. Contudo nem sempre queremos utilizar esses nesmos trechos de códigos em todas as páginas, então não seria interessante inclui-los no `base.html`. Mas como queremos evitar código duplicado o que podemos fazer é criar `partials`, que são pedaços de códigos, que podem ser reutilizados em diferentes páginas. Para a melhor organização do nosso projeto podemos criar um novo diretório com o nome de `partials` e dentro desse diretório criar os arquivo que serão compartilhados entre diferentes páginas. Esses arquivos, por convenção começam com um underline no nome. Da mesma forma que para o arquivo `base.html`, se necessário, incluimos a tag `{% load static %}` no começo da partials, porém a forma de incluir partials no código das nossa páginas é um pouco diferente. Para isso utilizamos a tag `{% inclue "caminho_para_o_arquivo_da_partials.html" %}`. Por exemplo, uma partials responsável pelo menu superior de um site pode ter como nome `_menu.html` e sua inclusão duranto o HTML será:

```html
...

{% include "receitas/partials/_menu.html" %}

...
```

As nossas receitas estão chumbadas no HTML do index, pois forma adicionadas manualmente no código. Esse procedimento não é aconselhável, uma vez que sempre que quisermos adicionar uma nova receita será necessário editar o arquivo `index.html` e o django tem uma forma de facilitar isso. Inicialmnete precisamos criar um dicionário com os nomes das nossas receitas lá no arquivo `views.py`, esse dicionário será passado como um terceiro argumento na função `render`, que retorna a página a ser exibida. No entanto esse dicionário precisa estar dentro de outro dicionário, para podermos fazer um loop em seu conteúdo. a estrutura desse dicionárioa ficara assim:

Arquivo `views.py`:

```python
from django.shortcuts import render

...

def index(request):
    receitas = {
        1: "Lasanha",
        2: "Sopa de Legumes",
        3: "Sovete",
        4: "Bolo de chocolate",
    }
    lista_de_receitas = {"nome_das_receitas": receitas}
    return render(request, "receitas/index.html", lista_de_receitas)
```

Agora precisamos alterar o arquivo `index.html`, para indicar onde o nome da receita deve ser substituido, além de fazer um loop para iterar em cada receita. Isso é feito com a tag `{% loop_for %}` do django, e dentro dela incluimos o nosso laço `for`, além dessa tag precisamos indicar também onde acaba nosso loop com a tag `{% endfor %}`. No nosso caso a tag do laço for ficará assim: `{% for chave, nome_da_receita in nome_das_receitas.items %}`. Dessa forma para cada entrada da chave `"nome_das_receitas"` do dicionário `lista_de_receitas` que criamos no arquivo `views.py` o django desempacotará uma  `chave`, que no caso é um número e um `nome_da_receita`, que é propriamente o nome da receita. Agora basta indicar no HTML, onde essa variável `nome_da_receita` aparecerá. Essa operação é realizada com a tag `{{ variavel_a_ser_exibida }}`. No django, quando usamos a tag `{% %}`, queremos que algum trecho de código seja executado/interpretado, já quando usamos a tag `{{ }}`, queremos que alguma variável seja exibida. Para exemplificar, o códi no arquivo `index.html` ficou assim:

```html
...

{% for chave, nome_da_receita in nome_das_receitas.items %}
        <!-- Single Best Receipe Area -->
        <div class="col-12 col-sm-6 col-lg-4">
          <div class="single-best-receipe-area mb-30">
            <img src="{% static "img/bg-img/foto_receita.png" %}" alt="">
            <div class="receipe-content">
              <a href="{% url "receita" %}">
                <h5>{{ nome_da_receita }}</h5>
              </a>
            </div>
          </div>
        </div>
        {% endfor %}

...
```

A melhor forma de armazenar os dados das nossas receitas é com um banco de dados. Nesse projeto vamos utilizar o banco de dados Postgresql. Após instalar e configurar o postgresql precisamos indicar para a nossa aplicação qual bando de dados vamos utilizar e as informações necessárias para acessar o DB. Essas configurações ficam no arquivo `settings.py` dentro do diretório principal do nosso projeto, em um dicionário chamado `DATABASES`. Por padrão nesse dicionário a engine do banco de dados será o sqlite3. Vamos alterar esse engine para postgresql, remover o `NAME` já existente para o nome do banco de dados criado no Postgresql e adicionar mais 3 entradas, uma para o usuário `USER`, uma para a senha do usuário `PASSWORD` e outra com o endereço do host `HOST`. Como algumas dessas informações são sensíveis, como a senha e o host, podemos armazenar essas informações no arquivo `.env`, junto com a `SECURITY_KEY`.

Arquivo `.env`:

```
...

POSTGRE_DB_NAME =  nome_do_banco_de_dados
POSTGRE_DB_USER = nome_do_usuario_do_banco_de_dados
POSTGRE_KEY = senha_do_usuario_do_banco_de_dados
POSTGRE_HOST = endereco_do_banco_de_dados
```

Arquivo `settings.py`:

```python
...

import os
from dotenv import load_dotenv

load_dotenv()

...

POSTGRE_DB_NAME = str(os.getenv("POSTGRE_DB_NAME"))
POSTGRE_DB_USER = str(os.getenv("POSTGRE_DB_USER"))
POSTGRE_KEY = str(os.getenv("POSTGRE_KEY"))
POSTGRE_HOST = str(os.getenv("POSTGRE_HOST"))

...

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRE_DB_NAME,
        "USER": POSTGRE_DB_USER,
        "PASSWORD": POSTGRE_KEY,
        "HOST": POSTGRE_HOST,
    }
}
```

Para que o django consiga conversar com o Postgresql é necessário instalar dois pacotes via `pip`, o `psycopg2` e o `psycopg2-binaries`.

Agora já podemos “modelar” o nosso banco de dados, definir os campos que o nosso banco de dados precisará para armazenar as informações sobre nossas receitas. Essas configurações ficam no arquivos `models.py` dentro do diretório do nosso applicativo. Segundo o django:

> Um modelo é um único e definitiva fonte de dados sobre os seus dados, Ele contém os campos e comportamentos essenciais dos dados que você está armazenando. Em geral, cada modelo mapeia para uam única tabela no seu banco de dados.
> 

Cada modelo é definido com uma classe, que é uma subclasse de `models.Model`. Ao criar nossa classe podemos definir os campos que queremos no nosso DB e qual o formato deles. Por enquanto vamos utilizar apenas os seguintes formatos:

- CharField: um campo para string de tamanho pequeno a grande, necessita de um tamanho maximo definido
- TextField: um campo para um texto grande, não precisa de nenhum argumento
- IntegerField: um campo para números inteiros de -2147483648 a 2147483648
- DateTimeField: um campo para data e hora representado pelo formato de uma instância de `datetime.datetime` do python.

Nosso modelo ficou com os seguintes campos:

```python
from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=Tru
```

Com esse modelo pronto podemos enviar essas informações para o nosso DB. Esse envio de informações é feito em duas etapas, primeiro utilizamos o comando `python manege.py makemigration` para que o django prepare um arquivo, dentro do diretório `migrations` do nosso app, contendo as informações do que será enviado para o DB e então utilizamos o comando `python manage.py migrate` para enviar, de fato, as informações para o DB.

Uma parte importante do django também é a do admin, pois é nela, por exemplo que podemos adicionar e remover conteúdos da nossa aplicação. Para utilizar a parte de admin para a nossa aplicação precisamos primeiro registrar nossa aplicação no arquilo `admin.py` dentro do diretório do nosso app. Basta importar a classe referente a nossa aplicação do arquivo `models.py` e então registrar no admin com:

```python
from django.contrib import admin
from .models import Receita

admin.site.register(Receita)
```

Além disso precisamos também criar um usuário para o nosso admin. Esse processo é feito com o comando `python manage.py createsuperuser`, então basta inserir o nome do usuário, o endereço de e-mail é opcional e a senha. Para a senha o próprio django sugere que ela senha maior do que 8 caracteres e que não seja muito comum, no entanto como é só um exemplo eu coloquei tanto o usuário quanto a senha como `admin`. Essas informações de usuário e senha são armazenadas no banco de dados, sendo que a senha é armazenada criptografada.

Para acessar a página do admin basta adicionar `/admin` após a porta do endereço da aplicação, no caso [localhost:8000/admin](http://localhost:8000/admin). Acessando esse recusro podemos entrar com nosso usuário e senha e então adicionar uma nova receita. Os campos que aparecerão na hora de adicionar uma nova receita serão os mesmos que especificamos quando criamos o nosso modelo.

Agora precisamos alterar a origem da lista de receitas que estão sendo mostradas no nosso site, pois precisamos usar as informações do banco de dados e não do dicionário que criamos em `views.py`. Para isso precisamos importar a nossa classe `Receita`do nosso arquivo `models.py` e alterar a nossa lista de receitas para todos os objetos que estão salvos no nosso DB. Isso é feito com o seguinte método `receitas = Receita.objects.all()`. Pois as nossas receitas são armazenadas como objetos no nosso DB. Agora é necessário alterar no arquivo HTML a forma como exibimos nossas receitas, uma vez que não temos mais a estrutura de id, nome_da_receita. Primeiro precisamos verificar se exite algo na listas de receitas com um `if`, então podemos fazer um loop para cada receita dentro de receitas e na hora de exibir a receita fazemos da mesma forma para acessar um atributo de um objeto que criamos em python, `receita.nome_receita`. O código todo fica da seguinte forma:

```python
        {% if receitas %}
        {% for receita in receitas %}

...

                <h5>{{ receita.nome_receita }}</h5>
...

        {% endfor %}
        {% else %}
        {% endif %}
```

O neovim irá apresentar um erro quando tentarmos utilizar o método para retornar todos os objetos do tipo `Receita` do nosso DB, para contornar esse erro basta instalar o modulo `django_stubs` com o `pip`.

Ao acessar a página da receita, ainda estará aparecendo o template básico da receita, pois não passamos o conteudo do nosso DB para o arquivo `receita.html`. Primeiro precisamos de uma maneira de identificar cada receita individualmente e uma das melhores formas de fazer isso é com o id da receita. Para acessar o id da receita basta no arquivo `index.html`, no campo onde passamos a url da nossa página da receita, indicar `receita.id` da seguinte maneira `<a href="{% url "receita"receita.id %}">`. Isso fará com que quando acessarmos alguma receita, ao invés de o endereço mudara para [localhost:8000/receita](http://localhost:8000/receita) ele ira mudar para [localhost:8000/1](http://localhost:8000/id) no caso da receita com id 1. Por isso devemos alterar também nosso arquivo `urls.py` para que ele direcione corretamente nossa página. Essa mudança é simples, agora o nosso arquivo `urls.py` não vai mais usar o parâmetro `path("receita/")` e sim `path("<int:receita_id>")`. O `receita_id` é apenas uma variável que vamos utilizar para capturar o id como forma de um inteiro.

O próximo arquivo que devemos alterar é o arquivo `views.py`, onde vamos especificar que além do request, a função responsável por renderizar a página de receitas também vai receber a variável `receita_id` como parâmetro. Definimos então uma variável para receber o objeto Receita armazenado no nosso banco de dados. Para fazer essa busca no banco de dados utilizamos a função `get_object_or_404()` do django, que precisa ser importada junto com a função render. Essa função retorna o objeto que estamos procurando ou um erro 404, sendo que precisamos identificar qual é o objeto que queremos buscar e qual a chave que vamos utilizar para fazer essa busca, no nosso caso vamos utilizar uma primary key (pk) que será igual ao parâmetro `receita_id`. Agora basta criar um dicionário com esse a variável que foi atribuida o objeto e passar esse dicionário junto com a função render. O código todo ficou assim:

```python
from django.shortcuts import render, get_object_or_404
from .models import Receita

...

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {"receita": receita}
    return render(request, "receitas/receita.html", receita_a_exibir)
```

Agora basta acessar o arquivo `receita.html` e alterar os campos que estão com informações de exemplo pela informações que queremos exibir as informações das nossas receitas e estão armazenadas no nosso DB usando a sintaxe `{{ receita.atributo }}`. Uma ultima alteração que precisamos fazer é que no nosso arquivo de partials `_menu.html` especificamos um endereço de url para receitas que não estamos utilizando mais, portanto, por hora, vamos excluir essa parte do código.