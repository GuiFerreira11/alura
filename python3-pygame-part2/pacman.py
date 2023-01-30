import pygame as pg
from abc import ABCMeta, abstractmethod
import random

yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
up = 1
down = 2
right = 3
left = 4


class GameElements(metaclass=ABCMeta):
    @abstractmethod
    def rule_calculation(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def event_processing(self):
        pass


class Scenery(GameElements):
    def __init__(self, size, player, enemy):
        self.pacman = player
        self.ghost = enemy
        self.size = size
        self.score = 0
        self.matrix = [
            [
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
            ],
            [
                2,
                0,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                1,
                1,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
            ],
            [
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
            ],
            [
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
            ],
            [
                2,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                0,
                0,
                0,
                0,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                2,
            ],
            [
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
            ],
            [
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
            ],
            [
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                1,
                1,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                2,
                1,
                2,
                2,
                2,
                2,
                1,
                2,
            ],
            [
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
            ],
            [
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
            ],
        ]

    def rule_calculation(self):
        directions = self.get_directions(self.ghost.line, self.ghost.column)
        if len(directions) >= 3:
            self.ghost.corner(directions)
        col = self.pacman.column_intent
        lin = self.pacman.line_intent
        if 0 <= col <= 27 and 0 <= lin <= 28:
            if self.matrix[lin][col] != 2:
                self.pacman.movement_aproved()
                if self.matrix[lin][col] == 1:
                    self.score += 1
                    self.matrix[lin][col] = 0
        col = int(self.ghost.column_intent)
        lin = int(self.ghost.line_intent)
        if 0 <= col <= 27 and 0 <= lin <= 28 and self.matrix[lin][col] != 2:
            self.ghost.movement_aproved()
        else:
            self.ghost.movement_denied(directions)

    def draw(self, screen, font):
        for id_line, line in enumerate(self.matrix):
            self.draw_line(screen, id_line, line)
        self.draw_score(screen, font)

    def get_directions(self, line, column):
        directions = []
        if self.matrix[int(line - 1)][int(column)] != 2:
            directions.append(up)
        if self.matrix[int(line + 1)][int(column)] != 2:
            directions.append(down)
        if self.matrix[int(line)][int(column + 1)] != 2:
            directions.append(right)
        if self.matrix[int(line)][int(column - 1)] != 2:
            directions.append(left)
        return directions

    def draw_line(self, screen, id_line, line):
        for id_column, column in enumerate(line):
            x = id_column * self.size
            y = id_line * self.size
            half = self.size / 2
            color = blue if column == 2 else black
            pg.draw.rect(screen, color, (x, y, self.size, self.size), 0)
            if column == 1:
                pg.draw.circle(screen, yellow, (x + half, y + half), self.size / 7, 0)

    def draw_score(self, screen, font):
        x_position = 30 * self.size
        img_text = font.render(f"Score: {self.score}", True, yellow)
        screen.blit(img_text, (x_position, 50))

    def event_processing(self, events):
        for e in events:
            if e.type == pg.QUIT:
                exit()


class Pacman(GameElements):
    def __init__(self, size, column=1, line=1):
        self.column = column
        self.line = line
        self.size = size
        self.center_x = 0
        self.center_y = 0
        self.radius = self.size / 2
        self.speed = 1
        self.speed_x = 0
        self.speed_y = 0
        self.column_intent = self.column
        self.line_intent = self.line

    def rule_calculation(self):
        # change pacman position
        self.column_intent = self.column + self.speed_x
        self.line_intent = self.line + self.speed_y

        self.center_x = self.size * self.column + self.radius
        self.center_y = self.size * self.line + self.radius

    def movement_aproved(self):
        self.column = self.column_intent
        self.line = self.line_intent

    def draw(self, screen):
        # draw pacman's body
        pg.draw.circle(screen, yellow, (self.center_x, self.center_y), self.radius, 0)

        # draw pacman's mouth
        mouth = [
            (self.center_x, self.center_y),
            (self.center_x + self.radius, self.center_y),
            (self.center_x + self.radius, self.center_y - self.radius),
        ]
        pg.draw.polygon(screen, black, mouth, 0)

        # draw pacman's eye
        eye_x = self.center_x + self.radius * 0.25
        eye_y = self.center_y - self.radius * 0.5
        eye_radius = self.radius * 0.125
        pg.draw.circle(screen, black, (eye_x, eye_y), eye_radius, 0)

    def event_processing(self, events):
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


class Ghost(GameElements):
    def __init__(self, color, size, column=6, line=8):
        self.column = column
        self.line = line
        self.column_intent = self.column
        self.line_intent = self.line
        self.color = color
        self.size = size
        self.direction = up
        self.speed = 1

    def rule_calculation(self):
        if self.direction == up:
            self.line_intent -= self.speed
        elif self.direction == down:
            self.line_intent += self.speed
        elif self.direction == left:
            self.column_intent -= self.speed
        elif self.direction == right:
            self.column_intent += self.speed

    def change_direction(self, directions):
        self.direction = random.choice(directions)

    def corner(self, directions):
        self.change_direction(directions)

    def movement_aproved(self):
        self.line = self.line_intent
        self.column = self.column_intent

    def movement_denied(self, directions):
        self.line_intent = self.line
        self.column_intent = self.column
        self.change_direction(directions)

    def draw(self, screen):
        # draw ghost's body
        slice = self.size / 14
        px = int(self.column * self.size)
        py = int(self.line * self.size)
        points = [
            (int(px), int(py + self.size)),
            (int(px + slice * 1), int(py + slice * 6)),
            (int(px + slice * 2), int(py + slice * 3)),
            (int(px + slice * 3), int(py + slice * 2)),
            (int(px + slice * 4), int(py + slice * 1)),
            (int(px + slice * 6), int(py)),
            (int(px + slice * 8), int(py)),
            (int(px + slice * 10), int(py + slice * 1)),
            (int(px + slice * 11), int(py + slice * 2)),
            (int(px + slice * 12), int(py + slice * 3)),
            (int(px + slice * 13), int(py + slice * 6)),
            (int(px + self.size), int(py + self.size)),
            (int(px + slice * 13), int(py + slice * 14)),
            (int(px + slice * 11), int(py + slice * 11)),
            (int(px + slice * 9), int(py + slice * 14)),
            (int(px + slice * 7), int(py + slice * 11)),
            (int(px + slice * 5), int(py + slice * 14)),
            (int(px + slice * 3), int(py + slice * 11)),
            (int(px + slice * 1), int(py + slice * 14)),
        ]
        pg.draw.polygon(screen, self.color, points, 0)

        # draw ghost's eyes
        external_eye_radius = int(slice * 1.5)
        internal_eye_radius = int(slice * 0.75)

        left_eye_x = int(px + slice * 5)
        left_eye_y = int(py + slice * 3)

        right_eye_x = int(px + slice * 9)
        right_eye_y = int(py + slice * 3)

        pg.draw.circle(screen, white, (left_eye_x, left_eye_y), external_eye_radius, 0)
        pg.draw.circle(screen, blue, (left_eye_x, left_eye_y), internal_eye_radius, 0)

        pg.draw.circle(
            screen, white, (right_eye_x, right_eye_y), external_eye_radius, 0
        )
        pg.draw.circle(screen, blue, (right_eye_x, right_eye_y), internal_eye_radius, 0)

    def event_processing(self):
        return super().event_processing()
