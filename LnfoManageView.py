import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QHeaderView,QDialog

from Utils import openDB
from UI.MySearchBatchModel import MySearchTableModel, CheckBoxHeader
from UI.SearchView import MySearchWidget
from UI.ShowInfoView import ShowInfoWidget
from Login_recorder import  distinctUserRight
from UI.updateFunctionView import updateFunctionWidget


class LnfoManageWidget(MySearchWidget):
    def __init__(self):
        super(LnfoManageWidget, self).__init__()
        self.select_conditions = ["id", "userId"]

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
        # 添加按钮 没必要
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setObjectName("addFunctionButton")
        self.addButton.setDisabled(True)
        self.addButton.setHidden(True)
        self.horizontalLayout_5.addWidget(self.addButton)

        # 查询按钮,没必要
        self.showInfo = QtWidgets.QPushButton(Form)
        self.showInfo.setObjectName("showInfo")
        self.showInfo.setHidden(False)
        self.showInfo.setDisabled(False)
        self.horizontalLayout_5.addWidget(self.showInfo)
        # 更新修改按钮
        self.alterButton = QtWidgets.QPushButton(Form)
        self.alterButton.setObjectName("alterFunctionButton")
        self.alterButton.setDisabled(True)
        self.alterButton.setHidden(True)
        self.horizontalLayout_5.addWidget(self.alterButton)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        # 删除按钮，没必要
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setObjectName("deleteFunctionButton")
        self.deleteButton.setDisabled(True)
        self.deleteButton.setHidden(True)
        self.horizontalLayout_3.addWidget(self.deleteButton)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # 查询框
        self.searchEdit = QtWidgets.QLineEdit(Form)
        self.searchEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        # 查询按钮
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

        # 待修改成需要展示的日志管理界面的表格
        self.db = openDB()
        self.tableView = QTableView()

        headerRow = ["日志条ID", "用户ID", "登录时间", "是否处于登录状态"]

        self.queryModel = MySearchTableModel("Login_info", headerRow)
        self.header = CheckBoxHeader()
        self.tableView.setHorizontalHeader(self.header)
        self.header.clicked.connect(self.queryModel.headerClick)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.queryModel)
        self.verticalLayout.addWidget(self.tableView)

        # self.tableView = QtWidgets.QTableView(Form)
        # self.tableView.setObjectName("tableView")
        # self.verticalLayout.addWidget(self.tableView)

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
        # 绑定按钮事件
        self.bindButton()

        currentUserRightID = distinctUserRight()
        if currentUserRightID == 0:
            self.showInfo.setHidden(True)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "查看登录日志"))

        self.addButton.setText(_translate("Form", "新建登录日志（暂未开放）"))
        self.showInfo.setText(_translate("Form", "查看系统日志"))

        self.alterButton.setText(_translate("Form", "修改登录日志"))
        self.deleteButton.setText(_translate("Form", "删除登录日志(暂未开放)"))
        self.searchButton.setText(_translate("Form", "查询"))

        self.comboBox.setItemText(0, _translate("Form", "日志条id查询"))
        self.comboBox.setItemText(1, _translate("Form", "用户id查询"))
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

        # 查看产品
        self.showInfo.clicked.connect(lambda: self.ShowInFoEvent(ShowInfoWidget()))

        # 下面是无需改动的按钮
        # 删除按钮
        self.deleteButton.clicked.connect(self.deleteButtonEvent)
        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.searchButton.clicked.connect(self.searchButtonEvent)

    def ShowInFoEvent(self,Widget):
        form = QDialog()
        w = Widget
        w.setupUi(form)
        form.show()
        a = form.exec_()
        # 如果对话框关闭，则
        if a == 0:
            return




if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = LnfoManageWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())