import os

from PyQt6.QtCore import QSettings, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QLineEdit, QDialog, QComboBox, QSlider, QCheckBox, QRadioButton
from src.ui_passwd import Ui_Passwd
from src.statick import msg
from src.settings import Settings

class Passwd(QDialog):
    def __init__(self, parent=None, wx=None):
        super(Passwd, self).__init__(parent)
        self.ui = Ui_Passwd()
        self.ui.setupUi(self)
        self.parent = parent
        self.setWindowTitle("Введите учетные данные")
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "../resource/freerdpgui-icon.svg")))
        self.setGeometry(760, 200, 380, 260)

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
        self.ui.server = QComboBox(self)
        self.ui.server.hide()
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

        self.ui.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.settings = Settings(self, self.parent.filepath)
        self.ui.username.setText(self.settings.value("SETTING_USERNAME", "", str))
        self.ui.domain.setText(self.settings.value("SETTING_DOMAIN", "", str))

        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_ok.clicked.connect(self.setPasswd)

        if QLineEdit.text(self.ui.username) != "":
            QLineEdit.setFocus(self.ui.password)
        else:
            QLineEdit.setFocus(self.ui.username)

    def setPasswd(self):
        if QLineEdit.text(self.ui.password) != "" and QLineEdit.text(self.ui.username) != "":
            self.parent.username = QLineEdit.text(self.ui.username)
            self.parent.domain = QLineEdit.text(self.ui.domain)
            self.parent.password = QLineEdit.text(self.ui.password)
            self.settings.setValue("SETTING_USERNAME", QLineEdit.text(self.ui.username))
            self.settings.setValue("SETTING_DOMAIN", QLineEdit.text(self.ui.domain))
            self.close()
            self.parent.freerdp.freerdp()
        else:
            msg("Не введены имя пользователя или пароль")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return.value or event.key() == Qt.Key.Key_Enter.value:
            self.setPasswd()
        elif event.key() == Qt.Key.Key_Escape.value:
            self.close()
        else:
            super(Passwd, self).keyPressEvent(event)