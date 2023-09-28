import os
import platform
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from src.main import Main
from src.tools import Tools
from src.statick import msg


class Window(QMainWindow):
    def __init__(self, filepath=None, parent=None):
        super(Window, self).__init__(parent)
        if platform != "linux" or platform != "linux2":
            self.pages = StackPage(self, filepath)
            self.setWindowTitle("Подключение к удаленному рабочему столу")
            self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "../resource/freerdpgui-icon.svg")))
            self.setGeometry(700, 200, 520, 260)
            self.setFixedSize(520, 260)
            self.setCentralWidget(self.pages)
        else:
            msg("Данная программа запускаеться только на ОС Linux")
            sys.exit()

    def resize_main(self):
        self.setFixedSize(520, 260)

    def resize_tools(self):
        self.setFixedSize(520, 420)


class StackPage(QStackedWidget):
    def __init__(self, parent=None, filepath=None):
        super(StackPage, self).__init__(parent)
        self.parent = parent

        self.page1 = Main(self, filepath)
        self.page2 = Tools(self, filepath)
        self.addWidget(self.page1)
        self.addWidget(self.page2)

        self.page1.mainRequest.connect(self.main)
        self.page2.toolsRequest.connect(self.tools)

    def main(self):
        self.setCurrentIndex(1)
        self.parent.resize_tools()

    def tools(self):
        self.setCurrentIndex(0)
        self.parent.resize_main()


def main(filepath=None):
    import sys

    app = QApplication(sys.argv)
    if filepath is None:
        window = Window()
    else:
        if os.path.exists(filepath):
            window = Window(filepath)
        else:
            window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
