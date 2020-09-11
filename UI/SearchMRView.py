# -*- coding: utf-8 -*-
import sys
import os

from Login_recorder import logToFile, getCurrentUserId
from MWPrinter import MWPrinterWidget
from SelectSingleMR import SelectSingleMRWidget
from Utils import openDB
from UI.MySearchBatchModel import MySearchTableModel, CheckBoxHeader
from UI.SearchView import MySearchWidget
from UI.AddMRView import AddMRWidget

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableView, QHeaderView, QApplication, QWidget, QMessageBox, QDialog
# 已经写了  mypart


class SelectMRWidget(MySearchWidget):
    # 李振
    def __init__(self):
        super(SelectMRWidget, self).__init__()
        self.select_conditions = ["MrID","MwID", "ProductID"]

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
     
        self.addProductButton = QtWidgets.QPushButton(Form)
        self.addProductButton.setObjectName("addProductButton")
        self.horizontalLayout_5.addWidget(self.addProductButton)

        self.selectProductComponent = QtWidgets.QPushButton(Form)
        self.selectProductComponent.setObjectName("selectProductComponent")
        self.horizontalLayout_5.addWidget(self.selectProductComponent)

        self.alterProductButton = QtWidgets.QPushButton(Form)
        self.alterProductButton.setObjectName("alterProductButton")
        self.horizontalLayout_5.addWidget(self.alterProductButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)

        self.deleteProductButton = QtWidgets.QPushButton(Form)
        self.deleteProductButton.setObjectName("deleteProductButton")
        self.horizontalLayout_3.addWidget(self.deleteProductButton)

        self.selectDocument = QtWidgets.QPushButton(Form)
        self.selectDocument.setObjectName("selectDocument")
        self.horizontalLayout_3.addWidget(self.selectDocument)

        # self.printProductButton = QtWidgets.QPushButton(Form)
        # self.printProductButton.setObjectName("printProductButton")
        # self.horizontalLayout_3.addWidget(self.printProductButton)

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


        # self.tableView = QtWidgets.QTableView(Form)
        # self.tableView.setObjectName("tableView")
        # self.verticalLayout.addWidget(self.tableView)

        # 中间手动代码部分 表格UI构建
        self.db = openDB()
        self.tableView = QTableView()


        # hsj 自动义的tableModel
        # headerRow = ["维保记录ID", "维保方式ID", "维保方式名称", "维保时间",
        #              "维保部位", "维保负责人", "维保确认人", "维保效果", "创建人员",
        #              "创建时间", "修改人员", "修改时间", "备注","编号"]

        headerRow = ["维保记录编号","产品编号","产品名称", "维保方式编号","维保方式名称", "维保时间",
                     "维保部位", "维保负责人", "维保效果", "备注"]
        self.queryModel = MySearchTableModel("MaintenanceRecord", headerRow)

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
        self.label.setText(_translate("Form", "维保记录查询"))
        self.addProductButton.setText(_translate("Form", "新建维保记录"))
        self.selectProductComponent.setText(_translate("Form", "查看维保记录"))
        self.alterProductButton.setText(_translate("Form", "修改维保记录"))
        self.deleteProductButton.setText(_translate("Form", "删除维保记录"))
        # self.printProductButton.setText(_translate("Form", "打印"))
        self.selectDocument.setText(_translate("Form", "查看文档"))

        self.searchButton.setText(_translate("Form", "查询"))
        self.comboBox.setItemText(0, _translate("Form", "按维保记录编号查询"))
        self.comboBox.setItemText(1, _translate("Form", "按维保方式编号查询"))
        self.comboBox.setItemText(2, _translate("Form", "按产品编号查询"))
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
        self.addProductButton.clicked.connect(lambda :self.addButtonEvent(AddMRWidget()))
        # # 查看产品
        self.selectProductComponent.clicked.connect(lambda: self.selectButtonEvent(SelectSingleMRWidget()))
        # 修改按钮
        self.alterProductButton.clicked.connect(lambda :self.updateButtonEvent(AddMRWidget()))
        # 查询文档
        self.selectDocument.clicked.connect(self.selectDocumentEvent)
        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.searchButton.clicked.connect(self.searchButtonEvent)

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
            logger.info("用户：" + str(UserId) + " 删除失败（没有选择要删除的数据）")
            return
        a = QMessageBox.information(QDialog(), "提示", "是否确认删除？", QMessageBox.Yes, QMessageBox.No)
        if a == QMessageBox.No:
            logger.info("用户：" + str(UserId) + " 取消删除")
            return
        logger.info("用户：" + str(UserId) + " 删除了" + str(tableName) + "中选中的数据：" + str(data))
        self.queryModel.deleteMR()
        self.queryModel.update()
        self.updateBottomWidget()

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
        result = self.queryModel.selectSingleTable()
        productDiglog = Widget
        form = QDialog()
        productDiglog.setupUi(form)
        productDiglog.setData(result)
        form.show()
        form.exec()

    def selectDocumentEvent(self):
        # 判断复选框是否只选中一个
        a = self.isCorrect()
        if a == 0:
            return
        result = self.queryModel.selectSingleTable()
        path = result[14]
        import os
        if path == "选择文档" or path == "" or not os.path.isfile(path):
            QMessageBox.information(QDialog(), "提示", "文件不存在！", QMessageBox.Yes, QMessageBox.Yes)
            return
        os.startfile(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = SelectMRWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())