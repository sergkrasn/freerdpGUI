# Form implementation generated from reading ui file 'tools.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Tools(object):
    def setupUi(self, Tools):
        Tools.setObjectName("Tools")
        Tools.resize(583, 473)
        self.gridLayout = QtWidgets.QGridLayout(Tools)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_tools = QtWidgets.QToolButton(parent=Tools)
        self.button_tools.setObjectName("button_tools")
        self.horizontalLayout_2.addWidget(self.button_tools)
        self.label = QtWidgets.QLabel(parent=Tools)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_enter = QtWidgets.QPushButton(parent=Tools)
        self.button_enter.setObjectName("button_enter")
        self.horizontalLayout.addWidget(self.button_enter)
        self.button_close = QtWidgets.QPushButton(parent=Tools)
        self.button_close.setObjectName("button_close")
        self.horizontalLayout.addWidget(self.button_close)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_5.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(parent=Tools)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.tab_tools = QtWidgets.QTabWidget(parent=Tools)
        self.tab_tools.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tab_tools.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tab_tools.setObjectName("tab_tools")
        self.general = QtWidgets.QWidget()
        self.general.setObjectName("general")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.general)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.general)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.server = QtWidgets.QComboBox(parent=self.groupBox_5)
        self.server.setEditable(True)
        self.server.setObjectName("server")
        self.gridLayout_6.addWidget(self.server, 1, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 1, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 1, 1, 1, 1)
        self.username = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.username.setObjectName("username")
        self.gridLayout_6.addWidget(self.username, 3, 2, 1, 1)
        self.domain = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.domain.setObjectName("domain")
        self.gridLayout_6.addWidget(self.domain, 4, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 5, 1, 1, 3)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.general)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.button_save = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.button_save.setObjectName("button_save")
        self.gridLayout_7.addWidget(self.button_save, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 0, 1, 1, 3)
        self.button_open = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.button_open.setObjectName("button_open")
        self.gridLayout_7.addWidget(self.button_open, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 1, 0, 1, 2)
        self.verticalLayout_4.addWidget(self.groupBox_6)
        self.tab_tools.addTab(self.general, "")
        self.tab_printers = QtWidgets.QWidget()
        self.tab_printers.setObjectName("tab_printers")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_printers)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem6, 1, 0, 1, 1)
        self.printers = QtWidgets.QCheckBox(parent=self.tab_printers)
        self.printers.setChecked(True)
        self.printers.setObjectName("printers")
        self.gridLayout_8.addWidget(self.printers, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab_printers)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_3.addItem(spacerItem7, 3, 2, 1, 1)
        self.printers_list = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.printers_list.setObjectName("printers_list")
        self.gridLayout_3.addWidget(self.printers_list, 1, 1, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 1, 4, 1, 1)
        self.label_priners = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_priners.setObjectName("label_priners")
        self.gridLayout_3.addWidget(self.label_priners, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tab_tools.addTab(self.tab_printers, "")
        self.screen = QtWidgets.QWidget()
        self.screen.setObjectName("screen")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.screen)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.screen)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.monitor1 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.monitor1.setObjectName("monitor1")
        self.gridLayout_2.addWidget(self.monitor1, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.resolution = QtWidgets.QSlider(parent=self.groupBox)
        self.resolution.setMinimum(1)
        self.resolution.setMaximum(12)
        self.resolution.setPageStep(12)
        self.resolution.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.resolution.setObjectName("resolution")
        self.gridLayout_2.addWidget(self.resolution, 1, 2, 1, 1)
        self.monitors = QtWidgets.QCheckBox(parent=self.groupBox)
        self.monitors.setObjectName("monitors")
        self.gridLayout_2.addWidget(self.monitors, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.change_displays = QtWidgets.QCheckBox(parent=self.groupBox)
        self.change_displays.setObjectName("change_displays")
        self.gridLayout_2.addWidget(self.change_displays, 6, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 1, 0, 1, 1)
        self.label_screen_resolution = QtWidgets.QLabel(parent=self.groupBox)
        self.label_screen_resolution.setText("")
        self.label_screen_resolution.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_screen_resolution.setObjectName("label_screen_resolution")
        self.gridLayout_2.addWidget(self.label_screen_resolution, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 1)
        self.monitor2 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.monitor2.setObjectName("monitor2")
        self.gridLayout_2.addWidget(self.monitor2, 5, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem11)
        self.floatbar = QtWidgets.QCheckBox(parent=self.screen)
        self.floatbar.setChecked(True)
        self.floatbar.setObjectName("floatbar")
        self.verticalLayout_2.addWidget(self.floatbar)
        self.tab_tools.addTab(self.screen, "")
        self.resurs = QtWidgets.QWidget()
        self.resurs.setObjectName("resurs")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.resurs)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.resurs)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 1, 1, 1)
        self.grab_keyboard = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.grab_keyboard.setObjectName("grab_keyboard")
        self.grab_keyboard.addItem("")
        self.grab_keyboard.addItem("")
        self.gridLayout_4.addWidget(self.grab_keyboard, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.resurs)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.homedir = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.homedir.setChecked(True)
        self.homedir.setObjectName("homedir")
        self.gridLayout_5.addWidget(self.homedir, 2, 2, 1, 1)
        self.clipboard = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.clipboard.setChecked(True)
        self.clipboard.setObjectName("clipboard")
        self.gridLayout_5.addWidget(self.clipboard, 2, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem13, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 1, 1, 1)
        self.multimedia = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.multimedia.setChecked(False)
        self.multimedia.setObjectName("multimedia")
        self.gridLayout_5.addWidget(self.multimedia, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.tab_tools.addTab(self.resurs, "")
        self.security = QtWidgets.QWidget()
        self.security.setObjectName("security")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.security)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.security)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.security_protocol = QtWidgets.QComboBox(parent=self.groupBox_7)
        self.security_protocol.setEditable(False)
        self.security_protocol.setCurrentText("")
        self.security_protocol.setObjectName("security_protocol")
        self.gridLayout_9.addWidget(self.security_protocol, 2, 2, 1, 2)
        spacerItem14 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_9.addItem(spacerItem14, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_7)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 0, 2, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_7)
        spacerItem15 = QtWidgets.QSpacerItem(20, 140, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_6.addItem(spacerItem15)
        self.disable_security = QtWidgets.QCheckBox(parent=self.security)
        self.disable_security.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.disable_security.setToolTipDuration(-1)
        self.disable_security.setCheckable(True)
        self.disable_security.setChecked(False)
        self.disable_security.setObjectName("disable_security")
        self.verticalLayout_6.addWidget(self.disable_security)
        self.tab_tools.addTab(self.security, "")
        self.verticalLayout_5.addWidget(self.tab_tools)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Tools)
        self.tab_tools.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Tools)

    def retranslateUi(self, Tools):
        _translate = QtCore.QCoreApplication.translate
        Tools.setWindowTitle(_translate("Tools", "Form"))
        self.button_tools.setText(_translate("Tools", "..."))
        self.label.setText(_translate("Tools", "Показать параметры"))
        self.button_enter.setText(_translate("Tools", "Войти"))
        self.button_close.setText(_translate("Tools", "Отмена"))
        self.groupBox_5.setTitle(_translate("Tools", "Параметры входа"))
        self.label_14.setText(_translate("Tools", "Домен:"))
        self.label_13.setText(_translate("Tools", "Пользователь:"))
        self.label_9.setText(_translate("Tools", "Введите имя удаленного компьютера"))
        self.label_12.setText(_translate("Tools", "Компьютер:    "))
        self.label_10.setText(_translate("Tools", "При подключение необходимо будет указать учетные данные"))
        self.groupBox_6.setTitle(_translate("Tools", "Параметры подключения"))
        self.button_save.setText(_translate("Tools", "Сохранить как ..."))
        self.label_11.setText(_translate("Tools", "Сохранить текущие подключения в frdp-файл, или открыть файл"))
        self.button_open.setText(_translate("Tools", "Открыть..."))
        self.tab_tools.setTabText(self.tab_tools.indexOf(self.general), _translate("Tools", "Общие"))
        self.printers.setText(_translate("Tools", "Подключить локальные  принтеры"))
        self.groupBox_2.setTitle(_translate("Tools", "Список принтеров"))
        self.label_priners.setText(_translate("Tools", "Выберити принтер:"))
        self.tab_tools.setTabText(self.tab_tools.indexOf(self.tab_printers), _translate("Tools", "Принтеры"))
        self.groupBox.setTitle(_translate("Tools", "Настройки отображения"))
        self.monitor1.setText(_translate("Tools", "Монитор 1"))
        self.label_5.setText(_translate("Tools", "Укажите размер удаленного рабочего стола"))
        self.monitors.setText(_translate("Tools", "Использовать все мониторы для удаленного сеанса"))
        self.label_3.setText(_translate("Tools", "Меньше"))
        self.change_displays.setText(_translate("Tools", "Поменять рабочие столы местами"))
        self.label_4.setText(_translate("Tools", "Больше"))
        self.monitor2.setText(_translate("Tools", "Монитор 2"))
        self.floatbar.setText(_translate("Tools", "Отображать панель включения при работе на полный экран"))
        self.tab_tools.setTabText(self.tab_tools.indexOf(self.screen), _translate("Tools", "Экран"))
        self.groupBox_3.setTitle(_translate("Tools", "Клавиатура"))
        self.label_7.setText(_translate("Tools", "Использование сочетания клавиш:"))
        self.label_6.setText(_translate("Tools", "Пример: ALT+TAB"))
        self.grab_keyboard.setItemText(0, _translate("Tools", "На удаленном компьютере"))
        self.grab_keyboard.setItemText(1, _translate("Tools", "На этом компьютере"))
        self.groupBox_4.setTitle(_translate("Tools", "Локальные устройства и ресурсы"))
        self.homedir.setText(_translate("Tools", "Домашняя деректория"))
        self.clipboard.setText(_translate("Tools", "Буфер обмена"))
        self.label_8.setText(_translate("Tools", "Выберите устройство и ресурсы."))
        self.multimedia.setText(_translate("Tools", "Мультимедиа"))
        self.tab_tools.setTabText(self.tab_tools.indexOf(self.resurs), _translate("Tools", "Локальные ресурсы"))
        self.groupBox_7.setTitle(_translate("Tools", "Принудительная защита протокола"))
        self.label_2.setText(_translate("Tools", "Выбирите протокол:"))
        self.disable_security.setText(_translate("Tools", "Включить защиту протокола"))
        self.tab_tools.setTabText(self.tab_tools.indexOf(self.security), _translate("Tools", "Подключение"))
