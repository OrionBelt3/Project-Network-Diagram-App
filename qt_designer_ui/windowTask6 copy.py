from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow6(object):
    def setupUi(self, MainWindow6):
        MainWindow6.setObjectName("MainWindow6")
        MainWindow6.resize(1611, 1123)
        self.centralwidget = QtWidgets.QWidget(MainWindow6)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow6.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow6)
        self.toolBar.setIconSize(QtCore.QSize(47, 42))
        self.toolBar.setObjectName("toolBar")
        MainWindow6.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow6)
        self.statusbar.setStyleSheet("background-color: #b8ffc0;")
        self.statusbar.setObjectName("statusbar")
        MainWindow6.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow6)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1611, 21))
        self.menuBar.setStyleSheet("background-color: #b8ffc0;")
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        # self.menuTask = QtWidgets.QMenu(self.menuBar)
        # # self.menuTask.setObjectName("menuTask")
        MainWindow6.setMenuBar(self.menuBar)
        self.actionNewFile = QtWidgets.QAction(MainWindow6)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/iconePack/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewFile.setIcon(icon)
        self.actionNewFile.setObjectName("actionNewFile")
        self.actionOpenFile = QtWidgets.QAction(MainWindow6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/iconePack/write.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenFile.setIcon(icon1)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionSaveFile = QtWidgets.QAction(MainWindow6)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/iconePack/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveFile.setIcon(icon2)
        self.actionSaveFile.setObjectName("actionSaveFile")
        self.actionSaveFileAs = QtWidgets.QAction(MainWindow6)
        self.actionSaveFileAs.setObjectName("actionSaveFileAs")
        self.actionForward = QtWidgets.QAction(MainWindow6)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/iconePack/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForward.setIcon(icon3)
        self.actionForward.setObjectName("actionForward")
        self.actionBackward = QtWidgets.QAction(MainWindow6)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/iconePack/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBackward.setIcon(icon4)
        self.actionBackward.setObjectName("actionBackward")
        self.actionbtnHome = QtWidgets.QAction(MainWindow6)
        self.actionbtnHome.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/iconePack/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnHome.setIcon(icon5)
        self.actionbtnHome.setObjectName("actionbtnHome")
        self.actionbtnZoomIn = QtWidgets.QAction(MainWindow6)
        self.actionbtnZoomIn.setCheckable(False)
        self.actionbtnZoomIn.setChecked(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/iconePack/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnZoomIn.setIcon(icon6)
        self.actionbtnZoomIn.setAutoRepeat(True)
        self.actionbtnZoomIn.setObjectName("actionbtnZoomIn")
        self.actionbtnZoomOut = QtWidgets.QAction(MainWindow6)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/iconePack/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnZoomOut.setIcon(icon7)
        self.actionbtnZoomOut.setObjectName("actionbtnZoomOut")
        self.actionHelpTask = QtWidgets.QAction(MainWindow6)
        self.actionHelpTask.setObjectName("actionHelpTask")



        self.actionHelpProgram = QtWidgets.QAction(MainWindow6)
        self.actionHelpProgram.setObjectName("actionHelpProgram")
        self.actionSetting = QtWidgets.QAction(MainWindow6)
        self.actionSetting.setObjectName("actionSetting")
        self.actionbtnCheck = QtWidgets.QAction(MainWindow6)
        self.actionbtnCheck.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources/iconePack/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnCheck.setIcon(icon8)
        self.actionbtnCheck.setObjectName("actionbtnCheck")
        self.actionbtnInfo = QtWidgets.QAction(MainWindow6)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("resources/iconePack/attachment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnInfo.setIcon(icon9)
        self.actionbtnInfo.setObjectName("actionbtnInfo")
        self.actionbtnDottedConnectNode = QtWidgets.QAction(MainWindow6)
        self.actionbtnDottedConnectNode.setCheckable(True)
        self.actionbtnDottedConnectNode.setEnabled(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("resources/iconePack/arrowsDotted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnDottedConnectNode.setIcon(icon10)
        self.actionbtnDottedConnectNode.setObjectName("actionbtnDottedConnectNode")
        self.actionbtnMoveNode = QtWidgets.QAction(MainWindow6)
        self.actionbtnMoveNode.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("resources/iconePack/axis_arrow_icon_138909.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnMoveNode.setIcon(icon11)
        font = QtGui.QFont()
        self.actionbtnMoveNode.setFont(font)
        self.actionbtnMoveNode.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionbtnMoveNode.setObjectName("actionbtnMoveNode")
        self.actionHelp = QtWidgets.QAction(MainWindow6)
        self.actionHelp.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("resources/iconePack/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon12)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.setVisible(False)
        self.actionHelpStud = QtWidgets.QAction(MainWindow6)
        self.actionHelpStud.setObjectName("actionHelpStud")
        self.actionHelpTeach = QtWidgets.QAction(MainWindow6)
        self.actionHelpTeach.setObjectName("actionHelpTeach")
        self.actionViewTask = QtWidgets.QAction(MainWindow6)
        self.actionViewTask.setObjectName("actionViewTask")
        self.actionSolveTask = QtWidgets.QAction(MainWindow6)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("resources/iconePack/document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSolveTask.setIcon(icon13)
        self.actionSolveTask.setObjectName("actionSolveTask")
        self.toolBar.addAction(self.actionbtnMoveNode)
        self.toolBar.addAction(self.actionbtnDottedConnectNode)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionbtnInfo)
        self.toolBar.addAction(self.actionHelp)
        # self.toolBar.addAction(self.actionSolveTask)
        self.toolBar.addAction(self.actionbtnHome)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionbtnCheck)
        self.menuHelp.addAction(self.actionHelpStud)
        self.menuHelp.addAction(self.actionHelpTeach)
        # self.menuTask.addAction(self.actionViewTask)
        self.menuHelp.addAction(self.actionViewTask)
        self.menuBar.addAction(self.menuHelp.menuAction())
        # self.menuBar.addAction(self.menuTask.menuAction())

        self.retranslateUi(MainWindow6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow6)








    def retranslateUi(self, MainWindow6):
        _translate = QtCore.QCoreApplication.translate
        MainWindow6.setWindowTitle(_translate("MainWindow6", "Задание 6"))
        self.toolBar.setWindowTitle(_translate("MainWindow6", "toolBar"))
        self.menuHelp.setTitle(_translate("MainWindow6", "Справка"))
        # self.menuTask.setTitle(_translate("MainWindow6", "Задание 6"))
        self.actionNewFile.setText(_translate("MainWindow6", "Новый файл"))
        self.actionNewFile.setToolTip(_translate("MainWindow6", "Создать новый файл"))
        self.actionOpenFile.setText(_translate("MainWindow6", "Открыть файл"))




        self.actionSaveFile.setText(_translate("MainWindow6", "Сохранить"))
        self.actionSaveFileAs.setText(_translate("MainWindow6", "Сохранить как"))
        self.actionForward.setText(_translate("MainWindow6", "Вперед        Ctrl+Y"))
        self.actionBackward.setText(_translate("MainWindow6", "Назад          Ctrl+Z"))
        self.actionbtnHome.setText(_translate("MainWindow6", "btnHome"))
        self.actionbtnHome.setToolTip(_translate("MainWindow6", "Перейти к выбору заданий / В меню"))
        self.actionbtnZoomIn.setText(_translate("MainWindow6", "btnZoomIn"))
        self.actionbtnZoomIn.setToolTip(_translate("MainWindow6", "Увеличить изображение"))
        self.actionbtnZoomOut.setText(_translate("MainWindow6", "btnZoomOut"))




        self.actionbtnZoomOut.setToolTip(_translate("MainWindow6", "Уменьшить изображение"))
        self.actionHelpTask.setText(_translate("MainWindow6", "Справка по заданию"))
        self.actionHelpProgram.setText(_translate("MainWindow6", "Справка по программе "))
        self.actionSetting.setText(_translate("MainWindow6", "Настройки программы"))
        self.actionbtnCheck.setText(_translate("MainWindow6", "btnCheck"))
        self.actionbtnCheck.setToolTip(_translate("MainWindow6", "<html><head/><body><p>Завершить работу</p></body></html>"))
        self.actionbtnInfo.setText(_translate("MainWindow6", "btnInfo"))
        self.actionbtnInfo.setToolTip(_translate("MainWindow6", "Материалы"))
        self.actionbtnDottedConnectNode.setText(_translate("MainWindow6", "btnDottedConnectNode"))
        self.actionbtnDottedConnectNode.setToolTip(_translate("MainWindow6", "Перемещение пунктирной стрелки"))
        self.actionbtnMoveNode.setText(_translate("MainWindow6", "btnMoveNode"))
        self.actionbtnMoveNode.setToolTip(_translate("MainWindow6", "Передвинуть элемент"))
        self.actionHelp.setText(_translate("MainWindow6", "подсказка"))
        self.actionHelp.setToolTip(_translate("MainWindow6", "подсказка (режим преподавателя)"))
        self.actionHelpStud.setText(_translate("MainWindow6", "студенту"))
        self.actionHelpTeach.setText(_translate("MainWindow6", "преподавателю"))
        self.actionViewTask.setText(_translate("MainWindow6", "Задание 6"))
        self.actionSolveTask.setText(_translate("MainWindow6", "SolveTask"))
        self.actionSolveTask.setToolTip(_translate("MainWindow6", "решить задание (режим преподавателя)"))