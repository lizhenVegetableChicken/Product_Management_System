# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OutStrorageView.ui'
# 许帅
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QHeaderView, QMessageBox

from Login_recorder import logToFile, getCurrentUserId
from UI.AddOutStorage import AddOutStorage
from UI.AlterOutStorage import AlterOutStorage
from UI.MySearchBatchModel import MySearchTableModel, CheckBoxHeader
from UI.SearchView import MySearchWidget
from UI.SelectOutStorage import SelectOutStorage


class OutStorageWidget(MySearchWidget):
    def __init__(self):
        super().__init__()
        self.select_conditions = ["ProductID", "OutNO"]

    def setupUi(self, OutStorageForm):
        OutStorageForm.setObjectName("OutStorageForm")
        OutStorageForm.resize(1171, 813)
        self.verticalLayout = QtWidgets.QVBoxLayout(OutStorageForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(OutStorageForm)
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
        self.addOutStorageButton = QtWidgets.QPushButton(OutStorageForm)
        self.addOutStorageButton.setObjectName("addOutStorageButton")
        self.horizontalLayout_5.addWidget(self.addOutStorageButton)
        self.selectOutStorageInfo = QtWidgets.QPushButton(OutStorageForm)
        self.selectOutStorageInfo.setObjectName("selectOutStorageInfo")
        self.horizontalLayout_5.addWidget(self.selectOutStorageInfo)
        self.alterOutStorageInfo = QtWidgets.QPushButton(OutStorageForm)
        self.alterOutStorageInfo.setObjectName("alterOutStorageInfo")
        self.horizontalLayout_5.addWidget(self.alterOutStorageInfo)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.deleteOutStorageInfo = QtWidgets.QPushButton(OutStorageForm)
        self.deleteOutStorageInfo.setObjectName("deleteOutStorageInfo")
        self.horizontalLayout_3.addWidget(self.deleteOutStorageInfo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = QtWidgets.QLineEdit(OutStorageForm)
        self.searchEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(OutStorageForm)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.comboBox = QtWidgets.QComboBox(OutStorageForm)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableView = QtWidgets.QTableView(OutStorageForm)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(OutStorageForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.jumpEdit = QtWidgets.QLineEdit(OutStorageForm)
        self.jumpEdit.setMaximumSize(QtCore.QSize(50, 50))
        self.jumpEdit.setMaxLength(9999)
        self.jumpEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.jumpEdit.setObjectName("jumpEdit")
        self.horizontalLayout_2.addWidget(self.jumpEdit)
        self.totalPageLabel = QtWidgets.QLabel(OutStorageForm)
        self.totalPageLabel.setObjectName("totalPageLabel")
        self.horizontalLayout_2.addWidget(self.totalPageLabel)
        self.jumpButton = QtWidgets.QPushButton(OutStorageForm)
        self.jumpButton.setObjectName("jumpButton")
        self.horizontalLayout_2.addWidget(self.jumpButton)
        self.previousButton = QtWidgets.QPushButton(OutStorageForm)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_2.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(OutStorageForm)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(OutStorageForm)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OutStorageForm)

    def retranslateUi(self, OutStorageForm):
        _translate = QtCore.QCoreApplication.translate
        OutStorageForm.setWindowTitle(_translate("OutStorageForm", "出库管理"))
        self.label.setText(_translate("OutStorageForm", "出库信息查询"))
        self.addOutStorageButton.setText(_translate("OutStorageForm", "新建出库信息"))
        self.selectOutStorageInfo.setText(_translate("OutStorageForm", "查看产品出库信息"))
        self.alterOutStorageInfo.setText(_translate("OutStorageForm", "修改出库信息"))
        self.deleteOutStorageInfo.setText(_translate("OutStorageForm", "删除出库信息"))
        self.searchButton.setText(_translate("OutStorageForm", "查询"))
        self.comboBox.setItemText(0, _translate("OutStorageForm", "按产品编号查询"))
        self.comboBox.setItemText(1, _translate("OutStorageForm", "按出库编号查询"))
        self.label_2.setText(_translate("OutStorageForm", "跳转至第"))
        self.jumpEdit.setText(_translate("OutStorageForm", "1"))
        self.totalPageLabel.setText(_translate("OutStorageForm", "/  " + str(self.queryModel.totalPage) + "  页"))
        self.jumpButton.setText(_translate("OutStorageForm", "跳转"))
        self.previousButton.setText(_translate("OutStorageForm", "上一页"))
        self.nextButton.setText(_translate("OutStorageForm", "下一页"))
        # tableView数据设置
        headerRow = ["出库编号", "产品编号", "出库库房", "出库日期", "出库数量", "登记人", "使用人", "使用部门"]
        self.tableView.setModel(self.queryModel)
        self.queryModel = MySearchTableModel("T_Out_Detail", headerRow)
        self.queryModel = MySearchTableModel("T_Out_Detail", headerRow)
        self.tableView.setModel(self.queryModel)
        self.header = CheckBoxHeader()
        self.tableView.setHorizontalHeader(self.header)
        self.header.clicked.connect(self.queryModel.headerClick)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.queryModel)
        # 按钮绑定事件
        self.addOutStorageButton.clicked.connect(lambda: self.addButtonEvent(AddOutStorage()))
        # 增加
        self.searchButton.clicked.connect(self.searchButtonEvent)
        # 查看
        self.selectOutStorageInfo.clicked.connect(lambda: self.selectButtonEvent(SelectOutStorage()))
        # 修改
        self.alterOutStorageInfo.clicked.connect(lambda: self.updateButtonEvent(AlterOutStorage()))

        # 下面是无需改动的按钮
        # 删除按钮
        self.deleteOutStorageInfo.clicked.connect(self.deleteButtonEvent)
        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.searchButton.clicked.connect(self.searchButtonEvent)

    def addButtonEvent(self, Widget):
        logger = logToFile()
        UserId = getCurrentUserId()
        tableName = self.queryModel.table
        logger.info("用户：" + str(UserId) + " 点击了添加按钮，试图在 " + str(tableName) + " 表中添加数据项")
        form = QDialog()
        w = Widget
        w.setupUi(form)
        form.show()
        a = form.exec_()
        # 如果对话框关闭，则对查询数据进行更行
        if a == 0:
            self.queryModel.refreshPage()
            self.queryModel.update()
            self.updateUI()

    def selectButtonEvent(self, Widget):
        """
        hsj 根据批次中的产品编号查询产品详细信息
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

    def deleteButtonEvent(self):
        """
        hsj 删除按钮绑定事件
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
            logger.info("用户：" + str(UserId) + " 删除失败（没有选择要删除的数据）")
            QMessageBox.warning(QDialog(), "警告", "没有数据被选中，请选中后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return
        a = QMessageBox.information(QDialog(), "提示", "是否确认删除？", QMessageBox.Yes, QMessageBox.No)
        if a == QMessageBox.No:
            logger.info("用户：" + str(UserId) + " 取消了删除")
            return
        self.queryModel.deleteOut()
        self.queryModel.update()
        self.updateBottomWidget()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = OutStorageWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
