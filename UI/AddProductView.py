# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddProductView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog

from Login_recorder import getCurrentUserId,logToFile
from Utils import openDB




class AddProductWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1097, 615)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(Dialog)
        self.titleLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(50, 30, 30, 10)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.iDLabel = QtWidgets.QLabel(Dialog)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.productNO = QtWidgets.QLineEdit(Dialog)
        self.productNO.setObjectName("productNO")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.productNO)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.batchNO = QtWidgets.QLineEdit(Dialog)
        self.batchNO.setObjectName("batchNO")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.batchNO)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.receiver = QtWidgets.QLineEdit(Dialog)
        self.receiver.setObjectName("receiver")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.receiver)
        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_5)


        self.receiverDate = QtWidgets.QDateEdit(Dialog)

        self.receiverDate.setDisplayFormat("yyyy-MM-dd")
        self.receiverDate.setMinimumDate(QDate(2015, 1, 1))
        self.receiverDate.setDate(QDate.fromString(time.strftime("%Y-%m-%d", time.localtime()), 'yyyy-MM-dd'))
        self.receiverDate.setMaximumDate(QDate(2199, 1, 1))
        self.receiverDate.setCalendarPopup(True)
        self.receiverDate.setObjectName("receiverDate")

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.receiverDate)
        self.Label_7 = QtWidgets.QLabel(Dialog)
        self.Label_7.setObjectName("Label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_7)
        self.receiverCompany = QtWidgets.QLineEdit(Dialog)
        self.receiverCompany.setObjectName("receiverCompany")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.receiverCompany)
        self.storePlace = QtWidgets.QComboBox(Dialog)
        self.storePlace.setObjectName("storePlace")
        self.storePlace.addItems(["模拟仓库一", "模拟仓库二", "模拟仓库三", "模拟仓库四"])

        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.storePlace)
        self.Label_11 = QtWidgets.QLabel(Dialog)
        self.Label_11.setObjectName("Label_11")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_11)

        self.lifeType = QtWidgets.QComboBox(Dialog)
        self.lifeType.setObjectName("lifeType")
        self.lifeType.addItems(["时间", "次数"])

        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lifeType)
        self.Label_13 = QtWidgets.QLabel(Dialog)
        self.Label_13.setObjectName("Label_13")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_13)
        self.lifeTime = QtWidgets.QSpinBox(Dialog)
        self.lifeTime.setObjectName("lifeTime")
        self.lifeTime.setMaximum(999999)
        self.lifeTime.setValue(1641)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lifeTime)
        self.Label_15 = QtWidgets.QLabel(Dialog)
        self.Label_15.setObjectName("Label_15")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_15)
        self.toLifeDays = QtWidgets.QSpinBox(Dialog)
        self.toLifeDays.setObjectName("toLifeDays")
        self.toLifeDays.setValue(30)
        self.toLifeDays.setMaximum(999999)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.toLifeDays)
        self.Label_9 = QtWidgets.QLabel(Dialog)
        self.Label_9.setObjectName("Label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_9)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(30, 30, 50, 10)
        self.formLayout_2.setHorizontalSpacing(15)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.productName = QtWidgets.QLineEdit(Dialog)
        self.productName.setObjectName("productName")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.productName)
        self.fatherLabel = QtWidgets.QLabel(Dialog)
        self.fatherLabel.setObjectName("fatherLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fatherLabel)
        self.count = QtWidgets.QSpinBox(Dialog)
        self.count.setObjectName("count")
        self.count.setMaximum(999999)
        self.count.setSingleStep(5)
        self.count.setValue(10)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.count)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.registerer = QtWidgets.QLineEdit(Dialog)
        self.registerer.setObjectName("registerer")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.registerer)
        self.displayOrderLabel = QtWidgets.QLabel(Dialog)
        self.displayOrderLabel.setObjectName("displayOrderLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.displayOrderLabel)

        self.registerDate = QtWidgets.QDateEdit(Dialog)
        self.registerDate.setObjectName("registerDate")
        self.registerDate.setDisplayFormat("yyyy-MM-dd")
        self.registerDate.setMinimumDate(QDate(2015, 1, 1))
        self.registerDate.setDate(QDate.fromString(time.strftime("%Y-%m-%d", time.localtime()), 'yyyy-MM-dd'))
        self.registerDate.setMaximumDate(QDate(2199, 1, 1))
        self.registerDate.setCalendarPopup(True)
        self.registerDate.setObjectName("registerDate")

        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.registerDate)
        self.Label_6 = QtWidgets.QLabel(Dialog)
        self.Label_6.setObjectName("Label_6")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.registerCompany = QtWidgets.QLineEdit(Dialog)
        self.registerCompany.setObjectName("registerCompany")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.registerCompany)
        self.Label_8 = QtWidgets.QLabel(Dialog)
        self.Label_8.setObjectName("Label_8")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_8)
        self.document = QtWidgets.QPushButton(Dialog)
        self.document.setObjectName("document")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.document)
        self.Label_10 = QtWidgets.QLabel(Dialog)
        self.Label_10.setObjectName("Label_10")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_10)

        self.firstMaintainTime = QtWidgets.QDateEdit(Dialog)
        self.firstMaintainTime.setObjectName("registerDate")
        self.firstMaintainTime.setObjectName("firstMaintainTime")
        self.firstMaintainTime.setDisplayFormat("yyyy-MM-dd")
        self.firstMaintainTime.setMinimumDate(QDate(2015, 1, 1))
        self.firstMaintainTime.setDate(QDate.fromString(time.strftime("%Y-%m-%d", time.localtime()), 'yyyy-MM-dd'))
        self.firstMaintainTime.setMaximumDate(QDate(2199, 1, 1))
        self.firstMaintainTime.setCalendarPopup(True)
        self.firstMaintainTime.setObjectName("firstMaintainTime")

        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.firstMaintainTime)
        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.maintainInterval = QtWidgets.QSpinBox(Dialog)
        self.maintainInterval.setObjectName("maintainInterval")
        self.maintainInterval.setMaximum(999999)
        self.maintainInterval.setValue(10)
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.maintainInterval)
        self.Label_14 = QtWidgets.QLabel(Dialog)
        self.Label_14.setObjectName("Label_14")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_14)
        self.toMaintainDays = QtWidgets.QSpinBox(Dialog)
        self.toMaintainDays.setObjectName("toMaintainDays")
        self.toMaintainDays.setMaximum(999999)
        self.toMaintainDays.setValue(10)
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.toMaintainDays)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
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

        self.retranslateUi(Dialog)
        self.bindButton(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # def getMwID(self):
    #     max_no = ''
    #     db = openDB()
    #     q = QSqlQuery()
    #     date_str = QDate.currentDate().toString("yyyyMMdd")
    #     sql = "SELECT MaintenanceWayID FROM MainteFnanceWay WHERE ID=(SELECT MAX(ID) FROM MaintenanceWay)"
    #     if q.exec(sql):
    #         while q.next():
    #             max_no = q.value(0)
    #     db.close()
    #     if date_str > max_no[1:9]:
    #         return 'W' + date_str + '001'
    #     else:
    #         return 'W' + str(int(max_no[1:]) + 1)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titleLabel.setText(_translate("Dialog", "新建产品信息"))
        self.iDLabel.setText(_translate("Dialog", "产品代号："))
        self.Label_2.setText(_translate("Dialog", "批次编号："))
        self.Label_4.setText(_translate("Dialog", "接收人："))
        self.Label_5.setText(_translate("Dialog", "接收日期："))
        self.Label_7.setText(_translate("Dialog", "接收单位："))
        self.Label_11.setText(_translate("Dialog", "寿命类型："))
        self.Label_13.setText(_translate("Dialog", "寿命时间："))
        self.Label_15.setText(_translate("Dialog", "距寿命到期时间提醒："))
        self.Label_9.setText(_translate("Dialog", "存放库房："))
        self.Label.setText(_translate("Dialog", "产品名称："))
        self.fatherLabel.setText(_translate("Dialog", "数量："))
        self.Label_3.setText(_translate("Dialog", "交付人："))
        self.displayOrderLabel.setText(_translate("Dialog", "交付日期："))
        self.Label_6.setText(_translate("Dialog", "交付单位："))
        self.Label_8.setText(_translate("Dialog", "技术文档："))
        self.document.setText(_translate("Dialog", "选择文档"))
        self.Label_10.setText(_translate("Dialog", "初次维保时间："))
        self.Label_12.setText(_translate("Dialog", "维保间隔："))
        self.Label_14.setText(_translate("Dialog", "距下次维保时间提醒："))
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))
        self.receiver.setText(getCurrentUserId())

    def bindButton(self, Dialog):
        """
        hsj 按钮绑定事件
        :param Dialog: 弹窗本身
        :return:
        """
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Dialog))
        self.document.clicked.connect(self.documentButtonEvent)

    def documentButtonEvent(self):
        filePath, _ = QFileDialog.getOpenFileName(caption="选择文件", filter="PDF文件 (*.pdf);Word文件 (*.doc;*.docx)")
        filename = filePath.split('/')[-1]
        self.document.setText(filePath)
        self.document.setDisabled(True)

    def cancelButtonEvent(self, Dialog):
        """
        取消按钮事件
        :return:
        """
        Dialog.close()

    def getProductID(self):
        max_no = ''
        db = openDB()
        q = QSqlQuery()
        date_str = QDate.currentDate().toString("yyyyMMdd")
        sql = "SELECT ProductID FROM T_Product_New WHERE ID=(SELECT MAX(ID) FROM T_Product_New)"
        if q.exec(sql):
            while q.next():
                max_no = q.value(0)
        db.close()
        if date_str > max_no[1:9]:
            return 'P' + date_str + '001'
        else:
            return 'P' + str(int(max_no[1:]) + 1)

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
        logger = logToFile()
        UserId = getCurrentUserId()

        productNO = self.productNO.text()
        productName = self.productName.text()
        batchNO = self.batchNO.text()
        receiver = self.receiver.text()
        receiverDate = self.receiverDate.text()
        receiverCompany = self.receiverCompany.text()
        registerer = self.registerer.text()
        registerDate = self.registerDate.text()
        registerCompany = self.registerCompany.text()
        count = self.count.text()
        storePlace = self.storePlace.currentText()
        lifeType = self.lifeType.currentText()
        lifeTime = self.lifeTime.text()
        toliftDays = self.toLifeDays.text()
        firstMaintainTime = self.firstMaintainTime.text()
        maintainInterval = self.maintainInterval.text()
        toMaintainDays = self.toMaintainDays.text()
        document = self.document.text()
        productID = self.getProductID()
        maintenanceWayID = self.getMwID()

        # 如果必要的信息都不为空
        if productNO == "" or productName == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            # import time
            # createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.db = openDB()
            self.query = QSqlQuery()
            insert_sql = "INSERT INTO T_Product_New VALUES (null, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %\
                         (productID, productNO, productName, batchNO, receiver, receiverDate, receiverCompany, registerer, registerDate, registerCompany, count, count, storePlace, lifeType, lifeTime , toliftDays, firstMaintainTime, toMaintainDays, maintainInterval, document)

            # print(insert_sql)
            self.query.exec_(insert_sql)

            maintenanceWayName = "默认维保方式"
            createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            sql = "insert into MaintenanceWay (MaintenanceWayID, MaintenanceWayName, ProductID, ProductName, ProductNO, " \
                  "FirstTime, RecentTime, Interva, AlterRule, Creator, CreateTime," \
                  " UpdateName,UpdateTime,Operation, Remark) " \
                  "values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '--', '%s','详情见技术文档', '无')" % (maintenanceWayID, maintenanceWayName, productID, productName, productNO,
                                 firstMaintainTime, firstMaintainTime, maintainInterval, toMaintainDays, registerer, createTime, createTime)
            self.query.exec_(sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "产品新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            logger.info("用户: " + str(UserId) + " 新建了一条T_Product_New表数据，新数据为:[" + str(productID) + "," + str(
                productNO) + "," + str(productName) + "," + str(batchNO) + "," +
                        str(receiver) + "," + str(receiverDate) + "," + str(receiverCompany) + "," + str(
                registerer) + "," + str(receiverDate) + "," + str(receiverCompany) + "," + str(count) + "," +
                        str(count) + "," + str(storePlace) + "," + str(lifeType) + "," + str(lifeTime) + "," + str(
                toliftDays) + "," + str(firstMaintainTime) + "," + str(toMaintainDays) + "," +
                        str(maintainInterval) + "," + str(document) + "]")
            if confirm == QMessageBox.Yes:
                Dialog.close()

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        self.pre_list = list
        list = list[1:]
        self.titleLabel.setText("修改产品信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda :self.updateButtonEvent(queryModel))

        self.productNO.setText(list[1])
        self.productName.setText(list[2])
        self.batchNO.setText(list[3])
        self.receiver.setText(list[4])
        self.receiverDate.setDate(QDate.fromString(list[5]))
        self.receiverCompany.setText(list[6])
        self.registerer.setText(list[7])
        self.registerDate.setDate(QDate.fromString(list[8]))
        self.registerCompany.setText(list[9])
        self.count.setValue(int(list[11]))
        self.storePlace.setCurrentText(list[12])
        self.lifeType.setCurrentText(list[13])
        self.lifeTime.setValue(int(list[14]))
        self.toLifeDays.setValue(int(list[15]))
        self.firstMaintainTime.setDate(QDate.fromString(list[16]))
        self.maintainInterval.setValue(int(list[17]))
        self.toMaintainDays.setValue(int(list[18]))
        self.document.setText(list[19])
        # self.productNO.setText(list[0])
        # self.life.setText(list[1])
        # # self.startDate.set
        # self.daysbefore.setText(list[3])
        # self.isUsedCountLimit.setText(list[4])
        # self.maxUsedCount.setText(list[5])
        # self.havaUsedCount.setText(list[6])
        # self.createID.setText(list[7])
        # self.createTime.setText(list[8])
        # self.createID.setText(list[9])
        # self.updateTime.setText(list[10])
        # self.remark.setText(list[11])

    def showData(self, list, queryModel):
        self.updateData(list, queryModel)
        self.titleLabel.setText("详细产品信息")
        self.productNO.setDisabled(True)
        self.productName.setDisabled(True)
        self.batchNO.setDisabled(True)
        self.receiver.setDisabled(True)
        self.receiverDate.setDisabled(True)
        self.receiverCompany.setDisabled(True)
        self.registerer.setDisabled(True)
        self.registerDate.setDisabled(True)
        self.registerCompany.setDisabled(True)
        self.count.setDisabled(True)
        self.storePlace.setDisabled(True)
        self.lifeType.setDisabled(True)
        self.lifeTime.setDisabled(True)
        self.toLifeDays.setDisabled(True)
        self.firstMaintainTime.setDisabled(True)
        self.maintainInterval.setDisabled(True)
        self.toMaintainDays.setDisabled(True)
        self.document.setDisabled(True)
        self.conserveButton.setVisible(False)
        self.cancelButton.setVisible(False)

    def updateButtonEvent(self, queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """
        logger = logToFile()
        UserId = getCurrentUserId()

        # print(self.pre_list)
        productID = self.pre_list[1]
        productNO = self.productNO.text()
        productName = self.productName.text()
        batchNO = self.batchNO.text()
        receiver = self.receiver.text()
        receiverDate = self.receiverDate.text()
        receiverCompany = self.receiverCompany.text()
        registerer = self.registerer.text()
        registerDate = self.registerDate.text()
        registerCompany = self.registerCompany.text()
        count = self.count.text()
        initCount = int(self.pre_list[11]) + int(count) - int(self.pre_list[12])

        storePlace = self.storePlace.currentText()
        lifeType = self.lifeType.currentText()
        lifeTime = self.lifeTime.text()
        toliftDays = self.toLifeDays.text()
        firstMaintainTime = self.firstMaintainTime.text()
        maintainInterval = self.maintainInterval.text()
        toMaintainDays = self.toMaintainDays.text()
        document = self.document.text()
        self.db = openDB()
        self.query = QSqlQuery()
        update_sql = "UPDATE T_Product_New SET (ProductNO, ProductName, BatchNO, Receiver, ReceiverDate, ReceiverCompany, Registerer, RegisterDate, RegisterCompany, InitCount, Count, StorePlace, LifeType, LifeTime, ToLifeDays, FirstMaintainTime, ToMaintainDays, MaintainInterval, Document) = " \
                     "('%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s','%s') WHERE ProductID = '%s'" % \
                     (productNO, productName, batchNO, receiver, receiverDate, receiverCompany, registerer, registerDate, registerCompany, initCount, count, storePlace, lifeType, lifeTime, toliftDays, firstMaintainTime, toMaintainDays, maintainInterval, document, productID)
        logger.info(
            "用户: " + str(UserId) + " 更新了一条T_Product_New表数据，新数据为:[" + str(productID) + "," + str(productNO) + "," + str(
                productName) + "," + str(batchNO) + "," +
            str(receiver) + "," + str(receiverDate) + "," + str(receiverCompany) + "," + str(registerer) + "," + str(
                receiverDate) + "," + str(receiverCompany) + "," + str(count) + "," +
            str(count) + "," + str(storePlace) + "," + str(lifeType) + "," + str(lifeTime) + "," + str(
                toliftDays) + "," + str(firstMaintainTime) + "," + str(toMaintainDays) + "," +
            str(maintainInterval) + "," + str(document) + "]")

        # print(update_sql)
        self.query.exec(update_sql)
        self.db.commit()
        confirm = QMessageBox.information(QDialog(), "提示", "产品更改成功！", QMessageBox.Yes, QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            self.dialog.close()
