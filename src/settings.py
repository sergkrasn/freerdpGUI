import os
import re
import shutil

from PyQt6.QtCore import QSettings


class Settings(QSettings):
    def __init__(self, parent=None, filepath=None, wx=None):
        super(Settings, self).__init__(parent)
        self.parent = parent
        self.filepath = filepath
        self.settings = QSettings('freerdp', 'freerdpGUI')

        if self.filepath is not None:
            self.copy_config()

        self.parent.ui.username.setText(self.settings.value("SETTING_USERNAME", "user", str))
        self.parent.ui.domain.setText(self.settings.value("SETTING_DOMAIN", "domain", str))
        self.parent.ui.monitors.setChecked(self.settings.value("SETTING_MONITOR", True, bool))
        self.parent.ui.resolution.setValue(self.settings.value("SETTING_RESOLUTION", 12, int))
        self.parent.ui.printers.setChecked(self.settings.value("SETTING_PRINTERS", True, bool))
        self.parent.ui.floatbar.setChecked(self.settings.value("SETTING_FLOATBAR", True, bool))
        self.parent.ui.homedir.setChecked(self.settings.value("SETTING_HOMEDIR", True, bool))
        self.parent.ui.clipboard.setChecked(self.settings.value("SETTING_CLIPBOARD", True, bool))
        self.parent.ui.disable_security.setChecked(self.settings.value("SETTING_DISABLE_SECURITY", False, bool))
        self.parent.ui.change_displays.setChecked(self.settings.value("SETTING_CHANGE-DISPLAY", False, bool))
        self.parent.ui.grab_keyboard.setCurrentIndex(self.settings.value("SETTING_KEYBOARD", 0, int))
        self.parent.ui.security_protocol.setCurrentText(self.settings.value("SETTING_SECURITY_PROTOCOL", "rdp", str))

        secure_list = ["rdp", "nla", "ext", "tls"]
        for security_protocol in secure_list:
            self.parent.ui.security_protocol.addItem(security_protocol)
            if self.settings.value("SETTING_SECURITY_PROTOCOL", str) == security_protocol:
                self.parent.ui.security_protocol.setCurrentText(security_protocol)


        if self.parent.ui.disable_security.isChecked():
            self.parent.ui.security_protocol.setEnabled(True)
        else:
            self.parent.ui.security_protocol.setEnabled(False)

        for servers in reversed(self.settings.value("SETTINGS_SERVER", [], "QStringList")):
            self.parent.ui.server.addItem(servers)

        printers = os.popen("lpstat -p").readlines()
        for printer in printers:
            if re.search(r'\bprinter |принтер \b', printer):
                printer = printer.strip()
                printer = re.sub(r"printer |принтер ", "", printer)
                printer = printer.split(" сейчас", 1)[0]
                printer = re.sub(r" is idle\..*| свободен\..*", "", printer)
                self.parent.ui.printers_list.addItem(printer)
                if self.settings.value("SETTING_PRINTERS-LIST", str) == printer:
                    self.parent.ui.printers_list.setCurrentText(printer)
        if len(self.parent.ui.printers_list) == 0:
            self.parent.ui.printers.setEnabled(False)

        if self.parent.ui.monitors.isChecked():
            self.parent.ui.resolution.setEnabled(False)
            self.parent.ui.change_displays.setEnabled(True)
        else:
            self.parent.ui.resolution.setEnabled(True)
            self.parent.ui.change_displays.setEnabled(False)
            self.parent.ui.change_displays.setChecked(False)

        if self.parent.ui.printers.isChecked():
            self.parent.ui.printers_list.setEnabled(True)
        else:
            self.parent.ui.printers_list.setEnabled(False)

    def copy_config(self):
        confpath = (('/'.join(self.settings.fileName().split('/')[:-1])) + '/' +
             os.path.splitext(os.path.basename(self.filepath))[0]) + '.conf'
        shutil.copy(self.filepath, confpath)
        self.settings = QSettings('freerdp', os.path.splitext(os.path.basename(self.filepath))[0])

