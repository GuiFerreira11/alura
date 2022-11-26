# Python: avançando na orientação a objetos

Podemos criar uma classe sem inicializar os atributos dela, para isso utilizamos o argumento `pass`

A partir do python3.6 o `print()`ganhou uma nova forma de imprimir textos formatados. Essa forma é a seguinte: dentro da função `print()` colocamos a letra `f` e escrevemos o texto entre aspas `"Exemplo"` . Quando queremos substituir algo por uma variável colocamos a variável entre chaves:

```python
print(f"Nome: {vingadores.nome}")
```

O python tem algumas funções para deixar algumas letras maiúsculas como o `.capitalize()` que muda apenas a primeira letra da frase para maiúscula e o `.title()`que transforma a primeira letra de cada palavra em maiúscula. 

Podemos criar um atributo com um valor inicial fixo que o usuário tem acesso na hora de inicializar o objeto, assim controlamos seu valor inicial, para isso basta acrescentar esse atributo dentro do `def __init__():` , mas sem colocar esse atributo dentro dos parênteses:

```python
class Serie:
    def __ini__(self, nome, ano, duracao):
       self.nome = nome.title()
       self.ano = ano
       self.duracao = duracao
       self.likes = 0
```

Assim o valor inicial do atributo likes vai ser 0 e o usuário não tem como definir um valor inicial diferente para ele.

Quando temos várias classes que compartilham os mesmos trechos de códigos pode ser um pouco contraprodutivo, pois caso seja necessário arrumar algum bug ou adicionar alguma funcionalidade precisaremos fazer isso para todas as classes. Para evitar isso podemos utilizar o conceito de Herença. Com esse conceito criamos uma nova classe que contém tudo o que é comum as duas classes e na hora de criar a classe colocamos entre parênteses o nome da classe mãe, de onde essa nova classe vai herdar os atributos, métodos, properties e setters.

```python
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0
```

A classe Programas é a classe mãe que contém o método `dar_likes` , os `@property` e `@nome.setter`. Para utilizar a herança dessa forma foi necessário remover a característica de privado dos atributos `nome`e `likes` , pois quando tornamos esse atributos privados só conseguimos acessar ele de fora da classe da seguinte forma `_Programa__nome` e para não precisar alterar de `__nome` para `_Programa__nome` em todos os lugares basta substituir os dois underlines por um só, isso indica para outros devs que aquele atributo, apesar de não estar privado não deve ser alterado diretamente e permite i acesso direto a esses atributos pelas classes filhas.

Ainda temos código “duplicado” no programa, pois estamos inicializando os atributos nome, ano e likes dentro das classes filhas, sendo que quando o usuário instanciar uma classe filha o programa já vai criar também a classe mãe. Podemos utilizar uma função do python que aproveita o inicializador da classe mãe para inicializar os objetos da classe filha, essa função é `super().__init__(nome,ano)` , não precisamos passar o self, pois ao utilizar o super dentro do `def __ini__():`de uma classe que tem herença o python já sabe quem é o self da função super, que no caso é a classe mãe.

```python
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

```

Com a herança ganhamos também outra propriedade que é o polimorfismo. Isso quer dizer que podemos assumir que uma classe filha é do mesmo tipo de uma classe mãe. Assim no exemplo da aula Serie é um Programa e Filme é um programa, mas Serie não é um Filme. Nesse caso podemos fazer uma lista e iterar sobre ela usando os atributos que a classe mãe tem sem ter que ficar fazendo verificações, porém para imprimir os atributos específico de cada objeto podemos fazer uma verificação, usando um `if` ternário `código_se_verdadeiro if teste_do_if else código_se_falso`.  Essa verificação normalmente é feita verificando de a classe em questão tem o atributo esperado e para isso é utilizado a função `hasattr` da seguinte maneita: `detalhe = programa.duracao if hasattr(programa, "duracao") else programa.temporadas`

Contudo essa não é a melhor forma de se fazer isso, pois para cada atributo específico que eu queira utilizar vou precisar fazer uma verificação. Uma alternativa para isso é que cada objeto soubesse imprimir os próprios atributos, com isso bastaria chamar o método de impressão do objeto e ele se encarregaria de imprimir as informações corretas que ele tem.

```python
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def imprime(self):
        print(f"{self._nome} - {self.ano} - {self._likes} Likes")

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes")

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes")

```

Essa forma ainda não é a melhor. Uma estratégia melhor seria utilizar uma função *Dunder* do python, *Dunder* vem de *double underscore* pq tem dois underlines, um no começo e outro no final da função.  Um exemplo de *Dunder* é o `__ini__`. A função que precisamos no momento é a `__str__`que devolve a string a ser impressa quando chamamos o objeto dentro de um `print`. Por isso não precisamos usar o `print()`dentro da função, devemos retornar apenas o que queremos imprimir, por exemplo `f"{self._nome}"` 

```python
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"

```

Essa forma permite a impressão do texto formatado e bonito para um usuário final, mas temos outra forma de representar nosso objeto como string é o `__repr__`

```python
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"  

   def __repr__(self):
       return f"Filme(nome={self._nome}, ano={self.ano}, duracao={self.duracao}, likes={self._likes})"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"

   def __repr__(self):
       return f"Serie(nome={self._nome}, ano={self.ano}, temporadas={self.temporadas}, likes={self._likes})"
```

Para chamar o resultado do `__repr__` precisamos usar um `print(repr(objeto))`

Podemos passar listas como argumentos de objetos também, porém não conseguimos iterar usando apenas o objeto, para isso precisamos conhecer a estrutura do objeto para saber se a lista está privada ou não e qual o nome do atributo que guarda a lista para fazer esse iteração, já que objetos não são iteráveis.

```python
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"  

   def __repr__(self):
       return f"Filme(nome={self._nome}, ano={self.ano}, duracao={self.duracao}, likes={self._likes})"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"

   def __repr__(self):
       return f"Serie(nome={self._nome}, ano={self.ano}, temporadas={self.temporadas}, likes={self._likes})"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)

```

Uma forma de tornar o objeto iterável é herdando esse comportamento do `list` assim além do comportamento de iteração ganhamos também as funcionalidade de tamanho e de saber se alguma variável está dentro do meu objeto com as funções `len()`e `in`

```python
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"  

   def __repr__(self):
       return f"Filme(nome={self._nome}, ano={self.ano}, duracao={self.duracao}, likes={self._likes})"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"

   def __repr__(self):
       return f"Serie(nome={self._nome}, ano={self.ano}, temporadas={self.temporadas}, likes={self._likes})"

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super.__init__(programas)
```

Com isso podemos utilizar o objeto Playlist da seguinte forma:

```python
print(f"O tamanho da playlist é: {(len(playlist_fim_de_semana)}")
for programa in playlist_dim_de_semanae:
    print(programa)
print(f"{demolidor.nome} está na playlist? {demolidor in playlist_fim_de_semana}")
```

Porém essa não é uma boa prática, pois não conhecemos todos os comportamentos do classe `list`assim poderíamos ter problema de sobrescrever algo que dará um erro, estamos introduzindo comportamentos que não se esperaria de uma `list`além de ficar preso a sua estrutura de dados

Ao usarmos herança temos que pensar em dois motivos para realizar isso, a interface - quando queremos resolver questões relativas a polimorfismo e quanto ao reuso de código, ou remoção de duplicações de código. O ideal é que tenhamos os dois motivos para utilizar a herança, caso contrário devemos avaliar se a herança é mesmo a melhor opção para resolver o problema. Nesse caso da playlist só estávamos utilizando a herança da classe *built-in* `list` para reutilizar suas funcionalidades de ser iterável e saber informar seu tamanho, porém adicionamos um acoplamento desnecessário a nossa classe, pois nossa classe filha utiliza poucas características da classe `list`.

O python tem um método Dunder especial para tornar o objeto iterável, assim não precisamos utilizar a herança da classe `list`para fazer isso, nem desenvolver um método novo para isso, é o método `__getitem__`

```python
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"  

   def __repr__(self):
       return f"Filme(nome={self._nome}, ano={self.ano}, duracao={self.duracao}, likes={self._likes})"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"

   def __repr__(self):
       return f"Serie(nome={self._nome}, ano={self.ano}, temporadas={self.temporadas}, likes={self._likes})"

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super.__init__(programas)

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanh0(self):
        return len(self._programas)
```

Esse método permite a utilização do objeto como um iterável em uma construção `for ... in ...` ou uma busca com o `... in ...`.

Existem duas formas de fazermos o reuso do código, a heraná cou extensão, onde temos uma superclasse ou classe mãe que tem um comportamento mais genérico que extendemos para adicionar alguma funcionalidade específica em uma subclasse ou classe filha, mas temos acesso a todo o código referente a classe mãe, caso quisermos algo diferente podemos sobreescrever esse comportamento na nossa classe filha. A outra maneira de fazer reuso de código é com a composição, onde não temos um acoplamento tão grande, assim uma modificação na superclasse não interfere de forma tão significativa uma subclasse. Assim a nova classe deixar de ter um comportamento **é um** para ter um comportamento **tem um**, foi o que fizemos com a classe playlist. Essa característica também é conhecida como Duck typing, pois segundo um engenheiro de computação, não precisamos necessariamente identificar uma ave para saber se ela é um pato ou não, basta saber se ela emite o mesmo som do pato, anda ou voa como ele.

Para resolver o problema do tamanho da playlist precisamos adicioanr o *dunder* `__len__`, esse método permite chamas `len(obj)`para obter o tamanho do mesmo. Esse e outros *dunder methods* formam um *Python Data Model*, que são métodos que permitem aos objetos que estamos criando se comportarem de uma forma mais compatível e próximo da linguagem. Entre os mais usados temos:

| Para que? | Método |
| --- | --- |
| Inicialização | __init__ |
| Representação | __str__, __repr__ |
| Container, sequência | __contains__, __iter__, __len__, __getitem__ |
| Numéricos | __add__, __sub__, __mul__, __mod__ |

Que funcioanm da seguinte forma:

| Para que? | Método |
| --- | --- |
| Inicialização | obj = Novo( ) |
| Representação | print(obj), str(obj), repr(obj) |
| Container, sequência | len(obj), item in obj, for i in obj, obj[2:3] |
| Numéricos | obj + outro_obj, obj * obj |

Existe uma série de classes dentro do python que para serem utilizadas como superclasse elas exigem que suas subclasses implementem alguns métodos *dunder*, essas classes são chamadas de *Abstract Base Classes* ou *ABC*. Isso serve para garantirmos que as subclasses terão um comportamento esperado. O pacote `collections.abc`possui diversas dessas classes. Ao compilarmos um código que utiliza alguma classes desse pacote como superclasse, caso não tenhamos implantado todos os métodos *dunder* necessários o programa vai dar erro e irá imprimir uma lista com todos os métodos necessários para implementar.

O python permite heranças multiplas, ou seja, uma subclasse pode ter duas super classes. Para isso basta informar, separando por virgulas, o nome das duas classes mães na hora de definir a classe filha, `class pleno(Alura, Caelum)`. O exemplo dado na aula foi de diferentes níveis de funcionários, junoir, pleno e senior, que podem acessar os métodos de diferentes classes, como o classe Alura, onde tem os métodos e funções específicas da escola alura e a classe caelum, também com seus métodos e funções próprias. Contudo esse temos que tomar cuidado com essa funcionalidade, pois comportamentos não desejados podem ocorrer.

Um desses comportamentos diz respeito a quando não temos um método implementado na nossa subclasse o python procura esse método na superclasse da primeira classe herdada, no caso `Alura`, caso não encontre ele tenta procurar pelo método na superclasse de `Alura`, no caso do exemplo `Funcionarios`, caso ainda sim não encontre ele vai então para a segunda classe herdada, `Caelum`e então para a superclasse de `Caelum`que também é `Funcionarios`

```python
class Funcionarios:
    pass

class Caelum(Funcionarios):
   pass

class Alura(Funcionarios):
   pass

class Junior(Alura):
   pass

class Pleno(Alura, Caelum):
   pass

class Senior(Caelum, Alura):
   pass
```

Nesse casa o algoritmo chamado *Method Resolution Order (MRO)* faria a seguinte busca por um método chamado a partir das classes Junior, Pleno e Senior:

```
Junior:
   Junior > Alura > Funcionarios

Pleno:
   Pleno (0) > Alura (1) > Funcionarios (2) > Caelum (1) > Funcionarios (2)

Senior:
   Senior (0) > Caelum (1) > Funcionarios (2) > Alura (1) > Funcionarios (2)
```

Contudo o algoritmo MRO faz uma verificação para checar se a classe é uma “boa cabeça” para fazer a verificação do método. Isso quer dizer que o algoritmo faz uma busca por calsses repetidas, caso a classe repetida for mãe de duas ou mais outras classes de mesmo nível, nesse caso `Alura`e `Caelum`são do mesmo nível, então a primeira busca na classe `Funcionarios~é removida, ficando assim:

```
Junior:
   Junior > Alura > Funcionarios

Pleno:
   Pleno (0) > Alura (1) > Caelum (1) > Funcionarios (2)

Senior:
   Senior (0) > Caelum (1) > Alura (1) > Funcionarios (2)
```

Temos também o conceito de mixins, que são pequenas classes, que não instanciam nada, masque alteram alguma coisa, pode ser a forma de apresentação de uma string, das classes em que ela é herdada.

```python
class Funcionarios:
    def __init__(self, nome):
    self.nome = nome

class Caelum(Funcionarios):
   pass

class Alura(Funcionarios):
   pass

class Junior(Alura):
   pass

class Pleno(Alura, Caelum):
   pass

class Senior(Caelum, Alura, Hipster):
   pass

class Hipster:
    def __str___(self):
        return f"Hipster, {self.nome}"
```