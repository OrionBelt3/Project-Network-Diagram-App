# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1334, 854)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        login.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(login)
        self.gridLayout.setObjectName("gridLayout")
        self.labelNumGroup = QtWidgets.QLabel(login)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.labelNumGroup.setFont(font)
        self.labelNumGroup.setObjectName("labelNumGroup")
        self.gridLayout.addWidget(self.labelNumGroup, 1, 0, 1, 1)
        self.labelSurname = QtWidgets.QLabel(login)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.labelSurname.setFont(font)
        self.labelSurname.setObjectName("labelSurname")
        self.gridLayout.addWidget(self.labelSurname, 0, 0, 1, 1)
        self.btnSignLab = QtWidgets.QPushButton(login)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnSignLab.setFont(font)
        self.btnSignLab.setStyleSheet("background-color: #66e3ff;")
        self.btnSignLab.setObjectName("btnSignLab")
        self.gridLayout.addWidget(self.btnSignLab, 3, 1, 1, 1)
        self.lineEditSurname = QtWidgets.QLineEdit(login)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEditSurname.setFont(font)
        self.lineEditSurname.setStyleSheet("background-color: #fffaea;")
        self.lineEditSurname.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditSurname.setMaxLength(25)
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.gridLayout.addWidget(self.lineEditSurname, 0, 1, 1, 1)
        self.labelGroup = QtWidgets.QLabel(login)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.labelGroup.setFont(font)
        self.labelGroup.setObjectName("labelGroup")
        self.gridLayout.addWidget(self.labelGroup, 2, 0, 1, 1)
        self.lineEditGroup = QtWidgets.QLineEdit(login)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEditGroup.setFont(font)
        self.lineEditGroup.setStyleSheet("background-color: #fffaea;")
        self.lineEditGroup.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditGroup.setMaxLength(15)
        self.lineEditGroup.setObjectName("lineEditGroup")
        self.gridLayout.addWidget(self.lineEditGroup, 2, 1, 1, 1)
        self.lineEditNumINGroup = QtWidgets.QLineEdit(login)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEditNumINGroup.setFont(font)
        self.lineEditNumINGroup.setStyleSheet("background-color: #fffaea;")
        self.lineEditNumINGroup.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditNumINGroup.setMaxLength(2)
        self.lineEditNumINGroup.setObjectName("lineEditNumINGroup")
        self.gridLayout.addWidget(self.lineEditNumINGroup, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 9)
        self.gridLayout.setColumnStretch(2, 2)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Данные студента"))
        self.labelNumGroup.setText(_translate("login", "<html><head/><body><p>ВАРИАНТ</p></body></html>"))
        self.labelSurname.setText(_translate("login", "<html><head/><body><p>Ф.И.О.</p></body></html>"))
        self.btnSignLab.setText(_translate("login", "Далее"))
        self.labelGroup.setText(_translate("login", "<html><head/><body><p>ВЗВОД</p></body></html>"))
