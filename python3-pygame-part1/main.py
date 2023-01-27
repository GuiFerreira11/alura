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

    pacman.move_pacman()

    screen.fill(Pacman.black)
    pacman.draw_pacman(screen)
    pg.display.update()

    event = pg.event.get()
    for e in event:
        if e == pg.QUIT:
            exit()
    pacman.process_event(event)
    # pacman.process_event_mouse(event)
