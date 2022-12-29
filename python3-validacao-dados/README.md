# Python Brasil: validação de dados no padrão nacional

O projeto desse curso será a construção de um programa que validará alguns dados no formato brasileiro, além de acessar uma API para consulta de endereço.

A primeira etapa do programa foi construir uma classe que fizesse uma validação simples do CPF, apenas verificando seu tamanho, para isso foi necessário transformar o CPF em uma string para poder utilizar o `len()`, além disso criamos uma máscara com o formato `{}.{}.{}-{}` para a impressão do documento formatado.

Para uma validação mais robusta precisaríamos implementar uma quantidade maior de código, pois existem algumas regras para um CPF ser valido. Para evitar reinventar a roda, podemos utilizar alguma biblioteca pronta para fazer essa validação. Podemos fazer uma busca no site - [PyPI · O Python Package Index](https://pypi.org/) - por alguma biblioteca que tenha esse recurso, após isso basta instalar de acordo com as orientações da página e consultar a documentação da biblioteca para entender como ele funciona.

Fiz algumas alterações na forma como foi implementada a validação do CNPJ, pois acredito que pedir para o usuário passar o tipo de documento é mais seguro do que determinar apenas pela quantidade de caracteres, uma vez que mais de um documento pode ter o mesmo número de caracteres. Além disso foi introduzido o conceito de *********factory,********* como temos duas classes muito semelhante, para não gerar complexidade a toa, separamos as classes que validam o CPF e o CNPJ e criamos uma terceira classes que tem como objetivo apenas verificar qual tipo de documento está sendo criado e instanciar o objeto correto, seja um CPF, seja um CNPJ, para isso não precisamos criar o `__init__`, basta criar um `@staticmethod` com a função que verifica o tipo e retorna o objeto.

Para a parte de validação de telefone foi necessário usar Regex. Definimos um padrão com 2 ou 3 dígitos para o DDI opcional, 2 dígitos obrigatórios para o DDD, 1 dígito opcional para o 9 dos celulares e dois grupos de 4 dígitos para o número do telefone em si. O Regex ficou assim

```
([0-9]{2,3}?)?([1-9]{2})(9)?([0-9]{4})([0-9]{4}$)

([0-9]{2,3}?)? --> esta parte analisa os primeiros dígitos de uma forma que a documentação chama de non-greedy, basicamente ele tenta preencher o grupo com o menor numero possível de combinações, neste caso {2,3}?, ele força o 2, caso sobre um digito, completa com 3
([1-9]{2}) --> Verificação simples de DDD
(9)? --> Verificação do 9º dígito, a '?' faz com que este campo não seja obrigatório
([0-9]{4}) --> Diz que o 4º grupo obrigatoriamente tem que ter 4 dígitos.
([0-9]{4})$ --> Por fim, temos esta expressão terminada em '$' que 'força' caber na expressão inteira, este sinal se faz necessário por causa da expressão do primeiro passo, se você não colocar seu padrão poderá ignorar o último dígito de um telefone, já que ele vai forçar o grupo 1 a ter 2 dígitos
```

Para imprimir foi necessário uma série de `if`, pois os grupos 1 e 3 poderiam retornar `None` já que são grupos opcionais e esse é o retorno quando usamos `.group()` e aquele grupo não existe.

```python
def _format(self):
        padrao = r"(\d{2,3}?)?(\d{2})(9?)(\d{4})(\d{4}$)"
        telefone = re.search(padrao, self._telefone)
        if telefone.group(1) == None and telefone.group(3) == None:
            return f"({telefone.group(2)}){telefone.group(4)}-{telefone.group(5)}"
        elif telefone.group(1) == None:
            return f"({telefone.group(2)}){telefone.group(3)}{telefone.group(4)}-{telefone.group(5)}"
        elif telefone.group(3) == None:
            return f"+{telefone.group(1)}({telefone.group(2)}){telefone.group(4)}-{telefone.group(5)}"
        else:
            return f"+{telefone.group(1)}({telefone.group(2)}){telefone.group(3)}{telefone.group(4)}-{telefone.group(5)}"
```

Para lidar com as datas de cadastro foi necessário utilizar a biblioteca `datetime` e os métodos da classe `datetime`. Foi possível formatar a data e hora no formato brasileiro `DD/MM/YYYY`, além de retornar o mês e o dia da semana por extenso com os métodos `.month()` e `.weekday()`. Como a classe `datetime` possui o método `__add__` e `__sub__` implementado é possível adicionar e subtrair datas entre si. Idealmente a data de cadastro vem de um banco de dados, e com o método `datetime.today()` podemos fazer a diferença em dias, meses, anos, horas, minutos e segundos da data de cadastro presente no banco de dados e a data atual, porém como no programa tudo está sendo instanciado em tempo de compilação sempre retorna uma diferença de 0.

Resumo de API:

```
Em resumo, os clientes acessam essa API enviando uma requisição http, seja get() para pegar informação, post() para criar, put() para atualizar algo que já existe ou delete() para *deletar*.
A partir disso, a API acessa o sistema ou banco de dados e faz uma ação que retorna uma resposta. Se somente for encontrar uma resposta, o retorno será uma resposta serializada.
Uma resposta serializada é em `json` ou `xml` e realiza a integração entre sistemas; com isso, poderemos pegá-la e mostrá-la à usuário ou usuário da forma que quisermos.
```

Para a última parte da aplicação foi necessário acessar uma API para verificação de um endereço a partir de um CEP e para isso utilizamos a biblioteca `requests` que faz acesso html. Foi utilizada a API do ViaCEP para fazer essas consultas. A utilização da biblioteca `requests` é simples, basta definir uma variável e atribuir a ela uma `r=requests.get(url)`. Se imprimirmos essa variável vamos obter o status de resposta da API, 200, 400, 404 e assim por diante. Para acessar a resposta de fato da API podemos fazer em forma de texto com a propriedade `.text` . Caso a resposta esteja no formato json podemos também utilizar o método `.json()` que retorna um dicionário, o que é muito mais fácil de se trabalhar. A partir dai é só acessar os elementos do dicionário que está interessado.