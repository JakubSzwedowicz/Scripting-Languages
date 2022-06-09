# Author: Jakub Szwedowicz
# Date: 09.06.2022
# e-mail: kuba.szwedowicz@gmail.com
import time
from PyQt6.QtWidgets import QApplication, QWidget
import sys
import game_logic
import game_ui
import game_engine


def run():
    app = QApplication(sys.argv)

    game = Game()
    game.run()

    sys.exit(app.exec())


class Game:
    def __init__(self):
        self._frames = {}
        self._actual_game = game_logic.PongGame()
        self._menu = game_ui.MenuScreen()

        self._frames['Menu'] = self._menu
        self._frames['Game'] = self._actual_game.scene_view.view

        self._menu.connect_button('Start', self._start_game_widget_callback(self._frames['Menu'], self._actual_game))

    def run(self):
        self._menu.show()

    @staticmethod
    def _start_game_widget_callback(to_hide: QWidget, game_to_show: game_logic.PongGame):
        def helper():
            to_hide.hide()
            game_to_show.scene_view.view.show()
            game_to_show.start_game()
        return helper

    @staticmethod
    def _change_visible_widget_callback(to_hide: QWidget, to_show: QWidget):
        def helper():
            to_hide.hide()
            to_show.show()
        return helper
