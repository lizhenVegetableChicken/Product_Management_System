# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddOutStorageTest.ui'
# 许帅
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QWidget, QDialogButtonBox

from Login_recorder import getCurrentUserId, logToFile
from Utils import openDB


class AddOutStorage(object):

    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(726, 781)
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.outNO = QtWidgets.QLineEdit(Dialog)
        self.outNO.setObjectName("outNO")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.outNO)
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.productID = QtWidgets.QComboBox(Dialog)
        self.productID.setObjectName("productID")
        self.productID.addItem("下拉选择产品编号")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.productID)
        self.iDLabel = QtWidgets.QLabel(Dialog)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.usedDepartmentNO = QtWidgets.QLineEdit(Dialog)
        self.usedDepartmentNO.setEnabled(True)
        self.usedDepartmentNO.setObjectName("usedDepartmentNO")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.usedDepartmentNO)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.usedID = QtWidgets.QLineEdit(Dialog)
        self.usedID.setObjectName("usedID")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.usedID)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.outDate = QtWidgets.QDateTimeEdit(Dialog)
        self.outDate.setObjectName("outDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.outDate)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.outStorageNo = QtWidgets.QLineEdit(Dialog)
        self.outStorageNo.setEnabled(True)
        self.outStorageNo.setObjectName("outStorageNo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.outStorageNo)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.outCount = QtWidgets.QSpinBox(Dialog)
        self.outCount.setObjectName("outCount")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.outCount)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.isReturn = QtWidgets.QComboBox(Dialog)
        self.isReturn.setObjectName("isReturn")
        self.isReturn.addItem("")
        self.isReturn.addItem("")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.isReturn)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.outRecorderPersonNO = QtWidgets.QLineEdit(Dialog)
        self.outRecorderPersonNO.setObjectName("outRecorderPersonNO")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.outRecorderPersonNO)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.outTechState = QtWidgets.QLineEdit(Dialog)
        self.outTechState.setEnabled(True)
        self.outTechState.setObjectName("outTechState")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.outTechState)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.outReason = QtWidgets.QLineEdit(Dialog)
        self.outReason.setObjectName("outReason")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.outReason)
        self.Label_13 = QtWidgets.QLabel(Dialog)
        self.Label_13.setObjectName("Label_13")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Label_13)
        self.createTime = QtWidgets.QDateTimeEdit(Dialog)
        self.createTime.setMouseTracking(True)
        self.createTime.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createTime.setAcceptDrops(True)
        self.createTime.setAutoFillBackground(True)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setEnabled(True)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "出库信息录入"))
        self.label.setText(_translate("Dialog", "出库信息录入"))
        self.label_2.setText(_translate("Dialog", "出库编号:"))
        self.Label.setText(_translate("Dialog", "产品编号："))
        self.iDLabel.setText(_translate("Dialog", "使用部门:"))
        self.label_5.setText(_translate("Dialog", "使  用  人:"))
        self.label_3.setText(_translate("Dialog", "出库日期:"))
        self.Label_2.setText(_translate("Dialog", "出库库房:"))
        self.label_9.setText(_translate("Dialog", "出库数量:"))
        self.label_4.setText(_translate("Dialog", "是否归还:"))
        self.isReturn.setItemText(0, _translate("Dialog", "否"))
        self.isReturn.setItemText(1, _translate("Dialog", "是"))
        self.label_10.setText(_translate("Dialog", "登  记  人:"))
        self.Label_4.setText(_translate("Dialog", "技术状态:"))
        self.label_6.setText(_translate("Dialog", "出库原因:"))
        self.Label_13.setText(_translate("Dialog", "创建时间:"))
        self.Label_12.setText(_translate("Dialog", "备       注："))
        self.createTime.setDateTime(QDateTime.currentDateTime())
        self.createTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        # 设置出库日期
        self.outDate.setDateTime(QDateTime.currentDateTime())
        self.outDate.setDisplayFormat("yyyy-MM-dd")
        # 设置出库编号(日期+三位流水号)
        self.outNO.setText(self.getOutNO())
        # 设置记录人ID
        self.outRecorderPersonNO.setText(str(getCurrentUserId()))
        # 提交和取消按钮点击事件
        cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)
        ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        cancel_button.setText("取消")
        ok_button.setText("提交")
        # 获取所有的productID
        self.get_product_NO()
        # 获取产品数量并设置校验的槽函数
        self.productID.currentTextChanged.connect(self.get_count)
        # 提交的槽函数
        ok_button.clicked.connect(self.ok_fun)
        # 取消的槽函数
        cancel_button.clicked.connect(self.cancel_fun)
        # 获取所有的产品编号

    def get_product_NO(self):
        db = openDB()
        q = QSqlQuery()
        sql = "SELECT ProductID FROM T_Product_New"
        q.exec(sql)
        while q.next():
            self.productID.addItem(str(q.value(0)))
        db.close()

    def getOutNO(self):
        max_no = ''
        db = openDB()
        q = QSqlQuery()
        date_str = QDate.currentDate().toString("yyyyMMdd")
        sql = "SELECT OutNO FROM T_Out_Base WHERE ID=(SELECT MAX(ID) FROM T_Out_Base)"
        if q.exec(sql):
            while q.next():
                max_no = q.value(0)
        db.close()
        if date_str > max_no[1:9]:
            return 'C' + date_str + '001'
        else:
            return 'C' + str(int(max_no[1:]) + 1)

    def get_count(self):
        global count
        db = openDB()
        q = QSqlQuery()
        sql = "SELECT Count FROM T_Product_New where productID='%s'" % self.productID.currentText()
        q.exec(sql)
        if q.next():
            count = int(q.value(0))
            self.outCount.setValue(count)
            self.outCount.setRange(0, count)
        else:
            QMessageBox.information(QDialog(), "错误", "产品编号输入错误,请重新输入", QMessageBox.Yes, QMessageBox.Yes)
        db.close()

    # 处理提交事件
    def ok_fun(self):
        logger = logToFile()
        UserId = getCurrentUserId()
        if all([self.outNO.text(),
                self.outDate.text(),
                self.usedID.text(),
                self.usedDepartmentNO.text(),
                self.outRecorderPersonNO.text(),
                self.outReason.text(),
                self.createTime.text(),
                self.remark.toPlainText(),
                self.productID.currentText(),
                self.outStorageNo.text(),
                self.outTechState.text(),
                self.isReturn.currentText(),
                self.createTime.text(),
                self.remark.toPlainText(),
                self.outCount.value()]):
            db = openDB()
            q = QSqlQuery()
            insert_sql = "INSERT INTO T_Out_Base(outno, outdate, usedid, useddepartmentid, recorderid, outreason, " \
                         "createid, createtime, updateid, updatetime, remark) VALUES ('%s','%s','%s','%s','%s','%s'," \
                         "'%s','%s','%s','%s','%s')" % \
                         (self.outNO.text(), self.outDate.text(), self.usedID.text(),
                          self.usedDepartmentNO.text(), self.outRecorderPersonNO.text(), self.outReason.text(),
                          1, self.createTime.text(), 0, self.createTime.text(), self.remark.toPlainText())
            q.exec(insert_sql)
            db.commit()
            insert_sql = "INSERT INTO T_Out_Detail(outno, ProductID, outstorageno, outtechstate, isreturn, createid, " \
                         "createtime, updateid, updatetime, remark,OutCount)VALUES ('%s','%s','%s','%s','%s','%s'," \
                         "'%s','%s','%s','%s','%s')" % \
                         (self.outNO.text(), self.productID.currentText(), self.outStorageNo.text(),
                          self.outTechState.text(), self.isReturn.currentText(), 1, self.createTime.text(),
                          0, self.createTime.text(), self.remark.toPlainText(), str(self.outCount.value()))
            q.exec(insert_sql)
            db.commit()
            logger.info("用户：" + str(
                UserId) + " 新建了一条产品出库基础信息" + "新数据为：[" + self.outNO.text() + " ," + self.outDate.text() + " ," +
                        self.usedID.text() + " ," + self.usedDepartmentNO.text() + " ," + self.outRecorderPersonNO.text() + " ," + self.outReason.text() +
                        " ," + str(UserId) + " ," + self.createTime.text() + " ," + str(
                UserId) + " ," + self.createTime.text() + " ," + self.remark.toPlainText() + "]")
            update_sql = "UPDATE T_Product_New SET Count='%s' WHERE productID='%s'" % (
                count - int(self.outCount.value()), self.productID.currentText())
            q.exec(update_sql)
            db.commit()
            logger.info("用户：" + str(UserId) + " 新建了一条产品出库详细信息" + "新数据为：["
                        + self.outNO.text() + " ," + self.productID.currentText() + " ," +
                        self.outStorageNo.text() + " ," + self.outTechState.text() + " ," +
                        self.isReturn.currentText() + " ," + str(UserId) + " ," +
                        self.createTime.text() + " ," + str(UserId) + " ," + self.createTime.text() +
                        " ," + self.remark.toPlainText() + " ," + str(self.outCount.value()) + "]")
            db.close()
            confirm = QMessageBox.information(QDialog(), "提示", "出库信息新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()
        else:
            logger.info("用户：" + str(UserId) + " 出库信息新建失败（重要数据输入值为空）")
            QMessageBox.information(QDialog(), "错误", "输入值不能为0或为空,请重新检查输入！", QMessageBox.Yes, QMessageBox.Yes)

    def cancel_fun(self):
        self.dialog.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../Images/MainWindow_1.png"))
    form = QWidget()
    w = AddOutStorage()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
