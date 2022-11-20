# Python: entendendo a Orientação a Objetos

A ideia central do paradigma de orientação a objetos é que dados e funcionalidades andem juntos, assim podemos encapsular e “garantir” como algumas coisas são criadas.

Para definir um objeto utilizamos o comando `class` e o nome do objeto

```python
class Conta:
    pass
```

Quanto “chamamos” o objeto o que é passado é o endereço na memória onde este objeto foi alocado, podemos atribuir isso a uma variável

```python
>>> from conta import Conta
>>> conta = Conta()
>>> conta
<conta.Conta object at 0x7ffac3d96f10>
```

Funções que começam com dois underline (`__`) são funções construtoras, elas são chamas logo após o instanciamento do objeto são executadas. Uma dessas funções é a `__init__` que inicializa o objeto, é nela que adicionamos as propriedades para construção do objeto e sempre tem como um do parâmetros a variável self que nada mais é do que a referência para o endereço na memória do objeto

```python
class Conta:

    def __init__(self):
        print("Construindo um objeto ... {}".format(self))
```

```python
>>> from conta import Conta
>>> conta = Conta()
Construindo um objeto ... <conta.Conta object at 0x7ffac3d96f10>
```

Para atribuir os valores que usamos ao inicializar o objeto utilizamos o `self` para acessar e atribuir esses valores

```python
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo um objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limit
```

Agora precisamos passar essas 4 propriedades na hora de criar o objetos, caso contrario ele da erro

```python
>>> from conta import Conta
>>> conta = Conta(123, "Gui", 55.0, 100.0)
Construindo um objeto ... <conta.Conta object at 0x7ffac3d96f10>
```

Podemos utilizar construtores com valores padrão caso algum atributo do objeto não varie muito

```python
class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Construindo um objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limit
```

Dessa forma todas as contas que forem criadas terão o valor de limite igual a 1000 sem que eu precise informar isso. Caso eu queira alterar esse valor para alguma conta especifica, basta passar o valor diferente para o atributo na hora de construir o objeto

```python
>>> conta1 = Conta(1, "Fulano", 0.0)
>>> conta2 = Conta(2, "Beltrano", 0.0)
>>> conta3 = Conta(3, "Sicrano", 0.0, 2000.0)
```

Para acessar o valor dos atributos do objeto utilizamos um ponto e o nome do atributo

```python
>>> conta.saldo
55.0
```

Atributos são as informações que um objeto tem e métodos são o que o objeto pode fazer

Para adicionar métodos dentro do objeto precisamos utilizar o comando `def` e, se vamos utilizar algum atributo do objeto precisamos passar o `self`

```python
class Conta:
    def __init__(self, numero, titular, saldo, limite):

        print("Construindo um objeto ...")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo do titular {} é R${:.2f}".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
```

Para acessar os métodos de um objeto é igual ao atributo, com ponto e o nome do método, para precisamos utilizar parênteses `()`

```python
>>> from conta import Conta
>>> conta = Conta(123, "Gui", 55.0, 100.0)
Construindo um objeto ...
>>> conta.extrato()
O saldo do titular Gui é R$55.00
>>> conta.deposita(100)
>>> conta.extrato()
O saldo do titular Gui é R$155.00
>>> conta.saca(500)
>>> conta.extrato()
O saldo do titular Gui é R$-345.00
```

Quando modificamos uma variável que guardava o endereço para um objeto esse objeto fica perdido sem ter como ser encontrado e fica ocupando memória, para evitar isso o python tem um Garbage Collector que procura esses objetos, joga fora e libera a memória. Com relação a isso, caso seja necessário, podemos desreferenciar um objeto de um variável, para isso precisamos “atribuir” o valor `None` para ela

```python
>>> conta = None
```

É importante garantir que os atributos não possam ser alterados de forma direta, caso tenhamos um método para fazer essa alteração é mais segura utilizar apenas o método. Uma forma de fazer isso é tornando os atributos privados, de forma que dificulte o acesso do usuário a esses atributos, para fazer isso basta adicionar dois underline antes do nome do atributo dentro do `__init__`. 

```python
class Conta:
    def __init__(self, numero, titular, saldo, limite):

        print("Construindo um objeto ...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo do titular {} é R${:.2f}".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
```

Assim quando importar o module do python ele não vai disponibilizar esses atributos no autocomplete dele, apenas os métodos que estão públicos, contudo ainda é possível acessar atributos privados caso você saiba de existência deles, o acesso é feito da seguinte forma: 

```python
>>> from conta import Conta
>>> conta = Conta(123, "Gui", 55.0, 100.0)
Construindo um objeto ...
>>> conta._Conta__saldo
55.0
```

A utilização de atributos privados é muito útil, porém caso seja necessário acessar esse atributo de forma simples ou fazer alguma alteração precisaremos de algum método para isso. Uma forma comum de se fazer isso é criando métodos que começam com `get_nome_do_método` para acessar os atributos e `setter_nome_do_método` para alterar os atributos, pois assim fica fácil para o usuário acessar/alterar os valores desses atributos. Contudo isso causa um transtorno no usuário, pois mesmo acessando o valor de um atributo precisaremos utilizar a sintaxe de um método com parênteses `conta.saldo()` e não `conta.saldo`. O python tem uma solução para isso que é a utilização de `@property` antes de getters e `@nome_do_atributo.setter` para setters, porém esses atributos precisam estar privados para a utilização dessa funcionalidade

```python
class Conta:
    def __init__(self, numero, titular, saldo, limite):

        print("Construindo um objeto ...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo do titular {} é R${:.2f}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
```

Dessa forma podemos acessar os atributos privados da seguinte maneira:

```python
>>> from conta import Conta
>>> conta = Conta(123, "Gui", 55.0, 100.0)
Construindo um objeto ...
>>> conta.numero
123
>>> conta.titular
'Gui'
>>> conta.saldo
55.0
>>> conta.limite
100.0
>>> conta.limite = 1000.0
>>> conta.limite
1000.0
```

Assim como os atributos podem ser privados os métodos também e para isso basta adicionar dois underline antes do nome do método

```python
class Conta:
    def __init__(self, numero, titular, saldo, limite):

        print("Construindo um objeto ...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo do titular {} é R${:.2f}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __credito_disponivel(self, valor_a_sacar):
        credito_total = self.__saldo + self.__limite
        return valor_a_sacar <= credito_total

    def sacar(self, valor):
        if self.__credito_disponivel(valor):
            self.__saldo -= valor
        else:
            print("Você não possui crédito suficiente para sacar o valor de R${:.2f}.".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
```

Pode ser necessário acessar alguma informação antes mesmo de criar o objeto, quando essa informação for comum a todos os objetos, por exemplo. Para isso podemos criar um método de classe, podendo assim acessar esse valor apenas importando a classe. Essa funcionalidade é implementada com o decorator `@staticmethod`

```python
@staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_dos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
```