# Python: começando com a linguagem

Lista de comandos uteis:

```python
print("fdsfsdfsdf", chute)
```

imprime o que está dentro das aspas e concatena com a variável (chute)

```python
chute = input("digite o seu numero: ")
```

O comando input “trava” o terminal esperando para o usuário digitar alguma coisa que pode ser atribuído a uma variável, porém esse comando sempre devolve uma variável do tipo string, se quiser utilizar como número precisamos fazer a conversão com int

```python
chute = int(chute_str)
```

Podemos usar o sinal de mais para concatenação de strings

```python
nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)

nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome)
```

Ambos os códigos irão imprimir: NicoSteppat. Como não tem espaço em nenhuma variável o nome fica grudado, caso queria inserir um espaço entre o nome e o sobrenome podemos modificar o separador padrão da função print

```python
nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome, sep="_")
```

Imprime: Nico Steppat

No pyhton o if precisa ser indentado com 4 espaços, ou um tab e : depois da condição

```python
if condição:
   print("True")
elif condição2:
	print("True2")
else:
   print("False")
```

Isso também serve para outras estruturas como o while e o for

Uma forma mais elegante de fazer o print de strings e utilizando a interpolação de strings com a função format (para chamar função no pyhton usamo o ponto → .format), que substitui os {} pelo texto que você passa para a função na ordem que os {} aparecem

```python
print("Tentativa {} de {}".format(rodada, total_de_tentativas)
```

É muito comum utilizar o loop for com a função range, que “gera” uma sequência de valores, sendo o primeiro inclusivo e o ultimo exclusivo

```python
for rodada in range(1,10):
    print("rodada")
```

Precisamos de uma variável que vai receber cada valor do range. No caso do exemplo acima o resultado seria o seguinte:

```python
1
2
3
4
5
6
7
8
9
```

Caso não especificamos o inicio do range ele vai ser 0.

Para interromper um loop no meio podemos usar o comando break, além dessa opção temos também o continue, que ignora o resto do código que está no loop e vai para uma nova iteração do laço.

Um pouco mais sobre interpolação de strings:

Podemos mudar a ordem que as strings vão ser inseridas no texto especificando o índice dessa string:

 

```python
print("Tentativa {1} de {0}".format(3,10))

>>> Tentativa 10 de 3
```

Também é possível formatar com a string irá aparecer, para isso precisamos digitar, entre as chaves, : e o formato, sendo f para float e d para inteiro. De maneira similar ao fortran para definir o formato do float o primeiro valor é o tamanho total da string, incluindo o ponto e o segundo é a quantidade de casa decimais, porém no python o primeiro valor é opcional. Podemos preencher os espaços “vazios” com 0 apenas colocando o 0 na frente do identificador da parte inteira

```python
print("R$ {:.2f}".format(1.2))
print("R$ {:6.2f}".format(1.2))
print("R$ {:06.2f}".format(1.2))
print("R$ {:06.2f}".format(123.2))

print("Data {:2d}/{:2d}".format(2,4))
print("Data {:02d}/{:02d}".format(2,4))

>>> R$ 1.20
>>> R$   1.20
>>> R$ 001.20
>>> R$ 123.20

>>> Data  2/ 4
>>> Data 02/04
```

Para utilizar funções que não são buitins, como print(), int(), input(), precisamos declarar um import no começo do programa com o nome da biblioteca que contém a funções que vamos utilizar. Uma biblioteca muito comum é a random, que serve para gerar números aleatórios. Verificar a documentação do python para var todas as funções que essa biblioteca fornece, porém duas básicas são:

```python
import random

random.radom()  # imprime um núemro aleatório entre 0.0 e 1.0
random.randrange(10) # imprime um número aleatório entre 0 e 9
random.randrange(1,101,2) # imprime um número aleatório entre 1 e 100 com intervalo de 2
```

Precisamos tomar cuidado ao criar novas bibliotecas, pois elas são executadas logo quando são importadas, para isso não ocorrer precisamos englobar as funcionalidades da nossa biblioteca dentro de funções que serão chamadas dentro do programa em que importamos as bibliotecas. Para definir uma função em python usamos:

```python
def mome_da_funcao(parametros para a funcao):
    comandos da função
    return resultado de retorno da funcao
```

Da mesma forma que no if e no for precisamos indentar.

Ao fazer o processo anterior não conseguimos mais executar diretamente o programa contido na biblioteca, para “corrigir” isso podemos verificar se o nome do programa que está sendo chamado é igual ao nome da biblioteca e então chamar a função que executa o programa dentro da biblioteca:

```python
if __name__ = "__main__":
    jogar()
```


# Python: avançando na linguagem

Uma forma de percorrer uma string é utilizando o for:

```python
for letra in palavra_secreta:
   comandos aqui
```

O código acima atribui a variável letra, uma letra da palavra_secreta a cada iteração

É necessário sempre tratar as entradas dos usuários, pois eles podem digitar espaços indesejados no inicio ou final das strings, isso é feito com o método strip() e para comparação de caracter devemos tomar o cuidado de utilizar um método upper() ou lower(), pois o usuário pode digitar uma letra maiúscula e nossa referência estar em letras minúsculas.

Em python temos algumas estruturas de dados, uma muito comum de se utilizar é a lista que é iniciada com colchete [ ]. Importante lembrar que listas são diferentes de arrays. 

Comandos úteis com listas:

```python
valores = [0,1,2,3,4,5,8]
type(valores)
>>> <class 'list'>
valores
>>> [0, 1, 2, 3, 4, 5, 8]
0 in valores
>> True
9 in valores
>>> False
valores[0]
>>> 0
valores[6]
>>> 8
valores[9]
>>> IndexError: list index out of range
min(valores)
>>> 0
max(valores)
>>> 8
len(valores)
>>> 6
valores.append(9) # adiciona um elemento ao fim da lista
valores
>>> [0, 1, 2, 3, 4, 5, 8, 9]
valores.pop() # mostra o último elemento da lista e remove ele
>>> 9
valores
>>> [0, 1, 2, 3, 4, 5, 8]
```

Outra estruturas importante sãos as tuplas (tuple), sua diferença para a lista é que ela é imutável, portanto não aceita as funções .append(), .pop() e é declarada com parentêses.

```python
valores = (0,1,2,3,4,5,8)
type(valores)
>>> <class 'tuple'>
valores
>>> (0, 1, 2, 3, 4, 5, 8)
0 in valores
>> True
9 in valores
>>> False
valores[0]
>>> 0
valores[6]
>>> 8
min(valores)
>>> 0
max(valores)
>>> 8
len(valores)
>>> 6
valores.append(9) 
>>> 'tuple' object has no attribute 'append'
```

Podemos “misturar” tuplas e listas

```python
Nome='Rogério'
Filhos=['Gui','Vini']
type(Filhos)
>>> <class 'list'>
Cadastro=(Nome,Filhos)
type(Cadastro)
>>> <class 'tuple'>
Cadastro
>>> ('Rogério',['Gui', 'Vini'])
Filhos.append('Bia')
Cadastro
>>> ('Rogério',['Gui', 'Vini', 'Bia'])
Cadastro[1]
>>> ['Gui', 'Vini', 'Bia']
Cadastro[1][0]
>>> 'Gui'

p1=(1,1)
type(p1)
>>> <class 'tuple'>
p2=(2,4)
type(p2)
>>> <class 'tuple'>
p3=(3,9)
type(p3)
>>> <class 'tuple'>
p4=(4,16)
type(p4)
>>> <class 'tuple'>
Pontos=[p1,p2,p3,p4]
type(Pontos)
>>> <class 'list'>
Pontos
>>> [(1,1),(2,4),(3,9),(4,16)]
p5=(5,25)
Pontos.append(p5)
Pontos
>>> [(1,1),(2,4),(3,9),(4,16),(5,25)]
Pontos[1]
>>> (2,4)
Pontos[1][1]
>>> 4
```

Podemos converter uma lista em uma tupla e vice-versa

```python
exemplo=[1,2,3]
type(exemplo)
>>> <class 'list'>
exemplo
>>> [1, 2, 3]
exemplo = tuple(exemplo)
type(exemplo)
>>> <class 'tuple'>
exemplo
>>> (1, 2, 3)
exemplo = list(exemplo)
type(exemplo)
>>> <class 'list'>
exemplo
>>> [1, 2, 3]
```

Também existe uma coleção chamada set. Essa coleção não possui índice, porém ela não permite a inserção de elementos duplicados. Essa coleção é declarada com chaves {}. Para adicionar elementos a um set devemos usar .add() ao invés de .append()

```python
colecao = {11122233344, 22233344455, 33344455566}
colecao
>>> {11122233344, 33344455566, 22233344455}
# A ordem que é impressa não necessariamente é a mesma da que foi declarada
colecao.add(44455566677)
colecao
>>> {11122233344, 44455566677, 33344455566, 22233344455}
colecao.add(11122233344)
# Não vai dar erro, porém como o elemento já existe, a coleção não será alterada
colecao
>>> {11122233344, 44455566677, 33344455566, 22233344455}
colecao[0]
>>> Traceback (most recent call last):
>>>   File "<stdin>", line 1, in <module>
>>> TypeError: 'set' object does not support indexing
# Como não tem índice, da erro se tentar acessar um elemento
```

Mais uma estrutura de dados importante é o dicionário. Assim como o set ele usa chaves para ser declarado {}, porém cada elemento do dicionário é composto por um par chave : valor. Assim conseguimos, utilizando a chave, recuperar o que está salvo no valor.

```python
instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
instrutores['Flavio']
>>> 37
```

Um recurso muito útil da linguagem é o List Comprehension, que permite inicializar listas de uma forma muito interessante:

```python
frutas = ["maçã", "banana", "laranja", "melancia"]
lista = [fruta.upper() for fruta in frutas]
# inicializa a lista "lista" com os elemtentos da lista "frutas" em maiusculas

inteiros = [1,3,4,5,7,8]
quadrados = [n*n for n in inteiros]
# inicializa a lista "quadrados" com o auqdarado de cada elemento da lista "interios"
```

Podemos usar o if junto do for em List Comprehension

```python
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]

# inicializa a lista "pares" somente se if x % 2 == 0 for true
```

Para trabalhar com Leitura e escrita de arquivos precisamos primeiro abrir o arquivo com o comando open(), para isso atribuímos uma variável a ação de abrir o arquivo. É necessário passar no mínimo um parâmetro para o comando open(), que é o nome do arquivo, o segundo é opcional e é o modo com que vamos acessar esse arquivo, pode ser “w” para escrita, “r” para leitura, “a” para adicionar e “x” para criar o arquivo. As opções “w” e “a” criam um arquivo novo caso o arquivo não exista, porém a opção “w” apaga o conteúdo existente do arquivo, enquanto que a opção “a” vai para a última linha e adiciona o conteúdo a parti daí. A opção “r” dá erro caso você tente abrir um arquivo que não existe, enquanto que a opção “x” dá erro caso você tente criar um arquivo que já existe. Ainda temos as opções “r+” para leitura e escrita, posicionando o cursor no inicio do arquivo, “w+” para escrita e leitura, apagando o conteúdo do arquivo e posicionando o cursor no inicio do arquivo e “a+” para escrita e leitura do arquivo, posicionando porém o cursor no final do arquivo.

Para escrever no arquivo utilizamos a função .write(), não esquecer que é necessário utilizar \n para pular de linha, caso contrário o programa vai escrever tudo em uma linha única, sem espaço entre o conteúdo de um .write() e outro.

Para ler o arquivo utilizamos .read(), esse comando porém lê o arquivo inteiro. Para ler apenas uma linha temo o comando .readline(). Quando atingimos o final de um arquivo esses comando de leitura “não funcionam” mais, pois o cursor já está no final do arquivo e ele retorna uma string vazia de tamanho 0. Podemos ler cada linha do arquivo com um laço for.

É importante também fechar o arquivo quando acabamos de utiliza-lo, para isso usar a função .close().

```python
arquivo = open("Nome_do_arquivo","Modo_de_leitura")
arquivo = open("teste.dat","w") # cria o arquivo caso ele não exista ou apaga o conteúdo e coloca o cursor na primeira linha

arquivo.write("Inicio do arquivo\n")
arquivo.close()

# arquivo = open("teste.dat","w") esse comando iria apagar o conteúdo escrito acima

arquivo = open("teste.dat","a") # esse comando iria abrir o arquivo e colocar o curso na fim do arquivo

arquivo.write("Mais uma linha\n")

arquivo.close()

arquivo = open("teste.dat","r")
arquivo.read()
>>> 'Inicio do arquivo\nMais uma linha\n'
arquivo.read()
>>> ''

arquivo = open("teste.dat","r")
arquivo.readline()
>>> 'Inicio do arquivo\n'
arquivo.close()

arquivo = open("teste.dat","r")
for linha in arquivo:
    print(linha)
>>> Inicio do arquivo
>>>
>>> Mais uma linha
>>>

```

O excesso de linhas em branco é porque no final de cada linha temos o caractere especial “\n” que pula uma linha e o comando print() por sua vez já pula uma linha também. Para contornar isso podemos usar o .strip() na linha, pois ele também remove esse caractere especial.

As variáveis utilizadas dentro da cada função são exclusivas daquela função, de forma que mesmo utilizando o mesmo nome precisamos tomar o cuidado de passar o valor para essa variável com um return ou como parâmetro da função:

```python
import random

def jogar():

    imprime_mensagem_de_abertura()
    palavra_secreta = inicializa_palavra_secreta() # a variável palavra_secreta aqui recebe o resultado (return) da função "inicializa_palavra_secreta()", que por acaso tem o mesmo nome, mas poderia ser outro
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta) # aqui a variável letras_acertadas recebe o resultado (return) da função "inicializa_letras_acertadas()" que tem como parâmetro a variável palavra_secreta, que vira a variável palavra dentre de seu escopo.

def imprime_mensagem_de_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def inicializa_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero]

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]
```

Podemos ter funções com parâmetros opcionais, para isso basta definir o valor “padrão” do parâmetro quando definimos a função. Normalmente não precisamos nomear os parâmetros passados as funções, porém caso o primeiro parâmetro seja opcional e vamos declarar o segundo precisamos nomear esse parâmetro, pois caso contrário o programa irá interpretar essa parâmetro como sendo o primeiro.

```python
def carrega_palavra_secreta(nome_arquivo="palavras.txt"): # definie a função "carrega_palavra_secreta()" com um parâmetro opcional, ou seja, caso nenhum parêmetro seja passado para a função ele será igual a "palavras.txt"

def carrega_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=0): # define a função "carrega_palavra_secreta()" com dois parâmetros opcionais, podemos chamar essa função de diferentes formas

carrega_palavra_secreta() # tudo opcional nome_arquivo="palavras.txt", primeira_linha_valida=0
carrega_palavra_secreta("frutas.txt") # Apenas o segundo parâmetro opcional
carrega_palavra_secreta(nome_arquivo="frutas.txt") # Igual o anterior, porém com o parâmetro nomeado
carrega_palavra_secreta(5) # Não serve para definir o parâmetro primeira_linha_valida, pois como ele é o segundo, ao chamar a função estamos definindo o primeiro parâmtero nome_arquivo como 5 e o segundo continua sendo opcional
carrega_palavra_secreta(primeira_linha_valida=5) # Agora sim, o primeiro parâmetro é opcional e o segundo é definido como 5
carrega_palavra_secreta("frutas.txt", 5) # Ambos os parâmetro definidos
carrega_palavra_secreta(nome_arquivo="frutas.txt", primeira_linha_valida= 5) # igual ao anterior, porém com os parâmetros nomeados
carrega_palavra_secreta(primeira_linha_valida=5, nome_arquivo="frutas.txt") # Igual ao anterior, porém como os parâmetros estão nomeados podemos mudar a ordem
```
