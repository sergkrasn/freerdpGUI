from subprocess import Popen
from PyQt6.QtCore import QCoreApplication
from src.statick import set_value, msg
from PyQt6.QtWidgets import QComboBox, QDialog


class FreeRDP(QDialog):
    def __init__(self, parent=None, wx=None):
        super(FreeRDP, self).__init__(parent)
        self.parent = parent

    def freerdp(self):
        package_name = 'xfreerdp'

        server = QComboBox.currentText(self.parent.ui.server)
        password = self.parent.password
        password.encode('utf-8')
        resolution = set_value(self.parent.ui.resolution.value())
        if len(server) == 0:
            msg("Не указан адрес сервера")
            return
        elif self.parent.username == '':
            msg("Не указан логин пользователя")
            return
        elif self.parent.password == '':
            msg("Не введен пароль")
            return
        else:
            command = [package_name,
                       "/v:" + server,
                       "/u:" + self.parent.username,
                       "/p:" + password,
                       "/cert:ignore"]

        if len(self.parent.domain) != 0:
            command.append("/d:" + self.parent.domain)

        if self.parent.ui.change_displays.isChecked():
            command.append("/monitors:1,0")
        else:
            command.append("/monitors:0,1")

        if self.parent.ui.monitors.isChecked():
            command.append('/multimon')

        if self.parent.ui.printers.isChecked():
            command.append("/a:printer," + self.parent.ui.printers_list.currentText())

        if self.parent.ui.floatbar.isChecked():
            command.append("/floatbar:sticky:on,default:visible,show:fullscreen")

        if self.parent.ui.homedir.isChecked():
            command.append("+home-drive")

        if self.parent.ui.clipboard.isChecked():
            command.append("+clipboard")

        if QComboBox.currentIndex(self.parent.ui.grab_keyboard) == 1:
            command.append("-grab-keyboard")

        if resolution != "fullscreen":
            command.append("/size:" + resolution)

        Popen(command)
        self.parent.save_settings()
        QCoreApplication.exit(0)
