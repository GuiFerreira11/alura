# Integração de modelos no Django: Filtros, buscas e admin

O curso atual é a continuação do curso anterior Django: modelos rotas e views.

Começamos melhorando a vizualização do admin da lista de receitas disponíveis, pois o padrão é ficar salvo como `Receita object(id)`. No início não teria tanto problema, mas conforme o número de receitas fosse aumentado, seria difícil lembrar qual receita é qual para poder fazer uma modificação. Por isso criamos uma classe no nosso arquivo `admin.py`, que herda da classe `admin.ModelAdmin` e dentro dessa classe definimos duas propriedades, a primeira será `list_display`, que será uma lista contendo os campos do meu modelo que eu quero que apareçam quando eu for gerenciar as minhas receitas e a segunda propriedades será a `list_display_links`, essa propriedade armazena os campos que serão considerados links para acessar e editar cada receita. Após criar a nossa classe precisamos fazer com que o registro do nosso admin também inclua essa classe, ficanod assim:

```python
from django.contrib import admin
from .models import Receita

class ListandoReceita(admin.ModelAdmin):
    list_display = ("id", "nome_receita", "categoria", "data_receita")
    list_display_links = ("id", "nome_receita")

admin.site.register(Receita, ListandoReceita)
```

Outras mudanças que podemos fazer na exibição da lista de receitas também são: permitir uma busca pelo nome da receita, exibir um filtro para por tipo de receita e criar uma paginação para quando nosso DB de receitas ficar muito grande o scroll da lista de receitas não ficar gigante. Todas essas funcionalidades podem ser adicionadas acrescentando propriedades específicas a classe criamos.

```python
from django.contrib import admin
from .models import Receita

class ListandoReceita(admin.ModelAdmin):
    list_display = ("id", "nome_receita", "categoria", "data_receita")
    list_display_links = ("id", "nome_receita")
    search_fields = ("nome_receita",)
    list_filter = ("categoria",)
    list_per_page = 10

admin.site.register(Receita, ListandoReceita)
```

Tanto `search_fields`, como `list_filter` precisam ser listas ou tuplas, por isso é necessário a virgula.

Um campo das nossas receitas que não estávamos utilizando era o de pessoa, onde indicaria qual o nome da pessoa que enviou aquela receita. Para fazer esse controle vamos criar um novo app chamado `pessoa`. Basta utilizar o comando `python manage.py startapp pessoa`. Com o app criado, registramos ele no arquivo `settings.py` do nosso projeto. Agora criamos um modelo no arquivo `models.py` com os campos `nome` e `email` como `models.CharField(max_length=200)` e fazemos a migração desse modelo para o DB com `python manage.py makemigrations` e `python manage.py migrate`. Com a migração feita registramos esse modelo dentro do arquivo `admin.py` e melhoramos sua vizualização com:

```python
from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ("id", "nome", "email")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 10

admin.site.register(Pessoa, ListandoPessoas)
```

Precisamos agora relacionar o banco de dados de `Pessoa` com o banco de dados de `Receita`, porém como vamos adicionar um nova campo no nosso banco de dados que não existia antes e ele vai estar vinculado a entradas de outra tabela, vamos excluir as receitas que já estão cadastradas sem esse campo. Para fazer esse relação entre dois bancos de daos utilizamos a opção `models.ForeignKey()` quando criamos o atributo na classe `Receita` e como parâmetros passamos a classe que será utilizada para preencher esse novo campo e a ação que o banco de dados realizará caso alguém exclua a entrada que está vinculada a nova tabela. Alguns exemplos de ações são:

- RESTRICT: o banco de dados não permite que você atualize ou exclua o registro na tabela pai, se houver um registro na tabela filha vinculada a esse registro
- CASCADE: o banco de dados automaticamente atualiza ou exclui os registros na tabela filha ao se atualizar algum registro ou excluir algum registro na tabela pai
- SET NULL: Define como `null` o campo da tabela filha quando se atualiza ou exclui o registro na tabela pai

No nosso caso vamos utilizar a ação `CASCADE`. Assim o nosso modelo de receita ficou da seguinte forma:

```python
from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
```

Após salvar as alterações basta preparar e realizar a migração.

Agora quando vamos adicionar uma nova receita, um novo campo, com uma lista de pessoas parece para selecionarmos quem é o responsável por aquela receita, porém na lista está aparecendo apenas `Pessoa object(id)`. Para evitar isso podemos definir a função `__str__` na nossa classe `Pessoa` para retornar o nome da seguinte maneira:

```python
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
```

Assim a nossa lista passará a exibir o nome da pessoa e não mais a referência para o objeto Pessoa. Outro lugar que precisamos fazer uma alteração para exibir o nome da pessoa é em `receita.html`. Como o nosso objeto `Receita` já contém as informações de `Pessoa` basta adicionar no lugar onde deve aparecer o nome da pessoa o seguinte código `{{ receita.pessoa }}`.

Com a intenção de incluir receitas novas não finalizadas no site, mas sem exibi-las na página principal, vamos adicionar um novo campo na tabela de receitas que será um `models.BooleanField` com o parâmetro `default=False` no nosso modelo, assim por padrão todas as receitas que forem adicionadas na nossa aplicação não serão publicadas por engando. Depois de preparar e fazer essa migração o campo `publicada` já estará aparecendo na parte de adicionar uma nova receita, porém todas as receitas continuam aparecendo na nossa página principal e toda vez que precisamos alterar algo em uma receita precisamos abrir a receita, ir até o final da página para desmarcar a opção de `publicada`.

Para resolver o primeiro, basta alterar como a lista de receitas esta sendo passada para a função que renderiza a home da nossa página em `views.py`. Não queremos mais passar todos os objetos e sim realizar um filtro para exibir apenas aqueles com a entrada `publicada` como `True`. Para isso trocamos a variável `receitas = Receita.objects.all()` para `receitas = Receita.objects.filter(publicada=True)`. Outro método que podemos adicionar nesse filtro é uma ordenação por data de publicação, por exemplo. Vamos utilizar o método `.order_by()` e como queremos que as ultimas receitas apareçam primeiro precisamos passar a `data_receita` em ordem decrescente da seguinte forma `receitas = Receita.objects.filter(publicada=True).order_by("-data_receita")`.

O segundo problema pode ser resolvido adicionando a entrada `publicada` na lista de `list_display` dentro do arquivo `admin.py` e adiciona-la também em uma nova lista a `list_editable`, isso fará com que essa entrada apareça na página de gerenciamento de receitas como uma checkbox que pode ser marcada e desmarcada e com o botão de salvar podemos alterar o estado dessa entrada para cada receita.

Todas as receitas estão com a mesma imagem, tanto na página principal, quanto na página que se refere a própria receita. Para mudar esse comportamento podemos permitir que quando alguém for fazer o cadastro de uma nova receita, essa possoa possa incluir uma imagem da receita. Será necessário criar uma nova entrada no banco de dados para armazenar o caminho para essa imagem, que será enviada para nossa página. O formato que teremos que utilizar é `models.ImageField()`, o primeiro argumento que vamos passar para esse modelo é o local onde ele poderá armazenar as imagens. Podemos fazer com que ele salve as imagens de acordo com o ano/mes/dia que a imagem foi enviada, assim será fácil acessar qualquer imagem caso seja necessário. O segundo argumento que vamos passar para esse modelo é que essa entrada pode ser deixada em branco caso o usuário escolha não enviar nenhuma imagem. A nossa nova entrada ficou assim `foto_receita = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)`. Antes de preparar e enviar a migração para o banco de dados precisamos usar o `pip` para instalar o modulo `Pillow` para lidar com as imagens. `python -m pip install Pillow`. É necessário também adicionar as configurações para se trabalhar com arquivos de media no nosso arquivo `settings.py` do nosso projeto. Ao final do arquivo vamos adicionar duas linha, uma contendo o caminho para a `MEDIA_ROOT` e outro para a `MEDIA_URL`, assim vamos especificar onde vamos armazenar as imagens que serão enviadas para a nossa página de receitas e o caminho para elas.

```python
...

# Media
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
```

Agora basta preparar e realizar a migração para o banco de dados e enviar uma imagem para fazer o teste.

É necessario alterar também os arquivos HTML para poder exibir as imagens específicas para cada receita, porém caso a receita não tenha uma imagem vamos continuar a exibir a imagem padrão. Para fazer essa verificação basta utilizar código python dentro do arquivo HTML e verificar se o atributo `receita.foto_receita` está em branco ou não, caso estaje em branco vamos direcionar o caminho para a imagem que já estamos utilizando, caso contrário, vamos direcionar para o caminho da imagem que foi enviada. Esse caminho é acessível através do método `.url` do atributo da nossa imagem `receita.foto_receita.url`

```html
 ...

          {% if receita.foto_receita == "" %}
              <img src="{% static "img/bg-img/tomate_banner.jpg" %}">
          {% else %}
              <img src="{{ receita.foto_receita.url }}" alt="">
          {% endif %}

...
```

Uma próxima funcionalidade que podemos incluir na nossa aplicação é a de realizar uma pesquisa por uma palavra especifica. Vamos iniciar criando uma nova rota em `urls.py` para a pégina de busca `path("buscar/", views.buscar, name="buscar")`. O próximo passo é alterar na partials `_menu.html` o comportamento do componente de busca das nossas páginas, para isso vamos alterar a tag `<form action="#" method="post">` para que a `action` redirecione para a url de busca que definimos acima.

```html
<div class="container">
    <div class="row">
      <div class="col-12">
        <form action="{% url "buscar" %}">
          <input type="search" name="search" placeholder="O que está procurando...">
          <button type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
        </form>
      </div>
    </div>
  </div>
</div>
```

Ao executar o código agora o navegador apresentará um erro, pois ainda não criamos nem a função `views.buscar` para responder a requisição, nem a página que será exibida. A função `views.buscar` precisa de um comportamento parecido com a a `views.index` no sentido de que precisa criar uma lista das receitas a serem exibidas e retornar essa lista no render da função. Para isso vamos come;car com uma variável que receberá todos os objetos, igual em `views.py`, depois vamos verificar se foi passada algum parâmetro na requisição HTML que recebemos. Como o nosso parâmetro para busca, no arquivo `_menu.html` ficou como `search` é por essa chave que devemos buscar. Essa busca é feita com o método `in` e para compara com a requisição utilizamo o método `.GET` no request `if "search" in request.GET:`. Agora precisamos recuperar a valor atribuido a essa chave. Utilizamos o mesmo método `.GET`, mas agora com uma lista contendo a chave que queremos. Basta então utilizar o método `.filter` na variável com todos os objetos de `Receitas` passando como parâmetro o atributo `nome_receita` que contenha as letras que buscamos. A verificação se o atributo nome_receita contém as letras da busca utilizamos o `__icontains=variavel_com_a_busca`. O código todo ficou assim:

```python
def buscar(request):
    receitas = Receita.objects.filter(publicada=True).order_by("-data_receita")
    if "search" in request.GET:
        nome_receita = request.GET["search"]
        if nome_receita:
            receitas = receitas.filter(nome_receita__icontains=nome_receita)
    lista_de_receitas = {"receitas": receitas}
    return render(request, "receitas/buscar.html", lista_de_receitas)
```

Agora falta apenas criar a página HTML da busca. Podemos copiar a página index porém alterando o comportamento para quando a lista de receitas a serem renderizadas estiver vazia, ao invés de mostrar a página sem nenhum conteúdo exibir um aviso como `Receita não encontrada`. Para isso basta, depois do `else` da verificação das receitas, criar algumas tags HTML para exibir o recado.

```html
<!-- ##### Best Receipe Area Start ##### -->
  <section class="best-receipe-area">

    ...

        {% if receitas %}
        {% for receita in receitas %}

		...

        {% endfor %}
        {% else %}
            <div class="col-12 col-sm-6 col-lg-4">
              <p>Receita não encontrada</p>
            </div>
        {% endif %}

		...

  </section>
  <!-- ##### Best Receipe Area End ##### -->
```

A administração do django possui uma parte onde é possível criar gurpos e usuários com premissões específicas para determinadas tarefas, como adicionar ou remover pessoas, receitas, alterar o conteúdo dessas aplicações, criar novos usuários e assim por diante.

Assim como fizemos com a aplicação de pessoas, vamos definir uma função `__str__` para a aplicação `Receitas`, que irá retornar o nome da receita, assim, quando fizermos alguma alteração nas receitas o recado que o django irá exibir será com o nome da receita e não mais com Object(x).