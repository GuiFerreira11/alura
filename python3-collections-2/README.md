# Python Collections parte 2: conjuntos e dicionários

Conjuntos ou `set` são estruturas do python que não permitem elementos duplicados, e não possuem acesso aleatório também, sendo que cada vez que imprimimos um `set` a ordem dos elementos pode mudar, portanto eles são úteis quando precisamos nos certificar que os dados não estão duplicados, como em uma lista de e-mails, por exemplo, não queremos mandar um e-mail duplicado para uma pessoa e também não nos importamos se o e-mail para a pessoa 1 vai ser disparado alguns instantes antes do e-mail para a pessoa 2. Listas usam `[ ]` para inicialização, tuplas `( )`, já conjuntos/set por sua vez utilizam `{ }`. Quando temos duas listas separadas e queremos criar uma lista nova contendo o conteúdo das duas listas, podemos começar copiando o conteúdo da primeira lista para a lista nova e então estender essa lista nova com o método `.extend()` com a segunda lista, porém ao criar a lista dessa forma, elementos duplicados podem estar presentes na lista nova.

```python
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
assistiram

>>> [15, 23, 43, 56, 13, 23, 56, 42]
```

Para remover esses elementos repetidos podemos transformar essa lista em um `set`

```python
set(assistiram)

>>> {13, 15, 23, 42, 43, 56}
```

Podemos iniciar um set do zero de duas maneiras, passando uma lista diretamente para seu contrutor `set()` ou então utilizando o inicializador `{ }`

```python
set([1,2,3,1])

>>> {1, 2, 3}

set{1,2,3,1}

>>> {1, 2, 3}
```

Como já dito anteriormente `set` não podem ser acessados aleatoriamente, assim o seguinte código não irá rodar e apresentará um erro:

```python
assistiram

>>> [15, 23, 43, 56, 13, 23, 56, 42]

unico = set(assistiram)
unico

>>> {13, 15, 23, 42, 43, 56}

unico[1]

>>> TypeError: 'set' object does not support indexing
```

Porém podemos iterar normalmente sobre o `set`

```python
for usuario in set(assistiram):
  print(usuario)

******>>> 42
>>> 43
>>> 13
>>> 15
>>> 23
>>> 56******
```

Da mesma forma que temos o método `.extend()` para estender listas, podemos fazer algo similar com os `set`, como o conceito de `set` é similar aquele de conjuntos matemáticos, onde os números não se repetem e temos por exemplo o conjunto dos números reais, naturais, inteiros …, para fazer essa extensão devemos perguntar se o elemento esta em um conjunto ou no outro e estender apenas os elementos únicos dos dois conjuntos, para isso utilizamos o operador `|`, pipe.

```python
usuarios_data_science | usuarios_machine_learning

>>> {13, 15, 23, 42, 43, 56}
```

Esse método é análogo a operação de união de conjuntos na matemática, outra operação matemática que também temos um análogo me python é a intersecção de conjuntos, que são elementos que estão presentes nos dois conjuntos ao mesmo tempo. O operador para isso é o E comercial `&`.

```python
usuarios_data_science & usuarios_machine_learning

>>> {23, 56}
```

Outra operação e a exclusão, onde eu removo os elementos de um conjunto A se eles também estiverem presentes em um conjunto B, essa operação é realizado com o sinal de menos `-`

```python
usuarios_data_science - usuarios_machine_learning

>>> {15, 43}
```

Assim como existe uma operação cria um conjunto com os elementos presentes em A e B, mas que aparecem apenas em um dos conjuntos e não nos dois conjuntos, é a operação de “ou exclusivo”, realizada pelo operador circunflexo `^`.

```python
usuarios_data_science ^ usuarios_machine_learning

>>> {15, 43, 13, 42}
```

Podemos utilizar alguns métodos que já estamos acostumados a utilizar com listas, como por exemplo a verificação se algum elemento está dentro daquele conjunto ou não com o operador `in`

```python
fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
15 in fez_ds_mas_nao_fez_ml

>>> True
```

Como conjuntos são estruturas mutáveis podemos adicionar novos elementos aos nossos conjuntos, porém não faz sentido usar o método `.append()` já que esse método adiciona um novo elemento ao final da nossa lista, e como conjuntos não tem começo ou final o método que usamos é o `.add()`. Porém como os conjuntos são compostos apenas por elementos únicos, ao tentar adicionar um elemento que já esta presente no nosso conjunto nada irá mudar.

```python
usuarios = {1,5,76,34,52,13,17}
len(usuarios)

>>> 7

usuarios.add(13)
len(usuarios)

>>> 7

usuarios.add(765)
len(usuarios)

>>> 8

usuarios

>>> {1, 5, 13, 17, 34, 52, 76, 765}
```

Contudo podemos tornar nosso conjunto uma estrutura imutável, para isso basta transforma-lo em um `frozenset()`

```python
usuarios = frozenset(usuarios)
usuarios

>>> frozenset({1, 5, 13, 17, 34, 52, 76, 765})

type(usuarios)

>>> frozenset
```

Apesar de ter mostrado apenas exemplos com números, conjuntos também podem ser utilizados com palavras. Por exemplo, ao fazer um split de um texto e passar esse split para um conjunto, teremos um conjunto com todas as palavras que aparecem no texto sem repetição.

```python
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
set(meu_texto.split())

>>> {'Bem',

'Guilherme',

'cachorro',

'de',

'e',

'eu',

'gosto',

'meu',

'muito',

'nome',

'nomes',

'o',

'tenho',

'vindo',

'é'}
```

Outro tipo de estrutura de dado muito comum é o dicionário que relaciona uma chave/key a um valor/value. Da mesma forma que o `set` os dicionários são inicializados com chaves `{ }` e entre a chave e o valor usamos dois pontos `:` da seguinte maneira `exemplo = {"gui" : 27, "vini" : 23, "rogeiro" : 51}`, outra forma de criar um dicionário, embora menos comum é utilizando seu construtor `dict()`, mas nesse caso a atribuição do conjunto chave/valor é feito com sinal de igual e não utilizamos aspas para a chave `exemplo = dict(gui = 27, vini = 23, rogerio = 51)`. Com os dicionários conseguimos utilizar a chave para retornar seu valor associado, basta passar a chave entre colchetes e aspas para o dicionário `exemplo["gui"] -> 23`, porém se a chave não existir o python retornará um `KeyError`. Para evitar isso podemos utilizar o método `.get()`, onde indicamos a chave e um valor a ser retornado caso aquela chave não exista.

```python
aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

type(aparicoes)

>>> dict 

aparicoes["Guilherme"]

>>> 1

aparicoes["cachorro"]

>>> 2 

aparicoes["xpto"]

>>> KeyError

aparicoes.get("xpto", 0)

>>> 0 

aparicoes.get("cachorro", 0)

>>> 2

aparicoes = dict(Guilherme = 2, cachorro = 1)
aparicoes

>>> {'Guilherme': 2, 'cachorro': 1}
```

Algumas operações comuns em dicionários são, adicionar um novo elemento:

```python
aparicoes["Carlos"] = 1
aparicoes

>>> {'Carlos': 1, 'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1}
```

Alterar o valor de um elemento

```python
aparicoes["Carlos"] = 2
aparicoes

>>> {'Carlos': 2, 'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1}
```

Podemos deletar também algum elemento, mas para isso precisamos utilizar o método `del`

```python
del aparicoes["Carlos"]
aparicoes

>>> {'Guilherme': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1}
```

De forma similar a outras estruturas de dados podemos também verificar se algum elemento em questão existe dentro do meu dicionário, porém isso é feito por padrão a partir das chaves

```python
"cachorro" in aparicoes

>>> True

"Carlos" in aparicoes

>>> False
```

Por isso, quando utilizamos um laço `for` para percorrer nosso dicionário, essa iteração ira acontecer com base nas chaves

```python
for elemento in aparicoes:
  print(elemento)

>>> Guilherme

cachorro

nome

vindo
```

Esse comportamento ocorre pois quando percorremos o dicionário essa iteração e realizada em `dict.keys()`, que retornam as chaves

```python
for elemento in aparicoes.keys():
  print(elemento)

>>> Guilherme

cachorro

nome

vindo
```

Mas podemos iterar sobre os values do dicionário com `dict.values()`, o mesmo vale para a verificação de algum value está dentro do dicionário

```python
for elemento in aparicoes.values():
  print(elemento)

>>> 1

2

2

1

1 in aparicoes.values()

>> True
```

Agora, caso seja necessário imprimir tanto a chave com o valor, temos algumas alternativas, uma mais manual

```python
for elemento in aparicoes.keys():
  print(elemento, aparicoes[elemento])

>>> Guilherme 1

cachorro 2

nome 2

vindo 1
```

E outra mais automática, para isso utilizamos o método `.items()`, que nos devolve uma tupla, onde o primeiro elemento é a chave e o segundo elemento é o valor associado aquela chave

```python
for elemento in aparicoes.items():
  print(elemento)

>>> ('Guilherme', 1)

('cachorro', 2)

('nome', 2)

('vindo', 1)
```

Por se tratar de uma tupla, podemos desempacotar seu conteúdo a medida que vamos iterando sobre o dicionário

```python
 for chave, valor in aparicoes.items():
  print(chave, "=", valor)

>>> Guilherme = 1

cachorro = 2

nome = 2

vindo = 1
```

Seguindo com a aplicação dos dicionários, podemos usá-los para contar quantas vezes uma palavra pareceu em um texto. Como o python diferencia maiúsculas de minúsculas, pode ser interessante transformar todas as palavras do texto um tipo só, com o `.lower()` por exemplo. As chaves do nosso dicionário serão as palavras que aparecem no texto e o valor a quantidade de vezes que essa palavra apareceu. Para separar as palavras podemos utilizar o método `.split()` e um laço for para percorrer todas as palavras do texto e ir aumentando o valor de cada palavra a medida que elas forem aparecendo, mas temos que tomar cuidado com a forma que vamos acessar as chaves do nosso dicionário para verificar se a palavra em questão está ou não no texto, pois no começo nosso dicionário estará vazio, já que não temos como saber de início quais as palavras existem no nosso texto. Portanto se utilizarmos a estratégia:

```python
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1

aparicoes
```

O programa apresentará um `KeyError`, pois a palavras ainda não estão “cadastradas” no nosso dicionário. Para contornar isso podemos utilizar o método `.get(key, std_value)`, assim quando a palavra aparecer pela primeira vez, o programa não levantará um erro e retornará o valor `0`.

```python
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
  ate_agora = aparicoes.get(palavra, 0)
  aparicoes[palavra] = ate_agora + 1

aparicoes

>>> {'bem': 1,

'cachorro': 2,

'de': 2,

'e': 2,

'eu': 1,

'gosto': 2,

'guilherme': 1,

'meu': 2,

'muito': 2,

'nome': 1,

'nomes': 1,

'o': 1,

'tenho': 1,

'vindo': 1,

'é': 1}
```

Como o valor que queremos retornar para o caso de uma palavra ainda não estar “cadastrada” no nosso dicionário é um valor padrão, podemos utilizar o `defaultdict` da biblioteca `collections` do python para isso. O `defaultdict` precisa de um fabricador de valor padrão, que é uma função que vai ser chamada toda a vez que alguma chave for chamada e ele não existir previamente no dicionário. Como queremos o valor `0`, podemos utilizar o tipo `int`, pois quando chamado como função `int()` ele retorna um inteiro de valor `0`. Então não precisamos mais utilizar o `.get()` e nosso código fica assim

```python
from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1

aparicoes

>>> defaultdict(int, {'bem': 1,

         'cachorro': 2,

         'de': 2,

         'e': 2,

         'eu': 1,

         'gosto': 2,

         'guilherme': 1,

         'meu': 2,

         'muito': 2,

         'nome': 1,

         'nomes': 1,

         'o': 1,

         'tenho': 1,

         'vindo': 1,

         'é': 1})
```

Podemos simplificar ainda mais nosso código, pois podemos aumentar o valor da quantidade de vezes que a palavra aparece direto

```python
from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  aparicoes[palavra] += 1
```

O `defaultdict` também pode servi como cache temporário, por exemplo com uma classe que na inicialização só imprime uma mensagem, ao tentar acessar um dicionário e não encontrar o elemento essa função inicializadora será chamada

```python
class Conta:
  def __init__(self):
    print("Criando uma conta")

contas = defaultdict(Conta)
contas[15]

>>> Criando uma conta <__main__.Conta at 0x7f6f781d4518>
```

Para contadores não precisaríamos nem utilizar o `defaultdict`, pois a própria biblioteca `collections` já possui o método `counter` que aceita um iterável.

```python
from collections import Counter

aparicoes = Counter(meu_texto.split())

aparicoes

>>> Counter({'bem': 1,

         'cachorro': 2,

         'de': 2,

         'e': 2,

         'eu': 1,

         'gosto': 2,

         'guilherme': 1,

         'meu': 2,

         'muito': 2,

         'nome': 1,

         'nomes': 1,

         'o': 1,

         'tenho': 1,

         'vindo': 1,

         'é': 1})
```