# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 455)
        MainWindow.setMinimumSize(QtCore.QSize(415, 455))
        MainWindow.setMaximumSize(QtCore.QSize(415, 455))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 411, 431))
        self.stackedWidget.setObjectName("stackedWidget")
        self.studenthome = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studenthome.sizePolicy().hasHeightForWidth())
        self.studenthome.setSizePolicy(sizePolicy)
        self.studenthome.setObjectName("studenthome")
        self.gridLayoutWidget = QtWidgets.QWidget(self.studenthome)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 391, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.view_attendance = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        self.view_attendance.setFont(font)
        self.view_attendance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.view_attendance.setObjectName("view_attendance")
        self.view_attendance.clicked.connect(self.view_attendance_clicked)
        self.gridLayout.addWidget(self.view_attendance, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.take_attendance = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        self.take_attendance.setFont(font)
        self.take_attendance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.take_attendance.setStyleSheet("border-color: rgb(170, 85, 255);")
        self.take_attendance.setObjectName("take_attendance")
        self.take_attendance.clicked.connect(self.take_attendance_clicked)
        self.gridLayout.addWidget(self.take_attendance, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.goto_admin = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.goto_admin.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        self.goto_admin.setFont(font)
        self.goto_admin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goto_admin.setObjectName("goto_admin")
        self.goto_admin.clicked.connect(self.goto_admin_clicked)
        self.horizontalLayout_2.addWidget(self.goto_admin, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 0, 1, 1)
        self.stackedWidget.addWidget(self.studenthome)
        self.view_attend = QtWidgets.QWidget()
        self.view_attend.setObjectName("view_attend")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.view_attend)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 381, 391))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget_2)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 6, 0, 1, 2)
        self.check_attendance = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.check_attendance.setFont(font)
        self.check_attendance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_attendance.setObjectName("check_attendance")
        self.check_attendance.clicked.connect(self.check_attendance_clicked)
        self.gridLayout_2.addWidget(self.check_attendance, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.student_name = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.student_name.setFont(font)
        self.student_name.setObjectName("student_name")
        self.gridLayout_2.addWidget(self.student_name, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.back_employeep = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.back_employeep.setFont(font)
        self.back_employeep.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_employeep.setObjectName("back_employeep")
        self.back_employeep.clicked.connect(self.back_employeep_clicked)
        self.gridLayout_2.addWidget(self.back_employeep, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.view_attend)
        self.admin_login = QtWidgets.QWidget()
        self.admin_login.setObjectName("admin_login")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.admin_login)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(40, 30, 341, 211))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(27)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.admin_password = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.admin_password.setFont(font)
        self.admin_password.setObjectName("admin_password")
        self.gridLayout_3.addWidget(self.admin_password, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)
        self.admin_login_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.admin_login_btn.setFont(font)
        self.admin_login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.admin_login_btn.setObjectName("admin_login_btn")
        self.admin_login_btn.clicked.connect(self.login)
        self.gridLayout_3.addWidget(self.admin_login_btn, 4, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.admin_name = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.admin_name.setFont(font)
        self.admin_name.setObjectName("admin_name")
        self.gridLayout_3.addWidget(self.admin_name, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.back_employeep2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.back_employeep2.setFont(font)
        self.back_employeep2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_employeep2.setObjectName("back_employeep2")
        self.back_employeep2.clicked.connect(self.back_employeep_clicked)
        self.gridLayout_3.addWidget(self.back_employeep2, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.admin_login)
        self.admin_portal = QtWidgets.QWidget()
        self.admin_portal.setObjectName("admin_portal")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.admin_portal)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 391, 371))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 6, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 4, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.delete_employee = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        self.delete_employee.setFont(font)
        self.delete_employee.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_employee.setObjectName("delete_employee")
        self.delete_employee.clicked.connect(self.delete_employee_clicked)
        self.gridLayout_4.addWidget(self.delete_employee, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 8, 0, 1, 1)
        self.add_employee = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        self.add_employee.setFont(font)
        self.add_employee.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_employee.setStyleSheet("border-color: rgb(170, 85, 255);")
        self.add_employee.setObjectName("add_employee")
        self.add_employee.clicked.connect(self.add_employee_clicked)
        self.gridLayout_4.addWidget(self.add_employee, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.admin_logout = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(14)
        self.admin_logout.setFont(font)
        self.admin_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.admin_logout.setObjectName("admin_logout")
        self.admin_logout.clicked.connect(self.admin_logout_clicked)
        self.horizontalLayout_3.addWidget(self.admin_logout, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 7, 0, 1, 1)
        self.stackedWidget.addWidget(self.admin_portal)
        self.admin_add_employee = QtWidgets.QWidget()
        self.admin_add_employee.setObjectName("admin_add_employee")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.admin_add_employee)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(30, 20, 351, 391))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setHorizontalSpacing(21)
        self.gridLayout_5.setVerticalSpacing(19)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.emp_add = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.emp_add.setFont(font)
        self.emp_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.emp_add.setObjectName("emp_add")
        self.emp_add.clicked.connect(self.add_employee_in_xl)
        self.gridLayout_5.addWidget(self.emp_add, 13, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.emp_name = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.emp_name.setFont(font)
        self.emp_name.setClearButtonEnabled(True)
        self.emp_name.setObjectName("emp_name")
        self.gridLayout_5.addWidget(self.emp_name, 6, 1, 1, 1)
        self.emp_email = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.emp_email.setFont(font)
        self.emp_email.setClearButtonEnabled(True)
        self.emp_email.setObjectName("emp_email")
        self.gridLayout_5.addWidget(self.emp_email, 9, 1, 1, 1)
        self.emp_phno = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.emp_phno.setFont(font)
        self.emp_phno.setClearButtonEnabled(True)
        self.emp_phno.setObjectName("emp_phno")
        self.gridLayout_5.addWidget(self.emp_phno, 10, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 10, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 6, 0, 1, 1)
        self.emp_id = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.emp_id.setFont(font)
        self.emp_id.setClearButtonEnabled(True)
        self.emp_id.setObjectName("emp_id")
        self.gridLayout_5.addWidget(self.emp_id, 5, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 11, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 12, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 9, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 5, 0, 1, 1)
        self.emp_dob = QtWidgets.QDateEdit(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.emp_dob.setFont(font)
        self.emp_dob.setMaximumDate(QtCore.QDate(9999, 12, 30))
        self.emp_dob.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.emp_dob.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.emp_dob.setCalendarPopup(True)
        self.emp_dob.setCurrentSectionIndex(2)
        self.emp_dob.setObjectName("emp_dob")
        self.gridLayout_5.addWidget(self.emp_dob, 11, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.upload_pic = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(11)
        font.setItalic(True)
        self.upload_pic.setFont(font)
        self.upload_pic.setObjectName("upload_pic")
        self.upload_pic.clicked.connect(self.uplaod_image)
        self.horizontalLayout_4.addWidget(self.upload_pic, 0, QtCore.Qt.AlignLeft)
        self.or_label = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.or_label.setFont(font)
        self.or_label.setObjectName("or_label")
        self.horizontalLayout_4.addWidget(self.or_label, 0, QtCore.Qt.AlignHCenter)
        self.click_pic = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(11)
        font.setItalic(True)
        self.click_pic.setFont(font)
        self.click_pic.setObjectName("click_pic")
        self.click_pic.clicked.connect(self.click_image)
        self.horizontalLayout_4.addWidget(self.click_pic, 0, QtCore.Qt.AlignRight)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 12, 1, 1, 1)
        self.stackedWidget.addWidget(self.admin_add_employee)
        self.admin_delete_employee = QtWidgets.QWidget()
        self.admin_delete_employee.setObjectName("admin_delete_employee")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.admin_delete_employee)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(20, 30, 371, 161))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(21)
        self.gridLayout_6.setVerticalSpacing(26)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_39 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout_6.addWidget(self.label_39, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.del_employee = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.del_employee.setFont(font)
        self.del_employee.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.del_employee.setObjectName("del_employee")
        self.del_employee.clicked.connect(self.delete_employee_from_xl)
        self.gridLayout_6.addWidget(self.del_employee, 6, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout_6.addWidget(self.label_36, 0, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.back_adminp = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.back_adminp.setFont(font)
        self.back_adminp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_adminp.setObjectName("back_adminp")
        self.back_adminp.clicked.connect(self.back_admin)
        self.gridLayout_6.addWidget(self.back_adminp, 6, 1, 1, 1)
        self.del_emp_id = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        self.del_emp_id.setFont(font)
        self.del_emp_id.setClearButtonEnabled(True)
        self.del_emp_id.setObjectName("del_emp_id")
        self.gridLayout_6.addWidget(self.del_emp_id, 5, 1, 1, 2)
        self.stackedWidget.addWidget(self.admin_delete_employee)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.view_attendance.setText(_translate("MainWindow", "View Attendance"))
        self.take_attendance.setText(_translate("MainWindow", "Take Attendance"))
        self.label.setText(_translate("MainWindow", "Attendance System"))
        self.goto_admin.setText(_translate("MainWindow", "Admin >"))
        self.check_attendance.setText(_translate("MainWindow", "Check"))
        self.label_12.setText(_translate("MainWindow", "Enter ID"))
        self.label_10.setText(_translate("MainWindow", "View Attendance"))
        self.back_employeep.setText(_translate("MainWindow", "Back"))
        self.label_17.setText(_translate("MainWindow", "Enter password:"))
        self.admin_login_btn.setText(_translate("MainWindow", "Login"))
        self.label_16.setText(_translate("MainWindow", "Enter your name:"))
        self.label_13.setText(_translate("MainWindow", "Admin Login"))
        self.back_employeep2.setText(_translate("MainWindow", "< Employee"))
        self.label_23.setText(_translate("MainWindow", "Attendance System"))
        self.label_21.setText(_translate("MainWindow", "Admin"))
        self.delete_employee.setText(_translate("MainWindow", "Delete Employee"))
        self.add_employee.setText(_translate("MainWindow", "Add Employee"))
        self.admin_logout.setText(_translate("MainWindow", "Logout"))
        self.emp_add.setText(_translate("MainWindow", "Add Employee"))
        self.label_25.setText(_translate("MainWindow", "Phone number"))
        self.label_4.setText(_translate("MainWindow", "Add Employee"))
        self.label_26.setText(_translate("MainWindow", "Name"))
        self.label_27.setText(_translate("MainWindow", "Date of birth"))
        self.label_28.setText(_translate("MainWindow", "Photo"))
        self.label_29.setText(_translate("MainWindow", "Email:"))
        self.label_30.setText(_translate("MainWindow", "Employee ID"))
        self.emp_dob.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.upload_pic.setText(_translate("MainWindow", "Upload"))
        self.or_label.setText(_translate("MainWindow", "OR"))
        self.click_pic.setText(_translate("MainWindow", "Click"))
        self.label_39.setText(_translate("MainWindow", "Employee ID"))
        self.del_employee.setText(_translate("MainWindow", "Delete"))
        self.label_36.setText(_translate("MainWindow", "Delete Employee"))
        self.back_adminp.setText(_translate("MainWindow", "Back"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
