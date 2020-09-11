import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QHeaderView

from Utils import openDB
from MySearchBatchModel import MySearchTableModel, CheckBoxHeader
from SearchView import MySearchWidget
from UI.addUserView import AddUserWidget
from Login_recorder import  distinctUserRight


class UserManageWidget(MySearchWidget):
    # 刘敬楷
    def __init__(self):
        super(UserManageWidget, self).__init__()
        self.select_conditions = ["UserId","IsAdmin"]

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(701, 281)
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
        #添加新用户按钮
        self.addUserButton = QtWidgets.QPushButton(Form)
        self.addUserButton.setObjectName("addUserButton")
        self.horizontalLayout_5.addWidget(self.addUserButton)
        #显示用户具体信息按钮
        self.showUserDetailButton = QtWidgets.QPushButton(Form)
        self.showUserDetailButton.setObjectName("showUserDetailButton")
        self.horizontalLayout_5.addWidget(self.showUserDetailButton)
        self.showUserDetailButton.setDisabled(True)
        self.showUserDetailButton.setHidden(True)
        #修改用户信息按钮
        self.alterUserButton = QtWidgets.QPushButton(Form)
        self.alterUserButton.setObjectName("alterUserButton")
        self.horizontalLayout_5.addWidget(self.alterUserButton)
        #删除用户按钮
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.deleteUserButton = QtWidgets.QPushButton(Form)
        self.deleteUserButton.setObjectName("deleteUserButton")

        self.horizontalLayout_3.addWidget(self.deleteUserButton)
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
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        #待修改成需要展示的用户管理界面的表格
        self.db = openDB()
        self.tableView = QTableView()

        headerRow = ["用户ID", "密码", "权限ID", "修改时间","修改人ID"]
        self.queryModel = MySearchTableModel("User", headerRow)
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
        self.bindButton()

        rightID = distinctUserRight()
        if rightID == 0 :
            self.addUserButton.setHidden(True)
            self.alterUserButton.setHidden(True)
            self.deleteUserButton.setHidden(True)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "用户信息管理"))
        self.addUserButton.setText(_translate("Form", "新建用户"))
        self.showUserDetailButton.setText(_translate("Form", "查看用户详细信息(暂未开放)"))
        self.alterUserButton.setText(_translate("Form", "修改用户信息"))
        self.deleteUserButton.setText(_translate("Form", "删除用户"))
        self.searchButton.setText(_translate("Form", "查询"))
        self.comboBox.setItemText(0, _translate("Form", "按用户id查询"))
        self.comboBox.setItemText(1, _translate("Form", "按权限查询"))
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
        # 新建用户按钮
        self.addUserButton.clicked.connect(lambda: self.addButtonEvent(AddUserWidget()))
        # 查看用户详细信息按钮
        #self.selectProduct.clicked.connect(lambda: self.selectButtonEvent(SelectSingleProductWidget()))
        # 修改用户信息
        self.alterUserButton.clicked.connect(lambda: self.updateButtonEvent(AddUserWidget()))

        # 下面是无需改动的按钮
        # 删除按钮
        self.deleteUserButton.clicked.connect(self.deleteButtonEvent)
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
    w = UserManageWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())