# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\畢專\MusicE\PyQt5\UI\frame4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame4(object):
    def setupUi(self, Frame4):
        Frame4.setObjectName("Frame4")
        Frame4.resize(1123, 794)
        Frame4.setMinimumSize(QtCore.QSize(1123, 794))
        Frame4.setMaximumSize(QtCore.QSize(1123, 794))
        Frame4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Frame4)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_import = QtWidgets.QPushButton(self.centralwidget)
        self.menu_import.setEnabled(True)
        self.menu_import.setGeometry(QtCore.QRect(533, 81, 119, 33))
        self.menu_import.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_import.setText("")
        self.menu_import.setObjectName("menu_import")
        self.menu_selection = QtWidgets.QPushButton(self.centralwidget)
        self.menu_selection.setEnabled(False)
        self.menu_selection.setGeometry(QtCore.QRect(669, 67, 151, 51))
        self.menu_selection.setText("")
        self.menu_selection.setObjectName("menu_selection")
        self.menu_download = QtWidgets.QPushButton(self.centralwidget)
        self.menu_download.setEnabled(False)
        self.menu_download.setGeometry(QtCore.QRect(845, 81, 60, 33))
        self.menu_download.setText("")
        self.menu_download.setObjectName("menu_download")
        self.menu_finish = QtWidgets.QPushButton(self.centralwidget)
        self.menu_finish.setEnabled(False)
        self.menu_finish.setGeometry(QtCore.QRect(949, 81, 59, 33))
        self.menu_finish.setText("")
        self.menu_finish.setObjectName("menu_finish")
        self.menu_main = QtWidgets.QPushButton(self.centralwidget)
        self.menu_main.setEnabled(True)
        self.menu_main.setGeometry(QtCore.QRect(412, 80, 89, 34))
        self.menu_main.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_main.setMouseTracking(False)
        self.menu_main.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.menu_main.setText("")
        self.menu_main.setObjectName("menu_main")
        self.btn_vocal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vocal.setGeometry(QtCore.QRect(296, 279, 122, 122))
        self.btn_vocal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_vocal.setText("")
        self.btn_vocal.setObjectName("btn_vocal")
        self.btn_vocal_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vocal_play.setGeometry(QtCore.QRect(307, 475, 91, 53))
        self.btn_vocal_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_vocal_play.setText("")
        self.btn_vocal_play.setObjectName("btn_vocal_play")
        self.btn_piano = QtWidgets.QPushButton(self.centralwidget)
        self.btn_piano.setGeometry(QtCore.QRect(502, 279, 122, 122))
        self.btn_piano.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_piano.setText("")
        self.btn_piano.setObjectName("btn_piano")
        self.btn_piano_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_piano_play.setGeometry(QtCore.QRect(515, 475, 91, 53))
        self.btn_piano_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_piano_play.setText("")
        self.btn_piano_play.setObjectName("btn_piano_play")
        self.btn_drum = QtWidgets.QPushButton(self.centralwidget)
        self.btn_drum.setGeometry(QtCore.QRect(711, 279, 122, 122))
        self.btn_drum.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_drum.setText("")
        self.btn_drum.setObjectName("btn_drum")
        self.btn_drum_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_drum_play.setGeometry(QtCore.QRect(726, 475, 91, 53))
        self.btn_drum_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_drum_play.setText("")
        self.btn_drum_play.setObjectName("btn_drum_play")
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setGeometry(QtCore.QRect(493, 612, 139, 50))
        self.btn_confirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_confirm.setText("")
        self.btn_confirm.setObjectName("btn_confirm")
        self.btn_vocal_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vocal_stop.setEnabled(True)
        self.btn_vocal_stop.setGeometry(QtCore.QRect(307, 475, 91, 53))
        self.btn_vocal_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_vocal_stop.setText("")
        self.btn_vocal_stop.setObjectName("btn_vocal_stop")
        self.btn_piano_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_piano_stop.setEnabled(True)
        self.btn_piano_stop.setGeometry(QtCore.QRect(515, 475, 91, 53))
        self.btn_piano_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_piano_stop.setText("")
        self.btn_piano_stop.setObjectName("btn_piano_stop")
        self.btn_drum_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_drum_stop.setEnabled(True)
        self.btn_drum_stop.setGeometry(QtCore.QRect(726, 475, 91, 53))
        self.btn_drum_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_drum_stop.setText("")
        self.btn_drum_stop.setObjectName("btn_drum_stop")
        Frame4.setCentralWidget(self.centralwidget)

        self.retranslateUi(Frame4)
        QtCore.QMetaObject.connectSlotsByName(Frame4)

    def retranslateUi(self, Frame4):
        _translate = QtCore.QCoreApplication.translate
        Frame4.setWindowTitle(_translate("Frame4", "MusicE"))
