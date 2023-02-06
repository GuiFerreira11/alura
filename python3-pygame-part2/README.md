# Pacman com Python e Pygame: colisão e pontuação

Um dos principios para se desenvolver um código que seja mais fácil de manter é o de abstração, onde focamos nos elementos mais importantes e comuns entrs nossas diferentes classes e ignoramos os elemtes irrelevantes . Isso nos permite ter uma previsibilidade sobre noas classes que herdam o comportamento de uma Classe mãe que contém as abstrações que julgamos necessárias. No caso do jogo pacman, os comportamentos de calcular as regras do jogo, desenhar o elemento principal na tela e processar os eventos são elementos importantes para nosso jogo como um todo e não apenas para uma das classes. Por isso devemos extrai-lo para uma classe genérica que terá esses elementos como métodos abstratos, obrigando assim as nossas classes filhas a implementar também esses método. Para isso precisamos importar da biblioteca `abc` o `ABCMeta` e `abstractmethod` ale’m de criar a classe.

```python
class GameElements(metaclass=ABCMeta):
    @abstractmethod
    def rule_calculation(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def event_processing(self):
        pass

class Scenery(GameElements):
...

class Pacman(GameElements):
....

```

Dessa formas as Classes `Scenery` e `Pacman` precisarão implementar um método `rule_calculation`, `draw` e `event_processing`.

O desenho dos fantasmas pode ser feito de maneira similar ao do pacman, mas precisamos utilizar o `pygame.draw.polygon()`para desenhar o corpo do fantasma, especificando os pontos para fazer o contorno do corpo do fantasma, além de que o fantasma tem dois olhos, com a parte brance e azul.

A movimentação dos fanstasmas foi construida de forma com que eles seguissem sempre uma mesma direção, até encontrar um parede ou uma bifurcação. Para isso definimos quatro variáveis `up=1 down=2 right=3 left=4` para facilitaro direcionamento dos fantasmas. Quem ficou responsável por verificar quais as possiveis direções que o fantasma pode seguir foi a Classe do Cenário. Isso é feito analisando se em uma linha para cima, uma linha para baixo, uma coluna para a esquerda e uma para a direita nãocontém uma parede. A Classe do Cenário também ficou responsável por verificar se a célula para qual o fantasma tem a intenção de se mover está livre ou não. Caso a célula esteja livre, uma função de aprovar o movimento do fantasma é invocada, de forma similar ao que é feito com o pacman. Caso a célula seja uma parede, uma função do fantasma que recusa o movimento é chamada e é passado como parâmetro para essa função a lista de direções que o fantasma pode tomar.

Outra função que a Classe do Cenário recebeu foi a de verificar a quantidade de movimento possíveis para os fantasmas, pois caso a quantidade de movimento seja maior ou igual a 3, quer dizer que o fantasma chegou em uma esquina/T. Nesse caso um função da Classe Fantasma, para sortear uma nova direção é invocada. Essa função também é chamada dentro da classe fantasma na execução da função que é invocada quando o movimento do fantasma foi negado, devido a uma colisão com a parede. A escolha da direção eleatória que o fantasma irá tomar foi feita com o método `.choice()`da biblioteca `random`.

Como a função de calcular as regras da Classe Cenário estaja repetitiva, uma vez que estavamos realizando testes quase identicos para o pacman e para os fantasmas, é uma boa pratica refatorar essa função. Para isso criamos uma nova classe abstrata `Moviveis` que contém os métodos abstratos `aceitar_movimento(self)  recusar_movimento(self, direcoes)  esquina(self, direcoes)` que foram herdadas pelas Classes Pacman e Fantasma. Como a Classe dos Fantasmas já implementava todos os métodos, não foi preciso alterar nada, porém foi necessário adicionar o métodos `recusar_movimento()` e `esquina()` na Classe Pacman. O método `recusar_movimento()` foi utilizado para resetar a posição da linha e coluna intenção, uma vez que se o usuário ficar tentando se mover repetidas vezes contra a pareda, uma hora os valores das intenções podem ficar muito grandes, ocasionando um errona comparação com as linhas e colunas da nossa matriz. Já o método `esquina()` não foi utilizado para nada, contendo apenas um `pass`.

Agora como sabemos que nossos objetos, Pacman e Fantasmas, possuem as propriedades de movíveis, podemos refatorar o método do `calcular_regras()`  do Cenário. Para isso colocamos os nossos objetos movíveis em uma lista e iteramos sobre ela fazendo as verificações, isso é:

- Qual a sua linha e coluna atual do objeto
- Qual a linha e coluna que o objeto tem a intenção de se mover
- Chamar a função da Classe Cenário que verifica a quantidade de direções que um objeto pode se mover
- Caso a quantidade de direções for maior ou igual a 3 chamar a função `esquina()` do respectivo objeto
- Verificar se a a célular que o objeto tem a intenção de se mover está dentro da martiz do labirinto e se não é uma parede
- Caso o movimento for permitido, chamar a função `aceitar_movimento()` do respectivo objeto
- Caso o movimento for recusado, chamar a função `recusar_movimento()` do respectivo objeto

Com a intenção de não gerar mais acoplamento, ao invés de já passar os objeto que são movíveis para a Classe Cenário, na sua criação/instanciamento um método que adiciona objeto na lista `self.moviveis = []` da Classe Cenário foi criado.

Esse padrão de projeto é conhecido como **Observer** ou ******************Publish-Subscriber******************. Esse padrão visa definir uma dependência entre objetos de forma que quando um muda alguma coisa todos os outros dependentes sejam atualizados automaticamente. Nesse padrão temos 4 classes que precisam ser implementadas.

- ***************ConcreteSubject*************** ou *******Publish*******, que é quem notifica que uma mudança ocorreu/pode ocorrer. No nosso caso essa classe é a classe Cenário, que verifica se os objetos movíveis podem se mover e em caso afirmativo chama uma função dessas classes para fazer a atualização em suas respectivas posições.
- Uma interface *******Subject*******, que é é uma classe abstrata que contém os métodos que a Classe ConcreteSubject precisa implementar, que no caso costumam ser: adicionar um observador, remover um observador e notificar um observador. No nosso jogo não implementamos essa classe, porém criamos o método que realiza a adição de um observado e o método `calcular_regras()` é o que notifica os objetos da mudança.
- Outra interface ********Observer********, que garante que os objetos observadores possuirão os métodos necessários para se atualizarem. No nosso programa, essa classe é a Classe Moviveis
- ****************ConcreteObserver**************** ou **********Subscriber**********, que é o objeto que vai ter seu comportamento alterado uma vez que o ConcreteSubject ou Publish, publicar/postar/chamar uma função que realize sua alteração de estado. No nosso programa essas classes são as Classes do Pacman e dos Fantasmas.

Precisamos fazer mais um teste no nosso método de calcular regras do Cenário, pois apenas o pacman pode comer as moedas. Para isso precisamos verificar se o objeto movível é do tipo Pacman. Isso é feito com o método `isinstance(objeto, Classe_que_queremos_testar)` nesse caso ficou assim `isinstance(movivel, Pacman)`. Além disso precisamos verificar se naquela posição da matriz temos uma moeda, apagar a moeda e somar um ponto na pontuação geral do jogo.

Uma funcionalidade muito útil para o nosso jogo é a e poder pausar o jogo. Essa funcionalidade pode ser implementada com o conceito de máquina de estados. Com esse conceito o nosso jogo pode assumir 4 estados diferentes, jogando, pause, game over ou vitória, sendo que podemos utilizar números para representar esses estados, como 0-jogando, 1-pause, 2-game over, 3-vitória, ou mesmo strings. A funcionalidade de máquina de estados será implementada na Classe do Cenário, pois é nessa classe que fazemos as chamadas para aceitar ou não o movimento, tanto do jogador como dos fantasma, ela é a nossa Classe *******Publish*******. O estado “padrão” do jogo será o 0-jogando, de forma que para se alterar o estado do jogo é necessário que algum evento ocorra, para isso o método `calcular_regras()` da Classe Cenário será renomeado para `calcular_regra_jogando()` e cada estado do jogo terá seu método `calcular_regra_estado()`, de forma que o antigo método `calcular_regra()` apenas irá verificar o estado do jogo e invocará o método correspondente. No caso do estado de pause, podemos fazer com o método encarregado de processar eventos do Cenário altere o estado de 0-jogando para 1-pause e vice-versa. 

Os outros dois cenário serão acessados quando, o método `calcular_regras_jogando()` do Cenário verificar que o objeto movível é um fantasma, e que ele está ocupando a mesma posição do que o pacman, então o jogo terá seu estado alterado para 2-game over. O estado de 3-vitória só será acessado quando, após o movimento do pacman ser aprovado, a pontuação calculada e a verificação da existência de moedas/pastilhas no tabuleiro. Essa verificação pode ser feita de várias formas, sendo que a forma que escolhi fazer foi `not any(1 in line for line in self.matrix)`, dessa forma o python verificará se existe algum número 1 dentro de uma linha para cada linha na matrix que define o labirinto, e o `not` irá inverter o estado de `False` para `True` quando não hover mais nenhuma moeda/pasitlha, mudando então o estado do jogo para 3-vitória.

Como não precisamos alterar a posição do pacman e dos fantasmas durante os estado 1-pause e 2-game over, os métodos `calcular_regras_pause()` e `calcular_regras_game_over()` podem simplesmente conter um `pass()`.

Outro método que precisará sofrer uma alteração, para ficar evidente a mudança de estado do jogo é o método de desenhar a tela, pois além de desenhar a configuração atual do cenário, é interessante que que ele desenhe também um texto indicando o jogo em pause, quando o jogador perder a mensagem de game over e quando ganhar a mensagem de vitória. Para isso podemos cirar um método que recebe o texto que será desenhado na tela, a superfície em que ele desenhará, no nosso caso será `screen`  e a fonte que será utilizada. Então basta desenhar o texto, que será alterado de acordo com o estado (PAUSE, GAME OVER ou YOU WIN), em uma variável com o método `img_text = font.render()`, encontrar o meio da tela para que a mesagem fique centralizada com `pos_x = (screen.get_width - img_text.get_width) // 2` e `pos_y = (screen.get_height - img_text.get_height) // 2` e utilizando o método `screen.blit()` mostrar o texto na tela.

É interessante que o jogador tenha mais de uma tentativa para ganhar o jogo, assim podemos adicionar uma propriedade de vidas ao nosso cenário, de forma que a cada vez que o pacman colidir com um fantasma sua vida será reduzida em 1 e ele será realocado na posição inicial do jogo, no canto superior esquerdo. Um bom local para exibir a quantidade de vidas restante do jogador é logo abaixo da pontuação.

Para finalizar o jogo podemos melhorar a aparencia do pacman fazendo com que ele abra e feche a boca. Como estamos utilizando o método de desenhar poligonos para desenhar a boca do pacman, sendo que a ponto inicial é o centro do pacman e os outros dois pontos são o lábio superior e lábio inferior, basta alterar a posição dos lábios. Para isso criamos a propriedade de velocidade de abertura da boca e tamanho da abertura da boca. Assim podemos começar com a boca fechada, onde o tamanho da abertura da boca será 0. A cada loop do jogo será realizado também uma verificação de o tamanho da abertuda da boca é maior do que um limite estabelecido, como 75% do raio do pacman, ou se ele é menor igual a 0. Com o limite da boca menor igual a 0 a velocidade de abertura da boca será positiva, assim vamos mudando a posição dos labios a cada loop do jogo, aumentando o tamanho da abertuda da boca, fazendo o lábio superior subir e o lábio inferior descer. Já com o limite da boca maior ao critério estabelecido, a velocidade de abertura da boca será negativa, assim vamos mudando a posição dos labios a cada loop do jogo, diminuindo o tamanho da abertuda da boca, fazendo o lábio superior descer e o lábio inferior subir.