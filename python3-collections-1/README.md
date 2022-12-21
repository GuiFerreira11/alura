# Python Collections parte 1: listas e tuplas

Propriedades de listas: São construídas para armazenar vários elementos, do mesmo tipo ou não, sendo mais comum o armazenamento de elementos do mesmo tipo. A lista é uma sequência de acesso aleatório, isso quer dizer que podemos acessar qualquer elemento de nossa lista sabendo sua posição, muto parecido com um array em outras linguagens, porém não podemos confundir lista com array em python, pois ele também tem um implementação de array. Entre as coisas que eu posso fazer com uma lista estão: consultar o tamanho dessa lista com o método `len(list)`, posso também acessar qualquer elemento da lista usando colchetes `list[0]`imprime o primeiro valor da lista, posso adicionar um novo elemento no final com `list.append(novo_elemento)`, posso iterar sobre a lista `for elemento in list: ....`, remover a primeira aparição de um elemento `list.remove(elemento)`, porém caso a lista não possua esse elemento um `ValueError: list.remove(x): not in list`será levantado, assim como se eu tentar acessar uma posição “vazia” o python irá levantar um `IndexError: list index out of range` posso também excluir todos os elementos da lista com `list.clear()`

Para não levantar um error ao tentar excluir um elemento que não está presente na nossa lista podemos antes fazer uma verificação se esse elementos existe, isso é feito com o `elemento in list` que retorna `True`caso o elemento exista dentro da lista e `False`caos contrário, assim podemos fazer algo como:

```python
if element in list:
   list.remove(element)
```

O método `.appen()`é muito útil quando queremos adicionar um novo elemento na nossa lista, porém ele só adiciona elementos no final, se eu quiser adicionar um elemento em alguma posição específica eu vou utilizar o método `list.insert(indice_do_novo_elemento, novo_elemento)`. Ambos os métodos, `.append()`e `.insert()`são úteis para a inserção de apenas um elemento, no case de adicionar mais de um elemento devemos utilizar o `list.extend(objeto_iteravel)`, sendo que `obejto_iteravel`pode ser uma lista contendo os novos valores que preciso inserir na minha lista inicial. 

Existem algumas formas de manipular uma lista criando uma nova lista com o resultado dessa manipulação. A maneira mais antiga é:

```python
new_list = []
for elemento in list:
   new_list.append(elemento+1)
```

Essa manipulação soma 1 ao valor de cada elemento e adiciona ele a `new_list`. Entretanto o python tem uma outra maneira de fazer isso:

```python
new_list = [(elemento + 1) for elemento in list]
```

Dessa forma criamos a `new_list`e já passamos para ela cada `elemento` dentro da `list`já realizando a manipulação necessária. Podemos inclusive adicionar uma condição a essa construção da nova lista

```python
new_list = [(elemento + 1) for elemento in list if elemento > x]
```

Caso a manipulação que precisamos realizar seja muito complexo é possível definir uma função que faz a alteração necessária e chamar a função dentro desse construtor

```python
def foo(arg):
   return arg+1

new_list = [foo(elemento) for elemento in list if elemento > x]
```

Uma das consequências de listas serem objetos mutáveis é que toda vez que passamos nossa lista como parâmetro de alguma função não podemos garantir como a nossa lista vai retornar. Outro problema é que se definirmos uma função que recebe como parâmetro uma lista e definimos que o valor padrão para esses parâmetro é uma lista vazia, essa lista vai ser instanciada e guardada em cache na memória e o nosso método vai acabar alterando essa lista guardada em cache, então se executarmos nossa função duas vezes, na segunda vez a lista que é referenciada como padrão pode já não estar mais vazia:

```python
def processa_lista(lista=[]):
   print(len(lista))
   print(lista)
   lista.append(1)

processa_lista()
>>> 0
>>> 0
processa_lista()
>>> 1
>>> [1]
processa_lista()
>>> 2
>>> [1, 1]
processa_lista()
>>> 3
>>> [1, 1, 1]
```

Para corrigir isso e garantir que sempre uma nova lista, em branco, vai ser gerada podemos colocar o valor padrão da lista como `None`e checar se o valor para a lista for `None`criar uma nova lista:

```python
def processa_lista(lista = None):
   if lista == None:
      lista = list()
   print(len(lista))
   print(lista)
   lista.append(1)

processa_lista()
>>> 0
>>> [ ]
processa_lista()
>>> 0
>>> [ ]
processa_lista()
>>> 0
>>> [ ]
processa_lista()
>>> 0
>>> [ ]
```

Podemos fazer uma lista de objetos no python, porém quando imprimimos essa lista inteira o que vai aparecer é o endereço de memória do objeto, mesmo que o objeto tenha a função `__str__`. Para isso precisamos iterar sobre a lista ou imprimir um objeto único.

```python
class ContaCorrente:

    def __ini__(self, codigo):
        self.codigo = codigo
        saldo = 0

    def deposita(self,valor):
        self.saldo += valor

    def __str__(self):
        return "[>>>codigo {} saldo {}<<<]".format(self.codigo, self.saldo)

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)

conta_da_dani = ContaCorrente(47685
conta_da_dani.deposita(1000)

print(conta_do_gui)
print(conta_da_dani)

[>>>codigo 15 saldo 500<<<]
[>>>codigo 47685 saldo 1000<<<]

contas = [conta_do_gui, conta_da_dani]
print(contas)

[<__main__.ContaCorrente object at 0x7fabla6d40>, <__main__.ContaCorrente object at 07fabfla6db70>]

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
   print(conta)

[>>>codigo 15 saldo 500<<<]
[>>>codigo 47685 saldo 1000<<<]

print(contas[0])

[>>>codigo 15 saldo 500<<<]
```

Podemos usar a posição do objeto da lista e utilizar os métodos que aquele objeto tem assim como incluir os objetos mais de uma vez na lista `contas`, porém como a variável `conta_do_gui`e `conta_da_dani`são apenas referências para o objeto, esses objetos vão possuir mais de uma referência.

```python
contas[0].deposita(100)
print(contas[0])

[>>>codigo 15 saldo 600<<<]

conas = [conta_do_gui, conta_da_dani, conta_do_gui]
```

Agora podemos acessar a `conta_do_gui`de 3 formas, com a própria variável `conta_do_gui` como pelos índices 0 e 2 da lista `contas`

```python
print(conta_do_gui)
print(contas[0])
print(contas[2])

[>>>codigo 15 saldo 600<<<]
[>>>codigo 15 saldo 600<<<]
[>>>codigo 15 saldo 600<<<]
```

Isso pode ser perigoso, pois se utilizarmos o índice 2 para fazer um depósito na conta, por exemplo, o objeto em si vai ser alterado, pois o objeto só é criado quando chamamos seu inicializador, inclui-lo em um lista não instancia um novo objeto.

Como já foi mencionado anteriormente, listas são estruturas mutáveis que podem conter elementos mutáveis ou não, são de acesso aleatório e que geralmente armazenam elementos de um mesmo tipo, não importando a ordem dos elementos. Com isso em mente, não seria indicado, por exemplo, que agora eu decidisse  que o primeiro elemento da minha lista de contas representasse a agência daquelas contas, como listas são mutáveis é só fazer:

```python
contas.insert(0,76)

for conta in contas:
   print(conta)

>>> 76 [>>>codigo 15 saldo 600<<<] [>>>codigo 47685 saldo 1000<<<]
```

Porém essa abordagem possui algumas falhas como, por ser mutável, alguém pode “sem querer” alterar esse elemento. Como os elementos da minha lista agora são de tipos diferentes algumas funções podem não mais funcionar como:

```python
def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
print(conta[0], conta[1])
deposita_para_todas(contas)
print(conta[0], conta[1])

>>> [>>>codigo 15 saldo 600<<<] [>>>codigo 47685 saldo 1000<<<]
>>> [>>>codigo 15 saldo 700<<<] [>>>codigo 47685 saldo 1100<<<]

contas.insert(0,76)
print(contas[0], contas[1], contas[2])
deposita_para_todas(contas)

>>> 76 [>>>codigo 15 saldo 700<<<] [>>>codigo 47685 saldo 1100<<<]
>>> AttributeError: 'int' object has no attribute 'deposita'
```

Isso porque o `76` não possui um método deposita. Aqui estamos tentando dar significados para as posições dos elementos da lista e normalmente quando posições diferentes significam coisas diferentes elas são de tipos diferentes, como acontece com nossa lista de contas.

Nesse caso o mais indicado é a utilização de `tuplas` que são estruturas com representação imutável, com um número de elementos definidos ao se inicializar a `tupla` e a posição do elemento possui significado, para `tuplas` utilizamos parênteses, porém para acessarmos os valores das tuplas continuamos a utilizar os colchetes, por exemplo, na representação de um usuário onde o primeiro elemento representa o nome, o segunda a idade e o terceiro o ano de nascimento:

```python
gui = ("Guilherme", 28, 1995)
vini = ("Vinicius", 24, 1999)

print(gui[0])

>>> Guilherme
```

Como tuplas são imutáveis, elas não possuem métodos como append, insert, etc:

```python
gui.append(123)

>>> AttributeError: 'tuple' object has no attribute 'append'
```

Nada impede que quando eu for criar um novo usuário eu mude a posição dos meus elementos, porém ai eu estaria quebrando a lógica que utilizei para criar os dois primeiros:

```python
rogerio = (51, "Rogério", 1971)
```

Nesse caso mais sensível é normal que essa tupla vire uma classe com atributos e métodos, pois com tuplas só temos os métodos inerentes a essa classe `tuple`. Poderíamos ter criados as contas como tuplas também, porém ai o valor do saldo seria imutável, não poderíamos adicionar novas informações a minha conta, nem criar métodos como o deposita, para isso seria necessário criar funções que manipulassem os valores. Dessa forma nosso código se aproxima de uma programação mais funcional, baseada em valores e funções isoladas do que de uma programação baseada em objetos e métodos.

```python
conta_do_gui = (15, 100)

conta_do_gui.deposita(100)  # variação OO

def deposita(conta, valor):  # variação funcional (separando o comportamento dos dados)
    novo_saldo = conta[1] + valor
    codigo = conta[0]
    return (codigo, novo_saldo)

deposita(conta_do_gui, 100)

>>> (15,200)
```

Em OO evitamos modelos “anêmicos”, onde temos os dados separados do comportamento, o que já é esperado para programação funcional. O valor que a função acima retorna não altera o valor da variável `conta_do_gui`, podemos verificar isso imprimindo seu valor. Para alterar o valor dessa variável precisamos passar a nova tupla para assim, assim a variável `conta_do_gui` vai deixar de apontar para a tupla `(15,100)` e vai começar a apontar para a tupla `(15,200)`

```python
print(conta_do_gui)

>>> (15,100)

conta_do_gui = deposita(conta_do_gui, 100)
print(conta_do_gui)

>>> (15,200)
```

Podemos utilizar tuplas também para casos onde os valores dos elementos são do mesmo tipo, como no caso acima da conta, outro exemplo pode ser uma tupla que represente os valores nas posições x e y e o código rgb de 0 a 255, nesse caso, como a posição de cada elemento da minha estrutura de dados tem um papel importante também devemos utilizar tuplas

```python
cor_do_pixel = (15,30,200,100,200)  # posição x, posição y, parâmetro r, parâmetro g, parâmetro b
```

Podemos misturar as duas estruturas de dados, pode ser que faça sentido uma lista de tuplas. Por exemplo eu posso fazer uma lista de usuários, em que cada usuário é uma tupla com o nome, idade e ano de nascimento, isso é interessante pois cada cadastro de usuário é imutável, mas como posso incluir novos usuário depois

```python
gui = ("Guilherme", 28, 1995)
vini = ("Vinicius", 24, 1999)

usuarios = [gui, vini]

usuarios

>>> [("Guilherme", 28, 1995), ("Vinicius", 24, 1999)]

usuarios.append(("Rogério", 51, 1971))

usuarios

>>> [("Guilherme", 28, 1995), ("Vinicius", 24, 1999), ("Rogério", 51, 1971)]

usuarios[0]

>>> [("Guilherme", 28, 1995)]

usuarios [0][0]

>>>[("Guilherme")]
```

Outro exemplo de utilização de tuplas, embora não muito comum, pois nesse caso só estamos interessados na imutabilidade da tupla e não no significado de cada posição e quando temos um relatório com um número pré-determinado de contas por exemplo e não queremos, podemos mudar esse número de contas, ou as contas em si, podemos fazer uma tupla com a referência para esses objetos `ContaCorrente`, porém ainda podemos alterar os atributos desses objetos, pois apenas a tupla é imutável, seus elementos podem ou não ser imutáveis, dependendo de suas naturezas

```python
conta_do_gui = ContaCorrente(15, 100)
conta_da_dani = ContaCorrente(47685, 500)
contas = (conta_do_gui, conta_da_dani)

for conta in contas:
    print(conta)

[>>>codigo 15 saldo 100<<<]
[>>>codigo 47685 saldo 500<<<]

contaw[0].deposita(100)

for conta in contas:
    print(conta)

[>>>codigo 15 saldo 200<<<]
[>>>codigo 47685 saldo 500<<<]
```

Os `arrays` nativos do python não são muito utilizados, são estruturas muito específicas e funcionam melhor quando utilizados com números. Para utilizar o `array` do python precisamos importar, além de definir seu tipo e passar todos os elementos logo na inicialização da estrutura. Para ver os tipos disponíveis acessar o site [array— Vetores eficientes de valores numéricos — documentação Python 3.10.9](https://docs.python.org/pt-br/3.10/library/array.html). Outra coisa é que o array padrão do python precisa possuir elementos de um um mesmo tipo.

```python
import array as arr

arr.array('d', [1, 3.5])

>>> array('d', [1.0, 3.5])
```

Portanto, no dia-a-dia usamos listas quando a posição dos elementos não tem importância, tuplas para quando a posição tem importância e quando precisamos de um alto desempenho na manipulação de valores numéricos utilizamos a biblioteca `numpy` 

```python
import numpy as np

numeros = np.array([1, 3.5])
numeros

>>> array([1., 3.5])
```

O numpy possui diversas funcionalidades já inclusas, podemos por exemplo somar um valor a todos os elementos do array de forma muito simples e fácil

```python
numeros + 3

>>> array([4., 6.5])
```

Quando criamos um objeto que vai ser utilizado para compor os elementos de uma lista que pretendemos iterar sobre essa lista é importante que todos os objetos dessa lista se comportem da mesma maneira, ou pareçam que se comportem da mesma maneira, com ducktyping. Por exemplo, posso ter uma classe `Conta` da qual outras classes `ContaCorrente`, `ContaPoupanca` e `ContaInvestimento` herdem seu comportamento através de herança, porém devido ao polimorfismo, como `ContaCorrente`, `ContaPoupanca` e `ContaInvestimento` também são `Conta` e possuem métodos em comum, posso utiliza-las dentro de uma mesma lista

```python
class Conta:

   def __init__(self, codigo):
       self._codigo = codigo
       self._saldo = 0

   def deposita(self, valor):
      self._saldo += valor

   def __str__(self):
      return "[>>>código {} Saldo {}<<<]".format(self._codigo, self.saldo)

class ContaCorrente(Conta):

   def passa_o_mes(self):
      self._saldo -= 2

class ContaPoupança(Conta):

   def passa_o_mes(self):
      self._saldo *= 1.01
      self._saldo -= 3

class ContaInvestimento(Conta):

   pass

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

>>> [>>Codigo 16 Saldo 998<<]

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

>>> [>>Codigo 17 Saldo 1007.0<<]

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
  conta.passa_o_mes() # duck typing

print(conta16)
print(conta17)

>>> [>>Codigo 16 Saldo 998<<]
>>> [>>Codigo 17 Saldo 1007.0<<]
```

Caso eu esqueça de criar o método `passa_o_mes` em todas as classes filhas, quando for utilizar a iteração sobre todos os elementos da lista vai dar erro, aqui eu posso instanciar o objeto `ContaInvestimento`, porém ao iterar sobre uma lista  que o contém e utilizar o método `passa_o_mes` ocorrerá um erro, uma vez que essa classe não tem o método `passa_o_mes`. Para corrigir temos algumas alternativas. Uma é definir o método `passa_o_mes` na classe mãe `Conta` o que com um `raise` para caso a pessoa que esta fazendo a implementação das classes filhas esquecer de sobrescrever esse método aparecer o erro

```python
class Conta:

   def __init__(self, codigo):
       self._codigo = codigo
       self._saldo = 0

   def deposita(self, valor):
      self._saldo += valor

   def passa_o_mes(self):
      raise NotImplementedError

   def __str__(self):
      return "[>>>código {} Saldo {}<<<]".format(self._codigo, self.saldo)
```

Porém esse erro só vai aparecer quando o método `passa_o_mes` for chamado, para evitar isso podemos utilizar um `@abstractmethod` assim logo que o objeto for instanciado já vai acusar o erro.

```python
from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

   def __init__(self, codigo):
       self._codigo = codigo
       self._saldo = 0

   def deposita(self, valor):
      self._saldo += valor

   @abstractmethod
   def passa_o_mes(self):
      raise NotImplementedError

   def __str__(self):
      return "[>>>código {} Saldo {}<<<]".format(self._codigo, self.saldo)

class ContaInvestimento(Conta):

   pass
```

Como já visto anteriormente precisamos implementar o método `__eq__` para fazer comparações entre objetos, pois por padrão a operação `eq` vai comparar o endereço de memória dos objetos, que sempre serão diferentes e não seu conteúdo. Outra coisa importante é comparar também o tipo do objeto, pois caso os objetos possuam os mesmos atributos, mas são de tipos diferentes, uma implementação simples do método `__eq__` irá retornar como `True`. Por exemplo uma conta salário e um conta corrente, ambas como o mesmo código de conta e mesmo saldo podem ser consideradas iguais de o tipo do objeto não for verificado, para isso podemos verificar o `type` do outro objeto a ser comparado, essa comparação permite apenas uma comparação direta, é ou não é, outra forma de fazer isso é verificar se o outro objeto é da mesma instância do nosso, `isinstance(ContaCorrente(37), ContaCorrente)`, essa forma é útil quando temos herança dentro das nossas classes, pois `ContaCorrente` herda de `Conta`, portanto a verificação do `isinstance` do `ContaCorrente(37)` com o tipo `Conta` também será verdadeira.

```python
class ContaCorrente

    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._valor)

class ContaSalario

    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        return self._codigo == outro._codigo and self._saldo == self._saldo

    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._valor)

conta1 = ContaCorrente(37)
conta2 = ContaSalario(37)

conta1 == conta2
>>> True

class ContaCorrente

    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._valor)

class ContaSalario

    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        ou
        if not isinstance(outro, ContaSalario):
           return False
        return self._codigo == outro._codigo and self._saldo == self._saldo

    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._valor)

conta1 = ContaCorrente(37)
conta2 = ContaSalario(37)

conta1 == conta2
>>> False
```

Dentro dos vários métodos buitins do python, um que também é muito útil é o `enumerate()` , esses método percorre uma lista enumerando seus elementos devolvendo um objeto do tipo `enumerate` que contem um lista com tuplas, onde o primeiro elemento é o índice daquele elemento e o segundo o valor da lista passada para o `enumerate`. Assim como o `range()` o `enumerate()` não gera a sequência assim que definimos ele, precisamos forçar essa criação, pois esses dois métodos são *lazy*, eles deixam tudo pronto e só vão gerando a medida que o programa solicita. Uma das formas de percorrer o `enumerate()` é com um `list`

```python
idades = [15, 87, 32, 65, 56, 32, 49, 37]
list(enumerate(idades))

>>> [(0, 15), (1, 87), (2, 32), (3, 65), (4, 56), (5, 32), (6, 49), (7, 37)]
```

Outra forma de passar por todos os valores que o `enumerate` gera é com um laço `for`, dessa forma temos maior controle de como vamos imprimir as `tuplas` geradas pelo `enumerate`, inclusive podemos “desempacotar” a `tupla`, passando duas variáveis para o laço `for` da seguinte maneira `for variable1, variable2 in enumerate(list)):`

```python
for valor in enumerate(idades):
  print(valor)

(0, 15)
(1, 87)
(2, 32)
(3, 65)
(4, 56)
(5, 32)
(6, 49)
(7, 37)

for indice, idade in enumerate(idades): # desempacotando a tupla
  print(indice, idade)

0 15
1 87
2 32
3 65
4 56
5 32
6 49
7 37

for indice, idade in enumerate(idades): # alterando a forma de imprimir a tupla
  print(indice, "x", idade)

0 x 15
1 x 87
2 x 32
3 x 65
4 x 56
5 x 32
6 x 49
7 x 37
```

Inclusive, essa forma de desempacotar as `tuplas` não precisa ser usada somente com `enumerate`, pode ser utilizada com qualquer `tupla` de qualquer tamanho, só precisamos passar a mesma quantidade de variáveis que a `tupla` tem como elementos para o laço `for`, porém nem todas as variáveis precisam estar declaradas, caso tenha elementos da `tupla` que não iremos utilizar podemos passar um underline no lugar daquela variável, apenas para  marcar o lugar daquele elemento da `tupla`. Isso inclusiva nos permite imprimir apenas os elementos que temos interesse. É uma boa prática nomear todas as variáveis, pois facilita quando precisar rever o código, ou quando outra pessoa for dar manutenção, pois assim não precisaremos ficar adivinhando a posição de cada elemento da nossa tupla

```python
usuraios = [
gui = ("Guilherme", 28, 1995),
vini = ("Vinicius", 24, 1999),
rogerio = ("Rogerio", 51, 1971)
]

for nome, idade, nascimento in usuarios: 
  print(nome)

Guilherme
Vinicius
Rogerio

for nome, _, _ in usuarios: 
  print(nome)

Guilherme
Vinicius
Rogerio
```

Podemos ordenar uma lista de algumas formas. Podemos gerar uma nova lista com a ordem que desejamos, ou podemos ordenar a lista em si, alterando seus valores, pois listas são mutáveis. Da primeira maneira utilizamos o método `sorted()` e passamos como parâmetro a lista que queremos ordenar. Como esse é um método *guloso* ele já nos devolve uma nova lista completa, ordenando nosso valores do menor para o maior

```python
idades = [15, 87, 32, 65, 56, 32, 49, 37]
sorted(idades)

>>> [15, 32, 32, 37, 49, 56, 65, 87]
```

A lista também pode ter sua ordem invertida com o método `reversed()` , mas como esse é um método *lazy* ele não vai retornar uma lista e sim um objeto iterável com a nossa lista invertida, para acessar os valores dessa lista invertida podemos utilizar o `list()`

```python
list(reversed(idades))

>>> [37, 49, 32, 56, 65, 32, 87, 15]
```

Agora para ordenar a lista do maior para o menor temos duas abordagens diferentes, pois o próprio método `sorted()` já tem como um de seus parâmetros a opção de inverter o ordenamento, esse parâmetro é o `reverse` que por padrão tem seu valor como `False`, mas como já foi visto o `sorted()` é um método *guloso*, enquanto que a outra abordagem seria utilizar o `sorted()` normalmente e então passar seu resultado para o `reversed()` que é um método *lazy*, e assim não iria gerar todo a lista de uma só vez, o que para lista muito grandes pode ser vantajoso.

```python
sorted(idades, reverse=True)

[87, 65, 56, 49, 37, 32, 32, 15]

list(reversed(sorted(idades)))

[87, 65, 56, 49, 37, 32, 32, 15]
```

Os métodos `sorted()` e `reversed()` não alteram a lista inicial, portanto se chamarmos a lista `idades` seus elementos ainda estarão na mesma ordem, para alterar a lista “no lugar” precisamos utilizar o método `.sort()`, que por baixo dos panos chama o método `sorted()`, e também possui como um de seus parâmetros a opção `reverse`.

```python
idades

>>> [15, 87, 32, 65, 56, 32, 49, 37]

idades.sort()
idades

>>> [15, 32, 32, 37, 49, 56, 65, 87]

```

O motivo do `sorted` ser **guloso** e o `reversed` ser ****lazy**** é que para ordenar uma lista o método precisa percorrer toda a lista para ter certeza de que aquele é o menor elemento, enquanto que para inverter a ordem de uma lista ele só precisa saber quem é o último, depois o penúltimo e assim por diante. Alguns elementos são fáceis de se ordenarem, pois já possuem uma ordem natural, como o caso de números e strings. No caso das strings, elas são ordenadas de A-Za-z.

```python
nomes = ["Guilherme", "Daniela", "Paulo"]
sorted(nomes)

>>> ['Daniela', 'Guilherme', 'Paulo']

nomes = ["guilherme", "Daniela", "Paulo"]
sorted(nomes)

>>> ['Daniela', 'Paulo', 'guilherme']
```

Para ordenar objetos não é tão simples, pois o método `sorted` utiliza o comparador `<` para determinar quem é o menor elemento de uma lista e como o método não sabe quem comparar dentro do objeto não conseguimos utilizar o `sorted` dessa forma simples, para isso precisamos utilizar uma `key`, que é uma função que irá retornar o valor a ser utilizado na comparação para determinar o menor elemento. Essa função pode ser definida anteriormente, ou utilizando a função anônima `lambda` do python

```python
class ContaSalario:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in contas:
  print(conta)

>>> [>>Codigo 17 Saldo 500<<]
>>> [>>Codigo 3 Saldo 1000<<]
>>> [>>Codigo 133 Saldo 510<<]

def extrai_saldo(conta):
  return conta._saldo

sorted(contas, key=extrai_saldo)

>>> [<__main__.ContaSalario at 0x7f48460f6470>,
 <__main__.ContaSalario at 0x7f48460f64e0>,
 <__main__.ContaSalario at 0x7f48460f64a0>]

for conta in sorted(contas, key=extrai_saldo):
  print(conta)

>>> [>>Codigo 17 Saldo 500<<]
>>> [>>Codigo 133 Saldo 510<<]
>>> [>>Codigo 3 Saldo 1000<<]

for conta in sorted(contas, key=lambda conta: conta._saldo):
  print(conta)

>>> [>>Codigo 17 Saldo 500<<]
>>> [>>Codigo 133 Saldo 510<<]
>>> [>>Codigo 3 Saldo 1000<<]
```

Outra forma de definir o parâmetro `key` é acessando o atributo diretamente, mas para isso precisamos do método `attrgetter` que precisa ser importado da biblioteca `operator`.

```python
from operator import attrgetter

for conta in sorted(contas, key=attrgetter("_saldo")):
  print(conta)

>>> [>>Codigo 17 Saldo 500<<]
>>> [>>Codigo 133 Saldo 510<<]
>>> [>>Codigo 3 Saldo 1000<<]
```

Um problema dessas duas abordagens é a necessidade de acessar um atributo privado da minha classe para fazer esse ordenamento

Uma maneira de evitar acessar esse atributo privado fora do escopo do objeto é definindo dentro da classe um ******dunder****** que permita a comparação de menor que, esse ******dunder****** é o `__lt__`, como a comparação `>` é inversa que a `<`, ao implementarmos o `__lt__` ”ganhamos” o `>` junto

```python
class ContaSalario

    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == self._saldo

    def __lt__(self, outro):
        return self._saldo < outro._saldo

    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._valor)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

conta_do_guilherme < conta_da_daniela

>>> True

conta_do_guilherme > conta_da_daniela

>>> False

for conta in sorted(contas):
  print(conta)

>>> [>>Codigo 17 Saldo 500<<]
>>> [>>Codigo 133 Saldo 510<<]
>>> [>>Codigo 3 Saldo 1000<<]
```

Em alguns casos o atributo que estamos usando para realizar o ordenamento é igual entre diferentes elementos, nesse caso podemos passar um critério de desempate, caso contrário o python manterá a ordem que os elementos apareceram. Quando utilizamos o parâmetro `key` em conjunto com o `attrgetter` podemos passar diretamente o criterio de desempate no `attrgetter`

```python
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
  print(conta)
```

Nesse caso o `sorted` irá ordenar primeiro pelo saldo e caso duas contas possuam o mesmo saldo ele ira ordenar pelo código. Também é possível fazer esse desempate dentro da classe, para isso basta verificar se o primeiro critério de comparação é igual, caso sim, definir o segundo critério

```python
class ContaSalario

    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == self._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._valor)

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(500)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas):
  print(conta)

[>>Codigo 3 Saldo 500<<]
[>>Codigo 133 Saldo 500<<]
[>>Codigo 1700 Saldo 500<<]
```

Ao todo temos 6 operações de comparação possiveis: igual (`==`), diferente (`!=`), menor que (`<`), maior que (`>`), menor igual (`<=`), maior igual (`>=`). Para não precisar implementar todas essas funções podemos utilizar um `decorator` na nossa classe e definir apenas duas dessas operações, a de igualdade (`__eq__`) e uma das outras entre `__lt__  __le__  __gt__  __ge__`, para isso basta importar o método `total_ordering` da biblioteca `functools` e decorar nossa classe com ele.

```python
from functools import total_ordering

@total_ordering
class ContaSalario:

    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == self._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._valor)
```