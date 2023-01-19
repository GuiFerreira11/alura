import pygame as pg

yellow = (255, 255, 0)
black = (0, 0, 0)

width = 1280
height = 960

speed = 1

pacman_x = 40
pacman_y = 40
radius = 40

pacman_speed_x = speed
pacman_speed_y = speed


screen = pg.display.set_mode((width, height), 0)

while True:

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

    # Desenha na tela

    screen.fill(black)
    pg.draw.circle(screen, yellow, (int(pacman_x), int(pacman_y)), radius, 0)
    pg.display.update()

    # Eventos

    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
