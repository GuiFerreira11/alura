# Pacman com Python e Pygame: cenário e ator

O pygame é uma biblioteca muito utilizada para a criação de jogos e de algumas aplicações gráficas no python. A;guns conceitos para trabalhar com ele são importantes como, a tela onde o jogo será exibida é dividida em pixels, sendo que o ponto inicial (0,0) está localizado no canto superior esquerdo. Além disso precisamos entender como representamos as cores no nosso jogo, o pygame utiliza o padrão rgb para representação das cores, assim o código (255, 255, 255) representa o branco, o (0, 0, 0) representa o preto, (255, 0, 0) representa o vermelho, (0, 255, 0) representa o verde e (0, 0, 255) representa o azul.

Para iniciar a representação de um objeto na tela, precisamos primeiro criar a tela. Isso é feito com o método `pygame.display.set_mode((width, height), flags, depth)`, onde *****width***** é a largura da tela, ******height****** é a altura, esses parâmetros são passados dentro de uma tupla, *****flags***** são algumas opções que podemos passar para a tela como fullscrenn e etc e *****depth***** é a profundidade do campo de cores indo de 2 bits até 32 bits.

Os jogos de modo geral rodam com um loop `while True:` para ficar verificando o jogo e atualizando a tela. Dentro desse loop podemos dividir nosso código em três partes:

- Calcular as regras do jogo: Nessa primeira parte implementamos as regras de negócio do nosso jogo, o que pode ou não ocorrer
- Desenhar na tela: esse parte é responsável por desenhar os elementos que aparecem na nossa telae atualizá-la
- Eventos: responsável por capturar qualquer evento, do teclado ou mouse, para a interação com nosso jogo

Como queremos que nossa tela permaneça aberta podemos implementar um evento que feche a tela e encerre nosso jogo apenas quando o usuários presionar o botão de fechar janela, o X. Para isso vamos utilizar o método `pygame.event.get()` e verificar de o tipo do evento foi `pygame.QUIT`

```python
for e in pygame.event.get():
    if e.type == pygame.QUIT:
        exit()
```

Existem deiversas formas que podem ser desenhadas na tela, a primeira que vamos utilizar é um circulo, uma vez que estamos recriando o jogo do pacman. Para isso vamos utilizar o método `pygame.draw.circle(surface, color, position, radius, line_width)`, onde:

- ********surface:******** é a superfice sobre a qual nós vamos desenhar, no nosso caso é a varaiável da tela
- ******color:****** é uma tupla com os elementos rgb da cor que iremos utilizar. Pode ser substituído por uma variável que represente essa tupla
- *********position:********* é uma tupla com a posição (x,y) onde o centro do nosso circulo será desenhado em pixels
- *******radius:******* é o raio em pixels que nosso circulo terá
- ********line_width:******** é a espessura do nosso circulo, caso seje 0 ou não informado, todo o nosso circulo será pintado com a *****color***** definida

Contudo não basta paenas desenhar, precisamos atualizar a tela, pois o pygame desenha tudo em memória para depois enviar as informações juntas para a tela. Essa atualização da tela é feita com o comando `pygame.display.update()`.

 O efeito de movimento nos jogos é feito deslocando-se o desenho alguns pixels para o lado que queremos mover o objeto, para isso substituimos os valores do ********position******** do método de ***draw*** por uma variável que tem seu valor alterado a cada passo do loop. Algumas informações podem ser definidas antes do loop, pois ela não mudam com o jogo, como a posição inicial do circulo, seu raio, as cores dos desenhos. Como queremos que nosso pacman se movimente por toda a tela precisamos implementar uma velocidade em x e outra em y e vamos atualizando a posição atual do pacman somando ou subtraindo a velocidade em x e y. Essa verificação é importante uma vez que não queremos que nosso desenho saia da tela, incluseive é preciso levar em conta o raio do objeto. Assim podemos utilizar ***ifs*** para determinar se a posição x atual + o raio do nosso pacman é maior que a largura da nossa tela e assim inverter o sentido da velocidade e de for menor do que zero, voltar a ser positivo. O mesmo vale para a altura e posição y. Essa lógica de movimentação já fica na parte que calcula as regras do jogo

```python
# Calcula regras do jogo

    pacman_x = pacman_x + pacman_speed_x
    pacman_y = pacman_y + pacman_speed_y

    if pacman_x + radius > width:
        pacman_speed_x = -speed
    if pacman_x - radius < 0:
        pacman_speed_x = speed
    if pacman_y + radius > height:
        pacman_speed_y = -speed
    if pacman_y - radius < 0:
        pacman_speed_y = speed
```

É importante também limpar a tela antes de fazer a movimentação do nosso desenho, se não ele irá deixar um rastro na tela, fazemos isso com o método `variavel_da_tela.fill(color)`, onde a cor é a mesma do **********background**********, que normalmente é preta (0, 0, 0).

Além de circulos o pygame também tem métodos para desenhar retangulos (`pygame.draw.rect()`), linhas (`pygame.draw.line()`) e poligonos (`pygame.draw.polygon()`), todos os comandos tem uma sintaxe parecida, iniciando com a *******surface******* em que o objeto será desenhado, a *****color***** do objeto, *******points/postion******* é uma lista com os pontos ou posições necessárias para desenhar o objeto e um **********line_width********** que é a espessura. O que muda entre esses métodos é o parâmetro *******points/position*******. Para o retangulo devemos passar uma tupla com duas tuplas dentro, a primeira é a posição inicial do retangulo, que fica no ponto superior esquerdo e a segunda tupla é o tamanho em x e y do retangulo. Para a linha passamos duas tuplas independentes, uma com a posição inicial e outra a posição final da nossa reta e por ultimo o poligono devemos passar uma lista de tuplas contendo os pontos, de forma sequencial, que o pygame ligará para contruir o poligono. Para o retangulo podemos usar a sintaxe anterior ou então criar um objeto retangulo que apenas guardará as informações do nosso retangulo e passar esse objeto. Para instanciar esse objeto utilizamos o comando `pygame.Rect()` passando o ponto inicial do retangulo e as dimensões (`pygame.Rect(10, 10, 40, 60)` irá desenhar um retangulo na posição x=10, y=10 com dimensões de 40 em x e 60 em y). Como podemos passar muitos pontos para a criação do nosso poligonos podemos criar uma variável com uma lista contendo os pontos que formarão o poligono.

É importante de atentar a ordem com que desenhamos nossas figuras, pois uma figura pode se sobrepor a outra.

O jogo como um todo pode ser dividido em três partes, uma parte de inicialização, onde todas as constantes são definidas, assets são carregados …., a segunda etapa do jogo é o loop do jogo, já discutido acima e a ultima é a finalização, que ocorre quando o jogador encerra o jogo, essa ultima etapa é opcional.

Como a execução do loop depende do nosso computador, nosso jogo pode rodar mais rápido ou mais lento dependendo do poder de processamento da cpu. Para evitar esse efeito podemos definir a quantidade de frams que queremos por segundo, isso é possivel com o método ****time**** do pygame, onde podemos determinar um delay, em milisegundos entre cada frame, assim um delay de 20 milisegundos gera um 50 quadros por segundo (`pygame.time.delay(20)`). Outra forma de se fazer isso é definindo o FPS direto do jogo, assim o programa vai ajustar o delay a cada execusão do loop, de acordo com o tempo que o processador levou para fazer aquela iteração para manter a taxa de quadro igual a que definimos. Isso é feito com a criação de um relógio, com o método `.Clock()`, que é atribuido a uma variável e então, dentro do loop do jogo, utilizamos o método `tick(frames_por_segundo)` para definir o FPS do nosso jogo.

```python
pygame.time.delay(20)  -> delay de 20 milisegundos a cada quadro ~ 50 FPS

clock = pygame.time.Clock()
# Dentro do loop do jogo
clock.tick(60)
```

Exitem alguns tipos de eventos com que o pygame trabalha, entre os mais comuns estão:

- QUIT: ocorre quando o usuário clica no botão de fechar a tela
- KEYDOWN: ocorre quando uma ou mais teclas são pressionadas
- KEYUP: ocorre quando uma ou mais teclas são soltas
- MOUSEMOTION: ocorre quando movemos o mouse
- MOUSEBUTTONDOWN: ocorre quando um ou mais botões do mouse são pressionados
- MOUSEBUTTONUP: ocorre quando um ou mais botões do mouse são soltos

Podemos acessar esses eventos de duas formas, diretamente ou com a fila de eventos. O acesso de forma direta é mais complicado, pois cada evento tem sua estrutura própria. A forma de acesso mais comum é a da fila de eventos, em que os eventos são armazenados em uma fila, que é acessado com o método `pygame.event.get()`. Quando esse método é executado a fila é zerada.

| Evento | Propriedade |
| --- | --- |
| QUIT | nenhuma |
| KEYDOWN | unicode(código unicodo do caractere pressionado), key(número relativo a tecla apertada), mod(se havia algum modificador, shift, crtl, alt, pressionado junto) |
| KEYUP | key, mod |
| MOUSEMOTION | pos(posição do mouse), rel(posição do mouse desde o ultimo moviemnto), buutons(botões do mouse pressionados) |
| MOUSEBUTTONDOWN | pos, button |
| MOUSEBUTTONUP | pos, button |

Como cada evento tem uma propiedade diferente precisamos verificar seu tipo para saber quais propriedades podemos utilizar

```python
for e in pygame.event.get():
    if e.type == pygame.KEYDOWN:
        print(e.key)
```

Para modificar a velocidade do pacman, basta verificarmos se alguma seta foi pressionada e então modificar a velocidade, em x ou y, dependendo da tecla, para fazer o pacman se mover. Precisamos também zerar essa velocidade quando a tecla pressionado for solta. Uma facilidade para não precisar gravar o nuúmero de todas as teclas é utilizar o atalho `K_UP, K_DOWN, K_LEFT, K_RIGHT` para as setas para cima, baixo, esquerda e direita.

A movimentação com o mouse é feita atribuindo a propriedade `e.pos` para duas variáveis, uma para o x e outra para o y e utilizamos essa variável para modificar a coluna e linha em que o pacman está, por exemplo. Caso o movimento fique muito rapido podemos dividir esse número por uma constante.

```python
def process_event_mouse(self, events):
        for e in events:
            if e.type == pg.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.column = (mouse_x - self.center_x) / 50
                self.line = (mouse_y - self.center_y) / 50
```

Uma forma de desenhar o cenário dos jogos é utilizando uma matriz, onde cada célula da matriz representa um conjunto linha, coluna do seu cenário/mapa. Podemos utilizar a relação de que as células com número 0 estão livres para o pacman andar, as com número 2 são as paredes do nosso labirinto e as com número 1, por exemplo são as bolinhas que o pacman precisa comer.

Como o cenário é uma “entidade” diferente, devemos criar uma nova classe para ele.

```python
def __init__(self, size):
        self.size = size
        self.matrix = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

    def draw_scenery(self, screen):
        for id_line, line in enumerate(self.matrix):
            self.draw_line(screen, id_line, line)

    def draw_line(self, screen, id_line, line):
        for id_column, column in enumerate(line):
            x = id_column * self.size
            y = id_line * self.size
            half = self.size/2
            color = blue if column == 2 else black
            pg.draw.rect(screen, color, (x, y, self.size, self.size), 0)
            if column == 1:
                pg.draw.circle(screen, red, (x + half, y + half), self.size/5, 0)
```

Como não queremos que o pacman saia do labirinto, ou que ele atravesse as paredes precisamos implementar uma regra para sua movimentação. Para isso podemos criar uma intenção de movimento do pacman, pois assim podemos verificar se o local para onde o jogador quer se mover é um local valido ou não antes de fazer a movimentação. A lógica para checar a colisão do pacmane se ele já saiu do labirinto é fácil, mas precisamos passar as informações do objeto pacman para nossa classe de cenário. Feito isso, basta compararmos se a linha e coluna que o jogador tem a inteção de mover o pacman é menor do que o número de linhas e colunas do labirinto e se aquela célula passou um valor diferente de 1, número que representa a parede na nossa matriz. Além disso, precisamos aceitar a movimentação do pacman, mas como não é indicado a Classe do Cenário fazer uma modificação diretamente em um atributo da Classe Pacman, criamos um método dentro da Classe Pacman que faz essa atualização na posição do jogador.

```python
Class Scenery:
def player_movement(self):
        col = self.pacman.column_intent
        lin = self.pacman.line_intent
        if 0 <= col <= 27 and 0 <= lin <= 28:
            if self.matrix[lin][col] != 2:
                self.pacman.movement_aproved()

Class Pacman:
def movement_aproved(self):
        self.column = self.column_intent
        self.line = self.line_intent
```

Uma vez que já estamos verificando o local para qual o pacman vai se mover, podemos verificar se esse local contem uma pastilha, em caso afirmativo, podemos aumentar a pontuação do jogador e remover a pastilha do labirinto, isso é feito trocando o valor da célula da matrix de 2 para 0.

Agora que já estamos calculando a pontuação do jogador, precisamos exibi-la na tela. Para isso vamos utilizar o modulo de fontes do próprio pygame. Com esse módulo nós criamos uma imagem com o texto que queremos e depois “colamos” esse texto na nossa tela. A utilização do módulo de fontes é a seguinte: `pygame.font`, para projetos simples podemos utilizar as fontes padrão do sistema `pygame.font.SysFont()`, dentro desse método precisamos indicar o nome da fonte que vamos utilizar, o tamanho e dois boleanos para indicar se o nosso texto estará em negrito e em itálico. Então para utilizar a fonte Arial, no tamanho 48, somente em negrito devemos criar um variável que receberá `pygame.font.SysFont("arial", 48, True, False)`. 

Depois de criada nossa variável com a fonte que queremos precisamos renderizar o nosso texto em uma imagem. Essa operação é feita com o método `.render()` da nossa fonte, onde devemos passar o texto que queremos que apareça na tela, um boleano para o recurso de Antialias, que torna as bordas do texto mais suave, uma tupla com a cor em (R,G,B) para o texto e outra para o fundo do texto. Caso esse ultimo valor seja omitido, nosso texto terá um fundo transparente.

Após renderizar nosso texto e atribui-lo a uma variável podemos “cola-lo” na nossa tela com o método `.blit(imagem, tupla com a posição que o texto vai ser colado)`. Essa operação de colagem deve ser feita dentro o loop do jogo.

Em projeto mais elaborados podemos não querer utilizar as fontes do sistema e sim uma fonte específica, para isso podemos utilizar o método `pygame.font.Font()` e devemos passar como parâmetros o caminho para a fonte que queremos no formato TrueTypeFonte ou .ttf, além do tamanho da fonte.