# String em Python: extraindo informações de uma URL

Strings são elementos imutáveis em python, podemos até ter a impressão que podemos mudar uma o valor de uma string.

```python
palavra = "abc"
palavra = "def"
```

Quando fazemos isso apenas mudamos a referência da variável para outra string

```
palavra ---> "abc"

palavra\      "abc"
        \___> "def
```

Podemos confirmar isso tentando substituir um único caractere de uma string

```python
palavra = "abc"
print(palavra)

>>> "abc"

print(palavra[0])

>>> "a"

palavra[0] = "x"

>>> TypeError : 'str' object does not support assignment
```

Uma consequência disso é a economia de memória, pois já que a string é imutável, várias variáveis podem apontar para ela, podemos confirmar isso com a função `id()`

```python
x = "abc"
y = "abc"

print(id(x) == id(y))
>>> True
```

URLs podem ser divididas em duas grandes parte, a base que contém o domínio e a página que estamos acessando e os parâmetros que essa página precisa. Essa separação é feita pelo caractere `?`, assim a URL `[https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100](https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100tem)` tem como base `https://bytebank.com/cambio` em que `[https://bytebank.co](https://bytebank.comé)m` é a base e `/cambio` é a página e   `[?moedaOrigem=real&moedaDestino=dolar&quantidade=100](https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100tem)` são os parâmetros, como uma página pode precisar de mais de um parâmetro eles são divididos por `&`dessa forma essa URL tem três parâmetros moedaOrigem=real, moedaDestino=dolar e quantidade=100, o parâmetro é separado de seu valor por um sinal de igual.

Quando queremos separar apenas os parâmetros de uma URL podemos buscar com o método `string.find( )`a `?` e fazer um slice a partir do valor de sua posição +1, pois o primeiro valor do slice no python é inclusivo. Já quando queremos separar os parâmetros entre si podemos fazer uma busca pelo `&`após o índice do inicio do parâmetro que procuramos para fazer o slice corretamente, contudo temos que tomar cuidado, pois caso o parâmetro buscado seja o ultimo método `.fin()`vai retornar o valor `-1`portanto temos que usar um if para checar se o vlaor é `-1`ou não

```python
url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

indice_interrogacao = url.find("?")

url_base = url[:indice_interrogacao]
print(url_base)

url_parametro = url[indice_interrogacao + 1 :]
print(url_parametro)

print(url)

# parametro_busca = "quantidade"
parametro_busca = "moedaDestino"
# parametro_busca = "moedaOrigem"
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find("&", indice_valor)

if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]

print(valor)
```

Antes de continuar o programa de validação de URLs podemos fazer uma checagem se a URL que foi passada está vazia ou não, para isso basta usar um if comparando o valor da URL a uma string vazia, caso a comparação seja verdadeira é melhor avisar o usuário que a URL está invalida, que ela está vazia, isso se chama **levantar uma exceção**,, para isso utilizamos o método `raise`ao invés do return com o parâmetro `ValueError()`do pyhton que irá indicar para o nosso usuário um erro de valor e podemos incluir uma mensagem dentro do `ValueError()` com `ValueError(A URL está vazia!)`. Porém os problemas ainda não acabaram, pois no python uma string com espaços em branco é diferente de uma string vazia, assim temos que sanitizar nossa url antes de fazer a verificação de string vazia. Temos várias formas de fazer isso, podemos usar o `string.replace("valor_procurado","valor_que_vai_substituir")`da seguinte maneira `url = url.replace(" ","")`, contudo esse método só remove os espaços em branco, caso a string tenha algum caractere especial de formatação como `\t`para tabulação ou `\n`para quebra de linha, o `.replace()`não irá funcionar, então podemos usar o método `.strip()` da seguinte maneira `url = url.strip()`

Em python o valor `None`é de um tipo especial que não tem o método `.strip()`por exemplo, portanto para fazer a sanitização do nosso código é importante verificar se a url é uma string ou não com `if url == str:`. Outra funcionalidade do `if`do python é que ele tenta transformar a expressão que passamos para um boleano e ai sim com o valor `True`ou `False`que ele executa o código e alguns valores como `0`, `""`e `None`são identificados pelo python como `False`

Saindo um pouco da aplicação e indo para *RegEx - Regular Expressions*, o regex nos permite buscar por padrões de forma mais simples do que ficar fazendo um monte de condicionais if no código. Para trabalhar com regex no python é preciso importar a biblioteca `re`. Cada caractere no regex pode ser representado por uma série de valores válidos dentro de um par de colchetes, assim o elemento `[0123456789]`representa um digito qualquer. Se repetirmos isso 5 vezes vamos estar criando um padrão de 5 dígitos. Caso não tenhamos certeza se um caractere está ou não presente na nossa string podemos usar um ponto de interrogação depois dos colchetes para indicar que esse padrão pode aparecer uma ou nenhuma vez na minha string. Quando utilizamos a biblioteca `re`precisamos criar um padrão de busca com o método `re.compile(padrão_a_ser_procurado)`, pro exemplo, para criar um padrão para a busca de um CEP podemos criar a seguinte variável

```python
padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
```

Agora para buscar esse padrão na minha string preciso utilizar outro método da biblioteca `re`o `.search(string)`esse método retorna ou um objeto `match` caso ele encontre o padrão ou o valor `None`, com isso podemos utilizar um condicional `if`para checar o valor da busca, denso que `objeto match == True`e `None == False`. Uma vez que o `re`encontre o padrão na nossa string podemos acessar o valor do padrão com o método `.group()`, isso porque o objeto `match`possui outras informações, como por exemplo em qual posição da string é que o padrão foi encontrado.

```python
endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"

import re

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)
```

Para simplificar um pouco as coisas podemos utilizar intervalos e quantificadores na criação dos padrões do `re`. O intervalo funciona com um hífen dentro dos colchetes para indicar um intervalo de valores válidos, assim `[0123456789]` é igual q `[0-9]`que representa o intervalo de números de 0 até 9. Já os quantificadores são expressos entre chaves logo após um grupo, assim o padrão `[0-9]{5}` indica um conjunto de 5 dígitos de 0 até 9. Para os quantificadores também podemos passar um limite colocando virgulas na hora de passar o quantificador, assim `[-]?`é igual a `[-]{0,1}`, pois a interrogação tem o significado de uma ou nenhuma vez. 

Utilizando regex para validar nossa URL podemos verificar de ela começa com https:// ou http:// se tem ou não o www. e se termina com .br ou não, além de garantir que vai ter bytebank.com/cambio. Como estamos procurando uma string e não um conjunto de caracteres colocamos essa string que procuramos entre parênteses para poder utilizar a interrogação como um quantificador de pode aparecer uma ou nehuma vez, `(http(s)://)?` como o s do `https`é apenas um caractere poderiamos ter escrito da seguinte forma também `(https?://)?`. Assim a validação completa da URL fica:

```python
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")
```

Aqui utilizamos o método `.match()` e não o método `.search()` pois queremos verificar se a string inteira bate com nosso padrão e não apenas de o nosso padrão pode ser encontrado dentro da nossa string, em outra posição, por exemplo.

Como já vimos no curso anterior existem métodos especiais, os dunder, qu implementam funcionalidades a nossa classe que aproximam ela de um objeto “padrão”do python, podendo utilizar métodos como o `.len()`e iterar sobre o objeto. As classes built-ins do python já tem esses métodos implementados, podemos acessar uma lista dos métodos de uma certa classe utilizando o método `dir(classe)`, por exemplo o comando `dir(str)`retorna:

```python
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

Quando usamos o comparador `==`no python ele está na verdade chamando o método `__eq__`para verificar se o argumento da esquerda é igual ao argumento da direita, então quando tentamos comparar objetos que não tem um implementação do método `__eq__`o python retorna erro, pois nesse caso ele está comparando o endereço de memória dos objetos, que claramente são diferentes, mesmo que eles possuam os mesmos atributos. Para comparar os atributos podemos definir o método `__eq__`dentro da nossa classe

```python
    def __eq__(self, other):
        return self.url == other.url
```

Como já visto no começo do curso podemos verificar o endereço de um objeo com o método `id()` e é isso que o python faz, busca o endereço dos objetos para compara-los, caso não tenhamos definido o método `__eq__`. Em alguns casos, mesmo possuindo endereços de memória diferentes o python pode retornar um valor `True`para uma comparação em alguns casos, como por exemplo o númeor `1`quando comparado com o valor `True`retorna `True`, mesmo possuindo valore diferentes de memória. Para comparar diretamento o valor de memória das variáveis devemos utilizar o comparador `is`, assim `1 is True`retorna `False`, pois eles não possuem o mesmo endereço de memória.