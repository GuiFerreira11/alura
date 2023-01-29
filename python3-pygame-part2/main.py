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

    pacman.rule_calculation()
    scenery.rule_calculation()

    screen.fill(black)
    scenery.draw(screen, font)
    pacman.draw(screen)
    pg.display.update()

    pg.time.delay(70)

    event = pg.event.get()
    pacman.event_processing(event)
    scenery.event_processing(event)
