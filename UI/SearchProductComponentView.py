import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QHeaderView, QApplication, QWidget, QTableView, QDialog, QMessageBox, QVBoxLayout

from ShowProductTree import TreeWidget, getTreeData
from UI.AddProductComponent import AddComponentWidget
from UI.MySearchBatchModel import MySearchTableModel, CheckBoxHeader
from UI.SearchView import MySearchWidget
from Utils import openDB
from Login_recorder import getCurrentUserId,logToFile


class SearchProductComponentWidget(MySearchWidget):
    def __init__(self):
        super(SearchProductComponentWidget, self).__init__()
        self.select_conditions = ["ComponentName", "ProductID", "ComponentType"]

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
        self.addComponentButton = QtWidgets.QPushButton(Form)
        self.addComponentButton.setObjectName("addComponentButton")
        self.horizontalLayout_5.addWidget(self.addComponentButton)
        self.selectComponent = QtWidgets.QPushButton(Form)
        self.selectComponent.setObjectName("selectComponent")
        self.horizontalLayout_5.addWidget(self.selectComponent)
        self.selectSubComponent = QtWidgets.QPushButton(Form)
        self.selectSubComponent.setObjectName("selectSubComponent")
        self.horizontalLayout_5.addWidget(self.selectSubComponent)
        self.alterComponentButton = QtWidgets.QPushButton(Form)
        self.alterComponentButton.setObjectName("alterComponentButton")
        self.horizontalLayout_5.addWidget(self.alterComponentButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.deleteComponentButton = QtWidgets.QPushButton(Form)
        self.deleteComponentButton.setObjectName("deleteComponentButton")
        self.horizontalLayout_3.addWidget(self.deleteComponentButton)
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
        headerRow = ["组件ID", "产品ID", "组件代号", "组件名称", "父节点ID", "组件类型", "组件数量"]
        self.queryModel = MySearchTableModel("T_ProductComponent_New", headerRow)
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
        self.label.setText(_translate("Form", "产品组件管理"))
        self.addComponentButton.setText(_translate("Form", "新建组件"))
        self.selectComponent.setText(_translate("Form", "查看组件"))
        self.selectSubComponent.setText(_translate("Form", "查看子组件"))
        self.alterComponentButton.setText(_translate("Form", "修改组件信息"))
        self.deleteComponentButton.setText(_translate("Form", "删除组件"))
        self.searchButton.setText(_translate("Form", "查询"))
        self.comboBox.setItemText(0, _translate("Form", "按组件名称查询"))
        self.comboBox.setItemText(1, _translate("Form", "按产品ID查询"))
        self.comboBox.setItemText(2, _translate("Form", "按组件类型查询"))
        self.label_2.setText(_translate("Form", "跳转至第"))
        self.jumpEdit.setText(_translate("Form", "1"))
        self.totalPageLabel.setText(_translate("Form", "/  " + str(self.queryModel.totalPage) + "  页"))
        self.jumpButton.setText(_translate("Form", "跳转"))
        self.previousButton.setText(_translate("Form", "上一页"))
        self.nextButton.setText(_translate("Form", "下一页"))
        self.selectComponent.setVisible(False)

    def bindButton(self):
        """
        hsj 绑定按钮
        :return:
        """
        # 删除按钮
        self.deleteComponentButton.clicked.connect(self.deleteButtonEvent)
        # # 新建按钮
        self.addComponentButton.clicked.connect(lambda :self.addButtonEvent(AddComponentWidget()))
        # # 查看子产品组件
        self.selectSubComponent.clicked.connect(self.selectSubComponentButtonEvent)
        # 修改批次
        self.alterComponentButton.clicked.connect(lambda :self.updateButtonEvent(AddComponentWidget()))
        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.searchButton.clicked.connect(self.searchButtonEvent)
        self.selectComponent.clicked.connect(lambda :self.selectDetailButtonEvent(AddComponentWidget()))

    def deleteButtonEvent(self):
        """
        hsj 删除批次按钮绑定事件
        :return:
        """
        # print(self.queryModel.checkList.count("Checked"))
        # 如果没有选中数据，则提示无数据
        UserId = getCurrentUserId()
        logger = logToFile()

        logger.info("用户："+str(UserId)+" 点击了删除按钮,试图删除："+str(self.queryModel.getData()))

        if self.queryModel.checkList.count("Checked") == 0:
            QMessageBox.warning(QDialog(), "警告", "没有数据被选中，请选中后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return
        a = QMessageBox.information(QDialog(), "提示", "是否确认删除？", QMessageBox.Yes, QMessageBox.No)
        if a == QMessageBox.No:
            return
        self.queryModel.deleteCompoment()
        self.queryModel.update()

    def selectSubComponentButtonEvent(self):
        a = self.isCorrect()
        if a == 0:
            return
        componentID, productID, componentName, componentType, count = self.queryModel.getSelectedComponentID()
        # if fatherID == "无父组件":
        #     QMessageBox.information(QDialog(), "该组件")
        init_level = getTreeData(productID, fatherID=componentID)
        if not init_level:
            QMessageBox.information(QDialog(), "提示", "当前组件无子组件！", QMessageBox.Yes, QMessageBox.Yes)
            return
        t = TreeWidget(productID, componentName, init_level, componentID, componentType, count)
        if not t.isNone:
            t.show()
            t.exec()

    # def selectSubComponentButtonEvent(self):
    #     """
    #     hsj 搜索产品组件的子组件
    #     :return:
    #     """
    #     # 判断复选框是否只选中一个
    #     a = self.isCorrect()
    #     if a == 0:
    #         return
    #     select_num = self.queryModel.selectNum()
    #     db = openDB()
    #     queryModel = QSqlQueryModel()
    #     query = QSqlQuery()
    #     sql = "SELECT * FROM T_ProductComponent_New WHERE FatherID = '%s'" % (self.queryModel.data_list[select_num][0])
    #     print(sql)
    #     query.exec(sql)
    #     if not query.next():
    #         QMessageBox.information(QDialog(), "提示", "该组件无其他子组件！", QMessageBox.Yes, QMessageBox.Yes)
    #         return
    #     # print("SELECT * FROM T_Product_Component WHERE ParentID = %s" % (self.queryModel.data_list[select_num][0]))
    #     queryModel.setQuery("SELECT * FROM T_ProductComponent_New WHERE FatherID = '%s'" % (self.queryModel.data_list[select_num][0]))
    #     headerRow = ["ID","组件编号", "产品编号", "组件代号", "组件名称", "父节点编号", "组件类型", "组件数量", "寿命类型", "寿命", "据到期提醒","最初维保时间", "维保间隔", "距维保提醒"]
    #     for i in range(len(headerRow)):
    #         queryModel.setHeaderData(i, Qt.Horizontal, headerRow[i])
    #     # queryModel
    #     form = QDialog()
    #     tableView = QTableView()
    #     tableView.setModel(queryModel)
    #     tableView.show()
    #     layout = QVBoxLayout()
    #     layout.addWidget(tableView)
    #     form.setLayout(layout)
    #     form.showMaximized()
    #     form.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = SearchProductComponentWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())