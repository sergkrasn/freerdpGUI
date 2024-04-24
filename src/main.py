import os

from PyQt6.QtCore import pyqtSignal, Qt, QCoreApplication, QFile
from PyQt6.QtWidgets import QFrame, QComboBox, QCheckBox, QSlider, QRadioButton
from src.passwd import Passwd
from src.freerdp import FreeRDP
from src.ui_main import Ui_Main
from src.settings import Settings


class Main(QFrame):
    mainRequest = pyqtSignal()

    def __init__(self, parent=None, filepath=None, wx=None):
        super(Main, self).__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.parent = parent
        self.filepath = filepath

        self.dialog = None
        self.ui.password = None
        self.freerdp = FreeRDP(self)
        self.ui.printers_list = QComboBox(self)
        self.ui.printers_list.hide()
        self.ui.change_displays = QCheckBox(self)
        self.ui.change_displays.hide()
        self.ui.monitors = QCheckBox(self)
        self.ui.monitors.hide()
        self.ui.printers = QCheckBox(self)
        self.ui.printers.hide()
        self.ui.floatbar = QCheckBox(self)
        self.ui.floatbar.hide()
        self.ui.clipboard = QCheckBox(self)
        self.ui.clipboard.hide()
        self.ui.homedir = QCheckBox(self)
        self.ui.homedir.hide()
        self.ui.grab_keyboard = QComboBox(self)
        self.ui.grab_keyboard.hide()
        self.ui.resolution = QSlider(self)
        self.ui.resolution.hide()
        self.ui.disable_security = QCheckBox(self)
        self.ui.disable_security.hide()
        self.ui.security_protocol = QComboBox(self)
        self.ui.security_protocol.hide()
        self.ui.multimedia = QCheckBox(self)
        self.ui.multimedia.hide()
        self.ui.monitor1 = QRadioButton(self)
        self.ui.monitor1.hide()
        self.ui.monitor2 = QRadioButton(self)
        self.ui.monitor2.hide()
        self.ui.token_change = QCheckBox(self)
        self.ui.token_change.hide()
        self.ui.token = QComboBox(self)
        self.ui.token.hide()

        QCoreApplication.setOrganizationName("freerdp")
        QCoreApplication.setApplicationName("freerdpGUI")
        self.settings = Settings(self, filepath)

        self.ui.button_enter.clicked.connect(self.dialog_passwd)
        self.ui.button_tools.clicked.connect(self.mainRequest)
        self.ui.button_close.clicked.connect(self.parent.parent.close)

    def dialog_passwd(self):
        self.dialog = Passwd(self)
        self.dialog.show()

    def save_settings(self):
        if self.filepath is not None:
            QFile((('/'.join(self.settings.fileName().split('/')[:-1])) + '/' +
               os.path.splitext(os.path.basename(self.filepath))[0]) + '.conf').remove()

        if len(self.settings.value("SETTINGS_SERVER", [], "QStringList")) == 0:
            self.settings.setValue("SETTINGS_SERVER", [QComboBox.currentText(self.ui.server)])
        else:
            server = []
            for servers in self.settings.value("SETTINGS_SERVER", [], "QStringList"):
                server.append(servers)
            server.append(QComboBox.currentText(self.ui.server))
            for x in server:
                if server.count(x) > 1:
                    server.remove(x)
            self.settings.setValue("SETTINGS_SERVER", server)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return.value or event.key() == Qt.Key.Key_Enter.value:
            self.dialog_passwd()
        else:
            super(Main, self).keyPressEvent(event)
