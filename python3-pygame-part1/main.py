import pygame as pg
import pacman

yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pg.init()

width = 900
height = 900
size = width / 30

screen = pg.display.set_mode((width, height), 0)

clock = pg.time.Clock()

scenery = pacman.Scenery(size)
pacman = pacman.Pacman(size)

while True:

    clock.tick(60)

    pacman.move_pacman()

    screen.fill(black)
    scenery.draw_scenery(screen)
    pacman.draw_pacman(screen)
    pg.display.update()

    event = pg.event.get()
    for e in event:
        if e == pg.QUIT:
            exit()
    pacman.process_event(event)
    # pacman.process_event_mouse(event)
