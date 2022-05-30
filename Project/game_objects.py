# Author: Jakub Szwedowicz
# Date: 29.05.2022
# e-mail: kuba.szwedowicz@gmail.com

from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSizeF


class Ball(QGraphicsEllipseItem):
    _speed_increase = 0.5

    def __init__(self, radius: int = 16, parent=None):
        super(Ball, self).__init__(parent)
        self.velocity = [0, 0]
        self.radius = radius

    def spawn_at_point(self, x: float, y: float) -> None:
        self.setRect(x, y, self.radius, self.radius)

    def reflectX(self) -> None:
        self.velocity[0] = -self.velocity[0]
        if self.velocity[0] < 0:
            self.velocity[0] -= self._speed_increase
        else:
            self.velocity[0] += self._speed_increase

    def reflectY(self) -> None:
        self.velocity[1] = -self.velocity[1]

    def move(self) -> None:
        self.setX(self.x() + self.velocity[0])
        self.setY(self.y() + self.velocity[1])


class Paddle(QGraphicsRectItem):
    _options = [[False, 'up'],
                [True, 'up'],
                [True, 'down']]
    _speed_increase = 10

    def __init__(self, max_height: int, size: QSizeF = QSizeF(10, 100), parent=None):
        super(Paddle, self).__init__(parent)
        self.max_height = max_height - size.height()
        self._size = size
        self._moving = self._options[0]

    def spawn_at_point(self, x: float, y: float):
        self.setRect(x, y, self._size.width(), self._size.height())

    def set_stop(self):
        self._moving = self._options[0]

    def set_move_up(self):
        self._moving = self._options[1]

    def set_move_down(self):
        self._moving = self._options[2]

    def move(self):
        if self._moving[0]:
            print(self._moving[1])
            if self._moving[1] == 'up':
                self._move_up()
            else:
                self._move_down()

    def _move_up(self):
        if self.y() > 0:
            self.setY(self.y() - self._speed_increase)

    def _move_down(self):
        if self.y() < self.max_height:
            self.setY(self.y() + self._speed_increase)
