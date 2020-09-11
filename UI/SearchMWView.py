# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchMWView.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
# 李振
#
# WARNING! All changes made in this file will be lost!
import shutil
import sys
import os
# import win32api
# import win32print

from PIL import Image
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtSql import QSqlQuery
from fpdf import FPDF

from Login_recorder import logToFile, getCurrentUserId
from MWPrinter import MWPrinterWidget
from UI.AddMWView import AddMWWidget
from Utils import openDB
from UI.SelectSingleMW import SelectSingleMWWidget
from UI.MySearchBatchModel import MySearchTableModel, CheckBoxHeader
from UI.SearchView import MySearchWidget

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QHeaderView, QMessageBox, QDialog


class SearchMWWidget(MySearchWidget):
    def __init__(self):
        super(MySearchWidget,self).__init__()
        self.select_conditions = ["ProductID", "ProductName", "MaintenanceWayID"]
        self.document_list = list()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(777, 813)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
       
        self.addMaintenanceWayButton = QtWidgets.QPushButton(Form)  
        self.addMaintenanceWayButton.setObjectName("addMaintenanceWayButton")
        self.horizontalLayout_7.addWidget(self.addMaintenanceWayButton)
       
        self.selectMaintenanceWay = QtWidgets.QPushButton(Form)
        self.selectMaintenanceWay.setObjectName("selectMaintenanceWay")     
        self.horizontalLayout_7.addWidget(self.selectMaintenanceWay)
    
        self.alterMaintenanceWayButton = QtWidgets.QPushButton(Form)
        self.alterMaintenanceWayButton.setObjectName("alterMaintenanceWayButton")
        self.horizontalLayout_7.addWidget(self.alterMaintenanceWayButton)
     
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        self.deleteMaintenanceWayButton = QtWidgets.QPushButton(Form)
        self.deleteMaintenanceWayButton.setObjectName("deleteMaintenanceWayButton")
        self.horizontalLayout_6.addWidget(self.deleteMaintenanceWayButton)
        
        self.printProductButton = QtWidgets.QPushButton(Form)
        self.printProductButton.setObjectName("printProductButton")
        self.horizontalLayout_6.addWidget(self.printProductButton)
        
        
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.searchEdit = QtWidgets.QLineEdit(Form)
        self.searchEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_8.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_8.addWidget(self.searchButton)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        # # 中间手动代码部分 表格UI构建
        self.db = openDB()
        self.tableView = QTableView()

        # hsj 自动义的tableModel
        # headerRow = ["维保方式", "产品编号","维保方式名称","初次维保时间",
        #              "维保间隔时间(天)", "维保到期前多少天提醒(天)", "创建人员",
        #              "创建时间", "修改人员", "修改时间", "备注","编号"]

        headerRow = ["维保方式编号", "维保方式名称","产品编号","产品名称","产品代号","维保间隔时间","维保到期提醒","最近维保时间"]
        self.queryModel = MySearchTableModel("MaintenanceWay", headerRow)
        # 这里有个setModel
        self.tableView.setModel(self.queryModel)

        self.header = CheckBoxHeader()
        self.tableView.setHorizontalHeader(self.header)
        self.header.clicked.connect(self.queryModel.headerClick)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 这里也有setModel
        self.tableView.setModel(self.queryModel)
        self.verticalLayout.addWidget(self.tableView)


        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.jumpEdit = QtWidgets.QLineEdit(Form)
        self.jumpEdit.setMaximumSize(QtCore.QSize(50, 50))
        self.jumpEdit.setMaxLength(9999)
        self.jumpEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.jumpEdit.setObjectName("jumpEdit")
        self.horizontalLayout_10.addWidget(self.jumpEdit)
        self.totalPageLabel = QtWidgets.QLabel(Form)
        self.totalPageLabel.setObjectName("totalPageLabel")
        self.horizontalLayout_10.addWidget(self.totalPageLabel)
        self.jumpButton = QtWidgets.QPushButton(Form)
        self.jumpButton.setObjectName("jumpButton")
        self.horizontalLayout_10.addWidget(self.jumpButton)
        self.previousButton = QtWidgets.QPushButton(Form)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_10.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_10.addWidget(self.nextButton)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        # 这里绑定按钮
        self.bindButton()

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "维保方式查询"))

        self.addMaintenanceWayButton.setText(_translate("Form", "新建维保方式"))
        self.selectMaintenanceWay.setText(_translate("Form", "查看维保方式"))
        self.alterMaintenanceWayButton.setText(_translate("Form", "修改维保方式"))
        self.deleteMaintenanceWayButton.setText(_translate("Form", "删除维保方式"))
        self.printProductButton.setText(_translate("Form", "打印"))

        self.searchButton.setText(_translate("Form", "查询"))
        self.comboBox.setItemText(0, _translate("Form", "按产品编号查询"))
        self.comboBox.setItemText(1, _translate("Form", "按产品名称查询"))
        self.comboBox.setItemText(2, _translate("Form", "按维保方式编号查询"))

        self.label_3.setText(_translate("Form", "跳转至第"))
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
        self.deleteMaintenanceWayButton.clicked.connect(self.deleteButtonEvent)
        # # 新建按钮
        self.addMaintenanceWayButton.clicked.connect(lambda: self.addButtonEvent(AddMWWidget()))
        # # 查看产品
        self.selectMaintenanceWay.clicked.connect(lambda :self.selectButtonEvent(SelectSingleMWWidget()))
        # 修改按钮
        self.alterMaintenanceWayButton.clicked.connect(lambda: self.updateButtonEvent(AddMWWidget()))

        # 打印按钮
        self.printProductButton.clicked.connect(self.printButtonEvent)

        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 查询按钮
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
            logger.info("用户：" + str(UserId) + " 删除失败（没有选择要删除的数据）")
            QMessageBox.warning(QDialog(), "警告", "没有数据被选中，请选中后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return
        a = QMessageBox.information(QDialog(), "提示", "是否确认删除？", QMessageBox.Yes, QMessageBox.No)
        if a == QMessageBox.No:
            logger.info("用户：" + str(UserId) + " 取消删除")
            return
        logger.info("用户：" + str(UserId) + " 删除了" + str(tableName) + "中选中的数据：" + str(data))
        # self.queryModel.deleteProduct()
        self.queryModel.deleteMW()
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


    # 在表格逻辑中找
    def delelteExactID(self,id):
        """
        李振
        :return:
        """
        db = openDB()
        query = QSqlQuery()
        #print("这里执行了：")
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "DELETE FROM MaintenanceWay WHERE ProductID = '%s'" % id
                query.exec(sql)
        db.commit()
        self.refreshPage()

    def printButtonEvent(self):

        """
       打印按钮绑定事件
       :return:
        """
        try:
            # 如果没有选中数据，则提示无数据
            if self.queryModel.checkList.count("Checked") == 0:
                QMessageBox.warning(QDialog(), "警告", "没有数据被选中，请选中后重试！", QMessageBox.Yes, QMessageBox.Yes)
                return
            results = self.queryModel.selectMultipleTable()
            for i, result in enumerate(results):
                w = MWPrinterWidget()
                w.setData(result)
                screen = w.Dialog.grab()
                screen.save("./test/%s.png" % (i))
                # break
                # w.Dialog.show()
                # w.Dialog.exec()
                # break
            # if self.document_list:
            #     for i in self.document_list:
            #         os.remove(i)
            # self.delelePdf()
            # 新建PDF文件夹
            if not os.path.exists("C:\\Users\\Public\\Documents\\PDF"):
                path = r'C:\\Users\\Public\\Documents'
                os.mkdir(path + './PDF')

            date_str = QDateTime.currentDateTime().toString("yyyy-MM-dd-hh-mm-ss")
            documentName = "C:\\Users\\Public\\Documents\\PDF\\" + date_str + ".pdf"
            self.makePdf(documentName, [("./test/" + imgFileName) for imgFileName in os.listdir('./test/') if imgFileName.endswith("png")])
            self.deleteImage(r"./test")
            QMessageBox.information(QDialog(), "提示", "文件已保存为pdf格式，请在打开pdf后进行打印！pdf保存位置为：%s" % (documentName), QMessageBox.Yes, QMessageBox.Yes)
            os.startfile(documentName)
            self.document_list.append(documentName)
            # win32api.ShellExecute(
            #     0,
            #     "print",
            #     documentName,
            #     #
            #     # If this is None, the default printer will
            #     # be used anyway.
            #     #
            #     '/d:"%s"' % win32print.GetDefaultPrinter(),
            #     ".",
            #     0
            # )

        except Exception as e:
            print(e)

    def delelePdf(self):
        # 删除指定目录中的PDF
        for parent, dirnames, filenames in os.walk('C:\\Users\\Public\\Documents\\PDF'):
            for fn in filenames:
                if fn.lower().endswith('.pdf'):
                    os.remove(os.path.join(parent, fn))

    def makePdf(self, pdfFileName, listPages):

        #print(listPages[0])
        cover = Image.open(listPages[0])
        width, height = cover.size

        pdf = FPDF(unit = "pt", format = [width, height])

        for page in listPages:
            pdf.add_page()
            pdf.image(page, 0, 0)

        pdf.output(pdfFileName, "F")

    def deleteImage(self, dir):
        del_list = os.listdir(dir)
        for f in del_list:
            file_path = os.path.join(dir, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = SearchMWWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
