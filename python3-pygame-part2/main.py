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
blinky = pac.Ghost(red, size, 11, 14)
pinky = pac.Ghost(purple, size, 13, 13)
inky = pac.Ghost(cyan, size, 14, 15)
clyde = pac.Ghost(orange, size, 16, 13)
scenery = pac.Scenery(size, pacman, blinky)

while True:

    clock.tick(60)

    pacman.rule_calculation()
    blinky.rule_calculation()
    scenery.rule_calculation()

    screen.fill(black)
    scenery.draw(screen, font)
    pacman.draw(screen)
    blinky.draw(screen)
    pinky.draw(screen)
    inky.draw(screen)
    clyde.draw(screen)
    pg.display.update()

    pg.time.delay(70)

    event = pg.event.get()
    pacman.event_processing(event)
    scenery.event_processing(event)
