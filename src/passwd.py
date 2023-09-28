import os

from PyQt6.QtCore import QSettings, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QLineEdit, QDialog
from src.ui_passwd import Ui_Passwd
from src.statick import msg


class Passwd(QDialog):
    def __init__(self, parent=None, wx=None):
        super(Passwd, self).__init__(parent)
        self.ui = Ui_Passwd()
        self.ui.setupUi(self)
        self.parent = parent
        self.setWindowTitle("Введите учетные данные")
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "../resource/freerdpgui-icon.svg")))
        self.setGeometry(760, 200, 380, 260)

        self.ui.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.settings = QSettings('freerdp', 'freerdpGUI')
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
            self.parent.freerdp.freerdp()
            # self.close()
        else:
            msg("Не введены имя пользователя или пароль")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return.value or event.key() == Qt.Key.Key_Enter.value:
            self.setPasswd()
        elif event.key() == Qt.Key.Key_Escape.value:
            self.close()
        else:
            super(Passwd, self).keyPressEvent(event)