import pygame as pg
import pacman as pac

yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
purple = (255, 184, 255)
cyan = (0, 255, 255)
orange = (255, 184, 82)

pg.init()

font = pg.font.SysFont("arial", 32, True, False)

width = 1200
height = 900
size = height / 30

screen = pg.display.set_mode((width, height), 0)

clock = pg.time.Clock()

pacman = pac.Pacman(size)
blinky = pac.Ghost(red, size)
pinky = pac.Ghost(purple, size)
inky = pac.Ghost(cyan, size)
clyde = pac.Ghost(orange, size)
scenery = pac.Scenery(size, pacman)

while True:

    clock.tick(60)

    pacman.rule_calculation()
    scenery.rule_calculation()

    screen.fill(black)
    scenery.draw(screen, font)
    pacman.draw(screen)
    blinky.draw(screen)
    pg.display.update()

    pg.time.delay(70)

    event = pg.event.get()
    pacman.event_processing(event)
    scenery.event_processing(event)
