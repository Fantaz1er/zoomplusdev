# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class UiRegistration(object):
    def __init__(self):
        self.pushButton_2 = None
        self.pushButton = None
        self.lineEdit_2 = None
        self.lineEdit_2 = None
        self.lineEdit = None
        self.verticalLayout = None
        self.horizontalLayout = None

    def setup_ui(self, Registration):
        Registration.setObjectName("Registration")
        Registration.setEnabled(True)
        Registration.resize(285, 225)
        Registration.setMinimumSize(QtCore.QSize(285, 225))
        Registration.setMaximumSize(QtCore.QSize(285, 225))
        Registration.setBaseSize(QtCore.QSize(285, 225))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Registration.setFont(font)
        Registration.setStyleSheet("background-color: #22222e;\n"
                                   "color: white;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Registration)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Registration)
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("bachground-color: #22222e;\n"
                                    "border: 2px solid #f66867;\n"
                                    "border-radius: 11px;\n"
                                    "color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(Registration)
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("bachground-color: #22222e;\n"
                                      "border: 2px solid #f66867;\n"
                                      "border-radius: 11px;\n"
                                      "color: white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(Registration)
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    color: white;\n"
                                      "    background-color: #fb5b5d;\n"
                                      "    border-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #fa4244;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Registration)
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    color: white;\n"
                                        "    background-color: #fb5b5d;\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #fa4244;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Authorization"))
        self.lineEdit.setPlaceholderText(_translate("Registration", "Login..."))
        self.lineEdit_2.setPlaceholderText(_translate("Registration", "Password..."))
        self.pushButton.setText(_translate("Registration", "Sign In"))
        self.pushButton_2.setText(_translate("Registration", "Sign Up"))
