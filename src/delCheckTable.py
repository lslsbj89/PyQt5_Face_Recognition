# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delCheckTable.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_delCheckTable(object):
    def setupUi(self, Form_delCheckTable):
        Form_delCheckTable.setObjectName("Form_delCheckTable")
        Form_delCheckTable.resize(400, 300)
        self.layoutWidget = QtWidgets.QWidget(Form_delCheckTable)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 344, 164))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lab_addTest_8 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_addTest_8.sizePolicy().hasHeightForWidth())
        self.lab_addTest_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_addTest_8.setFont(font)
        self.lab_addTest_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_addTest_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_addTest_8.setObjectName("lab_addTest_8")
        self.verticalLayout_3.addWidget(self.lab_addTest_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lab_addTest_6 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_addTest_6.sizePolicy().hasHeightForWidth())
        self.lab_addTest_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_addTest_6.setFont(font)
        self.lab_addTest_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_addTest_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_addTest_6.setObjectName("lab_addTest_6")
        self.verticalLayout.addWidget(self.lab_addTest_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_delCheckTable = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_delCheckTable.setObjectName("comboBox_delCheckTable")
        self.verticalLayout_2.addWidget(self.comboBox_delCheckTable)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_confirm = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_confirm.sizePolicy().hasHeightForWidth())
        self.btn_confirm.setSizePolicy(sizePolicy)
        self.btn_confirm.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_confirm.setFont(font)
        self.btn_confirm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout_2.addWidget(self.btn_confirm)
        self.btn_refresh = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_refresh.sizePolicy().hasHeightForWidth())
        self.btn_refresh.setSizePolicy(sizePolicy)
        self.btn_refresh.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_refresh.setFont(font)
        self.btn_refresh.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_refresh.setObjectName("btn_refresh")
        self.horizontalLayout_2.addWidget(self.btn_refresh)
        self.btn_cancel = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form_delCheckTable)
        QtCore.QMetaObject.connectSlotsByName(Form_delCheckTable)

    def retranslateUi(self, Form_delCheckTable):
        _translate = QtCore.QCoreApplication.translate
        Form_delCheckTable.setWindowTitle(_translate("Form_delCheckTable", "Form"))
        self.lab_addTest_8.setText(_translate("Form_delCheckTable", "删除考勤表"))
        self.lab_addTest_6.setText(_translate("Form_delCheckTable", "考勤表名称："))
        self.btn_confirm.setText(_translate("Form_delCheckTable", "确定"))
        self.btn_refresh.setText(_translate("Form_delCheckTable", "刷新"))
        self.btn_cancel.setText(_translate("Form_delCheckTable", "取消"))

