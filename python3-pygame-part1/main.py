import pygame as pg
import pacman as pac

yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pg.init()

font = pg.font.SysFont("arial", 32, True, False)

width = 1200
height = 900
size = height / 30

screen = pg.display.set_mode((width, height), 0)

clock = pg.time.Clock()

pacman = pac.Pacman(size)
scenery = pac.Scenery(size, pacman)

while True:

    clock.tick(60)

    pacman.move_pacman()
    scenery.player_movement()

    screen.fill(black)
    scenery.draw_scenery(screen, font)
    pacman.draw_pacman(screen)
    pg.display.update()

    pg.time.delay(70)

    event = pg.event.get()
    for e in event:
        if e == pg.QUIT:
            exit()
    pacman.process_event(event)
    # pacman.process_event_mouse(event)
