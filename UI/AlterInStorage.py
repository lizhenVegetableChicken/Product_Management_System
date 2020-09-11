# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlterInStorageTest.ui'
# 许帅
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys
from _datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog, QDialogButtonBox, QWidget, QApplication

from AddInStorage import AddInStorage
from Login_recorder import getCurrentUserId, logToFile
from Utils import openDB


class AlterInStorage(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(726, 823)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(50, 20, 50, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.inNO = QtWidgets.QLineEdit(Dialog)
        self.inNO.setEnabled(True)
        self.inNO.setObjectName("inNO")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inNO)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.productID = QtWidgets.QComboBox(Dialog)
        self.productID.setObjectName("productID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.productID)
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.outNO = QtWidgets.QLineEdit(Dialog)
        self.outNO.setEnabled(True)
        self.outNO.setObjectName("outNO")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.outNO)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.inDate = QtWidgets.QDateTimeEdit(Dialog)
        self.inDate.setEnabled(True)
        self.inDate.setObjectName("inDate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inDate)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.inStorageNo = QtWidgets.QLineEdit(Dialog)
        self.inStorageNo.setEnabled(True)
        self.inStorageNo.setObjectName("inStorageNo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inStorageNo)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.isUsed = QtWidgets.QComboBox(Dialog)
        self.isUsed.setEnabled(True)
        self.isUsed.setObjectName("isUsed")
        self.isUsed.addItem("")
        self.isUsed.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.isUsed)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.inRecorderPerson = QtWidgets.QLineEdit(Dialog)
        self.inRecorderPerson.setEnabled(True)
        self.inRecorderPerson.setObjectName("inRecorderPerson")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.inRecorderPerson)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.inTechState = QtWidgets.QLineEdit(Dialog)
        self.inTechState.setEnabled(True)
        self.inTechState.setObjectName("inTechState")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.inTechState)
        self.Label_13 = QtWidgets.QLabel(Dialog)
        self.Label_13.setObjectName("Label_13")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.Label_13)
        self.createTime = QtWidgets.QDateTimeEdit(Dialog)
        self.createTime.setEnabled(True)
        self.createTime.setMouseTracking(True)
        self.createTime.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createTime.setAcceptDrops(True)
        self.createTime.setAutoFillBackground(True)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.updateTime = QtWidgets.QDateTimeEdit(Dialog)
        self.updateTime.setEnabled(True)
        self.updateTime.setObjectName("updateTime")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.updateTime)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.updateID = QtWidgets.QLineEdit(Dialog)
        self.updateID.setEnabled(True)
        self.updateID.setObjectName("updateID")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.updateID)
        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setEnabled(True)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.inCount = QtWidgets.QSpinBox(Dialog)
        self.inCount.setObjectName("inCount")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.inCount)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "入库信息修改"))
        self.label.setText(_translate("Dialog", "入库信息修改"))
        self.label_10.setText(_translate("Dialog", "入库编号:"))
        self.label_2.setText(_translate("Dialog", "产品编号:"))
        self.Label.setText(_translate("Dialog", "入库编号:"))
        self.label_3.setText(_translate("Dialog", "入库日期:"))
        self.Label_2.setText(_translate("Dialog", "入库库房:"))
        self.label_4.setText(_translate("Dialog", "是否用过:"))
        self.isUsed.setItemText(0, _translate("Dialog", "是"))
        self.isUsed.setItemText(1, _translate("Dialog", "否"))
        self.Label_3.setText(_translate("Dialog", "登  记  人:"))
        self.Label_4.setText(_translate("Dialog", "技术状态:"))
        self.Label_13.setText(_translate("Dialog", "创建时间:"))
        self.label_7.setText(_translate("Dialog", "更新时间:"))
        self.label_8.setText(_translate("Dialog", "更  新  人:"))
        self.Label_12.setText(_translate("Dialog", "备       注："))
        self.label_6.setText(_translate("Dialog", "入库数量:"))


        cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)
        ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        cancel_button.setText("取消")
        ok_button.setText("修改")
        ok_button.clicked.connect(self.ok_fun)
        cancel_button.clicked.connect(self.cancel_fun)

    def updateData(self, list, queryModel):
        """
        修改入库信息
        :param list:
        :return:
        """
        self.productID.addItem(list[1])
        # 获取所有的productID
        AddInStorage.get_product_NO(self)
        self.inStorageNo.setText(list[2])
        self.inTechState.setText(list[4])
        self.isUsed.setItemText(0, list[5])
        self.updateID.setText(getCurrentUserId())
        self.createTime.setDateTime(datetime.strptime(list[7], "%Y-%m-%d %H:%M:%S"))
        self.createTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.updateTime.setDateTime(QDateTime.currentDateTime())
        self.updateTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.remark.setText(list[10])
        self.inNO.setText(str(list[11]))
        global in_count
        in_count = int(list[12])
        self.inCount.setRange(0, in_count)
        self.inCount.setValue(in_count)
        db = openDB()
        query = QSqlQuery()
        sql = "SELECT * FROM T_In_Base where InNO='%s'" % self.inNO.text()
        query.exec(sql)
        if query.next():
            self.outNO.setText(query.value(2))
            self.inDate.setDateTime(datetime.strptime(query.value(3), "%Y-%m-%d"))
            self.inDate.setDisplayFormat("yyyy-MM-dd")
            self.inRecorderPerson.setText(query.value(4))
            db.close()

    def ok_fun(self):
        logger = logToFile()
        UserId = getCurrentUserId()
        verify_values = [self.inNO.text(),
                         self.outNO.text(),
                         self.inDate.text(),
                         self.inRecorderPerson.text(),
                         self.remark.toPlainText(),
                         self.productID.currentText(),
                         self.inStorageNo.text(),
                         self.inTechState.text(),
                         self.isUsed.currentText(),
                         self.createTime.text(),
                         self.updateTime.text(),
                         self.updateID.text(),
                         str(self.inCount.value())]
        flag = True
        for value in verify_values:
            if value == ' ' or value == '0' or value == '':
                flag = False
        if flag:
            db = openDB()
            q = QSqlQuery()
            sql = "UPDATE T_In_Base SET  OutNO='%s', InRecoder='%s', CreateTime='%s', " \
                  "UpdateID='%s', UpdateTime='%s', Remark='%s'WHERE OutNO='%s'" \
                  % (self.outNO.text(), self.inRecorderPerson.text(), self.createTime.text(),
                     self.updateID.text(), self.updateTime.text(),
                     self.remark.toPlainText(), self.inNO.text())
            q.exec(sql)
            db.commit()
            logger.info("用户：" + str(UserId) + " 更新了产品入库基本信息表的数据，更新的数据为：[" + self.outNO.text() + "," +
                        self.inRecorderPerson.text() + "," + self.createTime.text() + "," + self.updateID.text() + "," +
                        self.updateTime.text() + "," + self.outNO.text() + "]")
            sql = "UPDATE T_In_Detail SET ProductID='%s', InStorageNO='%s', InTechState='%s', " \
                  "IsUsed='%s', createtime='%s', UpdateID='%s', updatetime='%s', remark='%s',InCount='%s'" \
                  "WHERE InNO='%s'" \
                  % (self.productID.currentText(), self.inStorageNo.text(), self.inTechState.text(),
                     self.isUsed.currentText(), self.createTime.text(), self.updateID.text(),
                     self.updateTime.text(), self.remark.toPlainText(), str(self.inCount.value()),
                     self.inNO.text())
            q.exec(sql)
            db.commit()
            logger.info("用户：" + str(UserId) + " 更新了产品入库详细信息表的数据，更新后的数据为：[" + self.productID.currentText() + "," +
                        self.inStorageNo.text() + "," + self.inTechState.text() + "," + self.isUsed.currentText() + "," +
                        self.createTime.text() + "," + self.updateID.text() + "," + self.updateTime.text() + "," + self.remark.toPlainText() +
                        "," + str(self.inCount.value()) + "]")
            sql = "UPDATE T_Product_New SET Count=Count+'%s' WHERE productID='%s'" % \
                  (int(self.inCount.value()) - in_count, self.productID.currentText())
            q.exec(sql)
            db.commit()
            db.close()
            confirm = QMessageBox.information(QDialog(), "提示", "入库信息修改成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()
        else:
            logger.info("用户：" + str(UserId) + " 入库信息更新失败（重要数据输入值不符合规范）")
            QMessageBox.information(QDialog(), "错误", "输入值不能为0或为空,请重新检查输入！", QMessageBox.Yes, QMessageBox.Yes)

    def cancel_fun(self):
        self.dialog.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../Images/MainWindow_1.png"))
    form = QWidget()
    w = AlterInStorage()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
