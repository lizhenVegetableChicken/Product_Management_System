# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addProductBatchView_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDialog, QFileDialog

from Utils import openDB


class AddProductBatchWidget(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(770, 800)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(50, 20, 50, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.batchNO = QtWidgets.QLineEdit(Dialog)
        self.batchNO.setObjectName("batchNO")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.batchNO)
        self.iDLabel = QtWidgets.QLabel(Dialog)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.productID = QtWidgets.QLineEdit(Dialog)
        self.productID.setObjectName("ProductID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.productID)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.deliverCompany = QtWidgets.QLineEdit(Dialog)
        self.deliverCompany.setObjectName("deliverCompany")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.deliverCompany)
        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.deliverer = QtWidgets.QLineEdit(Dialog)
        self.deliverer.setObjectName("deliverer")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.deliverer)
        self.Label_13 = QtWidgets.QLabel(Dialog)
        self.Label_13.setObjectName("Label_13")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_13)
        self.deliverDate = QtWidgets.QLineEdit(Dialog)
        self.deliverDate.setObjectName("deliverDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.deliverDate)
        self.Label_6 = QtWidgets.QLabel(Dialog)
        self.Label_6.setObjectName("Label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.receiveCompany = QtWidgets.QLineEdit(Dialog)
        self.receiveCompany.setObjectName("receiveCompany")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.receiveCompany)
        self.Label_7 = QtWidgets.QLabel(Dialog)
        self.Label_7.setObjectName("Label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_7)
        self.receiver = QtWidgets.QLineEdit(Dialog)
        self.receiver.setObjectName("receiver")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.receiver)
        self.Label_8 = QtWidgets.QLabel(Dialog)
        self.Label_8.setObjectName("Label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_8)
        self.createID = QtWidgets.QLineEdit(Dialog)
        self.createID.setObjectName("createID")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.createID)
        self.Label_9 = QtWidgets.QLabel(Dialog)
        self.Label_9.setObjectName("Label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Label_9)
        self.createTime = QtWidgets.QLineEdit(Dialog)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.Label_10 = QtWidgets.QLabel(Dialog)
        self.Label_10.setObjectName("Label_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.Label_10)
        self.updateID = QtWidgets.QLineEdit(Dialog)
        self.updateID.setObjectName("updateID")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.updateID)
        self.Label_11 = QtWidgets.QLabel(Dialog)
        self.Label_11.setObjectName("Label_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.Label_11)
        self.updateTime = QtWidgets.QLineEdit(Dialog)
        self.updateTime.setObjectName("updateTime")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.updateTime)
        self.Label_14 = QtWidgets.QLabel(Dialog)
        self.Label_14.setObjectName("Label_14")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Label_14)
        self.documentPathButton = QtWidgets.QPushButton(Dialog)
        self.documentPathButton.setObjectName("documentPathButton")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.documentPathButton)
        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Dialog)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.createID.setText("--")
        self.createTime.setText("--")
        self.updateTime.setText("--")
        self.updateID.setText("--")
        self.createID.setEnabled(False)
        self.createTime.setEnabled(False)
        self.updateTime.setEnabled(False)
        self.updateID.setEnabled(False)
        # hsj
        self.bindButton(Dialog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新增产品批次"))
        self.Label.setText(_translate("Dialog", "批次号："))
        self.iDLabel.setText(_translate("Dialog", "产品ID："))
        self.Label_4.setText(_translate("Dialog", "交付单位:"))
        self.Label_5.setText(_translate("Dialog", "交付人员："))
        self.Label_13.setText(_translate("Dialog", "交付日期："))
        self.Label_6.setText(_translate("Dialog", "接收单位："))
        self.Label_7.setText(_translate("Dialog", "接收人员："))
        self.Label_8.setText(_translate("Dialog", "创建人员："))
        self.Label_9.setText(_translate("Dialog", "创建时间："))
        self.Label_10.setText(_translate("Dialog", "修改人员："))
        self.Label_11.setText(_translate("Dialog", "修改时间："))
        self.Label_14.setText(_translate("Dialog", "技术文档："))
        self.documentPathButton.setText(_translate("Dialog", "选择文档"))
        self.Label_12.setText(_translate("Dialog", "备注："))
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))

    def bindButton(self, Dialog):
        """
        hsj 按钮绑定事件
        :param Dialog: 弹窗本身
        :return:
        """
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Dialog))
        self.documentPathButton.clicked.connect(self.documentPathButtonEvent)

    def conserveButtonEvent(self, Dialog):
        """
        hsj 新建批次界面的保存按钮事件
        :return:
        """
        batchNO = self.batchNO.text()
        productID = self.productID.text()
        recorder = self.recorder.text()
        recordDate = self.recordDate.text()
        deliverCompany = self.deliverCompany.text()
        deliverer = self.deliverer.text()
        deliverDate = self.deliverDate.text()
        receiveCompany = self.receiveCompany.text()
        receiver = self.receiver.text()
        createID = self.createID.text()
        createTime = self.createTime.text()
        updateID = self.updateID.text()
        updateTime = self.updateTime.text()
        remark = self.remark.toPlainText()
        documentPath = self.documentPathButton.text()
        # 如果必要的信息都不为空
        if batchNO == "" or productID == "" or recorder == "" or recordDate == "" or deliverCompany == "" or deliverer == "" \
                or deliverDate == "" or receiveCompany == "" or receiver == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(batchNO, productID)
            if num == 0:
                revert_sql = "INSERT INTO T_Product_BatchDetail VALUES ('%s', '--', '%s', '%s', '%s', '%s', '%s', '%s', '--', '%s', '--', '%s', '%s', '%s')" % (
                    self.pre_list[0], self.pre_list[2], self.pre_list[3], self.pre_list[4], self.pre_list[5], self.pre_list[6],
                    self.pre_list[7], self.pre_list[9], self.pre_list[11], self.pre_list[12], self.pre_list[13])
                self.query.exec(revert_sql)
                self.db.commit()
                return
            import time
            createTime = time.strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = "INSERT INTO T_Product_BatchDetail VALUES ('%s', '--', '%s', '%s', '%s', '%s', '%s', '%s', '--', '%s', '--', '--', '%s', '%s')" % (
                batchNO, productID, deliverDate, deliverCompany, deliverer, receiveCompany, receiver, createTime, documentPath, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "批次信息新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                Dialog.close()

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
        queryModel.delete()
        batchNO = self.batchNO.text()
        productID = self.productID.text()
        recorder = self.recorder.text()
        recordDate = self.recordDate.text()
        deliverCompany = self.deliverCompany.text()
        deliverer = self.deliverer.text()
        deliverDate = self.deliverDate.text()
        receiveCompany = self.receiveCompany.text()
        receiver = self.receiver.text()
        createID = self.createID.text()
        createTime = self.createTime.text()
        updateID = self.updateID.text()
        updateTime = self.updateTime.text()
        remark = self.remark.toPlainText()
        documentPath = self.documentPathButton.text()
        # 如果必要的信息都不为空
        if batchNO == "" or productID == "" or recorder == "" or recordDate == "" or deliverCompany == "" or deliverer == "" \
                or deliverDate == "" or receiveCompany == "" or receiver == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，修改失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(batchNO, productID)
            if num == 0:
                return
            import time
            updateTime = time.strftime("%Y-%m-%d %H:%M:%S")
            insert_sql = "INSERT INTO T_Product_BatchDetail VALUES ('%s', '--', '%s', '%s', '%s', '%s', '%s', '%s', '--', '%s', '--', '%s', '%s', '%s')" % (
                batchNO, productID, deliverDate, deliverCompany, deliverer, receiveCompany, receiver, createTime, updateTime, documentPath, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "批次信息更新成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()


    def documentPathButtonEvent(self):
        filePath, _ = QFileDialog.getOpenFileName(caption="选择文件", filter="PDF文件 (*.pdf);Word文件 (*.doc;*.docx)")
        self.documentPathButton.setText(filePath)
        self.documentPathButton.setDisabled(True)

    def checkOn(self, batchNO, productID):
        """
        检查批次号和产品号是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM T_Product_BatchDetail WHERE batchNO = '%s'" % batchNO
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.warning(QDialog(), "警告", "批次编号已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        # 如果产品编号不存在，则提示不能保存
        sql = "SELECT * FROM T_Product WHERE productNO = '%s'" % productID
        self.query.exec(sql)
        if not self.query.next():
            print(QMessageBox.warning(QDialog(), "警告", "产品不存在，请检查后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        self.pre_list = list
        self.label.setText("修改批次信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda :self.updateButtonEvent(queryModel))
        self.batchNO.setText(list[0])
        self.productID.setText(list[1])
        self.deliverDate.setText(list[2])
        self.deliverCompany.setText(list[3])
        self.deliverer.setText(list[4])
        self.receiveCompany.setText(list[5])
        self.receiver.setText(list[6])

        self.createID.setText(list[7])
        self.createTime.setText(list[8])
        self.updateID.setText(list[9])
        self.updateTime.setText(list[10])
        self.remark.setText(list[11])
        self.documentPathButton.setText(list[12])

    def showData(self, list, queryModel):
        self.updateData(list, queryModel)
        self.label.setText("详细批次信息")
        self.batchNO.setDisabled(True)
        self.productID.setDisabled(True)
        self.deliverDate.setDisabled(True)
        self.deliverCompany.setDisabled(True)
        self.deliverer.setDisabled(True)
        self.receiveCompany.setDisabled(True)
        self.receiver.setDisabled(True)

        self.createID.setDisabled(True)
        self.createTime.setDisabled(True)
        self.updateID.setDisabled(True)
        self.updateTime.setDisabled(True)
        self.remark.setDisabled(True)
        self.documentPathButton.setDisabled(True)
        self.conserveButton.setVisible(False)
        self.cancelButton.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QWidget()
    w = AddProductBatchWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())