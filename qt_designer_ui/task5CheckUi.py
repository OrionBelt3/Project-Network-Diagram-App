# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task5CheckForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_task5CheckUi(object):
    def setupUi(self, task5CheckForm):
        task5CheckForm.setObjectName("task5CheckForm")
        task5CheckForm.resize(494, 182)
        task5CheckForm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(task5CheckForm)
        self.verticalLayout.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(task5CheckForm)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 470, 123))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        # self.labelLeft = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.labelLeft.setFont(font)
        # self.labelLeft.setObjectName("labelLeft")
        # self.gridLayout.addWidget(self.labelLeft, 0, 0, 1, 1)
        # self.toolButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        # self.toolButton.setEnabled(True)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("resources/iconePack/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon.addPixmap(QtGui.QPixmap("resources/iconePack/crossRed.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        # self.toolButton.setIcon(icon)
        # self.toolButton.setCheckable(True)
        # self.toolButton.setObjectName("toolButton")
        # self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.closeButton = QtWidgets.QPushButton(task5CheckForm)
        self.closeButton.setEnabled(True)
        self.closeButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.closeButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(task5CheckForm)
        QtCore.QMetaObject.connectSlotsByName(task5CheckForm)

    def retranslateUi(self, task5CheckForm):
        _translate = QtCore.QCoreApplication.translate
        task5CheckForm.setWindowTitle(_translate("task5CheckForm", "Проверка"))
        # self.labelLeft.setText(_translate("task5CheckForm", "1 отделение построено верно"))
        # self.toolButton.setText(_translate("task5CheckForm", "..."))
        self.closeButton.setText(_translate("task5CheckForm", "Закрыть"))
