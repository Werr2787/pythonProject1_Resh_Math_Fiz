from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QMainWindow):
    def __init__(self, ):
        super().__init__()

        self.resize(1000, 1000)
        self.center()
        self.general()

    def general(self):
        # Menu Bar
        self.exitAction = QtWidgets.QAction('&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.triggered.connect(QtWidgets.qApp.quit)
        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu('&File')
        self.file_menu.addAction(self.exitAction)

        self.lbl = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap('')
        self.lbl.setPixmap(self.pix)
        self.lbl.move(200, 200)

    def center(self):
        frame_window = self.frameGeometry()
        center_coord = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_window.moveCenter(center_coord)
        self.move(frame_window.topLeft())


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    w = Window()
    w.show()

    sys.exit(app.exec_())