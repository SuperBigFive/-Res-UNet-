# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


# GUI界面设计
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 905)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelinput = QtWidgets.QLabel(self.centralwidget)
        self.labelinput.setGeometry(QtCore.QRect(150, 70, 384, 384))
        self.labelinput.setMinimumSize(QtCore.QSize(54, 20))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.labelinput.setFont(font)
        self.labelinput.setObjectName("labelinput")

        # 图片显示区域容器
        self.pic_box = QtWidgets.QGroupBox(self.centralwidget)
        self.pic_box.setGeometry(QtCore.QRect(610, 70, 384, 384))
        self.pic_box.setStyleSheet("border: 1px solid grey")


        self.labelresult = QtWidgets.QLabel(self.pic_box)
        self.labelresult.setGeometry(QtCore.QRect(0, 0, 384, 384))
        self.labelresult.setStyleSheet("border: 1px solid grey")
        self.labelresult.setAlignment(QtCore.Qt.AlignCenter)


        font = QtGui.QFont()
        font.setPointSize(40)
        self.labelresult.setFont(font)
        self.labelresult.setLineWidth(4)
        self.labelresult.setMidLineWidth(2)
        self.labelresult.setObjectName("labelresult")
        self.btnInput = QtWidgets.QPushButton(self.centralwidget)
        self.btnInput.setGeometry(QtCore.QRect(300, 570, 92, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnInput.setFont(font)
        self.btnInput.setObjectName("btnInput")
        self.btnTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnTest.setGeometry(QtCore.QRect(740, 570, 75, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnTest.setFont(font)
        self.btnTest.setObjectName("btnTest")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(250, 630, 621, 192))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.btnmultiInput = QtWidgets.QPushButton(self.centralwidget)
        self.btnmultiInput.setGeometry(QtCore.QRect(520, 570, 92, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnmultiInput.setFont(font)
        self.btnmultiInput.setObjectName("btnmultiInput")
        self.btnonlySmallBowel = QtWidgets.QPushButton(self.centralwidget)
        self.btnonlySmallBowel.setGeometry(QtCore.QRect(760, 480, 92, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnonlySmallBowel.setFont(font)
        self.btnonlySmallBowel.setObjectName("btnonlySmallBowel")
        self.btnonlyLargeBowel = QtWidgets.QPushButton(self.centralwidget)
        self.btnonlyLargeBowel.setGeometry(QtCore.QRect(650, 480, 92, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnonlyLargeBowel.setFont(font)
        self.btnonlyLargeBowel.setObjectName("btnonlyLargeBowel")
        self.btnonlyStomach = QtWidgets.QPushButton(self.centralwidget)
        self.btnonlyStomach.setGeometry(QtCore.QRect(870, 480, 92, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnonlyStomach.setFont(font)
        self.btnonlyStomach.setObjectName("btnonlyStomach")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnInput.clicked.connect(MainWindow.btnInput_Clicked) # type: ignore
        self.btnTest.clicked.connect(MainWindow.btnTest_Clicked) # type: ignore
        self.btnTest.pressed.connect(MainWindow.btnTest_Pressed) # type: ignore
        self.btnmultiInput.clicked.connect(MainWindow.btnmultiInput_Clicked) # type: ignore
        self.btnonlyLargeBowel.clicked.connect(MainWindow.btnonlyLargeBowel_Clicked) # type: ignore
        self.btnonlySmallBowel.clicked.connect(MainWindow.btnonlySmallBowel_Clicked) # type: ignore
        self.btnonlyStomach.clicked.connect(MainWindow.btnonlyStomach_Clicked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelinput.setText(_translate("MainWindow", "  输入图片"))
        self.labelresult.setText(_translate("MainWindow", "  结果图片"))
        self.btnInput.setText(_translate("MainWindow", "导入图片"))
        self.btnTest.setText(_translate("MainWindow", "检测"))
        self.btnmultiInput.setText(_translate("MainWindow", "导入多图"))
        self.btnonlySmallBowel.setText(_translate("MainWindow", "只看小肠"))
        self.btnonlyLargeBowel.setText(_translate("MainWindow", "只看大肠"))
        self.btnonlyStomach.setText(_translate("MainWindow", "只看胃"))
