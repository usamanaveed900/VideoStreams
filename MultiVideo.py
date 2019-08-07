# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultiVideos.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 276, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(289, 10, 781, 321))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Video_frame = QtWidgets.QLabel(self.frame_2)
        self.Video_frame.setText("")
        self.Video_frame.setObjectName("Video_frame")
        self.horizontalLayout_2.addWidget(self.Video_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.path=''

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionOpen.triggered.connect(self.viewFilesList)
        self.listWidget.itemClicked.connect(self.setup_camera)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

    # Views files in the folder to the list widget.
    def viewFilesList(self):
        self.path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory")
        fileNames=os.listdir(self.path)
        for items in fileNames:
            self.listWidget.addItem(items)

    #Any video file in list widget is loaded in the frame and previewed
    def setup_camera(self,item):
        self.capture = cv2.VideoCapture(self.path+"/"+ item.text())
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 461)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 301)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(10)

    def display_video_stream(self):
        _, frame = self.capture.read()
        frame = cv2.resize(frame,(320,320))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # cv2.imshow('Video',frame)
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], 
                       frame.strides[0], QtGui.QImage.Format_RGB888)
        self.Video_frame.setPixmap(QtGui.QPixmap.fromImage(image))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

