# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddMWView.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


import os
import sqlite3
import sys
import time
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QDate
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QWidget
from Login_recorder import getCurrentUserId, logToFile

from Utils import openDB

class AddMWWidget(object):
    def setupUi(self, Dialog):

        # 自己添加的，很重要
        self.dialog = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(1005, 767)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)

        # 设置全局字体
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(50, 30, 50, -1)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.maintenanceWayID = QtWidgets.QLineEdit(Dialog)
        self.maintenanceWayID.setObjectName("maintenanceWayID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.maintenanceWayID)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.maintenanceWayName = QtWidgets.QLineEdit(Dialog)
        self.maintenanceWayName.setObjectName("maintenanceWayName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maintenanceWayName)
        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.Label_7 = QtWidgets.QLabel(Dialog)
        self.Label_7.setObjectName("Label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_7)
        self.Label_9 = QtWidgets.QLabel(Dialog)
        self.Label_9.setObjectName("Label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_9)
        self.creator = QtWidgets.QLineEdit(Dialog)
        self.creator.setObjectName("creator")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.creator)
        self.Label_11 = QtWidgets.QLabel(Dialog)
        self.Label_11.setObjectName("Label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_11)
        self.updateName = QtWidgets.QLineEdit(Dialog)
        self.updateName.setObjectName("updateName")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.updateName)
        self.Label_13 = QtWidgets.QLabel(Dialog)
        self.Label_13.setObjectName("Label_13")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_13)

        # self.alterRule = QtWidgets.QLineEdit(Dialog)
        # self.alterRule.setObjectName("alterRule")
        # self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.alterRule)

        self.alterRule = QtWidgets.QSpinBox(Dialog)
        self.alterRule.setObjectName("alterRule")
        self.alterRule.setMaximum(999999)
        self.alterRule.setValue(3)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.alterRule)

        self.firstTime = QtWidgets.QDateEdit(Dialog)
        self.firstTime.setDisplayFormat("yyyy-MM-dd")
        self.firstTime.setMinimumDate(QDate(2015, 1, 1))
        self.firstTime.setDate(QDate.fromString(time.strftime("%Y-%m-%d", time.localtime()), 'yyyy-MM-dd'))
        self.firstTime.setMaximumDate(QDate(2199, 1, 1))
        self.firstTime.setCalendarPopup(True)
        self.firstTime.setObjectName("firstTime")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.firstTime)

        self.recentTime = QtWidgets.QDateEdit(Dialog)
        self.recentTime.setDisplayFormat("yyyy-MM-dd")
        self.recentTime.setMinimumDate(QDate(2015, 1, 1))
        self.recentTime.setDate(QDate.fromString(time.strftime("%Y-%m-%d", time.localtime()), 'yyyy-MM-dd'))
        self.recentTime.setMaximumDate(QDate(2199, 1, 1))
        self.recentTime.setCalendarPopup(True)
        self.recentTime.setObjectName("recentTime")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.recentTime)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.productName = QtWidgets.QLineEdit(Dialog)
        self.productName.setEnabled(True)
        self.productName.setReadOnly(False)
        self.productName.setObjectName("productName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.productName)
        self.Label_6 = QtWidgets.QLabel(Dialog)
        self.Label_6.setObjectName("Label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.productNO = QtWidgets.QLineEdit(Dialog)
        self.productNO.setObjectName("productNO")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.productNO)
        self.Label_8 = QtWidgets.QLabel(Dialog)
        self.Label_8.setObjectName("Label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_8)

        # self.interval = QtWidgets.QLineEdit(Dialog)
        # self.interval.setObjectName("interval")
        # self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.interval)

        self.interval = QtWidgets.QSpinBox(Dialog)
        self.interval.setObjectName("interval")
        self.interval.setMaximum(999999)
        self.interval.setValue(60)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.interval)

        self.Label_10 = QtWidgets.QLabel(Dialog)
        self.Label_10.setObjectName("Label_10")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_10)
        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.Label_14 = QtWidgets.QLabel(Dialog)
        self.Label_14.setObjectName("Label_14")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_14)
        self.remark = QtWidgets.QLineEdit(Dialog)
        self.remark.setObjectName("remark")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.createTime = QtWidgets.QDateTimeEdit(Dialog)
        self.createTime.setObjectName("createTime")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.updateTime = QtWidgets.QDateTimeEdit(Dialog)
        self.updateTime.setObjectName("updateTime")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.updateTime)
        self.productID = QtWidgets.QComboBox(Dialog)
        self.productID.setObjectName("productID")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.productID)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(50, 10, 50, -1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.operation = QtWidgets.QTextEdit(Dialog)
        self.operation.setMinimumSize(QtCore.QSize(0, 300))
        self.operation.setObjectName("operation")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.operation)
        self.Label_15 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.Label_15.setFont(font)
        self.Label_15.setObjectName("Label_15")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_15)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Dialog)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout_2.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # 设置更改
        self.creator.setEnabled(False)
        self.createTime.setEnabled(False)
        self.updateName.setEnabled(False)
        self.updateTime.setEnabled(False)
        self.productName.setEnabled(False)
        self.productNO.setEnabled(False)
        self.maintenanceWayID.setEnabled(False)

        self.retranslateUi(Dialog)
        # 自己加的
        self.bindButton(Dialog)
        self.addcombobox(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新增维保方式"))
        self.Label.setText(_translate("Dialog", "维保方式编号："))
        self.Label_3.setText(_translate("Dialog", "维保方式名称："))
        self.Label_5.setText(_translate("Dialog", "初次维保时间："))
        self.Label_7.setText(_translate("Dialog", "最近维保时间："))
        self.Label_9.setText(_translate("Dialog", "创建人员："))
        self.Label_11.setText(_translate("Dialog", "修改人员："))
        self.Label_13.setText(_translate("Dialog", "维保到期提醒："))
        self.firstTime.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd"))
        self.recentTime.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd"))
        self.Label_2.setText(_translate("Dialog", "产品编号："))
        self.Label_4.setText(_translate("Dialog", "产品名称："))
        self.Label_6.setText(_translate("Dialog", "产品代号："))
        self.Label_8.setText(_translate("Dialog", "维保时间间隔："))
        self.Label_10.setText(_translate("Dialog", "创建时间："))
        self.Label_12.setText(_translate("Dialog", "修改时间："))
        self.Label_14.setText(_translate("Dialog", "备注："))
        self.createTime.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm:ss"))
        self.updateTime.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm:ss"))
        self.Label_15.setText(_translate("Dialog", "维保操作说明："))
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))


        self.maintenanceWayID.setText(self.getMwID())
        self.creator.setText(getCurrentUserId())
        # 设置创建时间
        # 得到当前时间
        # now = datetime.now()
        # now.strftime('%Y/%m/%d %H/%M/%S')
        # self.createTime.setText(now)
        self.createTime.setDateTime(QDateTime.currentDateTime())
        self.updateTime.setDateTime(QDateTime.currentDateTime())

        # self.createTime.setText("--")
        self.updateName.setText("--")
        # self.updateTime.setText("--")

        # self.interval.setValue(60)
        # self.alterRule.setValue(3)


    def bindButton(self, Dialog):
        """
        hsj 按钮绑定事件
        :param Dialog: 弹窗本身
        :return:
        """
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Dialog))
        # 获取产品数量并设置校验的槽函数
        # self.productID.clicked.connect(self.getProduct)
        self.productID.currentIndexChanged.connect(self.getProduct)



    def addcombobox(self,Dialog):
        try:
            db = openDB()
            query = QSqlQuery()
            # print("getProduct这里执行了：")
            id_list = [""]
            # id_list = list()
            if not self.productID.hasFocus():
                sql = "SELECT ProductID From T_Product_New "
                # print(sql)
                query.exec(sql)
                while query.next():
                    id_list.append(query.value(0))
            # print(id_list)
            for i in id_list :
                self.productID.addItem(str(i))
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
                    productname = query.value(0)
                    productno = query.value(1)
                    self.productName.setText(productname)
                    self.productNO.setText(productno)
        except Exception as e:
            print(e)

    def getMwID(self):
        max_no = ''
        db = openDB()
        q = QSqlQuery()
        date_str = QDate.currentDate().toString("yyyyMMdd")
        sql = "SELECT MaintenanceWayID FROM MaintenanceWay WHERE ID=(SELECT MAX(ID) FROM MaintenanceWay)"
        if q.exec(sql):
            while q.next():
                max_no = q.value(0)
        db.close()
        if date_str > max_no[1:9]:
            return 'W' + date_str + '001'
        else:
            return 'W' + str(int(max_no[1:]) + 1)

    def conserveButtonEvent(self, Dialog):
        """
        hsj 新建产品界面的保存按钮事件
        :return:
        """
        maintenanceWayID = self.maintenanceWayID.text()
        maintenanceWayName = self.maintenanceWayName.text()
        productID = self.productID.currentText()
        productName = self.productName.text()
        productNO = self.productNO.text()
        firstTime = self.firstTime.text()
        recentTime = self.recentTime.text()
        interval = self.interval.text()
        alterRule = self.alterRule.text()
        creator = getCurrentUserId()
        # createTime是默认创建的，下面由系统自动生成
        createTime = self.createTime.text()
        updateName = self.updateName.text()
        updateTime = self.updateTime.text()
        operation = self.operation.toPlainText()
        remark = self.remark.text()

        logger = logToFile()
        UserId = getCurrentUserId()

        # 如果必要的信息都不为空
        if maintenanceWayID == "" or productID == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            logger.info("用户：" + str(UserId) + " 新建维保方式失败（必要信息为空）")
            return
        else:
            num = self.checkOn(maintenanceWayID)
            if num == 0:
                logger.info("用户：" + str(UserId) + " 新建维保方式失败（新建数据未通过检验）")
                return
            # createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            # insert_sql = "INSERT INTO MaintenanceWay VALUES ('%s', '%s', '%s', '%s', '%s'" \
            #              ", '%s', '%s','%s', '%s', '%s',%s)" % \
            #              (maintenanceWayID, productID, maintenanceWayName, firstTime, interval,
            #                 alterRule, creator, createTime, updateName, updateTime,remark)
            # self.query.exec(insert_sql)
            # self.db.commit()
            # confirm = QMessageBox.information(QDialog(), "提示", "维保方式新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            # if confirm == QMessageBox.Yes:
            #     Dialog.close()

            createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            conn = sqlite3.connect("./db/ProductManagement_new.db")
            # print('打卡db成功')
            cursor = conn.cursor()
            sql = "insert into MaintenanceWay (MaintenanceWayID, MaintenanceWayName, ProductID, ProductName, ProductNO, " \
                  "FirstTime, RecentTime, Interva, AlterRule, Creator, CreateTime," \
                  " UpdateName,UpdateTime,Operation, Remark) " \
                  "values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            try:
                cursor.execute(sql, (maintenanceWayID, maintenanceWayName, productID, productName, productNO,
                                     firstTime, recentTime, interval, alterRule, creator, createTime,
                                     updateName, updateTime, operation, remark))
                conn.commit()
                logger.info("用户：" + str(UserId) + " 新建了一条维保方式，新数据为：[" + str(maintenanceWayID) + " ," +
                            str(productID) + " ," + str(maintenanceWayName) + " ," + str(firstTime) + " ," +
                            str(interval) + " ," + str(alterRule) + " ," + str(creator) + " ," +
                            str(createTime) + " ," + str(updateName) + " ," + str(updateTime) + " ," +
                            str(operation) + " ," + str(remark) + " ]")
                confirm = QMessageBox.information(QDialog(), "提示", "维保方式新建成功！", QMessageBox.Yes, QMessageBox.Yes)
                if confirm == QMessageBox.Yes:
                    Dialog.close()
            except Exception as e:
                print(e)
                # self.errorMessage.setText("抱歉，您的输入有误：" + str(e))
                conn.rollback()

    def cancelButtonEvent(self, Dialog):
        """
        取消按钮事件
        :return:
        """
        Dialog.close()

    def updateButtonEvent(self, queryModel):
        print('updateButtonEvent执行了')
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """
        # print('updateButtonEvent执行了')

        maintenanceWayID = self.maintenanceWayID.text()
        maintenanceWayName = self.maintenanceWayName.text()
        productID = self.productID.currentText()
        productName = self.productName.text()
        productNO = self.productNO.text()
        firstTime = self.firstTime.text()
        recentTime = self.recentTime.text()
        interva = self.interval.text()
        alterRule = self.alterRule.text()
        creator = self.creator.text()
        createTime = self.createTime.text()
        updateName = getCurrentUserId()
        updateTime = self.updateTime.text()
        operation = self.operation.toPlainText()
        remark = self.remark.text()

        logger = logToFile()
        UserId = updateName

        # 如果必要的信息都不为空
        if maintenanceWayID == "" or productID == "":
            logger.info("用户：" + str(UserId) + " 更新维保方式失败（必要信息为空）")
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            # num = self.checkOn(maintenanceWayID)
            # if num == 0:
            #     logger.info("用户：" + str(UserId) + " 更新维保方式失败（未通过数据检测）")
            #     return

            updateTime = time.strftime("%Y-%m-%d %H:%M:%S")
            conn = sqlite3.connect("./db/ProductManagement_new.db")
            cursor = conn.cursor()
            sql = "update  MaintenanceWay set (MaintenanceWayName, ProductID, ProductName, ProductNO, FirstTime," \
                  " RecentTime, Interva, AlterRule, Creator, CreateTime, " \
                  "UpdateName,UpdateTime,Operation, Remark) " \
                  "= ('%s', '%s', '%s', '%s', '%s', " \
                  "'%s', '%s', '%s', '%s', '%s' ," \
                  "'%s', '%s', '%s', '%s') where MaintenanceWayID = ('%s')" %(
                  maintenanceWayName, productID, productName, productNO,firstTime,
                  recentTime, interva, alterRule, creator, createTime,
                  updateName, updateTime, operation, remark,maintenanceWayID)
            try:
                cursor.execute(sql)
                conn.commit()
                logger.info("用户：" + str(UserId) + " 更新维保方式成功！经过更新的部分数据为：[" + str(maintenanceWayID) + " ," +
                            str(productID) + " ," + str(maintenanceWayName) + " ," + str(firstTime) + " ," +
                            str(recentTime) + " ," + str(interva) + " ," + str(alterRule) + " ," + str(
                    creator) + " ," +
                            str(createTime) + " ," + str(updateName) + " ," + str(updateTime) + " ," +
                            str(operation) + " ," + str(remark) + "]")
                confirm = QMessageBox.information(QDialog(), "提示", "维保方式修改成功！", QMessageBox.Yes, QMessageBox.Yes)
                if confirm == QMessageBox.Yes:
                    self.dialog.close()
            except Exception as e:
                print(e)
                # self.errorMessage.setText("抱歉，您的输入有误：" + str(e))
                conn.rollback()

    def checkOn(self, maintenanceWayID):
        """
        检查维保方式id是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM MaintenanceWay WHERE MaintenanceWayID = '%s'" % maintenanceWayID
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "维保方式已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1

    # def getCurrentID(self):


    def updateData(self, list, queryModel):
        """
        修改维保方式信息
        :param list:
        :return:
        """
        # print('list',list)
        self.pre_list = list
        self.label.setText("修改维保方式信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda: self.updateButtonEvent(queryModel))
        # print("AddMWView中的updateData方法正常启动！")

        self.maintenanceWayID.setText(list[0])
        self.maintenanceWayName.setText(list[1])
        # try:
        #     for i in range(self.productID.count()):
        #         value = self.productID.itemText(i)
        #         # print(list[2],'sdfasd',value)
        #         if value == list[2]:
        #             self.productID.setCurrentIndex(i)
        # except Exception as e:
        #     print(e)
        self.productID.setCurrentText(list[2])
        self.productName.setText(list[3])
        self.productNO.setText(list[4])

        try:
            # print('验证updateData中的firstTime的setDateTime方法', list[5])
            self.firstTime.setDateTime(datetime.strptime(list[5], "%Y-%m-%d"))
            self.firstTime.setDisplayFormat("yyyy-MM-dd")
            self.recentTime.setDateTime(datetime.strptime(list[6],"%Y-%m-%d"))
            # self.recentTime.setDisplayFormat("yyyy-MM-dd")
        except Exception as e:
            # print('修改失败。。。。。')
            print(e)

        self.interval.setValue(int(list[7]))
        self.alterRule.setValue(int(list[8]))
        self.creator.setText(list[9])

        try:
            # print(list[10])
            self.createTime.setDateTime(datetime.strptime(list[10], "%Y-%m-%d %H:%M:%S"))
            self.createTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        except Exception as e:
            print(e)
        try:
            self.updateName.setText(getCurrentUserId())
            # 设置更新时间
            self.updateTime.setDateTime(QDateTime.currentDateTime())
            self.updateTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
            # print(len(list))
            self.operation.setText(list[13])
            # print(list[13])
            self.remark.setText(list[14])
            # print(list[14])
        except Exception as e:
            print('remark下面的异常，',e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = AddMWWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
