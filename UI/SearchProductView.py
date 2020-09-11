# -*- coding: utf-8 -*-
import sys

import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QTableView, QHeaderView, QApplication, QWidget, QMessageBox, QDialog, QVBoxLayout

from UI.AddProductView import AddProductWidget
from UI.MySearchBatchModel import MySearchTableModel, CheckBoxHeader
from UI.SearchView import MySearchWidget
from Utils import openDB
from Login_recorder import logToFile, getCurrentUserId
from ShowProductTree import TreeWidget


class SelectProductWidget(MySearchWidget):
    def __init__(self):
        super(SelectProductWidget, self).__init__()
        self.select_conditions = ["ProductName", "Registerer", "BatchNO"]

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1171, 854)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.addProductButton = QtWidgets.QPushButton(Form)
        self.addProductButton.setObjectName("addProductButton")
        self.horizontalLayout_5.addWidget(self.addProductButton)
        self.selectProductButton = QtWidgets.QPushButton(Form)
        self.selectProductButton.setObjectName("selectProductButton")
        self.horizontalLayout_5.addWidget(self.selectProductButton)
        self.alterProductButton = QtWidgets.QPushButton(Form)
        self.alterProductButton.setObjectName("alterProductButton")
        self.horizontalLayout_5.addWidget(self.alterProductButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.deleteProductButton = QtWidgets.QPushButton(Form)
        self.deleteProductButton.setObjectName("deleteProductButton")
        self.horizontalLayout_3.addWidget(self.deleteProductButton)
        self.documentButton = QtWidgets.QPushButton(Form)
        self.documentButton.setObjectName("documentButton")
        self.horizontalLayout_3.addWidget(self.documentButton)
        self.selectComponentButton = QtWidgets.QPushButton(Form)
        self.selectComponentButton.setObjectName("selectComponentButton")
        self.horizontalLayout_3.addWidget(self.selectComponentButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = QtWidgets.QLineEdit(Form)
        self.searchEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # 中间手动代码部分 表格UI构建
        self.db = openDB()
        self.tableView = QTableView()
        # hsj 自动义的tableModel
        headerRow = ["产品编号", "产品名称", "产品代号", "批次编号", "库存数量", "接收日期", "接收人", "接收单位", "交付日期", "交付人", "交付单位"]
        self.queryModel = MySearchTableModel("T_Product_New", headerRow)
        self.tableView.setModel(self.queryModel)
        self.header = CheckBoxHeader()
        self.tableView.setHorizontalHeader(self.header)
        self.header.clicked.connect(self.queryModel.headerClick)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.queryModel)
        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.jumpEdit = QtWidgets.QLineEdit(Form)
        self.jumpEdit.setMaximumSize(QtCore.QSize(50, 50))
        self.jumpEdit.setMaxLength(9999)
        self.jumpEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.jumpEdit.setObjectName("jumpEdit")
        self.horizontalLayout_2.addWidget(self.jumpEdit)
        self.totalPageLabel = QtWidgets.QLabel(Form)
        self.totalPageLabel.setObjectName("totalPageLabel")
        self.horizontalLayout_2.addWidget(self.totalPageLabel)
        self.jumpButton = QtWidgets.QPushButton(Form)
        self.jumpButton.setObjectName("jumpButton")
        self.horizontalLayout_2.addWidget(self.jumpButton)
        self.previousButton = QtWidgets.QPushButton(Form)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_2.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        self.bindButton()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "产品信息创建"))
        self.addProductButton.setText(_translate("Form", "新建产品信息"))
        self.selectProductButton.setText(_translate("Form", "查看产品信息"))
        self.alterProductButton.setText(_translate("Form", "修改产品信息"))
        self.deleteProductButton.setText(_translate("Form", "删除产品信息"))
        self.documentButton.setText(_translate("Form", "查看文档"))
        self.selectComponentButton.setText(_translate("Form", "查看产品组件"))
        self.searchButton.setText(_translate("Form", "查询"))
        self.comboBox.setItemText(0, _translate("Form", "按产品名称查询"))
        self.comboBox.setItemText(1, _translate("Form", "按接收人查询"))
        self.comboBox.setItemText(2, _translate("Form", "按批次号查询"))
        self.label_2.setText(_translate("Form", "跳转至第"))
        self.jumpEdit.setText(_translate("Form", "1"))
        self.totalPageLabel.setText(_translate("Form", "/  " + str(self.queryModel.totalPage) + "  页"))
        self.jumpButton.setText(_translate("Form", "跳转"))
        self.previousButton.setText(_translate("Form", "上一页"))
        self.nextButton.setText(_translate("Form", "下一页"))
    def bindButton(self):
        """
        hsj 绑定按钮
        :return:
        """
        # # 删除按钮
        self.deleteProductButton.clicked.connect(self.deleteButtonEvent)
        # # 新建按钮
        self.addProductButton.clicked.connect(lambda :self.addButtonEvent(AddProductWidget()))
        # # 查看产品
        self.selectProductButton.clicked.connect(lambda :self.selectDetailButtonEvent(AddProductWidget()))
        # 修改按钮
        self.alterProductButton.clicked.connect(lambda :self.updateButtonEvent(AddProductWidget()))
        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.searchButton.clicked.connect(self.searchButtonEvent)
        self.documentButton.clicked.connect(self.selectDocumentEvent)
        
        # self.selectComponentButton.clicked.connect(self.selectComponentButtonEvent)
        self.selectComponentButton.clicked.connect(self.selectComponentButtonEventTest)

    def selectComponentButtonEventTest(self):
        a = self.isCorrect()
        if a == 0:
            return
        productID, productName = self.queryModel.getSelectedID()
        t = TreeWidget(productID, productName)
        if not t.isNone:
            t.show()
            t.exec()



    def selectDocumentEvent(self):
        # 判断复选框是否只选中一个
        a = self.isCorrect()
        if a == 0:
            return
        result = self.queryModel.selectSingleTable()
        path = result[-1]
        import os
        if path == "选择文档" or path == "" or not os.path.isfile(path):
            QMessageBox.information(QDialog(), "提示", "文件不存在！", QMessageBox.Yes, QMessageBox.Yes)
            return
        os.startfile(path)
        # QMessageBox.information(QDialog(), "提示", "文件已打开！", QMessageBox.Yes, QMessageBox.Yes)

    def selectComponentButtonEvent(self):
        """
       hsj 搜索产品的相关组件
       :return:
       """
        # 判断复选框是否只选中一个
        a = self.isCorrect()
        if a == 0:
            return
        select_num = self.queryModel.selectNum()
        db = openDB()
        queryModel = QSqlQueryModel()
        query = QSqlQuery()
        sql = "SELECT * FROM T_ProductComponent_New WHERE ProductID = '%s'" % (self.queryModel.data_list[select_num][0])
        # print(sql)
        query.exec(sql)
        if not query.next():
            QMessageBox.information(QDialog(), "提示", "该产品无其他组件！", QMessageBox.Yes, QMessageBox.Yes)
            return
        queryModel.setQuery("SELECT * FROM T_ProductComponent_New WHERE ProductID = '%s'" % (self.queryModel.data_list[select_num][0]))
        headerRow = ["组件ID", "产品ID", "组件代号", "组件名称", "父节点ID", "组件类型", "组件数量", "寿命类型", "寿命", "据到期提醒","最初维保时间", "维保间隔", "距维保提醒"]
        for i in range(len(headerRow)):
            queryModel.setHeaderData(i, Qt.Horizontal, headerRow[i])
        form = QDialog()
        tableView = QTableView()
        tableView.setModel(queryModel)
        tableView.show()
        tableView.horizontalHeader().setStretchLastSection(True)
        layout = QVBoxLayout()
        layout.addWidget(tableView)
        form.setLayout(layout)
        form.showMaximized()
        form.exec()

    def deleteButtonEvent(self):
        """
        hsj 删除批次按钮绑定事件
        :return:
        """
        # print(self.queryModel.checkList.count("Checked"))
        # 如果没有选中数据，则提示无数据
        logger = logToFile()
        UserId = getCurrentUserId()
        data = self.queryModel.getAllCheckedData()
        tableName = self.queryModel.table
        logger.info("用户：" + str(UserId) + " 点击了删除按钮，试图删除 " + str(tableName) + " 表中的数据：" + str(data))
        if self.queryModel.checkList.count("Checked") == 0:
            QMessageBox.warning(QDialog(), "警告", "没有数据被选中，请选中后重试！", QMessageBox.Yes, QMessageBox.Yes)
            logger.info("用户：" + str(UserId) +" 删除失败（没有选择要删除的数据）")
            return
        a = QMessageBox.information(QDialog(), "提示", "删除产品将会导致关联的数据删除，是否确认删除？", QMessageBox.Yes, QMessageBox.No)
        if a == QMessageBox.No:
            return
        logger.info("用户：" + str(UserId) +" 删除了"+str(tableName)+"中选中的数据："+str(data))

        self.queryModel.deleteProduct()
        # self.queryModel.searchRefreshPage()
        self.updateBottomWidget()
        self.queryModel.refreshPage()
        self.queryModel.update()