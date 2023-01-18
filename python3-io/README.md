# Python: trabalhando com I/O

A primeira coisa importante ao se trabalhar com arquivos é ter a certeza que estamos utilizando o ********encoding******** correto. O encoding é o responsável por traduzir os caracteres que utilizamos em bits para serem armazenados no computador. Por exemplo o ASCII utiliza uma representação de 128 bits para cada caractere, isso é o suficiente para armazenar todas as letras maiúsculas e minúsculas e alguns caracteres especiais, porém não consegue armazenar letras com acentos, o cedilha entre outros elementos. Para utilizar esses caracteres precisamos de um outro encoding, um do mais utilizados é o UTF-8, que utiliza de um a quatro bytes (8bits) para representar os caracteres. Outra encoding comum aqui no Brasil é o `Latin1` ou `ISOIEC 8859-1` que trazem os caracters normalmente utilizados em linguas latinas. O python utiliza por padrão o encoding que o sistema operacional está utilizando, que na maioria dos casos é o UTF-8. Caso o arquivo que vamos trabalhar esteja em um formato diferente precisamos ou converter o arquivo para o formato padrão do nosso sistema operacional, ou em alguns casos que não podemos converter o arquivo, basta informar para o python qual o encoding do arquivo.

```python
arquivo = open("local_para_o_arquivo/nome_do_arquivo", encoding="latin_1")
```

Uma das formas de se ler o conteúdo de um arquivo é com o método `.readlines()`, que le todas as linahs do arquivo.

Quando lemos algum conteúdo de um arquivo e atribuimos esse conteudo para uma variável, cada linha do nosso arquivo é um item do tipo ******string****** de uma lista que tem o caractere especial **\n** ao final, que é o caractere padrão para uma nova linha. É esse caractere especial que o python busca quando esta fazendo a leitura do arquivo para saber quando uma linha terminou. Como método `print()`, por padrão já imprime uma nova linha ao terminar de imprimir o conteúdo da variável, isso faz com que em uma iteração sobre o conteúdo de um arquivo o python imprima uma linha em branco entre cada entrada, pois ele quebrou uma vez a linha com o caractere **\n** da variável e outra vez pelo comportamento padrão do `print()`. Para evitar isso basta passar o parâmetro `end=""` para o `print()`, assim ele não irá imprimir a linha padrão ao terminar a variável.

```python
arquivo = open("local_para_o_arquivo/nome_do_arquivo", encoding="latin_1")

conteudo = arquivo.readlines()

for linha in conteudo:
    print(linha)

>>> 1,Guilherme,guilherme@guilherme.com.br

2,Elias,elias@elias.com.br

3,Gabriel,gabriel@gabriel.com.br

4,Anderson,anderson@anderson.com.br

5,Alex,alex@alex.com.br

6,Vini,vini@vini.com.br

7,Letícia,leticia@leticia.com.br

8,Giulia,giulia@giulia.com.br

9,Felipe,felipe@felipe.com.br

10,Luísa,luisa@luisa

arquivo = open("local_para_o_arquivo/nome_do_arquivo", encoding="latin_1")

conteudo = arquivo.readlines()

for linha in conteudo:
    print(linha, end="")

>>> 1,Guilherme,guilherme@guilherme.com.br
2,Elias,elias@elias.com.br
3,Gabriel,gabriel@gabriel.com.br
4,Anderson,anderson@anderson.com.br
5,Alex,alex@alex.com.br
6,Vini,vini@vini.com.br
7,Letícia,leticia@leticia.com.br
8,Giulia,giulia@giulia.com.br
9,Felipe,felipe@felipe.com.br
10,Luísa,luisa@luisa
```

Outra forma de se ler as linhas de um arquivo é com o método `.readline()`, no singular. Quando abrimos um arquivo o python “coloca um ponteiro no início do arquivo, ao utilizar o método `.readline()` o python avança esse ponteiro pela linha até encontrar o caractere especial de quebra de linha (**\n**), então para de avançar a leitura. Quando chamamos esse método pela segunda vez, esse ponteiro é movido para a linha de baixo e começa a avançar novamente até encontrar o \n.

O método `.readline()` aceita um argumento, um númeor inteiro, que é a quantidade de caracteres para ler, pois algumas vezes estamos interessados apenas no começo da linha. Caso a quantidade de caracteres especificado seja maior do que a nossa linha tem ele não avança para a proxima linha. Uma vez que especificamos a quantidade de caracteres a serem lidos, o ponteiro de leitura do python vai parar no meio da linha, ao chamar o método `.readline()` novamente, o ponteiro ira avançar até encontrar o \n daquela linha.

Uma vantagem de usar o método `.readline()` ao invés do `.readlines()` é que o primeiro le apenas uma linha, economizando memória, enquato que o segundo método le todo o conteúdo do arquivo de um só vez e com isso ocupa mais memória do nosso sistema.

Uma terceira forma de se ler as linhas de um arquivo é com um laço for em cima do arquivo:

```python
f = open("./dados/contatos.csv", encoding="latin_1")

for l in f:
    print(l, end="")
```

Para escrever alguma informação em um arquivo com o python basta utilizar o método `.write("texto_para_ser_escrito")`, mas antes precisamos alterar o modo padrão de abertura de arquivos do python, que é de somente leitura, (mode=’r’). Para isso temos 3 modos que podem ser utilizados:

- ‘a’: esse modo funciona como um método `.apend()`, pois posiciona o ponteiro de escrita no final do arquivo, depois do último caractere, caso o arquivo não exista, um novo arquivo com o nome especificado é então criado.
- ‘w’: com esse modo o python apaga todo o conteúdo do arquivo original e sobreescreve o conteúdo que estamos escrevendo, também cria um arquivo novo caso o arquivo em questão não exista.
- ‘x’: muito similar ao modo ‘w’, mas nesse caso o arquivo não pode existir previamente, ele precisa ser criado na hora da excução.

Com isso conseguimos escrever o que queremos no arquivo. É importante também aundo vamos escrever algum text adicionar o caractere de quebra de linha ,\n, para que a próxima entrada não ocorra na mesma linha.

```python
f = open("./dados/contatos-novo.csv", encoding="latin_1", mode="w")

contatos = [
    "11,Carol,carol@carol.com.br\n",
    "12,Ana,ana@ana.com.br\n",
    "13,Tais,tais@tais.com.br\n",
    "14,Felipe,felipe@felipe.com.br\n",
]

for contato in contatos:
    f.write(contato)
```

Porém ao chamar o método `.write()` o python não escreve automaticamente no arquivo. Programas em python só realizam a esxrita de fato em arquivo quando não estamos mais trabalhando com eles, ou seja, quando o arquivo for fechado e isso pode ocorre de duas maneiras, ou quando o porgrama é encerrado, ou quando utilizamos o método `.close()`.

```python
f = open("./dados/contatos-novo.csv", encoding="latin_1", mode="w")

contatos = [
    "11,Carol,carol@carol.com.br\n",
    "12,Ana,ana@ana.com.br\n",
    "13,Tais,tais@tais.com.br\n",
    "14,Felipe,felipe@felipe.com.br\n",
]

for contato in contatos:
    f.write(contato)

f.close()
```

Contudo existem alguns sistemas que não é pratico ficar fechando e abrindo o mesmo arquivo todoa hora, somente para forçar o python escrever o que queremos, por isso existe o método `.flush()`, que obriga o python a atulizar o arquivo, escrevendo o que queremos, porém sem fechar o mesmo.

Caso seja necessário tanto escrever como ler o conteúdo de um arquivo precisamos adicionar o sinal +, que simboliza a ideia de update do arquivo. A leitura sempre ocorre a partir de onde o ponteiro de leitura/escrita está posicionado, portanto, se estamos em alguma posição no meio do arquivo o precesso de leitura se dará a partir desse ponto. Uma forma de alterarmos a posição do ponteiro de leitura é com o método `.seek(posição_desejada)`, assim, após ler todo o conteúdo de um arquivo podemos retornar para o inicio com o comando `file.seek(0)`. Temos que tomar cuidado com operações de escrita quando estamos no meio do arquivo, pois a quebra de linha é algo apenas visual, o python interpreta tudo de forma continua.

Outro ponto importante é a forma como abrimos o arquivo:

- ‘r+’: abre o arquivo para leitura e escreita com o ponteiro de leitura no inicio do arquivo. Começa o processo de escrita no ponto onde o ponteiro está, mesmo que no meio do arquivo, substituindo em sequência os caracteres, inclusive caracteres especiais como \n
- ‘w+’: abre o arquivo para leitura e escreita com o ponteiro de leitura no inicio do arquivo, porém apaga todo o conteudo do arquivo. Começa o processo de escrita no ponto onde o ponteiro está, mesmo que no meio do arquivo, substituindo em sequência os caracteres, inclusive caracteres especiais como \n
- ‘a+’: abre o arquivo para leitura com o ponteiro de leitura no final do arquivo. Não importa onde o ponteiro de leitura/escrita está começa o processo de escrita no final, mesmo que no meio do arquivo.

Quando um mesmo arquivo é aberto e atribuido a duas variáveis diferentes, ocorre uma concorrência de escrita no arquivo. Como, por padrão o primeiro arquivo que o python fecha sozinho é o primeiro que foi instanciado, caso não forcemos a escrita dos nossos dados no arquivo com o método `.flush()`, é o segundo processo de escrita que levará vantagem e terá seu conteúdo salvo.

```python
arquivo1 = open("dados.csv", mode="w")
arquivo2 = open("dados.csv", mode="w")

ana = "1,ana,ana@ana.com.br\n"
eliana = "2,eliana,eliana@eliana.com.br\n"

arquivo1.write(ana)
arquivo2.write(eliana)
```

O programa acima irá salvar apenas o contato eliana. Existem algumas formas de se tratar concorrência, como travar o arquivo quando abrimos, verificar as diferenças dos arquivo e tentar mesclar o conteúdo dos dois e assim por diante, mas esse não é o foco do curso. Devido a esse problema de concorrência devemos garantir de sempre fechar nossos arquivos ao terminar de trabalhar com eles.

Existem algumas formas de se gerenciar a abertura e fechamento de um arquivo. Podemos utilizar os blocos `try: ...... finally: .......`, sendo que escrevemos a abertura do arquivo no bloco `try:`, assim como toda a nossa operação com o arquivo e no bloco `finally:` fechamos o arquivo. Esse modo costuma levantar um erro quando simplemente tentaos fechar o arquivo com `nome_da_variavel_do_arquivo.close()`, pois caso o python falhe em abrir o arquivo, além de levantar um erro, ele não irá realizar a atribuição da variável do nome do arquivo, assim ao tentar fechar o arquivo que não conseguiu ser aberto acorrerá outro erro. Por isso a melhor maneira de se fazer esse gerenciamento de contexto do arquivo, isso é, fecha-lo assim que acabamos de utilizar para libera-lo para outro processo, é em conjunto com o método `with .... as ....:`

```python
with open("dados.csv", mode="r") as file:
    for line in file:
        print(line)

```

Com o código acima fecha o arquivo assim que terminar de executar o código que esta no interior do bloco `with`. Porém alguns erros, como o de arquivo não encontrado, ou permissão negada para a abertura/escrita de um arquivo ainda podem aparecer, por isso que devemos utilizar o `with as` em conjunto com o `try:`, pois temos a opção de tratar as excessões.

```python
try:
    with open("dados.csv", mode="r") as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Permissão de acesso negada")
```

O codigo acima trata tanto da excessão de o arquivo não ser encontrado, como a de não termos permissão de leitura/escrita em um arquivo.

O python utilizar um buffer para transferir os dados do arquivo que estamos trabalhando para o nosso programa, esse buffer é utilizado tanto em processos de leitura como de escrita. Contudo o buffer só aceita bytes em seu conteúdo. Existem duas formas de de transformar uma `str` em `bytes`, a primeira é inserindo a letra b antes da `str` como `b"Esse é um texto de exemplo"` , mas essa forma de conversão aceita apenas caracteres ASCII, para utilizar acentos devmos utilizar o método `bytes("texto para ser convertido", ëncoding a ser utilizado")`. O buffer do python pode ter alguns tipos, `BufferedReader` para arquivo abertos apenas para leitura, `BufferedWriter` para arquivos apenas de escrita e `BufferedRandom` para arquivos com a possibilidade de escrita e leitura. É possível acessar o buffer do python e inclusiver realizar operações de escrita utilizando ele, para isso precisamos utilizar os métodos `nome_da_variavel_do_arquivo.buffer.read()` e `nome_da_variavel_do_arquivo.buffer.write("texto")` .

 Como trabalhar com arquivos csv é algo normal o python já possui uma biblioteca que facilita esse trabalho, basta importar a biblioteca `csv`. Para fazer a leitura do conteúdo de um arquivo csv basta utilizar o método `csv.reader(nome_da_variável_do_arquivo)` e atribuir-lo a uma variavél. Essa variável que recebe o resultado da execusão do método `cvs.reader()` é um iterável, onde cada linha é um elemento de iteração e dentro de cada linha os elementos do csv são separados em uma lista iniciando pela posição de acordo com seu aparecimento na linha do arquivo csv.

```python
with open(path, encoding) as file:
    content = csv.reader(file)
    for line in content:
        id = line[0]
        nome = line[1]
        email = line[2]

OU

with open(path, encoding) as file:
    content = csv.reader(file)
    for line in content:
        id, nome, email = line
```

As vezes é necessário salvar um objeto em memória para continuar o trabalho em outra hora, pois se o objteno não for salvo teremos que reinstancia-lo novamete quando o programa for aberto. Para esse processo utilizamos a biblioteca `pickle`do python que faz um processo de serialização do objeto e salva em modo biário em um com extensão `.p` ou `.pickle` . Para salvar esso objeto em um arquivo utilizamos o método `.pickle.dump(objeto, nome_do_arquivo)`, já para ler seu conteúdo utilizamos o método `pickle.load(nome_do_arquivo)`.

```python
def contatos_to_pickle(contatos, path):
    with open(path, mode="wb") as file:
        pickle.dump(contatos, file)

def pickle_to_contatos(path):
    with open(path, mode="rb") as file:
        contatos = pickle.load(file)
    return contatos
```

Porém o formato `pickle` pode não ser seguro, pois como serializamos o nosso objeto pode haver uma injeção de código malicioso e quando vamos deserizlizar esse código malicioso pode ser executado junto. Existem algumas formas de tentar evitar isso, como por exemplo assinando nossos arquivo pickle, mas por segurança só devemos deserializar arquivos pickles de fontes conhecidas.

Apesar de ser muito útil, o formato pickle é exclusivo do python, então não conseguimos migrar o conteúdo desse arquivo para outro programas escritos em outras linguagens. Para essa função normalmente se utiliza o formato `json`. Assim como o csv e o pickle, já existe uma biblioteca para trabalhar com json no python `import json`. Nesse formato não salvamos a representação serializada do nosso objeto em formato binário, porém o método `json.dump(objeto, caminho)` não sabe como salvar nosso objeto, pois ele é um objeto que nós criamos. Devemos então informar qual será o comportamento padrão para serializar o nosso objeto com o parâmetro `default` ficando assim `json.dump(objeto, caminho, default=funcao_para_serializar)`. Por padrão todos os objetos do python possuem um ******dunder****** `.__dict__`, esse ******dunder****** transforma nosso objeto em um dicionário, onde as chaves serão o nome do atributo e os valores serão os valores atrelados a esses atributo, então um Objeto com atributi id=11, nome=Gui, email=gui@gui.com.br será transformado em um dict da seguinte forma `{"id":"11", "nome":"Gui", "email":"gui@gui.com.br"}` , logo podemos contruir uma função para serialização que retorne um dict. Ao ler os nossos objetos do arquivo json precisaremos recria-los, pois agora eles estão em um formato dict. Para instanciar esses objetos novamente lemos o conteúdo do json e atribuimos a uma variável que vamos iterar para fazer o instanciamento - `contato_json = json.load(caminho)` - depois disso basta iterar sobre a variável `contato_json` e ir instanciando o objeto, mas como as chaves do nosso dicionário possuem o mesmo nome dos atributos do nosso objeto, podemos simplesmente desempacotar o dicionário que o python já sabe como instanciar o objeto. Para realizar esse desenpacotamento basta utilizar dois asteriscos antes da variavél, dentro do objeto

```python
def json_to_contatos(path):
    contatos = []

    with open(path) as file:
        contatos_json = json.load(file)

        for contato in contatos_json:
            c = Contato(**contato)
            contatos.append(c)

    return contatos
```
