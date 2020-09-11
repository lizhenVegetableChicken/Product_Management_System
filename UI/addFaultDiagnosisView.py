# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addProductBatchView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
# 薛程耀
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDialog

from Utils import openDB


class AddFaultDiagnosisWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(792, 779)
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
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
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

        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.FaultType = QtWidgets.QLineEdit(Dialog)
        self.FaultType.setObjectName("FaultType")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.FaultType)
        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.FaultName = QtWidgets.QLineEdit(Dialog)
        self.FaultName.setObjectName("FaultName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.FaultName)

        self.Label_12 = QtWidgets.QLabel(Dialog)
        self.Label_12.setObjectName("Label_12")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setObjectName("remark")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.remark)

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



        # hsj
        self.bindButton(Dialog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新建故障信息"))
        self.Label.setText(_translate("Dialog", "序号："))

        self.Label_4.setText(_translate("Dialog", "故障类型:"))
        self.Label_5.setText(_translate("Dialog", "故障名称："))

        # self.Label_6.setText(_translate("Dialog", "故障诊断流程："))

        self.Label_12.setText(_translate("Dialog", "备注："))
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))




    def bindButton(self, Dialog):
        """
        按钮绑定事件
        :param Dialog: 弹窗本身
        :return:
        """
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Dialog))

    def conserveButtonEvent(self, Dialog):
        """
        hsj 新建故障界面的保存按钮事件
        :return:
        """
        batchNO = self.batchNO.text()
        FaultType = self.FaultType.text()
        FaultName = self.FaultName.text()

        remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if batchNO == "" or FaultType == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(batchNO)
            if num == 0:
                return

            insert_sql = "INSERT INTO T_Fault_Diagnosis VALUES ('%s','%s','%s','%s')" % \
                         ( batchNO,  FaultType, FaultName, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "故障信息新建成功！", QMessageBox.Yes, QMessageBox.Yes)
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
        FaultType = self.FaultType.text()
        FaultName = self.FaultName.text()

        remark = self.remark.toPlainText()


        # 如果必要的信息都不为空
        if batchNO == "" or FaultType == "" or FaultName == "":
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，修改失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(batchNO)
            if num == 0:
                return

            insert_sql = "INSERT INTO T_Fault_Diagnosis VALUES ('%s','%s','%s','%s')" % \
                         (batchNO, FaultType, FaultName, remark)
            self.query.exec(insert_sql)
            self.db.commit()
            confirm = QMessageBox.information(QDialog(), "提示", "批次信息更新成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()

    def checkOn(self, batchNO):
        """
        检查批次号和产品号是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM T_Fault_Diagnosis WHERE BatchNO = '%s'" % batchNO
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.warning(QDialog(), "警告", "批次编号已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        self.query.exec(sql)

        return 1

    def updateData(self, list, queryModel):
        """
        修改产品故障诊断信息
        :param list:
        :return:
        """
        self.label.setText("修改产品故障诊断信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda: self.updateButtonEvent(queryModel))

        self.batchNO.setText(list[0])
        self.FaultType.setText(list[1])
        self.FaultName.setText(list[2])

        self.remark.setText(list[4])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = AddFaultDiagnosisWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
