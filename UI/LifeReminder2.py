# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LifeReminder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
# 俞欣
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableView, QHeaderView, QApplication, QWidget

from SearchView import MySearchWidget
from UI.MySearchBatchModelPIM import CheckBoxHeader, MySearchTableModelPIM
from Utils import openDB


class LifeReminder2(MySearchWidget):
    def __init__(self):
        super(LifeReminder2, self).__init__()
        self.select_conditions = "ProductName"

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1009, 696)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")

        spacerItem = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.searchEdit = QtWidgets.QLineEdit(Dialog)
        self.searchEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.searchEdit.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 中间手动代码部分 表格UI构建
        self.db = openDB()
        self.tableView = QTableView()

        # hsj 自动义的tableModel
        slt = "T_Product_New.ProductID,ProductName,ProductNO,count(*),LifeTime,ToLifeDays"
        headerRow = ["产品编号", "产品名称", "产品代号", "已使用次数", "寿命", "据到期提醒"]
        self.queryModel = MySearchTableModelPIM("T_Product_New left join T_Out_Detail on T_Product_New.ProductID = T_Out_Detail.ProductID", headerRow, slt)
        self.tableView.setModel(self.queryModel)
        self.header = CheckBoxHeader()
        self.tableView.setHorizontalHeader(self.header)
        self.header.clicked.connect(self.queryModel.headerClick)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.queryModel)
        self.verticalLayout.addWidget(self.tableView)

        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.jumpEdit = QtWidgets.QLineEdit(Dialog)
        self.jumpEdit.setMaximumSize(QtCore.QSize(50, 50))
        self.jumpEdit.setMaxLength(9999)
        self.jumpEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.jumpEdit.setObjectName("jumpEdit")
        self.horizontalLayout_2.addWidget(self.jumpEdit)
        self.totalPageLabel = QtWidgets.QLabel(Dialog)
        self.totalPageLabel.setObjectName("totalPageLabel")
        self.horizontalLayout_2.addWidget(self.totalPageLabel)
        self.jumpButton = QtWidgets.QPushButton(Dialog)
        self.jumpButton.setObjectName("jumpButton")
        self.horizontalLayout_2.addWidget(self.jumpButton)
        self.previousButton = QtWidgets.QPushButton(Dialog)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_2.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(Dialog)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        self.bindButton()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "进入寿命提醒期的产品"))
        self.label_4.setText(_translate("Dialog", "产品名称"))
        self.pushButton_4.setText(_translate("Dialog", "查询"))
        self.label_2.setText(_translate("Dialog", "跳转至第"))
        self.jumpEdit.setText(_translate("Dialog", "1"))
        self.totalPageLabel.setText(_translate("Dialog", "/  " + str(self.queryModel.totalPage) + "  页"))
        self.jumpButton.setText(_translate("Dialog", "跳转"))
        self.previousButton.setText(_translate("Dialog", "上一页"))
        self.nextButton.setText(_translate("Dialog", "下一页"))

    def bindButton(self):
        """
        hsj 绑定按钮
        :return:
        """
        # 把需要使用的窗体传进去

        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.pushButton_4.clicked.connect(self.searchButtonEventL)


    def searchButtonEventL(self):
        """
        hsj 输入查询条件查询按钮事件
        没有日期的查询
        :return:
        """
        content = self.searchEdit.text()

        if content == "":
            sql = "WHERE LifeType = '次数' GROUP BY T_Product_New.ProductID"
            self.queryModel.searchTableL(sql)
            self.updateUI()

        else:
            sql = "WHERE LifeType = '次数' and %s = '%s' GROUP BY T_Product_New.ProductID" % (self.select_conditions, content)
            self.queryModel.searchTableL(sql)
            self.updateUI()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QWidget()
    w = LifeReminder2()
    w.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())