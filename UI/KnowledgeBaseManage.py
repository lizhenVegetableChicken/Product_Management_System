
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QHeaderView, QMessageBox, QDialog
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

from UI.MySearchBatchModel import MySearchTableModel, CheckBoxHeader
from UI.SearchView import MySearchWidget
from UI.SelectSingleKBMView import SelectrKnowledgeBase
from UI.SelectSingleProductView import SelectSingleProductWidget
from UI.AddKnowledgeBaseview import AddKBMWidge

from Utils import openDB


class KnowledgeBaseManage(MySearchWidget):

    def __init__(self):
        super(KnowledgeBaseManage, self).__init__()
        self.select_conditions = ["Num", "Title", "Source", "Publisher", "Rtime", "Etime", "Readrange"]
        
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)


        # 中间手动代码部分 表格UI构建
        self.db = openDB()
        self.tableView = QTableView()

        #czq 借鉴hsj的tableModel
        headerRow = ["序号", "标题", "来源", "发布人", "发布时间", "过期时间", "阅读范围", "内容"]
        self.queryModel = MySearchTableModel("T_Knowladge_Base_Mangement", headerRow)
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
        #self.comboBox.setCurrentIndex(0)
        self.bindButton()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "知识库管理"))
        self.addBatchButton.setText(_translate("Form", "新增知识"))
        self.selectProduct.setText(_translate("Form", "查看知识"))
        self.alterVBatchButton.setText(_translate("Form", "修改知识"))
        self.deleteBatchButton.setText(_translate("Form", "删除知识"))
        self.searchButton.setText(_translate("Form", "查询"))
        self.comboBox.setItemText(0, _translate("Form", "按序号查询"))
        self.comboBox.setItemText(1, _translate("Form", "按标题查询"))
        self.comboBox.setItemText(2, _translate("Form", "按来源查询"))
        self.comboBox.setItemText(3, _translate("Form", "按发布人查询"))
        self.comboBox.setItemText(4, _translate("Form", "按发布时间查询"))
        self.comboBox.setItemText(5, _translate("Form", "按过期时间查询"))
        self.comboBox.setItemText(6, _translate("Form", "按阅读范围查询"))
        self.label_2.setText(_translate("Form", "跳转至第"))
        self.jumpEdit.setText(_translate("Form", "1"))

        # 更新页码总页数 复制进去
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
        self.addBatchButton.clicked.connect(lambda :self.addButtonEvent(AddKBMWidge()))
        # 查看产品
        self.selectProduct.clicked.connect(lambda :self.selectButtonEvent(SelectrKnowledgeBase()))
        # 修改批次
        self.alterVBatchButton.clicked.connect(lambda :self.updateButtonEvent(AddKBMWidge()))

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
        productDiglog = Widget
        form = QDialog()
        productDiglog.setupUi(form)
        productDiglog.setData(result)
        form.show()
        form.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = KnowledgeBaseManage()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
