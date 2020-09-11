# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddMRView.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


import os
import sqlite3
from datetime import datetime
import time
from Login_recorder import getCurrentUserId, logToFile

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QDate
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog

from Utils import openDB


class AddMRWidget(object):
    def setupUi(self, Dialog):
        # 自己写的
        self.dialog = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(811, 904)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)

        # 设置全局字体
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)

        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.errorMessage = QtWidgets.QLabel(Dialog)
        self.errorMessage.setStyleSheet("color: rgb(255, 0, 0);")
        self.errorMessage.setObjectName("errorMessage")
        self.verticalLayout.addWidget(self.errorMessage)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, 8, 24)
        self.gridLayout.setHorizontalSpacing(26)
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.Label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_2.setFont(font)
        self.Label_2.setObjectName("Label_2")
        self.gridLayout.addWidget(self.Label_2, 3, 0, 1, 1)
        self.updateName = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateName.sizePolicy().hasHeightForWidth())
        self.updateName.setSizePolicy(sizePolicy)
        self.updateName.setObjectName("updateName")
        self.gridLayout.addWidget(self.updateName, 5, 3, 1, 1)
        self.creator = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creator.sizePolicy().hasHeightForWidth())
        self.creator.setSizePolicy(sizePolicy)
        self.creator.setObjectName("creator")
        self.gridLayout.addWidget(self.creator, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.Label_11 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_11.setFont(font)
        self.Label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_11.setObjectName("Label_11")
        self.gridLayout.addWidget(self.Label_11, 6, 2, 1, 1)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_4.setFont(font)
        self.Label_4.setObjectName("Label_4")
        self.gridLayout.addWidget(self.Label_4, 4, 0, 1, 1)
        self.mwName = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mwName.sizePolicy().hasHeightForWidth())
        self.mwName.setSizePolicy(sizePolicy)
        self.mwName.setObjectName("mwName")
        self.gridLayout.addWidget(self.mwName, 2, 1, 1, 1)
        self.Label_10 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_10.setFont(font)
        self.Label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_10.setObjectName("Label_10")
        self.gridLayout.addWidget(self.Label_10, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.productModelIDLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.productModelIDLabel.setFont(font)
        self.productModelIDLabel.setObjectName("productModelIDLabel")
        self.gridLayout.addWidget(self.productModelIDLabel, 2, 0, 1, 1)
        self.Label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label.setFont(font)
        self.Label.setObjectName("Label")
        self.gridLayout.addWidget(self.Label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.mrResult = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mrResult.sizePolicy().hasHeightForWidth())
        self.mrResult.setSizePolicy(sizePolicy)
        self.mrResult.setObjectName("mrResult")
        self.gridLayout.addWidget(self.mrResult, 4, 3, 1, 1)

        # self.mrTime = QtWidgets.QLineEdit(Dialog)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.mrTime.sizePolicy().hasHeightForWidth())
        # self.mrTime.setSizePolicy(sizePolicy)
        # self.mrTime.setObjectName("mrTime")
        # self.gridLayout.addWidget(self.mrTime, 3, 1, 1, 1)

        # 改成只要日期
        self.mrTime = QtWidgets.QDateEdit(Dialog)
        self.mrTime.setDisplayFormat("yyyy-MM-dd")
        self.mrTime.setMinimumDate(QDate(2015, 1, 1))
        self.mrTime.setDate(QDate.fromString(time.strftime("%Y-%m-%d", time.localtime()), 'yyyy-MM-dd'))
        self.mrTime.setMaximumDate(QDate(2199, 1, 1))
        self.mrTime.setCalendarPopup(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mrTime.sizePolicy().hasHeightForWidth())
        self.mrTime.setSizePolicy(sizePolicy)
        self.mrTime.setObjectName("mrTime")
        self.gridLayout.addWidget(self.mrTime, 3, 1, 1, 1)

        self.Label_7 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_7.setFont(font)
        self.Label_7.setObjectName("Label_7")
        self.gridLayout.addWidget(self.Label_7, 5, 0, 1, 1)
        self.Label_9 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_9.setFont(font)
        self.Label_9.setObjectName("Label_9")
        self.gridLayout.addWidget(self.Label_9, 6, 0, 1, 1)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_3.setFont(font)
        self.Label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_3.setObjectName("Label_3")
        self.gridLayout.addWidget(self.Label_3, 3, 2, 1, 1)

        # self.createTime = QtWidgets.QLineEdit(Dialog)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.createTime.sizePolicy().hasHeightForWidth())
        # self.createTime.setSizePolicy(sizePolicy)
        # self.createTime.setObjectName("createTime")
        # self.gridLayout.addWidget(self.createTime, 6, 1, 1, 1)

        # 把QLineEdit改成QDateTimeEdit,这样对用户更友好
        self.createTime = QtWidgets.QDateTimeEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createTime.sizePolicy().hasHeightForWidth())
        self.createTime.setSizePolicy(sizePolicy)
        self.createTime.setObjectName("createTime")
        self.gridLayout.addWidget(self.createTime, 6, 1, 1, 1)

        self.updateTime = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateTime.sizePolicy().hasHeightForWidth())
        self.updateTime.setSizePolicy(sizePolicy)
        self.updateTime.setObjectName("updateTime")
        self.gridLayout.addWidget(self.updateTime, 6, 3, 1, 1)

        # 把QLineEdit改成QDateEdit,这样对用户更友好
        self.updateTime = QtWidgets.QDateTimeEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateTime.sizePolicy().hasHeightForWidth())
        self.updateTime.setSizePolicy(sizePolicy)
        self.updateTime.setObjectName("updateTime")
        self.gridLayout.addWidget(self.updateTime, 6, 3, 1, 1)

        self.mrID = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mrID.sizePolicy().hasHeightForWidth())
        self.mrID.setSizePolicy(sizePolicy)
        self.mrID.setText("")
        self.mrID.setObjectName("mrID")
        self.gridLayout.addWidget(self.mrID, 0, 1, 1, 1)
        self.productName = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productName.sizePolicy().hasHeightForWidth())
        self.productName.setSizePolicy(sizePolicy)
        self.productName.setObjectName("productName")
        self.gridLayout.addWidget(self.productName, 1, 3, 1, 1)
        self.productNO = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productNO.sizePolicy().hasHeightForWidth())
        self.productNO.setSizePolicy(sizePolicy)
        self.productNO.setObjectName("productNO")
        self.gridLayout.addWidget(self.productNO, 2, 3, 1, 1)

        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.Label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_6.setFont(font)
        self.Label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_6.setObjectName("Label_6")
        self.gridLayout.addWidget(self.Label_6, 4, 2, 1, 1)
        self.mrPart = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mrPart.sizePolicy().hasHeightForWidth())
        self.mrPart.setSizePolicy(sizePolicy)
        self.mrPart.setObjectName("mrPart")
        self.gridLayout.addWidget(self.mrPart, 3, 3, 1, 1)
        self.mrLead = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mrLead.sizePolicy().hasHeightForWidth())
        self.mrLead.setSizePolicy(sizePolicy)
        self.mrLead.setObjectName("mrLead")
        self.gridLayout.addWidget(self.mrLead, 4, 1, 1, 1)
        self.productID = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.productID.setFont(font)
        self.productID.setObjectName("productID")
        self.gridLayout.addWidget(self.productID, 0, 3, 1, 1)

        self.mwID = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mwID.setFont(font)
        self.mwID.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.mwID, 1, 1, 1, 1)

        # 技术文档
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.documentPathButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.documentPathButton.sizePolicy().hasHeightForWidth())
        self.documentPathButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.documentPathButton.setFont(font)
        self.documentPathButton.setObjectName("documentPathButton")
        self.gridLayout.addWidget(self.documentPathButton, 7, 1, 1, 1)

        # 备注
        self.remarkLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.remarkLabel.setFont(font)
        self.remarkLabel.setObjectName("remarkLabel")
        self.gridLayout.addWidget(self.remarkLabel, 8, 0, 1, 1)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setObjectName("remark")
        self.gridLayout.addWidget(self.remark, 8, 1, 1, 3)

        self.gridLayout.setRowMinimumHeight(0, 30)
        self.gridLayout.setRowMinimumHeight(1, 30)
        self.gridLayout.setRowMinimumHeight(2, 30)
        self.gridLayout.setRowMinimumHeight(3, 30)
        self.gridLayout.setRowMinimumHeight(4, 30)
        self.gridLayout.setRowMinimumHeight(5, 30)
        self.gridLayout.setRowMinimumHeight(6, 30)
        self.gridLayout.setRowMinimumHeight(7, 30)

        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.conserveButton.setFont(font)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 设置更改
        self.mrID.setEnabled(False)
        self.creator.setEnabled(False)
        self.createTime.setEnabled(False)
        self.updateName.setEnabled(False)
        self.updateTime.setEnabled(False)
        self.productNO.setEnabled(False)
        self.productName.setEnabled(False)
        self.mwName.setEnabled(False)

        self.retranslateUi(Dialog)
        # 自己写的
        self.bindButton(Dialog)
        self.addcombobox(Dialog)
        # self.addmwID(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新增维保方式记录"))
        # self.errorMessage.setText(_translate("Dialog", "s"))
        self.Label_2.setText(_translate("Dialog", "维保时间："))
        self.label_5.setText(_translate("Dialog", "产品代号："))
        self.Label_11.setText(_translate("Dialog", "更新时间："))
        self.Label_4.setText(_translate("Dialog", "维保负责人："))
        self.Label_10.setText(_translate("Dialog", "更新人员："))
        self.label_2.setText(_translate("Dialog", "维保方式编号:"))
        self.productModelIDLabel.setText(_translate("Dialog", "维保方式名称："))
        self.Label.setText(_translate("Dialog", "维保记录编号："))
        self.label_3.setText(_translate("Dialog", "产品名称："))
        self.Label_7.setText(_translate("Dialog", "创建人员："))
        self.Label_9.setText(_translate("Dialog", "创建时间："))
        self.Label_3.setText(_translate("Dialog", "维保部位："))
        self.remarkLabel.setText(_translate("Dialog", "备注："))
        self.label_4.setText(_translate("Dialog", "产品编号："))
        self.Label_6.setText(_translate("Dialog", "维保效果："))
        self.label_6.setText(_translate("Dialog", "技术文档："))
        self.documentPathButton.setText(_translate("Dialog", "选择文档"))
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))


        self.mrTime.setDisplayFormat("yyyy-MM-dd")
        self.creator.setText("--")
        # 设置创建时间
                    # 得到当前时间
                    # now = datetime.now()
                    # now.strftime('%Y/%m/%d %H/%M/%S')
                    # self.createTime.setText(now)
        self.createTime.setDateTime(QDateTime.currentDateTime())
        self.updateTime.setDateTime(QDateTime.currentDateTime())
        self.createTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")

        # self.createTime.setText("--")
        self.updateName.setText("--")
        # self.updateTime.setText("--")
        self.updateTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.mrID.setText(self.getMrID())



    def bindButton(self, Dialog):
        """
        hsj 按钮绑定事件
        :param Dialog: 弹窗本身
        :return:
        """
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Dialog))
        self.productID.currentIndexChanged.connect(self.getProduct)
        self.mwID.currentTextChanged.connect(self.getMwName)
        self.documentPathButton.clicked.connect(self.documentPathButtonEvent)


    def addcombobox(self,Dialog):
        try:
            # 给产品id加上项目
            db = openDB()
            query = QSqlQuery()
            # print("getProduct这里执行了：")
            productid_list = [""]
            if not self.productID.hasFocus():
                sql = "SELECT ProductID From T_Product_New "
                # print(sql)
                query.exec(sql)
                while query.next():
                    productid_list.append(query.value(0))
            # print(productid_list)
            for i in productid_list :
                self.productID.addItem(str(i))
        except Exception as e:
            print(e)

    def addmwID(self):
        try:
            self.mwID.clear()
            # 给mwID加上项目
            db = openDB()
            query = QSqlQuery()
            productID = self.productID.currentText()
            # print(productID)
            mwid_list = ["该产品暂无相应的维保方式"]
            if not self.mwID.hasFocus():
                sql = "SELECT MaintenanceWayID From MaintenanceWay where ProductID =  '%s'" % (productID)
                # print(sql)
                query.exec(sql)
                while query.next():
                    mwid_list.append(query.value(0))
            # print(mwid_list)
            if len(mwid_list) > 1:
                mwid_list[0] = ""
                for i in mwid_list:
                    self.mwID.addItem(i)
                # for i in range(1,len(mwid_list)):
                #     self.mwID.addItem(str(mwid_list[i]))
            else:
                for i in mwid_list:
                    self.mwID.addItem(i)

        except Exception as e:
            print(e)

    def getProduct(self):
        try:
            db = openDB()
            query = QSqlQuery()
            # print("getProduct这里执行了：")
            if self.productID.hasFocus():
                sql = "SELECT ProductName,ProductNO From T_Product_New WHERE ProductID = '%s'" % (self.productID.currentText())
                # print(sql)
                query.exec(sql)
                if query.next():
                    # print('asdfa',query)
                    # print(query.value(0))
                    # print(query.value(1))
                    productname = query.value(0)
                    productno = query.value(1)
                    self.productName.setText(productname)
                    self.productNO.setText(productno)
            self.addmwID()
        except Exception as e:
            print(e)

    def getMwName(self):
        try:
            db = openDB()
            query = QSqlQuery()
            # print("getProduct这里执行了：")
            if self.mwID.hasFocus():
                sql = "SELECT MaintenanceWayName From MaintenanceWay WHERE MaintenanceWayID = '%s'" % (self.mwID.currentText())
                # print(sql)
                query.exec(sql)
                if query.next():
                    # print('asdfa',query)
                    # print(query.value(0))
                    mwName = query.value(0)
                    self.mwName.setText(mwName)
        except Exception as e:
            print(e)

    def getMrID(self):
        max_no = ''
        db = openDB()
        q = QSqlQuery()
        date_str = QDate.currentDate().toString("yyyyMMdd")
        sql = "SELECT MrID FROM MaintenanceRecord WHERE ID=(SELECT MAX(ID) FROM MaintenanceRecord)"
        if q.exec(sql):
            while q.next():
                max_no = q.value(0)
        db.close()
        if date_str > max_no[1:9]:
            return 'R' + date_str + '001'
        else:
            return 'R' + str(int(max_no[1:]) + 1)

    def documentPathButtonEvent(self):
        filePath, _ = QFileDialog.getOpenFileName(caption="选择文件", filter="PDF文件 (*.pdf);Word文件 (*.doc;*.docx)")
        self.documentPathButton.setText(filePath)
        self.documentPathButton.setDisabled(True)


    def conserveButtonEvent(self, Dialog):
        """
        hsj 新建产品界面的保存按钮事件
        :return:
        """
        mrID = self.mrID.text()
        productID = self.productID.currentText()
        productName = self.productName.text()
        productNO = self.productNO.text()
        mwID = self.mwID.currentText()
        mwName = self.mwName.text()
        mrTime = self.mrTime.text()
        mrPart = self.mrPart.text()
        mrLead = self.mrLead.text()
        mrResult = self.mrResult.text()
        creator = getCurrentUserId()
        createTime = self.createTime.text()
        updateName = self.updateName.text()
        updateTime = self.updateTime.text()
        documentPath = self.documentPathButton.text()
        remark = self.remark.toPlainText()

        logger = logToFile()
        UserId = getCurrentUserId()

        # 如果必要的信息都不为空
        if mrID == "" or mwID == "" or mwID == "该产品暂无相应的维保方式":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            logger.info("用户：" + str(UserId) + " 新建维保信息失败（必要信息为空）")
            return
        else:
            num = self.checkOn(mrID)
            if num == 0:
                logger.info("用户：" + str(UserId) + " 新建维保记录失败（新建数据未通过检验）")
                return
            createTime = time.strftime("%Y-%m-%d %H:%M:%S")

            conn = sqlite3.connect("./db/ProductManagement_new.db")
            cursor = conn.cursor()

            sql = "insert into MaintenanceRecord (MrID, ProductID, ProductName, ProductNO, MwID, " \
                                  "MwName, MrTime, MrPart, MrLead, MrResult, " \
                                  "Creator, CreateTime, UpdateName,UpdateTime,DocumentPath,Remark) " \
                  "values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            try:
                cursor.execute(sql, (mrID, productID, productName, productNO, mwID,
                                     mwName, mrTime, mrPart, mrLead, mrResult,
                                     creator, createTime, updateName,updateTime,documentPath,remark))
                conn.commit()
                logger.info("用户：" + str(UserId) + " 新建了一条维保记录，新数据为：[" + str(mrID) + " ," +
                            str(mwID) + " ," + str(mwName) + " ," + str(mrTime) + " ," +
                            str(mrPart) + " ," + str(mrLead) + " ," +
                            str(mrResult) + " ," + str(creator) + " ," + str(createTime) + " ," +
                            str(updateName) + str(updateTime) + " ," + str(documentPath)+" ,"+ str(remark) + " ]")
                # print("成功！！")
                confirm = QMessageBox.information(QDialog(), "提示", "维保记录创建完成！", QMessageBox.Yes, QMessageBox.Yes)
                if confirm == QMessageBox.Yes:
                    Dialog.close()
            except Exception as e:
                print(e)
                self.errorMessage.setText("抱歉，您的输入有误："+str(e))
                conn.rollback()

          # 获取RecentTime
            sql = 'SELECT RecentTime FROM MaintenanceWay where MaintenanceWayID=?'
            try:
                cursor.execute(sql,(mwID,))
                list = cursor.fetchone()
                if list[0]:
                    ss_recentTime = time.mktime(time.strptime(list[0],"%Y-%m-%d"))
                    ss_mrTime = time.mktime(time.strptime(mrTime,"%Y-%m-%d"))
                    # print(ss_mrTime)
                    # print(ss_recentTime)
                    diff = int(ss_mrTime) - int(ss_recentTime)
                    # print('diff',diff)
                    if diff :
                        sql = 'UPDATE MaintenanceWay set RecentTime=? where MaintenanceWayID=?'
                        cursor.execute(sql, (mrTime, mwID))
                        conn.commit()
                        conn.close()
                        # print('修改成功')
                else:
                    sql = 'UPDATE MaintenanceWay set RecentTime=? where MaintenanceWayID=?'
                    cursor.execute(sql, (mrTime, mwID))
                    conn.commit()
                    # print('修改成功')
                conn.close()
            except Exception as e:
                print(e)
                conn.close()
                # print('获取失败')

            # 修改MaintenanceWay表中的RecentTime
            # sql = 'UPDATE MaintenanceWay set RecentTime=? where MaintenanceWayID=?'
            # try :
            #     cursor.execute(sql,(mrTime,mwID))
            #     conn.commit()
            #     print('修改成功')
            # except Exception as e:
            #     print(e)
            #     print('获取失败')

    def cancelButtonEvent(self, Dialog):
        """
        取消按钮事件
        :return:
        """
        Dialog.close()

    def updateButtonEvent(self, queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """

        mrID = self.mrID.text()
        productID = self.productID.currentText()
        productName = self.productName.text()
        productNO = self.productNO.text()
        mwID = self.mwID.currentText()
        mwName = self.mwName.text()
        mrTime = self.mrTime.text()
        mrPart = self.mrPart.text()
        mrLead = self.mrLead.text()
        mrResult = self.mrResult.text()
        creator = self.creator.text()
        createTime = self.createTime.text()
        updateName = self.updateName.text()
        updateTime = getCurrentUserId()
        documentPath = self.documentPathButton.text()
        remark = self.remark.toPlainText()

        logger = logToFile()
        UserId = updateName


        if mrID == "" or mwID =="":
            logger.info("用户：" + str(UserId) + " 更新维保记录失败（重要字段信息为空）")
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            # num = self.checkOn(mrID)
            # if num == 0:
            #     logger.info("用户：" + str(UserId) + " 更新维保记录失败（未通过数据检测）")
            #     return
            updateTime = time.strftime("%Y-%m-%d %H:%M:%S")
            conn = sqlite3.connect("./db/ProductManagement_new.db")
            # print("success")
            cursor = conn.cursor()


            sql = "update MaintenanceRecord set (ProductID, ProductName, ProductNO, MwID, MwName, " \
                  "MrTime, MrPart, MrLead, MrResult, Creator, " \
                  "CreateTime, UpdateName,UpdateTime,DocumentPath,Remark) = " \
                  "('%s', '%s', '%s', '%s', '%s', " \
                  "'%s', '%s', '%s', '%s', '%s', " \
                  "'%s', '%s', '%s', '%s', '%s')" \
                  "where MrID = ('%s')" %(
                    productID, productName, productNO, mwID, mwName,
                    mrTime, mrPart, mrLead, mrResult, creator,
                    createTime, updateName, updateTime, documentPath, remark, mrID
                 )
            try:
                cursor.execute(sql)


                conn.commit()
                logger.info("用户：" + str(UserId) + " 更新维保记录成功，经过更新的部分数据为：[" + str(mrID) + " ," +
                            str(mwID) + " ," + str(mwName) + " ," + str(mrTime) + " ," +
                            str(mrPart) + " ," + str(mrLead) + " ," +
                            str(mrResult) + " ," + str(creator) + " ," + str(createTime) + " ," +
                            str(updateName) + str(updateTime) + " ," + str(documentPath)+" ," + str(remark) + " ]")
                confirm = QMessageBox.information(QDialog(), "提示", "维保记录修改成功！", QMessageBox.Yes, QMessageBox.Yes)
                if confirm == QMessageBox.Yes:
                    self.dialog.close()
            except Exception as e:
                print(e)
                self.errorMessage.setText("抱歉，您的输入有误：" + str(e))
                conn.rollback()

                # 获取RecentTime
            sql = 'SELECT RecentTime FROM MaintenanceWay where MaintenanceWayID=?'
            try:
                cursor.execute(sql, (mwID,))
                list = cursor.fetchone()
                if list[0]:
                    ss_recentTime = time.mktime(time.strptime(list[0], "%Y-%m-%d"))
                    ss_mrTime = time.mktime(time.strptime(mrTime, "%Y-%m-%d"))
                    # print(ss_mrTime)
                    # print(ss_recentTime)
                    diff = int(ss_mrTime) - int(ss_recentTime)
                    # print('diff', diff)
                    if diff:
                        sql = 'UPDATE MaintenanceWay set RecentTime=? where MaintenanceWayID=?'
                        cursor.execute(sql, (mrTime, mwID))
                        conn.commit()
                        conn.close()
                        # print('修改成功')
                else:
                    sql = 'UPDATE MaintenanceWay set RecentTime=? where MaintenanceWayID=?'
                    cursor.execute(sql, (mrTime, mwID))
                    conn.commit()
                    conn.close()
                    # print('修改成功')
            except Exception as e:
                print(e)
                conn.close()
                # print('获取失败')

    def checkOn(self, mrID):
        """
        检查产品号是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM MaintenanceRecord WHERE mrID = '%s'" % mrID
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "维保方式记录已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        # print("list",list)
        self.pre_list = list
        self.label.setText("修改维保记录信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda: self.updateButtonEvent(queryModel))
        # print("AddMWView中的updateData方法正常启动！"

        self.mrID.setText(list[0])
        self.productID.setCurrentText(list[1])
        self.productName.setText(list[2])
        self.productNO.setText(list[3])
        self.mwID.setCurrentText(list[4])
        self.mwName.setText(list[5])
        try:
            self.mrTime.setDateTime(datetime.strptime(list[6], "%Y-%m-%d"))
            self.mrTime.setDisplayFormat("yyyy-MM-dd")
        except Exception as e:
            print(e)
        self.mrPart.setText(list[7])
        self.mrLead.setText(list[8])
        self.mrResult.setText(list[9])
        self.creator.setText(list[10])

        try:
            # print(list[9])
            self.createTime.setDateTime(datetime.strptime(list[11], "%Y-%m-%d %H:%M:%S"))
            self.createTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
            # print('list9输出流')
        except Exception as e:
            print(e)
        self.updateName.setText(getCurrentUserId())
        # 设置更新时间

        try:
            self.updateTime.setDateTime(QDateTime.currentDateTime(),"%Y-%m-%d %H:%M:%S")
            self.updateTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        except Exception as e:
            print(e)

        self.documentPathButton.setText(list[14])
        self.remark.setText(list[15])


