import openpyxl
import os
import face_recognition
import cv2
from main import take_attendance
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 420)
        
        # Set up size policy
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(399, 420))
        MainWindow.setMaximumSize(QtCore.QSize(399, 420))
        
        # Create font
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        
        # Set up central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        
        # Set up grid layout widget
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # Create title label
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
        # Create attendance button
        self.take_attendance = QtWidgets.QPushButton(self.gridLayoutWidget)
        font.setPointSize(14)
        self.take_attendance.setFont(font)
        self.take_attendance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.take_attendance.setStyleSheet("border-color: rgb(170, 85, 255);")
        self.take_attendance.setObjectName("take_attendance")
        self.gridLayout.addWidget(self.take_attendance, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.take_attendance.clicked.connect(self.take_attendance_clicked)
        
        # Set up group info label
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_2.setIndent(-2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1, QtCore.Qt.AlignVCenter)
        
        # Set up button to view attendance
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        
        # Set up menu bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuStudent = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.menuStudent.setFont(font)
        self.menuStudent.setObjectName("menuStudent")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
        self.menuTeacher = QtWidgets.QMenu(self.menubar)
        self.menuTeacher.setObjectName("menuTeacher")
        MainWindow.setMenuBar(self.menubar)
        self.actionTeacher = QtWidgets.QAction(MainWindow)
        self.actionTeacher.setObjectName("actionTeacher")
        self.menubar.addAction(self.menuStudent.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuTeacher.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Facial Attendance System"))
        self.label.setText(_translate("MainWindow", "Attendance System"))
        self.take_attendance.setText(_translate("MainWindow", "Take attendance"))
        self.label_2.setText(_translate("MainWindow", "Developed by Group Flip-flops"))
        self.pushButton_2.setText(_translate("MainWindow", "View Attendance"))
        self.menuStudent.setTitle(_translate("MainWindow", "Student"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.menuTeacher.setTitle(_translate("MainWindow", "Teacher"))
        self.actionTeacher.setText(_translate("MainWindow", "Teacher"))
    
    def take_attendance_clicked(self):
        take_attendance()
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())