# Author: Jakub Szwedowicz
# Date: 09.06.2022
# e-mail: kuba.szwedowicz@gmail.com

from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from typing import Dict


def create_button(text: str) -> QPushButton:
    button = QPushButton(text)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setStyleSheet("*{Border: 4px solid '#BC006C';" +
                         "Border-radius: 15px;" +
                         "font-size: 35px;" +
                         "color: 'white';" +
                         "padding: 25px 0;" +
                         "margin: 100px 200px;}" +
                         "*:hover{background: '#BC006C';}")
    return button


class MenuScreen(QWidget):
    _DEFAULT_SCREEN_SIZE = [700, 400]

    def __init__(self, parent=None):
        super(MenuScreen, self).__init__(parent)
        self.setWindowTitle('Pong')
        self.setFixedSize(MenuScreen._DEFAULT_SCREEN_SIZE[0], MenuScreen._DEFAULT_SCREEN_SIZE[1])
        self.setStyleSheet('background: #161219;')

        self._grid = QGridLayout()
        self._buttons = {'Start': create_button('Start')}
        self._grid.addWidget(self._buttons['Start'], 1, 0)

        self.setLayout(self._grid)

    def get_start_button_name(self) -> str:
        return 'Start'

    def connect_button(self, button: str, function):
        self._buttons[button].clicked.connect(function)
