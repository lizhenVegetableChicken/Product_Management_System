# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchProductBatchDetailView_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QTableView, QDialog, QApplication, QWidget, QMessageBox

from UI.AddProductView import AddProductWidget
from MySearchBatchModel import CheckBoxHeader, MySearchTableModel
from SearchView import MySearchWidget
from SelectSingleProductView import SelectSingleProductWidget
from Utils import openDB
from addProductBatchView import AddProductBatchWidget


class SelectProductBatchDetailWidget(MySearchWidget):
    def __init__(self):
        super(SelectProductBatchDetailWidget, self).__init__()
        self.select_conditions = ["BatchNO", "ProductID", "ReceiveCompanyName"]

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1171, 813)
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
        self.addBatchButton = QtWidgets.QPushButton(Form)
        self.addBatchButton.setObjectName("addBatchButton")
        self.horizontalLayout_5.addWidget(self.addBatchButton)
        self.selectBatch = QtWidgets.QPushButton(Form)
        self.selectBatch.setObjectName("selectBatch")
        self.horizontalLayout_5.addWidget(self.selectBatch)
        self.selectProduct = QtWidgets.QPushButton(Form)
        self.selectProduct.setObjectName("selectProduct")
        self.horizontalLayout_5.addWidget(self.selectProduct)
        self.alterVBatchButton = QtWidgets.QPushButton(Form)
        self.alterVBatchButton.setObjectName("alterVBatchButton")
        self.horizontalLayout_5.addWidget(self.alterVBatchButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.deleteBatchButton = QtWidgets.QPushButton(Form)
        self.deleteBatchButton.setObjectName("deleteBatchButton")
        self.horizontalLayout_3.addWidget(self.deleteBatchButton)
        self.selectDocument = QtWidgets.QPushButton(Form)
        self.selectDocument.setObjectName("selectDocument")
        self.horizontalLayout_3.addWidget(self.selectDocument)
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
        headerRow = ["批次号", "产品编号", "交付日期", "交付单位", "交付人员", "接收单位", "接收人员", "备注"]
        self.queryModel = MySearchTableModel("T_Product_BatchDetail", headerRow)
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
        self.bindButton()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "产品信息管理"))
        self.addBatchButton.setText(_translate("Form", "新建批次"))
        self.selectBatch.setText(_translate("Form", "查看批次"))
        self.selectProduct.setText(_translate("Form", "查看产品"))
        self.alterVBatchButton.setText(_translate("Form", "修改批次"))
        self.deleteBatchButton.setText(_translate("Form", "删除批次"))
        self.selectDocument.setText(_translate("Form", "查看文档"))
        self.searchButton.setText(_translate("Form", "查询"))
        self.comboBox.setItemText(0, _translate("Form", "按产品号查询"))
        self.comboBox.setItemText(1, _translate("Form", "按产品名查询"))
        self.comboBox.setItemText(2, _translate("Form", "按批次号查询"))
        self.label_2.setText(_translate("Form", "跳转至第"))
        self.jumpEdit.setText(_translate("Form", "1"))
        # 更新页码总页数 复制进去
        self.totalPageLabel.setText(_translate("Form", "/  " + str(self.queryModel.totalPage) + "  页"))
        self.jumpButton.setText(_translate("Form", "跳转"))
        self.previousButton.setText(_translate("Form", "上一页"))
        self.nextButton.setText(_translate("Form", "下一页"))
    def bindButton(self):
        """
        hsj 绑定按钮
        :return:
        """
        # 把需要使用的窗体传进去
        # 新建按钮
        self.addBatchButton.clicked.connect(lambda :self.addButtonEvent(AddProductBatchWidget()))
        # 查看产品
        self.selectProduct.clicked.connect(lambda :self.selectButtonEvent(AddProductWidget()))
        # 修改批次
        self.alterVBatchButton.clicked.connect(lambda :self.updateButtonEvent(AddProductBatchWidget()))

        # 下面是无需改动的按钮
        # 删除按钮
        self.deleteBatchButton.clicked.connect(self.deleteButtonEvent)
        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.searchButton.clicked.connect(self.searchButtonEvent)
        # 查询文档
        self.selectDocument.clicked.connect(self.selectDocumentEvent)
        # 查询批次
        self.selectBatch.clicked.connect(lambda :self.selectDetailButtonEvent(AddProductBatchWidget()))

        # 下面是无需改动的按钮
        # 删除按钮))


    def selectButtonEvent(self, Widget):
        """
        hsj 根据批次中的产品Id查询产品详细信息
        :param Widget: 要显示的窗体
        :return:
        """
        # 判断复选框是否只选中一个
        a = self.isCorrect()
        if a == 0:
            return
        result = self.queryModel.selectSingleTableForeign()
        batchDialog = Widget
        form = QDialog()
        batchDialog.setupUi(form)
        batchDialog.showData(result, self.queryModel)
        form.show()
        a = form.exec()
        # 如果对话框关闭，则对查询数据进行更行
        if a == 0:
            self.queryModel.refreshPage()
            self.queryModel.update()

    def selectDocumentEvent(self):
        # 判断复选框是否只选中一个
        a = self.isCorrect()
        if a == 0:
            return
        result = self.queryModel.selectSingleTable()
        path = result[-1]
        import os
        if path == "选择文档" or path == "":
            return
        os.startfile(path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = SelectProductBatchDetailWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())