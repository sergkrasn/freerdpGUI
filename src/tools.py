import os

from os.path import expanduser
from PyQt6.QtCore import pyqtSignal, Qt, QCoreApplication, QFile
from PyQt6.QtWidgets import QFrame, QLineEdit, QComboBox, QFileDialog
from src.ui_tools import Ui_Tools
from src.passwd import Passwd
from src.freerdp import FreeRDP
from src.settings import Settings
import src.window


class Tools(QFrame):
    toolsRequest = pyqtSignal()

    def __init__(self, parent=None, filepath=None, wx=None):
        super(Tools, self).__init__(parent)
        self.ui = Ui_Tools()
        self.ui.setupUi(self)
        self.parent = parent
        self.filepath = filepath

        self.ui.password = None
        self.dialog = None
        self.freerdp = FreeRDP(self)

        QCoreApplication.setOrganizationName("freerdp")
        QCoreApplication.setApplicationName("freerdpGUI")
        self.settings = Settings(self, filepath)
        self.screen_resolution()
        QComboBox.setFocus(self.ui.server)

        self.ui.button_enter.clicked.connect(self.dialog_passwd)
        self.ui.button_tools.clicked.connect(self.toolsRequest)
        self.ui.button_close.clicked.connect(self.parent.parent.close)
        self.ui.resolution.valueChanged.connect(self.screen_resolution)
        self.ui.monitors.stateChanged.connect(self.check_monitors)
        self.ui.floatbar.stateChanged.connect(self.check_floatbar)
        self.ui.printers.stateChanged.connect(self.check_printers)
        self.ui.clipboard.stateChanged.connect(self.check_clipboard)
        self.ui.change_displays.stateChanged.connect(self.check_change_display)
        self.ui.homedir.stateChanged.connect(self.check_homedir)
        self.ui.grab_keyboard.currentTextChanged.connect(self.choosing_grab_keyboard)
        self.ui.button_open.clicked.connect(self.openFileNameDialog)
        self.ui.button_save.clicked.connect(self.saveFileNameDialog)
        self.ui.printers_list.currentTextChanged.connect(self.choosing_printers_list)
        self.ui.disable_security.stateChanged.connect(self.disable_security)
        self.ui.security_protocol.currentTextChanged.connect(self.security_protocol)
        self.ui.multimedia.stateChanged.connect(self.check_multimedia)
        self.ui.monitor1.clicked.connect(self.check_monitor1)
        self.ui.monitor2.clicked.connect(self.check_monitor2)

    def saveFileNameDialog(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Выбор путь для сохранения настроек",
                                                   expanduser(
                                                       "~/Desktop/" + QComboBox.currentText(self.ui.server)) + '.frdp',
                                                   "Free RDP settings files (*.frdp)")
        if file_name:
            value = '[General]\n'
            if not "SETTINGS_SERVER" in self.settings.allKeys():
                value += "SETTINGS_SERVER" + '=' + QComboBox.currentText(self.ui.server) + '\n'

            if not "SETTING_DOMAIN" in self.settings.allKeys():
                value += "SETTING_DOMAIN" + '=' + QLineEdit.text(self.ui.domain) + '\n'

            if not "SETTING_USERNAME" in self.settings.allKeys():
                value += "SETTING_USERNAME" + '=' + QLineEdit.text(self.ui.username) + '\n'

            for key in self.settings.allKeys():
                if key == "SETTINGS_SERVER":
                    value += "SETTINGS_SERVER" + '=' + QComboBox.currentText(self.ui.server) + '\n'
                else:
                    value += (key + '=' + str(self.settings.value(key)) + '\n')
            with open(file_name, 'w') as file:
                file.write(value)

    def openFileNameDialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выбор файла настроек",
                                                   expanduser("~/Desktop/"),
                                                   "Free RDP settings files (*.frdp)")
        if file_name:
            window = src.window.Window(file_name)
            window.show()

    def dialog_passwd(self):
        self.settings.setValue("SETTING_USERNAME", QLineEdit.text(self.ui.username))
        self.settings.setValue("SETTING_DOMAIN", QLineEdit.text(self.ui.domain))
        self.dialog = Passwd(self)
        self.dialog.show()

    def security_protocol(self):
        self.settings.setValue("SETTING_SECURITY_PROTOCOL", str(self.ui.security_protocol.currentText()))

    def disable_security(self):
        self.settings.setValue("SETTING_DISABLE_SECURITY", str(self.ui.disable_security.isChecked()))
        if self.ui.disable_security.isChecked():
            self.ui.security_protocol.setEnabled(True)
        else:
            self.ui.security_protocol.setEnabled(False)

    def check_monitor1(self):
        self.settings.setValue("MONITOR1", str(self.ui.monitor1.isChecked()))
        self.settings.setValue("MONITOR2", str(self.ui.monitor2.isChecked()))

    def check_monitor2(self):
        self.settings.setValue("MONITOR1", str(self.ui.monitor1.isChecked()))
        self.settings.setValue("MONITOR2", str(self.ui.monitor2.isChecked()))

    def check_multimedia(self):
        self.settings.setValue("MULTIMEDIA", str(self.ui.multimedia.isChecked()))

    def choosing_printers_list(self):
        self.settings.setValue("SETTING_PRINTERS-LIST", str(self.ui.printers_list.currentText()))

    def check_floatbar(self):
        self.settings.setValue("SETTING_FLOATBAR", str(self.ui.floatbar.isChecked()))

    def check_printers(self):
        if self.ui.printers.isChecked():
            self.ui.printers_list.setEnabled(True)
        else:
            self.ui.printers_list.setEnabled(False)
        self.settings.setValue("SETTING_PRINTERS", str(self.ui.printers.isChecked()))

    def check_clipboard(self):
        self.settings.setValue("SETTING_CLIPBOARD", str(self.ui.clipboard.isChecked()))

    def check_homedir(self):
        self.settings.setValue("SETTING_HOMEDIR", str(self.ui.homedir.isChecked()))

    def check_change_display(self):
        self.settings.setValue("SETTING_CHANGE-DISPLAY", str(self.ui.change_displays.isChecked()))

    def check_monitors(self):
        self.settings.setValue("SETTING_MONITOR", str(self.ui.monitors.isChecked()))
        self.ui.resolution.setValue(12)
        if self.ui.monitors.isChecked():
            self.ui.resolution.setEnabled(False)
            self.ui.change_displays.setEnabled(True)
            self.ui.monitor1.setEnabled(False)
            self.ui.monitor2.setEnabled(False)
        else:
            self.ui.resolution.setEnabled(True)
            self.ui.change_displays.setEnabled(False)
            self.ui.change_displays.setChecked(False)
            self.ui.monitor1.setEnabled(True)
            self.ui.monitor2.setEnabled(True)

    def choosing_grab_keyboard(self):
        self.settings.setValue("SETTING_KEYBOARD", int(QComboBox.currentIndex(self.ui.grab_keyboard)))

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

    def screen_resolution(self):
        value = int(self.ui.resolution.value())
        self.set_value(value)
        self.settings.setValue("SETTING_RESOLUTION", value)
        if value != 12:
            self.ui.monitor1.setEnabled(False)
            self.ui.monitor2.setEnabled(False)
        else:
            if not self.ui.monitors.isChecked():
                self.ui.monitor1.setEnabled(True)
                self.ui.monitor2.setEnabled(True)

    def set_value(self, value):
        if value == 1:
            self.ui.label_screen_resolution.setText("640 на 480 пикселей")
            self.ui.monitors.setChecked(False)
            return "640x480"
        if value == 2:
            self.ui.label_screen_resolution.setText("800 на 600 пикселей")
            self.ui.monitors.setChecked(False)
            return "800x600"
        if value == 3:
            self.ui.label_screen_resolution.setText("1024 на 768 пикселей")
            self.ui.monitors.setChecked(False)
            return "1024x768"
        if value == 4:
            self.ui.label_screen_resolution.setText("1280 на 720 пикселей")
            self.ui.monitors.setChecked(False)
            return "1280x720"
        if value == 5:
            self.ui.label_screen_resolution.setText("1280 на 768 пикселей")
            self.ui.monitors.setChecked(False)
            return "1280x768"
        if value == 6:
            self.ui.label_screen_resolution.setText("1280 на 800 пикселей")
            self.ui.monitors.setChecked(False)
            return "1280x800"
        if value == 7:
            self.ui.label_screen_resolution.setText("1280 на 1024 пикселей")
            self.ui.monitors.setChecked(False)
            return "1280x1024"
        if value == 8:
            self.ui.label_screen_resolution.setText("1366 на 768 пикселей")
            self.ui.monitors.setChecked(False)
            return "1366x768"
        if value == 9:
            self.ui.label_screen_resolution.setText("1440 на 900 пикселей")
            self.ui.monitors.setChecked(False)
            return "1440x900"
        if value == 10:
            self.ui.label_screen_resolution.setText("1400 на 1050 пикселей")
            self.ui.monitors.setChecked(False)
            return "1400x1050"
        if value == 11:
            self.ui.label_screen_resolution.setText("1920 на 1080 пикселей")
            self.ui.monitors.setChecked(False)
            return "1920x1080"
        if value == 12:
            self.ui.label_screen_resolution.setText("Во весь экран")
            # self.ui.monitors.setChecked(True)
            return "fullscreen"

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return.value or event.key() == Qt.Key.Key_Enter.value:
            self.dialog_passwd()
        else:
            super(Tools, self).keyPressEvent(event)
