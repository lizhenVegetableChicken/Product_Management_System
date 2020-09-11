# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import qdarkstyle
from PyQt5.QtSql import *


class ProductStorageViewer2(QWidget):
    def __init__(self):
        super(ProductStorageViewer2, self).__init__()
        self.resize(700, 500)
        self.setWindowTitle("欢迎使用产品管理系统")
        # 查询模型
        self.queryModel = None
        # 数据表
        self.tableView = None
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecord = 0
        # 每页数据数
        self.pageRecord = 10
        self.setUpUI()

    def setUpUI(self):
        self.layout = QVBoxLayout()
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()
        self.Hlayout3 = QHBoxLayout()   # Zgg 增加“添加一行”、“删除一行”按钮

        # Hlayout1控件的初始化
        self.searchEdit = QLineEdit()
        self.searchEdit.setFixedHeight(32)
        font = QFont()
        font.setPixelSize(15)
        self.searchEdit.setFont(font)

        self.searchButton = QPushButton("查询")
        self.searchButton.setFixedHeight(32)
        self.searchButton.setFont(font)
        self.searchButton.setIcon(QIcon(QPixmap("./Images/search.png")))

        self.condisionComboBox = QComboBox()
        searchCondision = ['按产品名查询', '按产品号查询', '按批次号查询']
        self.condisionComboBox.setFixedHeight(32)
        self.condisionComboBox.setFont(font)
        self.condisionComboBox.addItems(searchCondision)

        self.Hlayout1.addWidget(self.searchEdit)
        self.Hlayout1.addWidget(self.searchButton)
        self.Hlayout1.addWidget(self.condisionComboBox)

        # Hlayout2初始化
        self.jumpToLabel = QLabel("跳转到第")
        self.pageEdit = QLineEdit()
        self.pageEdit.setFixedWidth(60)
        s = "/" + str(self.totalPage) + "页"
        self.pageLabel = QLabel(s)
        self.jumpToButton = QPushButton("跳转")
        self.prevButton = QPushButton("前一页")
        self.prevButton.setFixedWidth(100)
        self.backButton = QPushButton("后一页")
        self.backButton.setFixedWidth(100)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(self.jumpToLabel)
        Hlayout.addWidget(self.pageEdit)
        Hlayout.addWidget(self.pageLabel)
        Hlayout.addWidget(self.jumpToButton)
        Hlayout.addWidget(self.prevButton)
        Hlayout.addWidget(self.backButton)
        widget = QWidget()
        widget.setLayout(Hlayout)
        widget.setFixedWidth(500)
        self.Hlayout2.addWidget(widget)

        # Zgg 增加“添加一行”、“删除一行”按钮
        self.addBtn = QPushButton('添加一行')
        self.addBtn.clicked.connect(self.AddRow)

        self.delBtn = QPushButton('删除一行')
        self.delBtn.clicked.connect(self.DelRow)

        Hlayout_temp = QHBoxLayout()
        Hlayout_temp.addWidget(self.addBtn)
        Hlayout_temp.addWidget(self.delBtn)
        widget3 = QWidget()
        widget3.setLayout(Hlayout_temp)
        widget3.setFixedWidth(500)
        self.Hlayout3.addWidget(widget3)

        # tableView
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('./db/ProductManagement.db')
        self.db.open()
        self.tableView = QTableView()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #self.queryModel = QSqlQueryModel()

        # Zgg
        self.queryModel = QSqlTableModel()
        self.queryModel.setTable('Product')
        self.queryModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.queryModel.select()

        self.queryModel.setHeaderData(0, Qt.Horizontal, "产品名")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "产品代号")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "技术文档")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "批次号")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "产品编号")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "交付日期")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "交付单位")
        self.queryModel.setHeaderData(7, Qt.Horizontal, "交付者")
        self.queryModel.setHeaderData(8, Qt.Horizontal, "接收单位")
        self.queryModel.setHeaderData(9, Qt.Horizontal, "接收者")
        self.queryModel.setHeaderData(10, Qt.Horizontal, "登记日期")
        self.queryModel.setHeaderData(11, Qt.Horizontal, "登记人")
        self.queryModel.setHeaderData(12, Qt.Horizontal, "存放地点")
        self.queryModel.setHeaderData(13, Qt.Horizontal, "存储环境")
        self.queryModel.setHeaderData(14, Qt.Horizontal, "存储时间")
        self.queryModel.setHeaderData(15, Qt.Horizontal, "产品状态")
        self.queryModel.setHeaderData(16, Qt.Horizontal, "出入库信息")
        self.queryModel.setHeaderData(17, Qt.Horizontal, "寿命")
        self.queryModel.setHeaderData(18, Qt.Horizontal, "寿命起日期")
        self.queryModel.setHeaderData(19, Qt.Horizontal, "寿命止日期")
        self.queryModel.setHeaderData(20, Qt.Horizontal, "寿命到期前多少天提醒")

        self.searchButtonClicked()
        self.tableView.setModel(self.queryModel)

        # Zgg
        self.tableView.clicked.connect(self.FindRow)

        self.layout.addLayout(self.Hlayout1)
        self.layout.addLayout(self.Hlayout3)
        self.layout.addWidget(self.tableView)
        self.layout.addLayout(self.Hlayout2)


        self.setLayout(self.layout)
        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.prevButton.clicked.connect(self.prevButtonClicked)
        self.backButton.clicked.connect(self.backButtonClicked)
        self.jumpToButton.clicked.connect(self.jumpToButtonClicked)
        self.searchEdit.returnPressed.connect(self.searchButtonClicked)

    def FindRow(self, i):
        delrow = i.row()
        print('del row=%s' % str(delrow))

    def AddRow(self):
        ret = self.queryModel.insertRows(self.queryModel.rowCount(),1)
        print('insertRow=%s' % str(ret))

    def DelRow(self):
        ret = self.queryModel.removeRow(self.tableView.currentIndex().row())
        print('delRow=%s' % str(ret))

    def setButtonStatus(self):
        if(self.currentPage==self.totalPage):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(False)
        if(self.currentPage==1):
            self.backButton.setEnabled(True)
            self.prevButton.setEnabled(False)
        if(self.currentPage<self.totalPage and self.currentPage>1):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(True)

    # 得到记录数
    def getTotalRecordCount(self):
        #self.queryModel.setQuery("SELECT * FROM Product")
        self.totalRecord = self.queryModel.rowCount()
        return

    # 得到总页数
    def getPageCount(self):
        self.getTotalRecordCount()
        # 上取整
        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        return

    # 分页记录查询
    def recordQuery(self, index):
        queryCondition = ""
        conditionChoice = self.condisionComboBox.currentText()
        if (conditionChoice == "按产品名查询"):
            conditionChoice = 'ProductName'
        elif (conditionChoice == "按产品号查询"):
            conditionChoice = 'ProductId'
        else:
            conditionChoice = 'ProductPiCiHao'  # (conditionChoice == "按批次号查询"):
        #else:
        #    conditionChoice = 'Publisher'

        if (self.searchEdit.text() == ""):
            queryCondition = "select * from Product"
            self.queryModel.setQuery(queryCondition)
            self.totalRecord = self.queryModel.rowCount()
            self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
            label = "/" + str(int(self.totalPage)) + "页"
            self.pageLabel.setText(label)
            queryCondition = ("select * from Product ORDER BY %s  limit %d,%d " % (conditionChoice,index, self.pageRecord))
            self.queryModel.setQuery(queryCondition)
            self.setButtonStatus()
            return

        # 得到模糊查询条件
        temp = self.searchEdit.text()
        s = '%'
        for i in range(0, len(temp)):
            s = s + temp[i] + "%"
        queryCondition = ("SELECT * FROM Product WHERE %s LIKE '%s' ORDER BY %s " % (
            conditionChoice, s,conditionChoice))
        self.queryModel.setQuery(queryCondition)
        self.totalRecord = self.queryModel.rowCount()
        # 当查询无记录时的操作
        if(self.totalRecord==0):
            print(QMessageBox.information(self,"提醒","查询无记录",QMessageBox.Yes,QMessageBox.Yes))
            queryCondition = "select * from Product"
            self.queryModel.setQuery(queryCondition)
            self.totalRecord = self.queryModel.rowCount()
            self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
            label = "/" + str(int(self.totalPage)) + "页"
            self.pageLabel.setText(label)
            queryCondition = ("select * from Product ORDER BY %s  limit %d,%d " % (conditionChoice,index, self.pageRecord))
            self.queryModel.setQuery(queryCondition)
            self.setButtonStatus()
            return

        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        label = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(label)
        queryCondition = ("SELECT * FROM Product WHERE %s LIKE '%s' ORDER BY %s LIMIT %d,%d " % (
            conditionChoice, s, conditionChoice,index, self.pageRecord))
        self.queryModel.setQuery(queryCondition)
        self.setButtonStatus()
        return

    # 点击查询
    def searchButtonClicked(self):
        self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        self.getPageCount()
        s = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(s)
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 向前翻页
    def prevButtonClicked(self):
        self.currentPage -= 1
        if (self.currentPage <= 1):
            self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 向后翻页
    def backButtonClicked(self):
        self.currentPage += 1
        if (self.currentPage >= int(self.totalPage)):
            self.currentPage = int(self.totalPage)
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 点击跳转
    def jumpToButtonClicked(self):
        if (self.pageEdit.text().isdigit()):
            self.currentPage = int(self.pageEdit.text())
            if (self.currentPage > self.totalPage):
                self.currentPage = self.totalPage
            if (self.currentPage <= 1):
                self.currentPage = 1
        else:
            self.currentPage = 1
        index = (self.currentPage - 1) * self.pageRecord
        self.pageEdit.setText(str(self.currentPage))
        self.recordQuery(index)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = ProductStorageViewer2()
    mainMindow.show()
    sys.exit(app.exec_())
