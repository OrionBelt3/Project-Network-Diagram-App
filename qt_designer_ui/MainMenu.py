# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1558, 926)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        MainMenu.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/login_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainMenu.setWindowIcon(icon)
        MainMenu.setStyleSheet("#centralwidget{background-color: #d5fffe;}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableVar = QtWidgets.QTableWidget(self.frame)
        self.tableVar.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.tableVar.setFont(font)
        self.tableVar.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableVar.setAutoFillBackground(False)
        self.tableVar.setStyleSheet("background-color: #fffaea;\n"
"\n"
"")
        self.tableVar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableVar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableVar.setLineWidth(2)
        self.tableVar.setMidLineWidth(0)
        self.tableVar.setAutoScrollMargin(16)
        self.tableVar.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableVar.setGridStyle(QtCore.Qt.SolidLine)
        self.tableVar.setRowCount(0)
        self.tableVar.setColumnCount(6)
        self.tableVar.setObjectName("tableVar")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableVar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableVar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableVar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableVar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableVar.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableVar.setHorizontalHeaderItem(5, item)
        self.tableVar.horizontalHeader().setVisible(True)
        self.tableVar.horizontalHeader().setCascadingSectionResizes(True)
        self.tableVar.horizontalHeader().setDefaultSectionSize(243)
        self.tableVar.horizontalHeader().setHighlightSections(True)
        self.tableVar.horizontalHeader().setMinimumSectionSize(70)
        self.tableVar.horizontalHeader().setSortIndicatorShown(False)
        self.tableVar.horizontalHeader().setStretchLastSection(True)
        self.tableVar.verticalHeader().setVisible(True)
        self.tableVar.verticalHeader().setCascadingSectionResizes(True)
        self.tableVar.verticalHeader().setDefaultSectionSize(35)
        self.tableVar.verticalHeader().setMinimumSectionSize(25)
        self.tableVar.verticalHeader().setSortIndicatorShown(False)
        self.tableVar.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableVar)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.btnTask5 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask5.setFont(font)
        self.btnTask5.setStyleSheet("background-color: #66e3ff;")
        self.btnTask5.setObjectName("btnTask5")
        self.gridLayout.addWidget(self.btnTask5, 5, 2, 1, 1)
        self.btnPrint = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnPrint.setFont(font)
        self.btnPrint.setStyleSheet("background-color: #66e3ff;")
        self.btnPrint.setObjectName("btnPrint")
        self.gridLayout.addWidget(self.btnPrint, 2, 3, 1, 1)
        self.btnTask6 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask6.setFont(font)
        self.btnTask6.setStyleSheet("background-color: #66e3ff;")
        self.btnTask6.setObjectName("btnTask6")
        self.gridLayout.addWidget(self.btnTask6, 6, 2, 1, 1)
        self.btnTask2 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask2.setFont(font)
        self.btnTask2.setStyleSheet("background-color: #66e3ff;")
        self.btnTask2.setObjectName("btnTask2")
        self.gridLayout.addWidget(self.btnTask2, 2, 2, 1, 1)
        self.btnTask4 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask4.setFont(font)
        self.btnTask4.setStyleSheet("background-color: #66e3ff;")
        self.btnTask4.setObjectName("btnTask4")
        self.gridLayout.addWidget(self.btnTask4, 4, 2, 1, 1)
        self.btnReportSign = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnReportSign.setFont(font)
        self.btnReportSign.setStyleSheet("background-color: #66e3ff;")
        self.btnReportSign.setObjectName("btnReportSign")
        self.gridLayout.addWidget(self.btnReportSign, 3, 3, 1, 1)
        self.btnEditTaskVariant = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnEditTaskVariant.setFont(font)
        self.btnEditTaskVariant.setStyleSheet("background-color: #66e3ff;")
        self.btnEditTaskVariant.setObjectName("btnEditTaskVariant")
        self.gridLayout.addWidget(self.btnEditTaskVariant, 4, 3, 1, 1)
        self.btnSaveReportAs = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnSaveReportAs.setFont(font)
        self.btnSaveReportAs.setStyleSheet("background-color: #66e3ff;")
        self.btnSaveReportAs.setObjectName("btnSaveReportAs")
        self.gridLayout.addWidget(self.btnSaveReportAs, 6, 3, 1, 1)
        self.btnTask3 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask3.setFont(font)
        self.btnTask3.setStyleSheet("background-color: #66e3ff;")
        self.btnTask3.setObjectName("btnTask3")
        self.gridLayout.addWidget(self.btnTask3, 3, 2, 1, 1)
        self.btnTeacherMode = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTeacherMode.setFont(font)
        self.btnTeacherMode.setStyleSheet("background-color: #66e3ff;")
        self.btnTeacherMode.setCheckable(True)
        self.btnTeacherMode.setObjectName("btnTeacherMode")
        self.gridLayout.addWidget(self.btnTeacherMode, 5, 3, 1, 1)
        self.btnTask1 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask1.setFont(font)
        self.btnTask1.setStyleSheet("background-color: #66e3ff;")
        self.btnTask1.setObjectName("btnTask1")
        self.gridLayout.addWidget(self.btnTask1, 1, 2, 1, 1)
        self.previewReport = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.previewReport.setFont(font)
        self.previewReport.setStyleSheet("background-color: #66e3ff;")
        self.previewReport.setObjectName("previewReport")
        self.gridLayout.addWidget(self.previewReport, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        MainMenu.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainMenu)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1558, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAboutProgram = QtWidgets.QMenu(self.menuBar)
        self.menuAboutProgram.setObjectName("menuAboutProgram")
        MainMenu.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)
        self.actionPrintReport = QtWidgets.QAction(MainMenu)
        self.actionPrintReport.setObjectName("actionPrintReport")
        self.actionOpenReport = QtWidgets.QAction(MainMenu)
        self.actionOpenReport.setObjectName("actionOpenReport")
        self.actionactionSaveReportReport_3 = QtWidgets.QAction(MainMenu)
        self.actionactionSaveReportReport_3.setObjectName("actionactionSaveReportReport_3")
        self.actionVersion = QtWidgets.QAction(MainMenu)
        self.actionVersion.setObjectName("actionVersion")
        self.actionDevelopers = QtWidgets.QAction(MainMenu)
        self.actionDevelopers.setObjectName("actionDevelopers")
        self.actionHelpWithProg = QtWidgets.QAction(MainMenu)
        self.actionHelpWithProg.setObjectName("actionHelpWithProg")
        self.actionHelpWithTheory = QtWidgets.QAction(MainMenu)
        self.actionHelpWithTheory.setObjectName("actionHelpWithTheory")
        self.menuHelp.addAction(self.actionHelpWithProg)
        self.menuHelp.addAction(self.actionHelpWithTheory)
        self.menuAboutProgram.addAction(self.actionVersion)
        self.menuAboutProgram.addAction(self.actionDevelopers)
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuAboutProgram.menuAction())

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Меню"))
        item = self.tableVar.horizontalHeaderItem(0)
        item.setText(_translate("MainMenu", "Шифр работы"))
        item = self.tableVar.horizontalHeaderItem(1)
        item.setText(_translate("MainMenu", "Номер отделения\n"
"выполняющего\n"
"работу"))
        item = self.tableVar.horizontalHeaderItem(2)
        item.setText(_translate("MainMenu", "Число людей,\n"
"выполняющих работы"))
        item = self.tableVar.horizontalHeaderItem(3)
        item.setText(_translate("MainMenu", "Продолжительность\n"
"работ (час)"))
        item = self.tableVar.horizontalHeaderItem(4)
        item.setText(_translate("MainMenu", "Номер\n"
"отделения"))
        item = self.tableVar.horizontalHeaderItem(5)
        item.setText(_translate("MainMenu", "Количество\n"
"людей\n"
"в отделении"))
        self.btnTask5.setText(_translate("MainMenu", "Задание 5"))
        self.btnPrint.setText(_translate("MainMenu", "Печать отчета"))
        self.btnTask6.setText(_translate("MainMenu", "Задание 6"))
        self.btnTask2.setText(_translate("MainMenu", "Задание 2"))
        self.btnTask4.setText(_translate("MainMenu", "Задание 4"))
        self.btnReportSign.setText(_translate("MainMenu", "Изменить данные студента"))
        self.btnEditTaskVariant.setText(_translate("MainMenu", "Редактировать варианты"))
        self.btnSaveReportAs.setText(_translate("MainMenu", "Сохранить отчет как"))
        self.btnTask3.setText(_translate("MainMenu", "Задание 3"))
        self.btnTeacherMode.setText(_translate("MainMenu", "Режим преподавателя"))
        self.btnTask1.setText(_translate("MainMenu", "Задание 1"))
        self.previewReport.setText(_translate("MainMenu", "Предпросмотр отчета"))
        self.menuHelp.setTitle(_translate("MainMenu", "справка"))
        self.menuAboutProgram.setTitle(_translate("MainMenu", "о программе"))
        self.actionPrintReport.setText(_translate("MainMenu", "печать отчета"))
        self.actionOpenReport.setText(_translate("MainMenu", "открыть отчет"))
        self.actionactionSaveReportReport_3.setText(_translate("MainMenu", "сохранить отчет"))
        self.actionVersion.setText(_translate("MainMenu", "версия"))
        self.actionDevelopers.setText(_translate("MainMenu", "разработчики"))
        self.actionHelpWithProg.setText(_translate("MainMenu", "справка по работе с программой"))
        self.actionHelpWithTheory.setText(_translate("MainMenu", "справка по теории"))
# import backGround_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())
