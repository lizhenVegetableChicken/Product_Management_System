
import sys

import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QHeaderView
from Thread.SearchProductBatchThread import SearchProductBatchDetailThread
from UI.MySearchBatchModel import MySearchTableModel


class SelectProductBatchWidget(QWidget):
    """暂时弃用"""
    def __init__(self):
        super(SelectProductBatchWidget, self).__init__()
        # self.setThread()

    def setThread(self):
        table_thread = SearchProductBatchDetailThread()  # 实例化子线程
        table_thread.start()  # 启动线程
        # 将子线程信号连接到槽
        table_thread.update_date.connect(self.table_data_update)

    def table_data_update(self):
        #print("刷新函数")
        self.queryModel.select()

    def setupUi(self, Form):
        """自动生成UI + 表格组件"""
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
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(600, 0))
        self.widget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = QtWidgets.QLineEdit(self.widget)
        self.searchEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignRight)


        # 中间手动代码部分 表格UI构建
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("./db/ProductManagement_new.db")
        self.db.open()
        self.tableView = QTableView()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        headerRow = ["ID", "组件名称", "DisplayOrder", "创建人员ID", "创建时间", "修改人员ID", "修改时间", "备注"]
        self.queryModel = MySearchTableModel("T_Product_ComponentType", headerRow)
        # self.queryModel.setTable()
        # self.queryModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        # self.queryModel.select()

        # self.queryModel.setHeaderData(0, Qt.Horizontal, "ID")
        # self.queryModel.setHeaderData(1, Qt.Horizontal, "产品ID")
        # self.queryModel.setHeaderData(2, Qt.Horizontal, "批次号")
        # self.queryModel.setHeaderData(3, Qt.Horizontal, "交付日期")
        # self.queryModel.setHeaderData(4, Qt.Horizontal, "交付人员")
        # self.queryModel.setHeaderData(5, Qt.Horizontal, "接收单位")
        # self.queryModel.setHeaderData(6, Qt.Horizontal, "接收人员")
        # self.queryModel.setHeaderData(8, Qt.Horizontal, "创建人员ID")
        # self.queryModel.setHeaderData(9, Qt.Horizontal, "创建时间")
        # self.queryModel.setHeaderData(10, Qt.Horizontal, "修改人员ID")
        # self.queryModel.setHeaderData(11, Qt.Horizontal, "修改时间")
        # self.queryModel.setHeaderData(12, Qt.Horizontal, "备注")

        self.tableView.setModel(self.queryModel)
        self.verticalLayout.addWidget(self.tableView)


        # self.tableView = QtWidgets.QTableView(Form)
        # self.tableView.setObjectName("tableView")
        # self.verticalLayout.addWidget(self.tableView)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setMaximumSize(QtCore.QSize(600, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.jumpEdit = QtWidgets.QLineEdit(self.widget_2)
        self.jumpEdit.setMaximumSize(QtCore.QSize(50, 50))
        self.jumpEdit.setMaxLength(9999)
        self.jumpEdit.setObjectName("jumpEdit")
        self.horizontalLayout_2.addWidget(self.jumpEdit)
        self.totalPageLabel = QtWidgets.QLabel(self.widget_2)
        self.totalPageLabel.setObjectName("totalPageLabel")
        self.horizontalLayout_2.addWidget(self.totalPageLabel)
        self.jumpButton = QtWidgets.QPushButton(self.widget_2)
        self.jumpButton.setObjectName("jumpButton")
        self.horizontalLayout_2.addWidget(self.jumpButton)
        self.previousButton = QtWidgets.QPushButton(self.widget_2)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_2.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(self.widget_2)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "产品批次查询"))
        self.searchButton.setText(_translate("Form", "查询"))
        self.comboBox.setItemText(0, _translate("Form", "按产品号查询"))
        self.comboBox.setItemText(1, _translate("Form", "按产品名查询"))
        self.comboBox.setItemText(2, _translate("Form", "按批次号查询"))
        self.label_2.setText(_translate("Form", "跳转至第"))
        self.jumpEdit.setText(_translate("Form", "1"))
        self.totalPageLabel.setText(_translate("Form", "页"))
        self.jumpButton.setText(_translate("Form", "跳转"))
        self.previousButton.setText(_translate("Form", "上一页"))
        self.nextButton.setText(_translate("Form", "下一页"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = SelectProductBatchWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())