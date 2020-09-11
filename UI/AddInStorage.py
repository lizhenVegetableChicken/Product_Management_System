# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddInStorageTest.ui'
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
from PyQt5.QtWidgets import QDialogButtonBox, QMessageBox, QDialog, QApplication, QWidget

from Login_recorder import getCurrentUserId, logToFile
from Utils import openDB


class AddInStorage(object):

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
        self.inNO = QtWidgets.QLineEdit(Dialog)
        self.inNO.setObjectName("inNO")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inNO)
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
        self.outNO = QtWidgets.QLineEdit(Dialog)
        self.outNO.setEnabled(True)
        self.outNO.setObjectName("outNO")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.outNO)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.inDate = QtWidgets.QDateTimeEdit(Dialog)
        self.inDate.setObjectName("inDate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inDate)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.inStorageNo = QtWidgets.QLineEdit(Dialog)
        self.inStorageNo.setEnabled(True)
        self.inStorageNo.setObjectName("inStorageNo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inStorageNo)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.inRecorderPerson = QtWidgets.QLineEdit(Dialog)
        self.inRecorderPerson.setEnabled(True)
        self.inRecorderPerson.setObjectName("inRecorderPerson")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.inRecorderPerson)
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
        self.createTime.setMouseTracking(True)
        self.createTime.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createTime.setAcceptDrops(True)
        self.createTime.setAutoFillBackground(True)
        self.createTime.setObjectName("createTime")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.createTime)
        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setEnabled(True)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.remark)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.isUsed = QtWidgets.QComboBox(Dialog)
        self.isUsed.setObjectName("isUsed")
        self.isUsed.addItem("")
        self.isUsed.addItem("")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.isUsed)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
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
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "入库信息录入"))
        self.label.setText(_translate("Dialog", "入库信息录入"))
        self.label_2.setText(_translate("Dialog", "入库编号:"))
        self.Label.setText(_translate("Dialog", "产品编号:"))
        self.iDLabel.setText(_translate("Dialog", "出库编号:"))
        self.label_3.setText(_translate("Dialog", "入库日期:"))
        self.Label_2.setText(_translate("Dialog", "入库库房:"))
        self.Label_3.setText(_translate("Dialog", "入  库  人:"))
        self.Label_4.setText(_translate("Dialog", "技术状态:"))
        self.Label_13.setText(_translate("Dialog", "创建时间:"))
        self.Label_12.setText(_translate("Dialog", "备       注："))
        self.label_4.setText(_translate("Dialog", "是否用过:"))
        self.isUsed.setItemText(0, _translate("Dialog", "是"))
        self.isUsed.setItemText(1, _translate("Dialog", "否"))
        self.label_6.setText(_translate("Dialog", "入库数量:"))
        self.outNO.setDisabled(True)
        self.createTime.setDisabled(True)

        # 设置创建时间
        self.createTime.setDateTime(QDateTime.currentDateTime())
        self.createTime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        # 设置入库日期
        self.inDate.setDateTime(QDateTime.currentDateTime())
        self.inDate.setDisplayFormat("yyyy-MM-dd")
        # 设置入库编号(日期+三位流水号)
        self.inNO.setText(self.getInNO())
        # 设置登记人ID
        self.inRecorderPerson.setText(str(getCurrentUserId()))
        # 提交和取消按钮点击事件
        cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)
        ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        cancel_button.setText("取消")
        ok_button.setText("提交")
        # 获取所有的产品编号
        self.get_product_NO()
        # 设置productID的完成编辑信号和获取数据库中出库编号的槽函数
        self.productID.currentTextChanged.connect(self.getOutNO)
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
        sql = "SELECT ProductID FROM T_Out_Detail where IsReturn='否'"
        q.exec(sql)
        while q.next():
            self.productID.addItem(str(q.value(0)))
        db.close()

    # 获取出库编号
    def getOutNO(self):
        global out_no
        db = openDB()
        q = QSqlQuery()
        if self.productID.hasFocus():
            product_no = self.productID.currentText()
            sql_code = "SELECT OutNO FROM T_Out_Detail WHERE ProductID='%s' AND IsReturn='否'" % product_no
            q.exec(sql_code)
            if q.next():
                out_no = q.value(0)
                self.outNO.setText(out_no)
            else:
                QMessageBox.information(QDialog(), "错误", "产品编号输入错误,请重新输入", QMessageBox.Yes, QMessageBox.Yes)
            db.close()

    # 获取入库编号
    def getInNO(self):
        max_no = ''
        db = openDB()
        q = QSqlQuery()
        date_str = QDate.currentDate().toString("yyyyMMdd")
        sql = "SELECT InNO FROM T_In_Base WHERE ID=(SELECT MAX(ID) FROM T_In_Base)"
        if q.exec(sql):
            while q.next():
                max_no = q.value(0)
        db.close()
        if date_str > max_no[1:9]:
            return 'R' + date_str + '001'
        else:
            return 'R' + str(int(max_no[1:]) + 1)

    # 获取数量
    def get_count(self):
        global out_count
        db = openDB()
        q = QSqlQuery()
        if not self.outNO.hasFocus():
            sql = "SELECT OutCount FROM T_Out_Detail where OutNO='%s'" % self.outNO.text()
            q.exec(sql)
            if q.next():
                out_count = int(q.value(0))
                self.inCount.setValue(out_count)
                self.inCount.setRange(0, out_count)
            else:
                QMessageBox.information(QDialog(), "错误", "出库编号输入错误,请重新输入", QMessageBox.Yes, QMessageBox.Yes)
                self.outNO.setFocus()
                self.outNO.clear()
        db.close()

    # 处理提交事件
    def ok_fun(self):
        logger = logToFile()
        UserId = getCurrentUserId()
        db = openDB()
        q = QSqlQuery()

        inNO = self.inNO.text()
        outNO = self.outNO.text()
        inDate = self.inDate.text()
        inRecorderPerson = self.inRecorderPerson.text()
        createTime = self.createTime.text()
        remark = self.remark.toPlainText()
        productID = self.productID.currentText()
        inStorageNo = self.inStorageNo.text()
        inTechState = self.inTechState.text()
        isUsed = self.isUsed.currentText()
        createTime = self.createTime.text()
        inCount = self.inCount.value()


        # 判断所有值均不为空
        if all([self.inNO.text(),
                self.outNO.text(),
                self.inDate.text(),
                self.inRecorderPerson.text(),
                self.createTime.text(),
                self.remark.toPlainText(),
                self.productID.currentText(),
                self.inStorageNo.text(),
                self.inTechState.text(),
                self.isUsed.currentText(),
                self.createTime.text(),
                self.inCount.value()]):
            insert_sql = "INSERT INTO T_In_Base(InNO, OUTNO, INDATE, INRECODER, CREATEID, CREATETIME, UPDATEID, " \
                         "UPDATETIME, REMARK) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                         (inNO, outNO, inDate,
                         inRecorderPerson, UserId, createTime,
                          UserId, createTime, remark)
            # print(insert_sql)
            q.exec(insert_sql)
            # print(1111)
            db.commit()

            logger.info("用户：" + str(UserId) + " 新建了一条产品入库基础信息" + "新数据为：[" +
                        self.inNO.text() + " ," + self.outNO.text() + " ," + self.inDate.text() + " ," +
                        self.inRecorderPerson.text() + " ," + str(UserId) + " ," + self.createTime.text() + " ," +
                        str(UserId) + " ," + self.createTime.text() + " ," + self.remark.toPlainText() + "]")
            insert_sql = "INSERT INTO T_In_Detail(InNO,ProductID, InStorageNO, InTechState, IsUsed, " \
                         "CreateID,CreateTime, UpdateID, UpdateTime, Remark,InCount)VALUES ('%s','%s','%s','%s','%s'," \
                         "'%s','%s','%s','%s','%s','%s')" % \
                         (inNO, productID, inStorageNo,
                          inTechState, isUsed, UserId, createTime,
                          UserId, createTime, remark, inCount)
            q.exec(insert_sql)
            db.commit()
            # print("ok2")
            logger.info("用户：" + str(UserId) + " 与此同时！新建了一条产品入库详细信息" + "新数据为：["
                        + inNO + " ," + productID + " ," +
                        inStorageNo + " ," + inTechState + " ," +
                        isUsed + " ," + str(UserId) + " ," +
                        createTime + " ," + str(UserId) + " ," + createTime +
                        " ," + remark + " ," + str(inCount) + "]")
            # print("ok")
            update_sql = "UPDATE T_Product_New SET Count=Count+'%s' WHERE productID='%s'" \
                         % (int(inCount), productID)
            logger.info("用户：" + str(UserId) + " 与此同时！新增了与产品入库相关的产品库存信息(位置在产品表)" + "修改的库存产品编号为：" + self.productID.currentText() +"，增加了" + self.inCount.text() + "的库存")
            q.exec(update_sql)
            db.commit()
            if int(out_count) == int(self.inCount.value()):
                update_sql = "UPDATE T_Out_Detail SET IsReturn='是'where OutNO='%s'" % out_no
                q.exec(update_sql)
                db.commit()
            db.close()
            confirm = QMessageBox.information(QDialog(), "提示", "入库信息新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()
        else:
            QMessageBox.information(QDialog(), "错误", "输入值不能为0或为空,请重新检查输入！", QMessageBox.Yes, QMessageBox.Yes)

    def cancel_fun(self):
        self.dialog.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../Images/MainWindow_1.png"))
    form = QWidget()
    w = AddInStorage()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
