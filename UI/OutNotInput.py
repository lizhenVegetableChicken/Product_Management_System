# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductInventory.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
# 俞欣
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QHeaderView

from SearchView import MySearchWidget
from UI.MySearchBatchModelPIM import MySearchTableModelPIM, CheckBoxHeader
from Utils import openDB


class OutNotInput(MySearchWidget):
    def __init__(self):
        super(OutNotInput, self).__init__()
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

        spacerItem = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.searchEdit = QtWidgets.QLineEdit(Dialog)
        self.searchEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.searchEdit.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # 中间手动代码部分 表格UI构建
        self.db = openDB()
        self.tableView = QTableView()

        # hsj 自动义的tableModel
        slt = "ProductNO,ProductName,T_Out_Detail.ProductID,OutDate,UsedID"
        headerRow = ["产品代号", "产品名称","产品编号","出库时间","使用人"]
        self.queryModel = MySearchTableModelPIM("T_Out_Base,T_Out_Detail,T_Product_New", headerRow, slt)
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
        self.label.setText(_translate("Dialog", "出库未入库产品"))
        self.label_4.setText(_translate("Dialog", "产品名称"))
        self.pushButton_2.setText(_translate("Dialog", "查询"))
        self.label_2.setText(_translate("Dialog", "跳转至第"))
        self.jumpEdit.setText(_translate("Dialog", "1"))
        # 更新页码总页数 复制进去
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
        self.pushButton_2.clicked.connect(self.searchButtonEventI)

    def searchButtonEventI(self):
        """
        hsj 输入查询条件查询按钮事件
        没有日期的查询
        :return:
        """
        content = self.searchEdit.text()

        if content == "":
            self.queryModel.refreshPage()
            self.queryModel.update()

        else:
            sql = "WHERE T_Out_Base.ID = T_Out_Detail.ID and T_Out_Detail.ProductID = T_Product_New.ProductID and IsReturn ='否' and %s = '%s'" % (self.select_conditions, content)
            self.queryModel.searchTable(sql)
            self.updateUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QWidget()
    w = OutNotInput()
    w.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())