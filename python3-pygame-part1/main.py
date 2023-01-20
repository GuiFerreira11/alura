import pygame as pg
from pacman import Pacman


pg.init()

width = 1280
height = 1024

screen = pg.display.set_mode((width, height), 0)

clock = pg.time.Clock()

pacman = Pacman(width)

while True:

    clock.tick(24)

    pacman.move_pacman(width, height)

    screen.fill(Pacman.black)
    pacman.draw_pacman(screen)
    pg.display.update()

    for e in pg.event.get():
        if e == pg.QUIT:
            exit()
