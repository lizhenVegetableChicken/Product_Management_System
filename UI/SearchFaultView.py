import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QHeaderView, QMessageBox, QDialog

from AddFaultView import AddFaultWidget
from Login_recorder import logToFile, getCurrentUserId
from MySearchBatchModel import MySearchTableModel, CheckBoxHeader
from SearchView import MySearchWidget
from StartDiagnoseView import StartDiagnoseWidget
from Utils import openDB


class SelectFaultWidget(MySearchWidget):
    def __init__(self):
        super(SelectFaultWidget, self).__init__()
        self.select_conditions = ["FaultName", "ProductName", "AnswerCount"]

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
        self.addFaultButton = QtWidgets.QPushButton(Form)
        self.addFaultButton.setObjectName("addFaultButton")
        self.horizontalLayout_5.addWidget(self.addFaultButton)
        self.selectFaultButton = QtWidgets.QPushButton(Form)
        self.selectFaultButton.setObjectName("selectFaultButton")
        self.horizontalLayout_5.addWidget(self.selectFaultButton)
        self.alterFaultButton = QtWidgets.QPushButton(Form)
        self.alterFaultButton.setObjectName("alterFaultButton")
        self.horizontalLayout_5.addWidget(self.alterFaultButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.deleteFaultButton = QtWidgets.QPushButton(Form)
        self.deleteFaultButton.setObjectName("deleteFaultButton")
        self.horizontalLayout_3.addWidget(self.deleteFaultButton)
        self.startDiagnoseButton = QtWidgets.QPushButton(Form)
        self.startDiagnoseButton.setObjectName("startDiagnoseButton")
        self.horizontalLayout_3.addWidget(self.startDiagnoseButton)
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
        self.db = openDB()
        self.tableView = QTableView()
        # hsj 自动义的tableModel
        headerRow = ["故障编号", "故障名称", "产品名称", "故障分支深度", "解决问题编号"]
        self.queryModel = MySearchTableModel("T_Diagnose", headerRow)
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
        self.label.setText(_translate("Form", "故障树管理"))
        self.addFaultButton.setText(_translate("Form", "新建故障分支"))
        self.selectFaultButton.setText(_translate("Form", "查询故障分支"))
        self.alterFaultButton.setText(_translate("Form", "修改故障分支"))
        self.deleteFaultButton.setText(_translate("Form", "删除故障分支"))
        self.startDiagnoseButton.setText(_translate("Form", "开始诊断"))
        self.searchButton.setText(_translate("Form", "查询"))
        self.comboBox.setItemText(0, _translate("Form", "按故障名称查询"))
        self.comboBox.setItemText(1, _translate("Form", "按产品查询"))
        self.comboBox.setItemText(2, _translate("Form", "按故障分支深度查询"))
        self.label_2.setText(_translate("Form", "跳转至第"))
        self.jumpEdit.setText(_translate("Form", "1"))
        self.totalPageLabel.setText(_translate("Form", "/  " + str(self.queryModel.totalPage) + "  页"))
        self.jumpButton.setText(_translate("Form", "跳转"))
        self.previousButton.setText(_translate("Form", "上一页"))
        self.nextButton.setText(_translate("Form", "下一页"))

    def bindButton(self):
        self.addFaultButton.clicked.connect(lambda :self.addButtonEvent(AddFaultWidget()))
        self.deleteFaultButton.clicked.connect(self.deleteButtonEvent)
        self.selectFaultButton.clicked.connect(lambda :self.selectDetailButtonEvent(AddFaultWidget()))
        self.alterFaultButton.clicked.connect(lambda :self.updateButtonEvent(AddFaultWidget()))
        self.startDiagnoseButton.clicked.connect(self.startDiagnoseButtonEvent)
        # 上一页
        self.previousButton.clicked.connect(self.preButtonEvent)
        # 下一页
        self.nextButton.clicked.connect(self.nextButtonEvent)
        # 跳转按钮
        self.jumpButton.clicked.connect(self.jumpButtonEvent)
        # 添加查询
        self.searchButton.clicked.connect(self.searchButtonEvent)

    def deleteButtonEvent(self):
        logger = logToFile()
        UserId = getCurrentUserId()
        data = self.queryModel.getAllCheckedData()
        tableName = self.queryModel.table
        logger.info("用户：" + str(UserId) + " 点击了删除按钮，试图删除 " + str(tableName) + " 表中的数据：" + str(data))
        if self.queryModel.checkList.count("Checked") == 0:
            QMessageBox.warning(QDialog(), "警告", "没有数据被选中，请选中后重试！", QMessageBox.Yes, QMessageBox.Yes)
            logger.info("用户：" + str(UserId) + " 删除失败（没有选择要删除的数据）")
            return
        a = QMessageBox.information(QDialog(), "提示", "是否确认删除该故障分支？", QMessageBox.Yes, QMessageBox.No)
        if a == QMessageBox.No:
            logger.info("用户：" + str(UserId) + " 取消了删除")
            return
        logger.info("用户：" + str(UserId) + " 删除了" + str(tableName) + "中选中的数据：" + str(data))
        self.queryModel.delete()
        self.queryModel.update()
        self.updateBottomWidget()

    def startDiagnoseButtonEvent(self):
        w = StartDiagnoseWidget()
        dialog = QDialog()
        w.setupUi(dialog)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = SelectFaultWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
