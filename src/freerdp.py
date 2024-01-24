import subprocess
import sys
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

        if self.parent.ui.monitors.isChecked():
            command.append('/multimon:force')
            if self.parent.ui.change_displays.isChecked():
                command.append("/monitors:1,0")
            else:
                command.append("/monitors:0,1")
        else:
            if resolution != "fullscreen":
                command.append("/size:" + resolution)
            else:
                command.append("/monitors:0")
                command.append("/multimon")

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

        if self.parent.ui.disable_security.isChecked():
            command.append("/sec:" + self.parent.ui.security_protocol.currentText())

        if self.parent.ui.multimedia.isChecked():
            command.append("/sound:sys:alsa")
            command.append("/sound:sys:oss,dev:1,format:1")
            command.append("/microphone:sys:alsa")
            command.append("/microphone:sys:oss,dev:1,format:1")

        process = subprocess.Popen(command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        i = 0
        try:
            for line in iter(process.stdout.readline, ''):
                i +=1
                # sys.stdout.flush()
                print(">>> " + str(line.rstrip()))
                if i >= 50:
                    print(">>> " + 'Output by iteration number')
                    break
                elif str(line.rstrip()) == "b''":
                    return
                elif "ERRCONNECT_CONNECT_TRANSPORT_FAILED" in str(line.rstrip()):
                    print(">>> " + str(line.rstrip()))
                    msg("Ошибка при подключении\n"
                        "Ошибка выбора протокола\n"
                        "Ошибка: ERRCONNECT_CONNECT_TRANSPORT_FAILED")
                    return
                elif "HYBRID_REQUIRED_BY_SERVER" in str(line.rstrip()):
                    print(">>> " + str(line.rstrip()))
                    msg("Ошибка при подключении\n"
                        "Ошибка выбора протокола\n"
                        "Ошибка: ERRCONNECT_SECURITY_NEGO_CONNECT_FAILED")
                    return
                elif "ERRCONNECT_SECURITY_NEGO_CONNECT_FAILED" in str(line.rstrip()):
                    print(">>> " + str(line.rstrip()))
                    msg("Ошибка при подключении\n"
                        "Ошибка выбора протокола\n"
                        "Ошибка: ERRCONNECT_SECURITY_NEGO_CONNECT_FAILED")
                    return
                elif "ERRCONNECT_DNS_NAME_NOT_FOUND" in str(line.rstrip()):
                    print(">>> " + str(line.rstrip()))
                    msg("Ошибка при подключении\n"
                        "Сервер не найден\n"
                        "Ошибка: ERRCONNECT_DNS_NAME_NOT_FOUND")
                    return
                elif "ERRCONNECT_LOGIN_FAILURE" in str(line.rstrip()):
                    print(">>> " + str(line.rstrip()))
                    msg("Ошибка при подключении\n"
                        "Проверьте правильность ввода имени пользователя или пароля\n"
                        "Ошибка: ERRCONNECT_LOGIN_FAILURE")
                    return
                elif "STATUS_LOGON_FAILURE" in str(line.rstrip()):
                    print(">>> " + str(line.rstrip()))
                    msg("Ошибка при подключении\n"
                        "Проверьте правильность ввода имени пользователя или пароля\n"
                        "Ошибка: STATUS_LOGON_FAILURE")
                elif "ERRCONNECT_CONNECT_FAILED" in str(line.rstrip()):
                    print(">>> " + str(line.rstrip()))
                    msg("Ошибка при подключении\n"
                        "Сервер не отвечает\n"
                        "Ошибка: ERRCONNECT_CONNECT_FAILED")
                    return
                # sys.stdout.flush()
            self.parent.save_settings()
            QCoreApplication.exit(0)
        except:
            msg("Ошибка приложения")
