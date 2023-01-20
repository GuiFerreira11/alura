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
        self.speed_x = self.speed
        self.speed_y = self.speed

    def move_pacman(self, screen_width, screen_heigth):
        # change pacman position
        self.column = self.column + self.speed_x
        self.line = self.line + self.speed_y

        self.center_x = self.size * self.column + self.radius
        self.center_y = self.size * self.line + self.radius

        # delimit screen for pacman
        if self.center_x + self.radius > screen_width:
            self.speed_x = -self.speed
        if self.center_x - self.radius < 0:
            self.speed_x = self.speed
        if self.center_y + self.radius > screen_heigth:
            self.speed_y = -self.speed
        if self.center_y - self.radius < 0:
            self.speed_y = self.speed

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
