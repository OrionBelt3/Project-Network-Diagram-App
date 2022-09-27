
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_winTableNumPeopleInSquad(object):
    def setupUi(self, winTableNumPeopleInSquad):
        winTableNumPeopleInSquad.setObjectName("winTableNumPeopleInSquad")
        winTableNumPeopleInSquad.resize(753, 989)
        self.verticalLayout = QtWidgets.QVBoxLayout(winTableNumPeopleInSquad)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableNumPeopleInSquad = QtWidgets.QTableWidget(winTableNumPeopleInSquad)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.tableNumPeopleInSquad.setFont(font)
        self.tableNumPeopleInSquad.setStyleSheet("background-color: #fffaea;")
        self.tableNumPeopleInSquad.setObjectName("tableNumPeopleInSquad")
        self.tableNumPeopleInSquad.setColumnCount(2)
        self.tableNumPeopleInSquad.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableNumPeopleInSquad.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableNumPeopleInSquad.setHorizontalHeaderItem(1, item)
        self.tableNumPeopleInSquad.horizontalHeader().setDefaultSectionSize(350)
        self.verticalLayout.addWidget(self.tableNumPeopleInSquad)
        self.btnExitAndClose = QtWidgets.QPushButton(winTableNumPeopleInSquad)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnExitAndClose.setFont(font)
        self.btnExitAndClose.setStyleSheet("background-color: #66e3ff;")
        self.btnExitAndClose.setObjectName("btnExitAndClose")
        self.verticalLayout.addWidget(self.btnExitAndClose)

        self.retranslateUi(winTableNumPeopleInSquad)
        QtCore.QMetaObject.connectSlotsByName(winTableNumPeopleInSquad)

    def retranslateUi(self, winTableNumPeopleInSquad):
        _translate = QtCore.QCoreApplication.translate
        winTableNumPeopleInSquad.setWindowTitle(_translate("winTableNumPeopleInSquad", "Таблица численности отделений"))
        item = self.tableNumPeopleInSquad.horizontalHeaderItem(0)
        item.setText(_translate("winTableNumPeopleInSquad", "Порядковый номер отделения"))
        item = self.tableNumPeopleInSquad.horizontalHeaderItem(1)
        item.setText(_translate("winTableNumPeopleInSquad", "Число людей в отделении"))
        self.btnExitAndClose.setText(_translate("winTableNumPeopleInSquad", "Сохранить и выйти"))

