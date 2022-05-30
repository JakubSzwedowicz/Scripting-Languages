# Author: Jakub Szwedowicz
# Date: 29.05.2022
# e-mail: kuba.szwedowicz@gmail.com

# from PyQt6.QtCore import pyqtSignal, pyqtBoundSignal, Qt, QObject
# from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
# from PyQt6.QtGui import QPainter, QKeyEvent
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


# class View(QGraphicsView, QObject):
class View(QGraphicsView):
    Wpress = pyqtSignal()
    Wrelease = pyqtSignal()
    Spress = pyqtSignal()
    Srelease = pyqtSignal()
    UPpress = pyqtSignal()
    UPrelease = pyqtSignal()
    DownPress = pyqtSignal()
    Downrelease = pyqtSignal()

    def __init__(self, size: QSizeF, parent=None):
        super(View, self).__init__(parent)
        self.setFixedSize(size.width(), size.height())
        # self.setSceneRect()
        self.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.setWindowTitle('Pong')
        self.setRenderHint(QPainter.RenderHint.Antialiasing)

        # self.setSceneRect(self.x() - 2, self.y() + self.height() / 2 - 2, self.width(), self.height())
        # print(self.x())
        # self.setSceneRect(5, 5, self.width() - 10, self.height() - 10)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.isAutoRepeat():
            return
        print('press: ' + event.text())
        if event.key() == Qt.Key.Key_W:
            self.Wpress.emit()
        elif event.key() == Qt.Key.Key_S:
            self.Spress.emit()
        elif event.key() == Qt.Key.Key_Up:
            self.UPpress.emit()
        elif event.key() == Qt.Key.Key_Down:
            self.DownPress.emit()

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        if event.isAutoRepeat():
            return
        print('release: ' + event.text())
        if event.key() == Qt.Key.Key_W:
            self.Wrelease.emit()
        elif event.key() == Qt.Key.Key_S:
            self.Srelease.emit()
        elif event.key() == Qt.Key.Key_Up:
            self.UPrelease.emit()
        elif event.key() == Qt.Key.Key_Down:
            self.Downrelease.emit()


class SceneAndView:
    _boundry = [5, 5]
    _view_point = QPointF(-10, -10)
    _view_size = QSizeF(700, 400)
    # _scene_point = QPointF(_boundry[0], _boundry[1])
    _scene_point = QPointF(0, 0)
    _scene_size = QSizeF(_view_size.width() - _boundry[0], _view_size.height() - _boundry[1])

    def __init__(self):
        self.scene = QGraphicsScene()
        # self.scene.setSceneRect(QRectF(self._scene_point, self._scene_size))
        # self.scene.setSceneRect(QRectF(self._scene_point, self._scene_size))
        self.view = View(size=self._view_size)
        self.view.setScene(self.scene)
        self.view.setSceneRect(QRectF(self._scene_point, self._scene_size))
