# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modern.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1594, 813)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1661, 61))
        self.frame.setStyleSheet("background-color: rgb(0, 147, 220);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(1430, 10, 211, 31))
        self.label_15.setTextFormat(QtCore.Qt.RichText)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_15.setObjectName("label_15")
        self.lbLogo = QtWidgets.QLabel(self.frame)
        self.lbLogo.setGeometry(QtCore.QRect(40, -10, 271, 71))
        self.lbLogo.setText("")
        self.lbLogo.setPixmap(QtGui.QPixmap("../../Mirallis-PySimpleGUI/logo.ico"))
        self.lbLogo.setObjectName("lbLogo")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 60, 201, 831))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 120, 141, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(0, 5))
        self.label_13.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setLineWidth(2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.inputUser = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inputUser.setMinimumSize(QtCore.QSize(0, 30))
        self.inputUser.setStyleSheet("background: #fff; \n"
"border-color: rgb(207, 207, 207);")
        self.inputUser.setAlignment(QtCore.Qt.AlignCenter)
        self.inputUser.setObjectName("inputUser")
        self.verticalLayout.addWidget(self.inputUser)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setMinimumSize(QtCore.QSize(0, 5))
        self.label_14.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setLineWidth(2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.inputPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inputPassword.setMinimumSize(QtCore.QSize(0, 30))
        self.inputPassword.setStyleSheet("background: #fff; \n"
"border-color: rgb(207, 207, 207);")
        self.inputPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPassword.setObjectName("inputPassword")
        self.verticalLayout.addWidget(self.inputPassword)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 660, 131, 81))
        self.pushButton_2.setStyleSheet("QPushButton{color: #fff;}\n"
"QPushButton:hover{background: gold; color: black;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.btSign = QtWidgets.QPushButton(self.frame_2)
        self.btSign.setGeometry(QtCore.QRect(40, 280, 121, 23))
        self.btSign.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);color:#fff}\n"
"QPushButton:hover{background: gold; color: black;}")
        self.btSign.setObjectName("btSign")
        self.lbName = QtWidgets.QLabel(self.frame_2)
        self.lbName.setGeometry(QtCore.QRect(36, 430, 141, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lbName.setFont(font)
        self.lbName.setStyleSheet("color: #fff;")
        self.lbName.setAlignment(QtCore.Qt.AlignCenter)
        self.lbName.setObjectName("lbName")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(230, 100, 361, 61))
        self.frame_3.setStyleSheet("background-color: rgb(0, 147, 220);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 341, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setEnabled(True)
        self.frame_4.setGeometry(QtCore.QRect(230, 160, 361, 621))
        self.frame_4.setStyleSheet("QFrame{background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-color: rgb(0, 0, 0);}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 20, 301, 501))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setMinimumSize(QtCore.QSize(0, 5))
        self.label_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setLineWidth(2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.inputCod = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.inputCod.setMinimumSize(QtCore.QSize(0, 30))
        self.inputCod.setStyleSheet("QLineEdit{background: #fff; \n"
"border-color: rgb(207, 207, 207);\n"
"border: 1px solid gray;\n"
"border-radius: 3px;}")
        self.inputCod.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputCod.setObjectName("inputCod")
        self.verticalLayout_3.addWidget(self.inputCod)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.inputName = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.inputName.setMinimumSize(QtCore.QSize(0, 30))
        self.inputName.setStyleSheet("QLineEdit{background: #fff; \n"
"border-color: rgb(207, 207, 207);\n"
"border: 1px solid gray;\n"
"border-radius: 3px;}")
        self.inputName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputName.setObjectName("inputName")
        self.verticalLayout_3.addWidget(self.inputName)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setLineWidth(2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.cbInputArea = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.cbInputArea.setMinimumSize(QtCore.QSize(0, 30))
        self.cbInputArea.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.cbInputArea.setObjectName("cbInputArea")
        self.verticalLayout_3.addWidget(self.cbInputArea)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setLineWidth(2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.inputCity = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.inputCity.setMinimumSize(QtCore.QSize(0, 30))
        self.inputCity.setStyleSheet("QLineEdit{background: #fff; \n"
"border-color: rgb(207, 207, 207);\n"
"border: 1px solid gray;\n"
"border-radius: 3px;}")
        self.inputCity.setObjectName("inputCity")
        self.verticalLayout_3.addWidget(self.inputCity)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setLineWidth(2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.inputEmail = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.inputEmail.setMinimumSize(QtCore.QSize(0, 30))
        self.inputEmail.setStyleSheet("QLineEdit{background: #fff; \n"
"border-color: rgb(207, 207, 207);\n"
"border: 1px solid gray;\n"
"border-radius: 3px;}")
        self.inputEmail.setObjectName("inputEmail")
        self.verticalLayout_3.addWidget(self.inputEmail)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setLineWidth(2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.inputPhone1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.inputPhone1.setMinimumSize(QtCore.QSize(0, 30))
        self.inputPhone1.setStyleSheet("QLineEdit{background: #fff; \n"
"border-color: rgb(207, 207, 207);\n"
"border: 1px solid gray;\n"
"border-radius: 3px;}")
        self.inputPhone1.setObjectName("inputPhone1")
        self.verticalLayout_3.addWidget(self.inputPhone1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setLineWidth(2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.inputPhone2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.inputPhone2.setMinimumSize(QtCore.QSize(0, 30))
        self.inputPhone2.setStyleSheet("QLineEdit{background: #fff; \n"
"border-color: rgb(207, 207, 207);\n"
"border: 1px solid gray;\n"
"border-radius: 3px;}")
        self.inputPhone2.setObjectName("inputPhone2")
        self.verticalLayout_3.addWidget(self.inputPhone2)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setLineWidth(2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.inputLink = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.inputLink.setMinimumSize(QtCore.QSize(0, 30))
        self.inputLink.setStyleSheet("QLineEdit{background: #fff; \n"
"border-color: rgb(207, 207, 207);\n"
"border: 1px solid gray;\n"
"border-radius: 3px;}")
        self.inputLink.setObjectName("inputLink")
        self.verticalLayout_3.addWidget(self.inputLink)
        self.btSave = QtWidgets.QPushButton(self.frame_4)
        self.btSave.setEnabled(True)
        self.btSave.setGeometry(QtCore.QRect(30, 540, 161, 31))
        self.btSave.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);color:#fff}\n"
"QPushButton:hover{background: gold; color: black;}")
        self.btSave.setObjectName("btSave")
        self.btUpdate = QtWidgets.QPushButton(self.frame_4)
        self.btUpdate.setEnabled(False)
        self.btUpdate.setGeometry(QtCore.QRect(30, 580, 161, 31))
        self.btUpdate.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);color:#fff}\n"
"QPushButton:hover{background: gold; color: black;}")
        self.btUpdate.setObjectName("btUpdate")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(610, 100, 951, 61))
        self.frame_5.setStyleSheet("background-color: rgb(0, 147, 220);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame_5)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 931, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(610, 160, 951, 621))
        self.frame_6.setStyleSheet("QFrame{background-color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-color: rgb(0, 0, 0);}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.cbSearch = QtWidgets.QComboBox(self.frame_6)
        self.cbSearch.setGeometry(QtCore.QRect(30, 60, 781, 31))
        self.cbSearch.setObjectName("cbSearch")
        self.groupBox = QtWidgets.QGroupBox(self.frame_6)
        self.groupBox.setGeometry(QtCore.QRect(840, 10, 101, 80))
        self.groupBox.setStyleSheet("QGroupBox{border-radius: 10px}")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 81, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.rbName = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.rbName.setObjectName("rbName")
        self.verticalLayout_5.addWidget(self.rbName)
        self.rbArea = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.rbArea.setWhatsThis("")
        self.rbArea.setObjectName("rbArea")
        self.verticalLayout_5.addWidget(self.rbArea)
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setGeometry(QtCore.QRect(30, 20, 391, 32))
        self.label_12.setMinimumSize(QtCore.QSize(0, 5))
        self.label_12.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(106, 106, 106);\n"
"border-bottom-right-radius:0px;")
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setLineWidth(2)
        self.label_12.setObjectName("label_12")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_6)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 911, 481))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.btStartSearch = QtWidgets.QPushButton(self.frame_6)
        self.btStartSearch.setGeometry(QtCore.QRect(710, 30, 101, 23))
        self.btStartSearch.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);color:#fff}\n"
"QPushButton:hover{background: gold; color: black;}")
        self.btStartSearch.setObjectName("btStartSearch")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_15.setText(_translate("MainWindow", "Search on Google"))
        self.label.setText(_translate("MainWindow", "LOGIN"))
        self.label_13.setText(_translate("MainWindow", "User"))
        self.label_14.setText(_translate("MainWindow", "Password"))
        self.pushButton_2.setText(_translate("MainWindow", "Application by \n"
"\n"
"Renato Dantas"))
        self.btSign.setText(_translate("MainWindow", "Sign in"))
        self.lbName.setText(_translate("MainWindow", "Welcome User!"))
        self.label_2.setText(_translate("MainWindow", "Supplier Information"))
        self.label_3.setText(_translate("MainWindow", "Cod Mirallis"))
        self.label_4.setText(_translate("MainWindow", "Name"))
        self.label_5.setText(_translate("MainWindow", "Field Area"))
        self.label_6.setText(_translate("MainWindow", "City"))
        self.label_7.setText(_translate("MainWindow", "E-Mail"))
        self.label_8.setText(_translate("MainWindow", "Phone 1"))
        self.label_9.setText(_translate("MainWindow", "Phone 2"))
        self.label_10.setText(_translate("MainWindow", "Website"))
        self.btSave.setText(_translate("MainWindow", "SAVE "))
        self.btUpdate.setText(_translate("MainWindow", "UPDATE VALUES"))
        self.label_11.setText(_translate("MainWindow", "Consult Information"))
        self.groupBox.setTitle(_translate("MainWindow", "Parameter"))
        self.rbName.setText(_translate("MainWindow", "Name"))
        self.rbArea.setText(_translate("MainWindow", "Area"))
        self.label_12.setText(_translate("MainWindow", "Search"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cod Mirallis"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Field Area"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "E-Mail"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Phone 1"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Phone 2"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Website"))
        self.btStartSearch.setText(_translate("MainWindow", "Start Search"))