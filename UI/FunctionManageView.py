import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QHeaderView

from Utils import openDB
from MySearchBatchModel import MySearchTableModel, CheckBoxHeader
from SearchView import MySearchWidget
from UI.updateFunctionView  import updateFunctionWidget
from Login_recorder import distinctUserRight


class FunctionManageWidget(MySearchWidget):

    def __init__(self):
        super(FunctionManageWidget, self).__init__()
        self.select_conditions = ["ID","ChineseName"]

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 1000)
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
        #添加按钮 没必要
        self.addFunctionButton = QtWidgets.QPushButton(Form)
        self.addFunctionButton.setObjectName("addFunctionButton")
        self.horizontalLayout_5.addWidget(self.addFunctionButton)
        self.addFunctionButton.setDisabled(True)
        self.addFunctionButton.setHidden(True)
        #查询按钮,没必要
        self.showInfo = QtWidgets.QPushButton(Form)
        self.showInfo.setObjectName("showInfo")
        self.horizontalLayout_5.addWidget(self.showInfo)
        self.showInfo.setHidden(True)
        self.showInfo.setDisabled(True)
        #更新修改按钮
        self.alterFunctionButton = QtWidgets.QPushButton(Form)
        self.alterFunctionButton.setObjectName("alterFunctionButton")
        self.horizontalLayout_5.addWidget(self.alterFunctionButton)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        #删除按钮，不行没必要
        self.deleteFunctionButton = QtWidgets.QPushButton(Form)
        self.deleteFunctionButton.setObjectName("deleteFunctionButton")
        self.deleteFunctionButton.setDisabled(True)
        self.deleteFunctionButton.setHidden(True)
        self.horizontalLayout_3.addWidget(self.deleteFunctionButton)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #查询框
        self.searchEdit = QtWidgets.QLineEdit(Form)
        self.searchEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        #查询按钮
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        #待修改成需要展示的用户管理界面的表格
        self.db = openDB()
        self.tableView = QTableView()

        headerRow = ["业务ID", "业务中文名称", "业务英文名称","是否可用", "修改时间","修改人","备注"]
        self.queryModel = MySearchTableModel("Admin_Menu", headerRow)
        self.tableView.setModel(self.queryModel)
        self.header = CheckBoxHeader()
        self.tableView.setHorizontalHeader(self.header)
        self.header.clicked.connect(self.queryModel.headerClick)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.queryModel)
        self.verticalLayout.addWidget(self.tableView)

        #self.tableView = QtWidgets.QTableView(Form)
        #self.tableView.setObjectName("tableView")
        #self.verticalLayout.addWidget(self.tableView)

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
        #绑定按钮事件
        self.bindButton()
        currentUserRightID = distinctUserRight()
        if currentUserRightID == 0:
            self.alterFunctionButton.setHidden(True)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "业务功能管理"))

        self.addFunctionButton.setText(_translate("Form", "新建业务（暂未开放）"))
        self.showInfo.setText(_translate("Form", "查看业务详细信息"))

        self.alterFunctionButton.setText(_translate("Form", "修改业务信息"))
        self.deleteFunctionButton.setText(_translate("Form", "删除业务(暂未开放)"))
        self.searchButton.setText(_translate("Form", "查询"))

        self.comboBox.setItemText(0, _translate("Form", "业务id查询"))
        self.comboBox.setItemText(1, _translate("Form", "业务中文名称查询"))
        self.label_2.setText(_translate("Form", "跳转至第"))
        self.jumpEdit.setText(_translate("Form", "1"))
        self.totalPageLabel.setText(_translate("Form", "/  " + str(self.queryModel.totalPage) + "  页"))
        self.jumpButton.setText(_translate("Form", "跳转"))
        self.previousButton.setText(_translate("Form", "上一页"))
        self.nextButton.setText(_translate("Form", "下一页"))

    def bindButton(self):
        """
        绑定按钮
        :return:
        """
        # 把需要使用的窗体传进去
        # 新建按钮
        #self.addBatchButton.clicked.connect(lambda: self.addButtonEvent(AddProductBatchWidget()))
        # 查看产品
        #self.selectProduct.clicked.connect(lambda: self.selectButtonEvent(SelectSingleProductWidget()))
        # 修改业务
        self.alterFunctionButton.clicked.connect(lambda: self.updateButtonEvent(updateFunctionWidget()))

        # 下面是无需改动的按钮
        # 删除按钮
        self.deleteFunctionButton.clicked.connect(self.deleteButtonEvent)
        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.searchButton.clicked.connect(self.searchButtonEvent)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = FunctionManageWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())