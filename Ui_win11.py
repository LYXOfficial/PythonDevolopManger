# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\项目\PythonDevelopManger\win11.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setting(object):
    def setupUi(self, setting):
        setting.setObjectName("setting")
        setting.resize(1049, 811)
        font = QtGui.QFont()
        font.setFamily("萍方0")
        font.setPointSize(10)
        setting.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(setting)
        self.gridLayout.setContentsMargins(12, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 13, 1, 1, 1)
        self.view = QtWidgets.QStackedWidget(setting)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.view.setFont(font)
        self.view.setObjectName("view")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.page_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_7.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\项目\\PythonDevelopManger\\effects/pics/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(12, 12))
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_7.addWidget(self.toolButton, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_7.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.toolButton_2 = QtWidgets.QToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setText("")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(12, 12))
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_8.addWidget(self.toolButton_2, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_8.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_8.addWidget(self.tableWidget_2, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.gridLayout_15.addWidget(self.tableWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.view.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_3.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 4, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_11.addWidget(self.pushButton_8, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem1, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_11.addWidget(self.label_15, 1, 0, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setObjectName("label_30")
        self.gridLayout_11.addWidget(self.label_30, 2, 0, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_11.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.toolButton_7 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_7.setObjectName("toolButton_7")
        self.gridLayout_11.addWidget(self.toolButton_7, 2, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(72)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_11.addWidget(self.pushButton_7, 3, 0, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_11.addWidget(self.label_16, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 6, 0, 1, 3)
        self.pushButton_5 = QtWidgets.QPushButton(self.page_4)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 7, 0, 1, 3)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 8, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(self.page_4)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_9.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_9.addWidget(self.label_11, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_9.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 2, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_9.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_9.addWidget(self.pushButton_4, 2, 3, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 3, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 9, 0, 1, 3)
        self.view.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.checkBox = SwitchButton(self.groupBox_2)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_10.addWidget(self.checkBox, 0, 2, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setObjectName("label_32")
        self.gridLayout_10.addWidget(self.label_32, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 3, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_14.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("萍方0")
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_14.addWidget(self.label_33, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem5, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.view.addWidget(self.page_2)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_6.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_19 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.page_6)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 4, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_12.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_12.addWidget(self.label_22, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem6, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_6, 3, 0, 1, 3)
        self.groupBox_7 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_28 = QtWidgets.QLabel(self.groupBox_7)
        self.label_28.setObjectName("label_28")
        self.gridLayout_13.addWidget(self.label_28, 2, 0, 2, 2)
        self.label_27 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_13.addWidget(self.label_27, 1, 0, 1, 5)
        self.label_36 = QtWidgets.QLabel(self.groupBox_7)
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.gridLayout_13.addWidget(self.label_36, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_7)
        self.label_26.setOpenExternalLinks(True)
        self.label_26.setObjectName("label_26")
        self.gridLayout_13.addWidget(self.label_26, 0, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_7)
        self.label_24.setOpenExternalLinks(True)
        self.label_24.setObjectName("label_24")
        self.gridLayout_13.addWidget(self.label_24, 0, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_7)
        self.label_29.setOpenExternalLinks(True)
        self.label_29.setObjectName("label_29")
        self.gridLayout_13.addWidget(self.label_29, 2, 2, 1, 4)
        self.label_25 = QtWidgets.QLabel(self.groupBox_7)
        self.label_25.setOpenExternalLinks(True)
        self.label_25.setObjectName("label_25")
        self.gridLayout_13.addWidget(self.label_25, 0, 2, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem7, 0, 5, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_7, 5, 0, 1, 3)
        self.label_18 = QtWidgets.QLabel(self.page_6)
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("e:\\项目\\PythonDevelopManger\\effects/pics/logo2.png"))
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 0, 0, 2, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem8, 6, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.page_6)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.page_6)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 2, 1, 1, 1)
        self.view.addWidget(self.page_6)
        self.gridLayout.addWidget(self.view, 4, 2, 15, 3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 14, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 10, 1, 1, 1)
        self.menu = QtWidgets.QListWidget(setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("萍方0")
        font.setPointSize(10)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("e:\\项目\\PythonDevelopManger\\effects/pics/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("e:\\项目\\PythonDevelopManger\\effects/pics/qt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("e:\\项目\\PythonDevelopManger\\effects/pics/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("e:\\项目\\PythonDevelopManger\\effects/pics/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.menu.addItem(item)
        self.gridLayout.addWidget(self.menu, 6, 1, 3, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 12, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 15, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem14, 0, 0, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self.page)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout_5.addWidget(self.toolButton_4, 0, 4, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.page)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout_5.addWidget(self.toolButton_3, 0, 2, 1, 1)
        self.toolButton_5 = QtWidgets.QToolButton(self.page)
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout_5.addWidget(self.toolButton_5, 0, 1, 1, 1)
        self.toolButton_6 = QtWidgets.QToolButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_6.sizePolicy().hasHeightForWidth())
        self.toolButton_6.setSizePolicy(sizePolicy)
        self.toolButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("e:\\项目\\PythonDevelopManger\\effects/pics/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(10, 10))
        self.toolButton_6.setObjectName("toolButton_6")
        self.gridLayout_5.addWidget(self.toolButton_6, 0, 3, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 3)
        self.label_9 = QtWidgets.QLabel(setting)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(setting)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.page_9)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_10)
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.page_10)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.stackedWidget_2.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_11)
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.page_11)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.stackedWidget_2.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_12)
        self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.page_12)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        font.setPointSize(24)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.stackedWidget_2.addWidget(self.page_12)
        self.gridLayout.addWidget(self.stackedWidget_2, 3, 2, 1, 3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 9, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(setting)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem16, 16, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem17, 5, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem18, 11, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 17, 1, 1, 1)

        self.retranslateUi(setting)
        self.view.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.menu.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.menu.currentRowChanged['int'].connect(self.view.setCurrentIndex)
        self.menu.currentRowChanged['int'].connect(self.stackedWidget_2.setCurrentIndex)
        self.toolButton_4.clicked['bool'].connect(setting.close)
        self.toolButton_5.clicked.connect(setting.showMinimized)
        self.toolButton_3.clicked['bool'].connect(setting.showMaximized)
        self.toolButton_3.clicked.connect(self.toolButton_3.hide)
        self.toolButton_3.clicked.connect(self.toolButton_6.show)
        self.toolButton_6.clicked.connect(self.toolButton_3.show)
        self.toolButton_6.clicked.connect(setting.showNormal)
        self.toolButton_6.clicked.connect(self.toolButton_6.hide)
        self.checkBox.clicked['bool'].connect(self.label_33.setDisabled)
        self.checkBox.clicked['bool'].connect(self.comboBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(setting)

    def retranslateUi(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate("setting", "设置"))
        self.lineEdit.setPlaceholderText(_translate("setting", "搜索库..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("setting", "已安装"))
        self.lineEdit_2.setPlaceholderText(_translate("setting", "搜索库..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("setting", "安装包"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("setting", "下载管理"))
        self.label_14.setText(_translate("setting", ".ui转.py"))
        self.label_4.setText(_translate("setting", "仅支持PyQt5 5.9+版本！！！"))
        self.pushButton_8.setText(_translate("setting", "转换"))
        self.label_15.setText(_translate("setting", "源文件(可拖拽或选择）"))
        self.label_30.setText(_translate("setting", "/"))
        self.toolButton_7.setText(_translate("setting", "..."))
        self.pushButton_7.setText(_translate("setting", "+"))
        self.label_16.setText(_translate("setting", "目标位置"))
        self.pushButton_5.setText(_translate("setting", "解决PyQt疑难杂症"))
        self.pushButton_6.setText(_translate("setting", "拷贝一份PyQt程序基本框架"))
        self.label_6.setText(_translate("setting", "s"))
        self.label_12.setText(_translate("setting", "s"))
        self.label_11.setText(_translate("setting", "s"))
        self.pushButton_2.setText(_translate("setting", "安装"))
        self.label_3.setText(_translate("setting", "PyQt5-tools-{} 用于使用Qt Designer和Qt Linguist"))
        self.label_2.setText(_translate("setting", "PyQt5-{}"))
        self.label_13.setText(_translate("setting", "PyQtWebEngine 用于加载QWebEngine的必要插件（没有内置）"))
        self.pushButton_3.setText(_translate("setting", "安装"))
        self.pushButton_4.setText(_translate("setting", "安装"))
        self.label.setText(_translate("setting", "库完整度检测"))
        self.label_32.setText(_translate("setting", "自动选择下载源"))
        self.label_31.setText(_translate("setting", "下载源设置"))
        self.comboBox.setItemText(0, _translate("setting", "PyPI官方源"))
        self.comboBox.setItemText(1, _translate("setting", "清华源"))
        self.comboBox.setItemText(2, _translate("setting", "豆瓣源"))
        self.comboBox.setItemText(3, _translate("setting", "阿里云"))
        self.comboBox.setItemText(4, _translate("setting", "中科大"))
        self.label_33.setText(_translate("setting", "选择下载源"))
        self.label_19.setText(_translate("setting", "PythonDevelopManger"))
        self.pushButton.setText(_translate("setting", "更新日志"))
        self.label_22.setText(_translate("setting", "Version {}"))
        self.label_28.setText(_translate("setting", "PyQt5\n"
""))
        self.label_27.setText(_translate("setting", "参考资料及使用第三方库："))
        self.label_26.setText(_translate("setting", "<a href=\"https://space.bilibili.com/369280472\">Bilibili</a href>"))
        self.label_24.setText(_translate("setting", "<a href=\"https://github.com/lyxofficial\">Github</a href>"))
        self.label_29.setText(_translate("setting", "感谢大佬<a href=\"https://github.com/zhiyiyo\">@zhiyiyo</a href>的众多Fluent解决方案！"))
        self.label_25.setText(_translate("setting", "<a href=\"https://lyxofficial.github.io\">Blog</a href>"))
        self.label_20.setText(_translate("setting", "By LYXOfficial"))
        __sortingEnabled = self.menu.isSortingEnabled()
        self.menu.setSortingEnabled(False)
        item = self.menu.item(0)
        item.setText(_translate("setting", "PyPI包管理"))
        item = self.menu.item(1)
        item.setText(_translate("setting", "PyQt5"))
        item = self.menu.item(2)
        item.setText(_translate("setting", "设置"))
        item = self.menu.item(3)
        item.setText(_translate("setting", "关于"))
        self.menu.setSortingEnabled(__sortingEnabled)
        self.toolButton_4.setText(_translate("setting", "✕"))
        self.toolButton_3.setText(_translate("setting", "□"))
        self.toolButton_5.setText(_translate("setting", "–"))
        self.label_9.setText(_translate("setting", "  PythonDevelopManger"))
        self.label_5.setText(_translate("setting", "PyPI包管理"))
        self.label_7.setText(_translate("setting", "PyQt5"))
        self.label_8.setText(_translate("setting", "设置"))
        self.label_17.setText(_translate("setting", "关于"))
        self.label_10.setText(_translate("setting", "   菜单"))
from switchButton import SwitchButton
