from PyQt6.QtWidgets import QMessageBox


def set_value(value):
    if value == 1:
        return "640x480"
    if value == 2:
        return "800x600"
    if value == 3:
        return "1024x768"
    if value == 4:
        return "1280x720"
    if value == 5:
        return "1280x768"
    if value == 6:
        return "1280x800"
    if value == 7:
        return "1280x1024"
    if value == 8:
        return "1366x768"
    if value == 9:
        return "1440x900"
    if value == 10:
        return "1400x1050"
    if value == 11:
        return "1920x1080"
    if value == 12:
        return "fullscreen"


def msg(text):
    message = QMessageBox()
    message.setIcon(QMessageBox.Icon.Warning)
    message.setWindowTitle("Ошибка")
    message.setText(str(text))
    message.exec()
