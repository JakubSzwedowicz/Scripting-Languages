# Author: Jakub Szwedowicz
# Date: 29.05.2022
# e-mail: kuba.szwedowicz@gmail.com
import random

from PyQt6.QtWidgets import *
from PyQt6.QtCore import QPointF, QTimer, Qt
from PyQt6.QtGui import *
import game_engine
import game_objects


class PongGame:
    _timers_interval = 30

    def __init__(self, parent=None):
        self.scene_view = game_engine.SceneAndView()
        self.boundary = [self.scene_view.view.width(), self.scene_view.view.height()]
        self._score = [0, 0]

        self._ball = game_objects.Ball()
        self.scene_view.scene.addItem(self._ball)

        self._paddle_left = game_objects.Paddle(max_height=self.boundary[1])
        self.scene_view.scene.addItem(self._paddle_left)

        self._paddle_right = game_objects.Paddle(max_height=self.boundary[1])
        self.scene_view.scene.addItem(self._paddle_right)

        self.scene_view.scene.addLine(self.boundary[0] / 2, 0, self.boundary[0] / 2,
                                      self.boundary[1], QPen(Qt.GlobalColor.white))

        self._score_text = QGraphicsTextItem()
        self._score_text.setDefaultTextColor(Qt.GlobalColor.white)
        self._reset_scoreboard()
        self._score_text.setPos(self.boundary[0] / 2 - self._score_text.boundingRect().width() / 2, 0)
        self.scene_view.scene.addItem(self._score_text)

        self._initialize()

    def start_game(self):
        self._reset_scoreboard()
        self._reset_gameobjects()
        self.serve(random.choice([True, False]))
        self._run()

    def _run(self):
        self._timer.start(30)

    def _initialize(self):
        self._reset_gameobjects()
        self._reset_scoreboard()
        self._initialize_connexions()
        self._set_timer()

    def _reset_gameobjects(self):
        self._ball.spawn_at_point((self.boundary[0] - self._ball.radius) / 2, self.boundary[1] / 2)
        self._paddle_left.spawn_at_point(0, 0)
        self._paddle_right.spawn_at_point(self.boundary[0] - 15, 0)

    def _reset_scoreboard(self):
        self._score = [0, 0]
        self.update_sore()

    def _initialize_connexions(self):
        self.scene_view.view.Wpress.connect(self._paddle_left.set_move_up)
        self.scene_view.view.Wrelease.connect(self._paddle_left.set_stop)
        self.scene_view.view.Spress.connect(self._paddle_left.set_move_down)
        self.scene_view.view.Srelease.connect(self._paddle_left.set_stop)
        self.scene_view.view.UPpress.connect(self._paddle_right.set_move_up)
        self.scene_view.view.UPrelease.connect(self._paddle_right.set_stop)
        self.scene_view.view.DownPress.connect(self._paddle_right.set_move_down)
        self.scene_view.view.Downrelease.connect(self._paddle_right.set_stop)

    def _set_timer(self):
        self._timer = QTimer(self.scene_view.view)
        self._timer.setInterval(self._timers_interval)
        self._timer.timeout.connect(self.ball_move)
        self._timer.timeout.connect(self._paddle_left.move)
        self._timer.timeout.connect(self._paddle_right.move)

    def update_sore(self):
        msg = f'{self._score[0]}   {self._score[1]}'
        self._score_text.setPlainText(msg)

    def serve(self, serve_left: bool):
        self._ball.setPos(0, random.choice(range(int((-self.boundary[1] - self._ball.radius) / 2), int(self.boundary[1] / 2))))
        if serve_left:
            self._ball.velocity = [-10, random.choice(range(-3, 4, 1))]
        else:
            self._ball.velocity = [10, random.choice([-3, -2, -1, 3, 2, 1])]

    def ball_hits_paddle(self):
        return self._ball.collidesWithItem(self._paddle_left) or self._ball.collidesWithItem(self._paddle_right)

    def ball_hits_boundary(self):
        return self._ball.y() < -self.boundary[1] / 2 + 15 or self._ball.y() > self.boundary[1] / 2 - 15

    def ball_missed(self):
        if self._ball.x() < -self.boundary[0] / 2:
            return True, 'left'
        elif self._ball.x() > self.boundary[0] / 2:
            return True, 'right'
        else:
            return False, 'none'

    def ball_move(self):
        if self.ball_hits_boundary():
            self._ball.reflectY()
        elif self.ball_hits_paddle():
            self._ball.reflectX()
        elif (missed := self.ball_missed())[0]:
            if missed[1] == 'left':
                self._score[1] += 1
                self.serve(True)
            elif missed[1] == 'right':
                self._score[0] += 1
                self.serve(False)
            self.update_sore()
        self._ball.move()

