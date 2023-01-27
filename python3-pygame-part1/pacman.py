import pygame as pg


class Pacman:

    yellow = (255, 255, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    def __init__(self, width, column=1, line=1):
        self.column = column
        self.line = line
        self.size = width / 30
        self.center_x = 0
        self.center_y = 0
        self.radius = self.size / 2
        self.speed = 1
        self.speed_x = 0
        self.speed_y = 0

    def move_pacman(self):
        # change pacman position
        self.column = self.column + self.speed_x
        self.line = self.line + self.speed_y

        self.center_x = self.size * self.column + self.radius
        self.center_y = self.size * self.line + self.radius

    def draw_pacman(self, screen):
        # draw pacman's body
        pg.draw.circle(
            screen, Pacman.yellow, (self.center_x, self.center_y), self.radius, 0
        )

        # draw pacman's mouth
        mouth = [
            (self.center_x, self.center_y),
            (self.center_x + self.radius, self.center_y),
            (self.center_x + self.radius, self.center_y - self.radius),
        ]
        pg.draw.polygon(screen, Pacman.black, mouth, 0)

        # draw pacman's eye
        eye_x = self.center_x + self.radius * 0.25
        eye_y = self.center_y - self.radius * 0.5
        eye_radius = self.radius * 0.125
        pg.draw.circle(screen, Pacman.black, (eye_x, eye_y), eye_radius, 0)

    def process_event(self, events):
        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_RIGHT:
                    self.speed_x = self.speed
                elif e.key == pg.K_LEFT:
                    self.speed_x = -self.speed
                elif e.key == pg.K_UP:
                    self.speed_y = -self.speed
                elif e.key == pg.K_DOWN:
                    self.speed_y = self.speed
            elif e.type == pg.KEYUP:
                if e.key == pg.K_RIGHT:
                    self.speed_x = 0
                elif e.key == pg.K_LEFT:
                    self.speed_x = 0
                elif e.key == pg.K_UP:
                    self.speed_y = 0
                elif e.key == pg.K_DOWN:
                    self.speed_y = 0

    def process_event_mouse(self, events):
        for e in events:
            if e.type == pg.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.column = (mouse_x - self.center_x) / 50
                self.line = (mouse_y - self.center_y) / 50
