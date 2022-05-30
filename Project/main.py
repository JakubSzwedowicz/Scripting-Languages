from PyQt6.QtWidgets import QApplication
import sys

import game_logic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = game_logic.PongGame()
    game._scene_view.view.show()
    sys.exit(app.exec())

