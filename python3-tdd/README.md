# Python e TDD: explorando testes unitários

É importante criarmos ambientes virtuais quando estamos trabalhando com projetos python, pois assim podemos isolar as dependências do nosso código, garantido que temos as versões corretas das bibliotecas utilizadas no nosso programa apenas para aquele diretório, podendo assim ter outras versões da mesma biblioteca em outros projetos

Testes podem ser divididos em testes unitários, testes de integração e teste de ponta a ponta (E2E - end to end).

- Testes unitários: São testes de muito baixo nível, normalmente realizados pelos programadores envolvidos no projeto e tem a função de testar as menores unidades do sistema, como métodos e funções das classes ou pacotes utilizados. Testam as unidades isoladamentes, garantindo que a lógica daquela porção está correta. São os mais rápidos de se executarem, mais baratos, sendo facilmente utilizado em servidores de integração contínua.
- Testes de integração: São testes que verificam a interação entre os diferentes elementos da nossa aplicação. São mais complexos tanto de serem desenvolvidos, como de serem executados. Idealmente são executados em servidores de integração contínua após os testes unitários serem validados.
- Testes de ponta a ponta: Tem o objetivo de testar a aplicação como um todo, simulando o comportamento de um usuário final e é o ultimo teste antes de o projeto ir para produção. Deve simular o uso no mundo real, interagindo com banco de dados, usando comunicação de rede e interagindo com outros aplicativos, sistemas ou hardwares. São os mais complexos e os mais demorados para se executarem e por se tratar de um teste de mais alto nível, não se atem a pequenos detalhes, não retornando descrições profundas sobre os erros encontrados.

Podemos ainda dividir a maneira como os testes são executados, podendo ser testes manuais e testes automatizados, amobs os testes costumam ser utilizados em conjunto devidos as vantagens e desvantagens das duas metodologias.

- Testes manuais: Dependem de um analista, desenvolvedor ou especialista em qualidade para serem executados. A pessoa responsável pelo teste executa cada passo necessário para sua execução, possui uma vlaor de investimento menor e permite uma interação real entre código e humano, porém são lentos e sujeitos a falhas humanas.
- Testes automatizados: São testes que após criados pelos desenvolvedores passam a rodar por meio de scripts e ferramentas específicas, ajudando a descobrir rapidamente falhas nos programas. São mais confiáveis por não dependerem de uma interferência humana, o que também é uma desvantagem em testes onde a usabilidade é importante, além disso são mais caros de de desenvolverem e implementarem.

A ferramenta de testes que vamos utilizar é a pytest, basta instalar pelo pip `python -m pip install pytest`. Uma funcionalidade muito interessante do pip é o ******freeze****** que lista todos os pacotes intalados no ambiente virtual, com isso podemos criar uma lista, que geralemente recebe o nome de “requirements.txt” que contém essa relação dos pacotes e versões necessárias para rodar nosso código `pip freeze > requirements.txt`. Dessa forma, quando compartilharmos nosso código, basta o outro deve instalar todos os pacotes desse arquivo para ter certeza que conseguirá rodar nosso programa `pip install -r requirements.txt`.

Para utilizar o pytest precisamos criar o diretório “tests” na raiz do nosso projeto, o nome do diretório precisa ser esse. O pytest depende de alguns nomes padrão para conseguir executar todos os testes corretamente. Dentro desse diretório precisamos criar um aruiqvo, que inicialmente pode estar vazio chamado “__init__.py”. Sim , o *********dunder********* inicializador que utilizamos em classes. Isso irá indicar para o python que esse nosso diretório é um módulo. \

Cada teste escrito dentro do diretório tests precisam começar com “test_nome_do_teste.py”. Dentro do arquivo de teste criamos nossa classe com os métodos que serão utilizados nos teste. É importante que os nomes do métodos sejam bem verbosos, descrevendo muito bem sua funcionalidade, pois isso ajuda na hora da identificação quando os testes forem rodados. Assim um possivel nome para um teste é “test_quando_idade_recebe_13_03_2000_deve_retornar_23”. 

Uma das metodologias para o desenvolvimento de testes é a **************Given-When-Then**************, que se baseia em dado um contexto, podemos tentar realizar uma ação e então esperamos um resultado. ******Given-When-Then****** pode ser traduzido então como Contexto-Ação-Desfecho. Para a verificação do nosso desfecho usamos o método `assert` que irá comparar o resultado obtido com o nosso teste com o resultado esperado e então prosseguirá ou não.

```python
from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' # Given-Contexto
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado  # Then-desfecho
```

Como estamos escrevendo nosso teste dentro do diretório “~/projeto/test” e estamos testando nossa classe que está dentro do diretório “~/projeto/codigo” na hora de importar nossa classe precisamos usar “from codigo.nome_da_biblioteca import Classe_que_vou_testar”, pois o teste é rodado no diretório raiz do nosso projeto “~/projeto”. Para executar o nosso teste basta digitar pytest na linah de comando dentro da pasta raiz do projeto, com a flag -v obtemos uma resposta mais completa.

```python
>>> pytest

=========================================================================== test session starts ===========================================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /mnt/d/OneDrive/Alura/python3-tdd
collected 1 item

tests/test_bytebank.py .                                                                                                                                            [100%]

============================================================================ 1 passed in 0.15s ============================================================================
```

```python
>>> pytest -v

=========================================================================== test session starts ===========================================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /usr/sbin/python3
cachedir: .pytest_cache
rootdir: /mnt/d/OneDrive/Alura/python3-tdd
collected 1 item

tests/test_bytebank.py::TestClass::test_quando_idade_recebe_13_03_2000_deve_retornar_23 PASSED                                                                      [100%]

============================================================================ 1 passed in 0.13s ============================================================================
```

```python
>>> pytest -v 

=========================================================================== test session starts ===========================================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /usr/sbin/python3
cachedir: .pytest_cache
rootdir: /mnt/d/OneDrive/Alura/python3-tdd
collected 2 items

tests/test_bytebank.py::TestClass::test_quando_idade_recebe_13_03_2000_deve_retornar_23 PASSED                                                                      [ 50%]
tests/test_bytebank.py::TestClass::test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho PASSED                                                        [100%]

============================================================================ 2 passed in 0.18s ============================================================================
```

Quando um teste falha, além indicar em qual teste que ocorreu a falha, o pytest também devolve o erro encontrado e os valores do `assert`

```python
>>> python -v

=========================================================================== test session starts ===========================================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /usr/sbin/python3
cachedir: .pytest_cache
rootdir: /mnt/d/OneDrive/Alura/python3-tdd
collected 2 items

tests/test_bytebank.py::TestClass::test_quando_idade_recebe_13_03_2000_deve_retornar_23 FAILED                                                                      [ 50%]
tests/test_bytebank.py::TestClass::test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho PASSED                                                        [100%]

================================================================================ FAILURES =================================================================================
_____________________________________________________ TestClass.test_quando_idade_recebe_13_03_2000_deve_retornar_23 ______________________________________________________
self = <tests.test_bytebank.TestClass object at 0x7f0dc1a73250>

    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = "13/03/2001"  # Given-contexto
        esperado = 23

        funcionario_teste = Funcionario("Teste", entrada, 1000)
        resposta = funcionario_teste.idade()  # When-ação

>       assert resposta == esperado  # Then-desfecho
E       assert 22 == 23

tests/test_bytebank.py:12: AssertionError
========================================================================= short test summary info =========================================================================
FAILED tests/test_bytebank.py::TestClass::test_quando_idade_recebe_13_03_2000_deve_retornar_23 - assert 22 == 23
======================================================================= 1 failed, 1 passed in 0.21s =======================================================================
```

Quando o contexto de um teste se repete em vários outros podemos isola-los para poder reutilizar essa parte do teste. No pytest temos uma forma especial de fazer isso que é com o decorator `@pytest.fixture`, com esse decorator podemos simplesmente passar o nome da função que está decorada e instanciando o objeto que queremos como parâmetro para o nosso método de teste. Cada fixture pode ter um escopo diferente de quando ela é instanciada, o padrão é o `@pytest.fixture(scope='function')`, onde a cada vez que uma função/método chama uma fixture, um novo objeto, limpo é instanciado. Isso acontece devido a problemas que objetos reaproveitados podem ocorrem, pois já foram modificados, pois já foram modificados pelos testes iniciais, então é sempre bom garantir que temos um cenário limpo e sem efeitos colaterais de outros testes anteriores. Contudo, existem objeto que não tem se valor alterado durante a execução dos teste, nesse caso podemos instancia-los com um outro escopo, outro cenário em que podemos querer mudar o escopo de instanciamento de um objeto é na conexão com um banco de dados, com um servidor de e-mail ou com um serviço externo, onde essa conexão é muito custosa de fazer varias vezes. Entre os escopos disponíveis temos:

- function: é instanciado a cada vez que é chamado por uma função/método
- class: é instanciado apenas uma vez na execução dos testes daquela classe em que foi declarado
- module: instancia o objeto no começo do módulo de testes, ou seja, no arquivo de testes
- session: o objeto é instanciado no começo de uma sessão de testes, com mais de um módulos de testes por exemplo
- package: instancia o objeto quando o pacotes de teste, o diretório, é carregado.

Exemplo de teste sem a definição de fixture

```python
from src.compras import CarrinhoDeCompras, ItemDoCarrinho, Usuario

class TestCarrinhoDeCompras:
    def test_deve_retornar_subtotal_dos_itens_no_carrinho(self):
        usuario = Usuario(‘Matheus’)
        carrinho = CarrinhoDeCompras(usuario)
        celular = ItemDoCarrinho('Celular', 2100.0, 1)
        notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
        caneta = ItemDoCarrinho('Caneta', 3.00, 5)

        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta)

        valor_esperado = 6615.0
        assert valor_esperado == carrinho.subtotal

    def test_deve_retornar_total_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self):
        usuario = Usuario(‘Matheus’)
        carrinho = CarrinhoDeCompras(usuario)
        celular = ItemDoCarrinho('Celular', 2100.0, 1)
        notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
        caneta = ItemDoCarrinho('Caneta', 3.00, 5)

        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta)

        valor_esperado = 6615.0
        assert valor_esperado == carrinho.total

    def test_deve_aplicar_desconto_ao_subtotal_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self):
        usuario = Usuario('Matheus')
        carrinho = CarrinhoDeCompras(usuario)
        celular = ItemDoCarrinho('Celular', 2100.0, 1)
        notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
        caneta = ItemDoCarrinho('Caneta', 3.00, 5)

        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta)
        carrinho.aplica_desconto(500)

        valor_esperado = 6115.0
        assert valor_esperado == carrinho.total
```

Exemplo de teste com a definição de fixture

```python
from src.compras import CarrinhoDeCompras, ItemDoCarrinho, Usuario

class TestCarrinhoDeCompras:

		@pytest.fixture
    def usuario(self):
		    return Usuario('Matheus')

		@pytest.fixture
		def carrinho(self, usuario):
		    return CarrinhoDeCompras(usuario)

		@pytest.fixture
		def celular(self):
		    return ItemDoCarrinho('Celular', 2100.0, 1)

		@pytest.fixture
		def notebook(self):
		    return ItemDoCarrinho('Notebook', 4500.0, 1)

		@pytest.fixture
		def caneta_qtd5(self):
		    return ItemDoCarrinho('Caneta', 3.00, 5)

		def test_deve_retornar_subtotal_dos_itens_no_carrinho(self, usuario, carrinho, celular, notebook, caneta_qtd5):
        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta)

        valor_esperado = 6615.0
        assert valor_esperado == carrinho.subtotal

   def test_deve_retornar_total_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self):
        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta)

        valor_esperado = 6615.0
        assert valor_esperado == carrinho.total

    def test_deve_aplicar_desconto_ao_subtotal_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self):
        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta)
        carrinho.aplica_desconto(500)

        valor_esperado = 6115.0
        assert valor_esperado == carrinho.total
```

Uma metodologia comum para o desenvolvimento de software é o TDD - *****Test Driven Development***** ou Desenvolvimento Guiado por Testes. Com esse conceito primeiro criamos os testes para o nosso códigos, pois eles é que garantem que a nossa regra de negócio esta sendo respeitada, só então, com os testes já feitos é que começamos a escrever o código, que normalmente não ficam totalmente otimizados, pois escrevemos o código com o objetivo simplesmente de passar nos teste, contudo, uma vez que todo nosso código esta passando em todos os testes começamos a etapa de refatoração do código, melhorando e otimizando, tanto a performance com a legibilidade do mesmo, sempre refazendo os testes para garantir que as mudanças não alteraram alguma regra de negócio.

Em python os erros podem ser dividios em dois grupos:

- Erros de sintaxe: Onde digitamoas algum comando errado, esquecemos algumas aspas, parênteses, etc. Acredito que sejam identificados na hora da interpretação do código.
- Runtime Errors: São erros relacionados ao funcionamento do código em si, algum método que não existe, um parâmetro passado de forma errada, uma divisão por zero e etc. Acredito que dependam da execução daquela parte especifica do código.

Em alguns casos podemos querer que nosso programa apresente um Runtime Error, mas com uma mensagem personalizada informando o motivo do erro de acordo com a nossa regra de negócio. Para isso utilizamos o método `raise` junto com `Exceptio("mensagem de erro")`.

Nesse caso, quando queremos testar a excessão, precisamos de uma estrutura diferente com o pytest, pois nosso teste não deveria parar e apresentar uma excessão, caso seja esse o intuito do teste. Para isso precisamos importar a biblioteca do pytest e colocar nosso teste dentro do seguinte bloco `with pytest.raises(Exception):`, nesse caso não precisamos definir um valor esperado, pois esse valor já um `raise Exception("alguma mesagem")`, só precisamo fazer o `assert` com a resposta.

```python
def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000  # Given

            funcionario_teste = Funcionario("Teste", "13/03/2000", entrada)
            resposta = funcionario_teste.calcular_bonus()  # When

            assert resposta  # Then
```

Nem sempre vamos querer rodar todos os testes de uma só vez. Existem algumas formas de selecionar os testes que queremos. A primeira é usando a flag `-k`, com essa flag basta digitar um palavra chave e o pytest irá rodar todos os testes que contenham aquela palavra. Outra opção é utilizando a flag `-m`, mas dessa vez com um ******marker******. Esses markers precisam ser definidos dentro da classe de teste com um decorator `@pytest.mark.nome_do_mark`. O pytest já possui alguns markers padrão, que precisamos apenas decorar dentro do codigo:

- filterwarnings()
- skip()
- skipif()
- xfail()
- parametrize()
- usefixtures()

Cada um desses markers pode receber parâmetros específicos como argumentos. Para markers personalizados, o pytest irá levantar um warning, avisando que esse mark não é um mark padrão e sugerindo para registra-lo para evitar esses warnings. Esse registro é feito em um arquivo com o nome de “pytest.ini” que deve estar localizado no diretório raiz do projeto.

```python
[pytest]
markers =
    bonus: Testes para o metodo calcular_bonus
```

Algo importante de se atentar é sobre a cobertura dos nossos testes, devemos cobrir o máximo possivél nosso programa com testes, mas sem ficar testando métodos desnecessários, como o método `__str__`. Para verificar a cobertura dos nossos testes podemos utilizar a ferramenta de cobertura do pytest `pytest --cov`. Mas precisamos instalar essa ferramenta com o pip antes. O comando básico dessa ferramenta `pytest --cov` irá verificar a cobertura de todos os arquivos, porém isso não é necessário, uma vez que não faz sentido verificar a cobertura dos testes para o arquivo test_nome_do_arquivo.py, onde ficam os teste, ou do arquivo __init__.py

```python
>>> pytest --cov
=========================================================================== test session starts ===========================================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /mnt/d/OneDrive/Alura/python3-tdd, configfile: pytest.ini
plugins: cov-4.0.0
collected 5 items

tests/test_bytebank.py .....                                                                                                                                        [100%]

---------- coverage: platform linux, python 3.10.8-final-0 -----------
Name                     Stmts   Miss  Cover
--------------------------------------------
codigo/bytebank.py          34      1    97%
tests/__init__.py            0      0   100%
tests/test_bytebank.py      37      1    97%
--------------------------------------------
TOTAL                       71      2    97%

============================================================================ 5 passed in 0.51s ============================================================================
```

Para evitar isso podemos especificar o diretório onde está o arquivo que queremos testar com `pytest --cov=diretorio`

```python
>>> pytest --cov=codigo
=========================================================================== test session starts ===========================================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /mnt/d/OneDrive/Alura/python3-tdd, configfile: pytest.ini
plugins: cov-4.0.0
collected 5 items

tests/test_bytebank.py .....                                                                                                                                        [100%]

---------- coverage: platform linux, python 3.10.8-final-0 -----------
Name                 Stmts   Miss  Cover
----------------------------------------
codigo/bytebank.py      34      1    97%
----------------------------------------
TOTAL                   34      1    97%

============================================================================ 5 passed in 0.43s ============================================================================
```

Outra flag muito útil que podemos usar é a `--cov-report term-missing`, com essa flag obtemos informações sobre o que falta testar na nossa aplicação, no caso, a linha onde começa o método que não está coberto por um teste.

```python
>>> pytest --cov=codigo --cov-report term-missing
=========================================================================== test session starts ===========================================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /mnt/d/OneDrive/Alura/python3-tdd, configfile: pytest.ini
plugins: cov-4.0.0
collected 5 items

tests/test_bytebank.py .....                                                                                                                                        [100%]

---------- coverage: platform linux, python 3.10.8-final-0 -----------
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
codigo/bytebank.py      34      1    97%   53
--------------------------------------------------
TOTAL                   34      1    97%

============================================================================ 5 passed in 0.44s ============================================================================
```

Outra forma de visualizar a cobertura dos testes é com a flag `--cov=report html`. Com essa flag o pytest vai criar um diretório htmlcov com arquivos que permitem abrir, no navegador, uma descrição melhor da cobertura do nosso programa.

Nesse caso temos duas opções, ou fazer um teste que cubra essa parte do nosso código, ou então, caso o método em questão não precise ser testado, como no caso de métodos `__str__` podemos excluir a busca desse código da procura por cobertura do nosso programa.

Essa exclusão é feita com um arquivo de configuração “.coveragerc” que também precisa ficar na raiz do projeto contendo algo que identifique a ométodo que deve ser ignorado, no caso podemos utilizar o próprio nome do método

```python
[run]

[report]
exclude_lines = 
    def __str__
```

Dentro desse arquivo podemos fazer mais algumas presonalizações, como definir o diretório em que pytest-cov deve verificar a cobertura, fazer o report com o `term-missing` por padrão, além de definir um diretório diferente para o pytest salvar o report em html

```python
[run]
source = ./codigo

[report]
exclude_lines =
    def __str__

[html]
directory = coverage_relatorio_html
```

Podemos fazer algo semelhante com o arquivo pytest.ini, assim podemos definir um comportamento padrão para o pytest e não precisaremos ficar colocando varias flags

```python
[pytest]
addopts = -v --cov
markers = 
    bonus: Testes para o metodo calcular_bonus
```

Outro formato comum de se reportar o resultado dos testes e sua cobertura é com arquivo xml, para isso podemos gerar um arquivo xml somente do pytest, com as informações dos testes que rodaram e um arquivo xml do pytest-cov com os seguinte comandos `pytest --junitxml nome_do_arquivo.xml` para o pytest e `pytest --cov-report xml` para o pytest-cov.