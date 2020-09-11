# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddProductComponent.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog
from Login_recorder import logToFile,getCurrentUserId

from Utils import openDB


class AddComponentWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 681)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(75, -1, 75, -1)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.iDLabel = QtWidgets.QLabel(Dialog)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iDLabel)

        self.productID = QtWidgets.QComboBox(Dialog)
        self.productID.setObjectName("productID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.productID)

        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.componentNO = QtWidgets.QLineEdit(Dialog)
        self.componentNO.setObjectName("componentNO")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.componentNO)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.componentName = QtWidgets.QLineEdit(Dialog)
        self.componentName.setObjectName("componentName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.componentName)
        self.iDLabel_2 = QtWidgets.QLabel(Dialog)
        self.iDLabel_2.setObjectName("iDLabel_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.iDLabel_2)
        self.fatherID = QtWidgets.QComboBox(Dialog)
        self.fatherID.setObjectName("fatherID")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fatherID)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.componentType = QtWidgets.QComboBox(Dialog)
        self.componentType.setObjectName("componentType")
        self.componentType.addItems(["组件", "分组件", "部件", "零件"])
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.componentType)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.count = QtWidgets.QSpinBox(Dialog)
        self.count.setObjectName("count")
        self.count.setValue(10)
        self.count.setSingleStep(5)
        self.count.setMaximum(99999999)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.count)
        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.lifeType = QtWidgets.QComboBox(Dialog)
        self.lifeType.setObjectName("lifeType")
        self.lifeType.addItems(["时间", "次数"])
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lifeType)
        self.Label_6 = QtWidgets.QLabel(Dialog)
        self.Label_6.setObjectName("Label_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.lifeTime = QtWidgets.QSpinBox(Dialog)
        self.lifeTime.setObjectName("lifeTime")
        self.lifeTime.setMaximum(9999999)
        self.lifeTime.setValue(1471)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lifeTime)
        self.Label_7 = QtWidgets.QLabel(Dialog)
        self.Label_7.setObjectName("Label_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_7)
        self.toLifeDays = QtWidgets.QSpinBox(Dialog)
        self.toLifeDays.setObjectName("toLifeDays")
        self.toLifeDays.setValue(30)
        self.toLifeDays.setMaximum(999999)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.toLifeDays)
        self.Label_8 = QtWidgets.QLabel(Dialog)
        self.Label_8.setObjectName("Label_8")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.Label_8)
        self.firstMaintainTime = QtWidgets.QDateEdit(Dialog)
        self.firstMaintainTime.setObjectName("registerDate")
        self.firstMaintainTime.setObjectName("firstMaintainTime")
        self.firstMaintainTime.setDisplayFormat("yyyy-MM-dd")
        self.firstMaintainTime.setMinimumDate(QDate(2015, 1, 1))
        self.firstMaintainTime.setDate(QDate.fromString(time.strftime("%Y-%m-%d", time.localtime()), 'yyyy-MM-dd'))
        self.firstMaintainTime.setMaximumDate(QDate(2199, 1, 1))
        self.firstMaintainTime.setCalendarPopup(True)
        self.firstMaintainTime.setObjectName("firstMaintainTime")

        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.firstMaintainTime)
        self.Label_9 = QtWidgets.QLabel(Dialog)
        self.Label_9.setObjectName("Label_9")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.Label_9)
        self.maintainInterval = QtWidgets.QSpinBox(Dialog)
        self.maintainInterval.setObjectName("maintainInterval")
        self.maintainInterval.setMaximum(9999999)
        self.maintainInterval.setValue(60)
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.maintainInterval)
        self.Label_10 = QtWidgets.QLabel(Dialog)
        self.Label_10.setObjectName("Label_10")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Label_10)
        self.toMaintainDays = QtWidgets.QSpinBox(Dialog)
        self.toMaintainDays.setObjectName("toMaintainDays")
        self.toMaintainDays.setValue(5)
        self.toMaintainDays.setMaximum(9999999)
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.toMaintainDays)
        self.verticalLayout.addLayout(self.formLayout)
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
        self.addProductID(Dialog)
        self.addComponentID(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新建产品组件"))
        self.iDLabel.setText(_translate("Dialog", "产品ID:"))
        self.Label.setText(_translate("Dialog", "组件代号："))
        self.Label_2.setText(_translate("Dialog", "组件名称："))
        self.iDLabel_2.setText(_translate("Dialog", "父组件ID："))
        self.Label_3.setText(_translate("Dialog", "组件类型："))
        self.Label_4.setText(_translate("Dialog", "组件数量："))
        self.Label_5.setText(_translate("Dialog", "寿命类型："))
        self.Label_6.setText(_translate("Dialog", "寿命："))
        self.Label_7.setText(_translate("Dialog", "距寿命到期提醒："))
        self.Label_8.setText(_translate("Dialog", "最初维保时间："))
        self.Label_9.setText(_translate("Dialog", "维保时间间隔："))
        self.Label_10.setText(_translate("Dialog", "距维保到期提醒："))
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))

    def addProductID(self,Dialog):
        try:
            db = openDB()
            query = QSqlQuery()
            productID_list = list()
            if not self.productID.hasFocus():
                sql = "SELECT ProductID From T_Product_New "
                # print(sql)
                query.exec(sql)
                while query.next():
                    productID_list.append(query.value(0))
            # print(mwid_list)
            for i in productID_list :
                self.productID.addItem(str(i))
        except Exception as e:
            print(e)

    def addComponentID(self, Dialog):
        try:
            db = openDB()
            query = QSqlQuery()
            ComponentID_list = [0]
            if not self.fatherID.hasFocus():
                sql = "SELECT ComponentID From T_ProductComponent_New "
                # print(sql)
                query.exec(sql)
                while query.next():
                    ComponentID_list.append(query.value(0))
            # print(mwid_list)
            for i in ComponentID_list:
                self.fatherID.addItem(str(i))
        except Exception as e:
            print(e)

    def bindButton(self, Dialog):
        """
        hsj 按钮绑定事件
        :param Dialog: 弹窗本身
        :return:
        """
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Dialog))
        self.fatherID.currentIndexChanged.connect(self.getProductIDEvent)

    def getProductIDEvent(self):
        try:
            db = openDB()
            query = QSqlQuery()
            # print("getProduct这里执行了：")
            if self.fatherID.hasFocus():
                sql = "SELECT ProductID From T_ProductComponent_New WHERE ComponentID = '%s'" % (self.fatherID.currentText())
                #print(sql)
                query.exec(sql)
                if query.next():
                    # print('asdfa',query)
                    # print(query.value(0))
                    productID = query.value(0)
                    #print(productID)
                    self.productID.setCurrentText(productID)
        except Exception as e:
            print(e)

    def getComponentID(self):
        max_no = ''
        db = openDB()
        q = QSqlQuery()
        date_str = QDate.currentDate().toString("yyyyMMdd")
        sql = "SELECT ComponentID FROM T_ProductComponent_New WHERE ID=(SELECT MAX(ID) FROM T_ProductComponent_New)"
        if q.exec(sql):
            while q.next():
                max_no = q.value(0)
        db.close()
        if date_str > max_no[1:9]:
            return 'Z' + date_str + '001'
        else:
            return 'Z' + str(int(max_no[1:]) + 1)

    def conserveButtonEvent(self, Dialog):
        """
        hsj 新建产品组件界面的保存按钮事件
        :return:
        """
        logger = logToFile()
        UserId = getCurrentUserId()

        productID = self.productID.currentText()
        componentNO = self.componentNO.text()
        componentName = self.componentName.text()
        fatherID = self.fatherID.currentText()
        componentType = self.componentType.currentText()
        count = self.count.text()
        liftType = self.lifeType.currentText()
        lifeTime = self.lifeTime.text()
        tolifeDays = self.toLifeDays.text()
        firstMaintainTime = self.firstMaintainTime.text()
        maintainInterval = self.maintainInterval.text()
        toMaintainDays = self.toMaintainDays.text()
        componentID = self.getComponentID()
        if fatherID == "0":
            fatherID = "无父组件"
        # 如果必要的信息都不为空
        if productID == "" or componentNO == "":
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(productID, fatherID)
            if num == 0:
                return
            insert_sql = "INSERT INTO T_ProductComponent_New VALUES (null, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                         % (componentID, productID, componentNO, componentName, fatherID, componentType, count, liftType, lifeTime, tolifeDays, firstMaintainTime, maintainInterval, toMaintainDays)
            self.query.exec(insert_sql)
            self.db.commit()

            logger.info("用户：" + str(UserId) + " 新建了一个 T_ProductComponent_New 表的数据，新数据为：["+str(componentID)+","+str(productID)+","+str(componentNO)+","+str(componentName)+","+str(fatherID)+","+str(componentType)+","+str(count)+","+str(liftType)+","+str(lifeTime)+","+str(tolifeDays)+ "," +str(firstMaintainTime)+","+str(maintainInterval)+","+str(toMaintainDays)+"]")

            confirm = QMessageBox.information(QDialog(), "提示", "组件新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                Dialog.close()

    def checkOn(self, productID, componentID):
        """
        检查ID, 组件名称和产品号是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        if componentID != "无父组件":
            sql = "SELECT * FROM T_ProductComponent_New WHERE ComponentID = '%s'" % componentID
            self.query.exec(sql)
            if not self.query.next():
                print(QMessageBox.information(QDialog(), "提示", "父组件ID不存在，请确认后重试！", QMessageBox.Yes, QMessageBox.Yes))
                return 0
        sql = "SELECT * FROM T_Product_New WHERE ProductID = '%s'" % productID
        self.query.exec(sql)
        if not self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "对应的产品不存在！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1

    def cancelButtonEvent(self, Dialog):
        """
        取消按钮事件
        :return:
        """
        Dialog.close()

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        self.pre_list = list
        # list = list[1:]
        self.label.setText("修改产品组件")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda :self.updateButtonEvent(queryModel))
        self.productID.setCurrentText(list[2])
        self.componentNO.setText(list[3])
        self.componentName.setText(list[4])
        if list[5] == "无父组件":
            list[5] = 0
        self.fatherID.setCurrentText(str(list[5]))
        self.componentType.setCurrentText(list[6])
        self.count.setValue(int(list[7]))
        self.lifeType.setCurrentText(list[8])
        self.lifeTime.setValue(int(list[9]))
        self.toLifeDays.setValue(int(list[10]))
        self.firstMaintainTime.setDate(QDate.fromString(list[11]))
        self.maintainInterval.setValue(int(list[12]))
        self.toMaintainDays.setValue(int(list[13]))
        #print(list)

    def updateButtonEvent(self, queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """

        UserId = getCurrentUserId()
        logger = logToFile()

        # print(self.pre_list)
        ComponentID = self.pre_list[1]
        productID = self.productID.currentText()
        componentNO = self.componentNO.text()
        componentName = self.componentName.text()
        fatherID = self.fatherID.currentText()
        componentType = self.componentType.currentText()
        count = self.count.text()
        liftType = self.lifeType.currentText()
        lifeTime = self.lifeTime.text()
        tolifeDays = self.toLifeDays.text()
        firstMaintainTime = self.firstMaintainTime.text()
        maintainInterval = self.maintainInterval.text()
        toMaintainDays = self.toMaintainDays.text()
        componentID = self.getComponentID()
        if fatherID == "0":
            fatherID = "无父组件"
        # 如果必要的信息都不为空
        if productID == "" or componentNO == "":
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "UPDATE T_ProductComponent_New SET (productID, componentNO, componentName, fatherID, componentType, count, lifeType,lifeTime, tolifeDays, firstMaintainTime, maintainInterval, toMaintainDays) = ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') WHERE ComponentID = '%s'"\
              % (productID, componentNO, componentName, fatherID, componentType, count, liftType, lifeTime, tolifeDays, firstMaintainTime, maintainInterval, toMaintainDays, ComponentID)
        # print(sql)
        # update_sql = "UPDATE T_Product_New SET (ProductNO, ProductName, BatchNO, Receiver, ReceiverDate, ReceiverCompany, Registerer, RegisterDate, RegisterCompany, InitCount, Count, StorePlace, LifeType, LifeTime, ToLifeDays, FirstMaintainTime, ToMaintainDays, MaintainInterval, Document) = " \
        #              "('%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s','%s') WHERE ProductID = '%s'" % \
        #              (productNO, productName, batchNO, receiver, receiverDate, receiverCompany, registerer, registerDate, registerCompany, initCount, count, storePlace, lifeType, lifeTime, toliftDays, firstMaintainTime, toMaintainDays, maintainInterval, document, productID)

        self.query.exec(sql)
        self.db.commit()
        logger.info("用户：" + str(UserId) + " 修改了 T_ProductComponent_New 表的数据，新数据为：[" + str(componentID) + "," + str(productID) + "," +str(componentNO) + "," + str(componentName) + "," + str(fatherID) + "," + str(componentType) + "," + str(count) + "," + str(liftType) + "," + str(lifeTime) + "," + str(tolifeDays)+ "," + str(firstMaintainTime) + "," + str(maintainInterval) + "," + str(toMaintainDays) + "]")
        confirm = QMessageBox.information(QDialog(), "提示", "产品更改成功！", QMessageBox.Yes, QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            self.dialog.close()
