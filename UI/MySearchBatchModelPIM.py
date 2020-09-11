import sys
import datetime

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)

from Utils import openDB


class CheckBoxHeader(QHeaderView):
    # 俞欣
    clicked = pyqtSignal(bool)

    _x_offset = 3
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isOn = False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height()-self._width)/2.)

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isOn:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 == index:
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isOn:
                    self.isOn = False
                else:
                    self.isOn = True
                self.clicked.emit(self.isOn)
                self.update()
        super(CheckBoxHeader, self).mousePressEvent(event)


class MySearchTableModelPIM(QAbstractTableModel):
    def __init__(self, table, headerRow,slt, parent=None):
        """
        hsj 初始化TableModel
        :param table: 查询的表
        :param headerRow: 查询显示界面的标题
        :param parent:
        """
        super(MySearchTableModelPIM, self).__init__(parent)

        self.table = table
        self.slt = slt
        self.setTableInformation()
        # 总数据
        self.totalData = self.getData()

        # hsj 每页显示的信息数, 总页数
        self.perPageNum = 20
        self.currentPage = 0
        self.data_list = []
        self.totalPage = self.getTotalPage()
        # print(self.totalPage)

        self.initList()

        self.headerRow = headerRow
        self.checkList = ['Unchecked' for i in range(len(self.data_list))]

    def setTableInformation(self):
        """
        hsj 设置表相关信息
        :return:
        """
        if  self.table == "T_Product_New":
            self.tableKey = "ProductID"
            self.tableLength = 20
        elif self.table == "T_Out_Base,T_In_Detail,T_In_Base":
            self.tableKey = "ProductID"
            self.tableLength = 5
        elif self.table == "MaintenanceRecord":
            self.tableKey = "ProductNO,ProductID"
            self.tableLength = 4
        elif self.table == "MaintenanceWay":
            self.tableKey = "ProductNO,ProductID"
            self.tableLength = 8
        elif self.table == "T_Out_Base,T_Out_Detail,T_Product_New":
            self.tableKey = "ProductNO,T_Out_Detail.ProductID"
            self.tableLength = 6
        elif self.table == "T_Product_New left join T_Out_Detail on T_Product_New.ProductID = T_Out_Detail.ProductID":
            self.tableKey = "T_Product_New.ProductID"
            self.tableLength = 6

    def initList(self):
        """
        hsj 初始化界面数据
        :return:
        """
        if len(self.totalData) <= self.perPageNum:
            self.data_list = self.totalData
        else:
            self.data_list = self.totalData[:self.perPageNum]

    def selectSingleTableForeign(self):
        """
        hsj 查询单个外键表信息
        :return:
        """
        list = []
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "SELECT * FROM %s WHERE %s = '%s'" % (self.tableForeign, self.tableForeignKey, self.data_list[i][self.tableForeignKeyPosition])
                query.exec(sql)
                break
        if query.next():
            list = [str(query.value(i)) for i in range(self.tableForeignLength)]
        # print(list)
        return list

    def searchTable(self,sql):
        """
        hsj 根据条件查询信息，并返回界面
        :param select_condition: 列名
        :param content: 具体查询条件
        :return:
        """
        list = []
        db = openDB()
        query = QSqlQuery()
        sql1 = "SELECT %s FROM %s %s ORDER BY %s" % (self.slt,self.table, sql, self.tableKey)
        query.exec(sql1)
        while query.next():
            list.append([str(query.value(i)) for i in range(self.tableLength)])

        self.searchRefreshPage(list)
        self.update()

    def searchTableF(self,sql):

        list = []
        db = openDB()
        query = QSqlQuery()
        sql1 = "SELECT %s FROM %s %s ORDER BY %s" % (self.slt, self.table, sql, self.tableKey)
        query.exec(sql1)
        while query.next():
            dateStart = datetime.datetime.strptime(query.value(3),"%Y-%m-%d")
            life = int(query.value(4))
            Rlife = life-int(query.value(5))
            dateEnd = (dateStart + datetime.timedelta(days=life)).strftime("%Y-%m-%d")
            LRDate = dateStart + datetime.timedelta(days=Rlife)
            if datetime.datetime.now() > LRDate:
                L = [str(query.value(i)) for i in range(0, 8)]
                L[3] = dateEnd
                list.append(L)

        self.searchRefreshPage(list)
        self.update()

    def searchTableL(self,sql):

        list = []
        db = openDB()
        query = QSqlQuery()
        sql1 = "SELECT %s,T_Out_Detail.ProductID FROM %s %s ORDER BY %s" % (self.slt, self.table, sql, self.tableKey)
        query.exec(sql1)
        while query.next():
            counts = int(query.value(3))
            if query.value(6) == 'null':
                counts -= 1
            life = int(query.value(4))
            Tlife = int(query.value(5))
            if life - counts < Tlife:
                list.append([str(query.value(i)) for i in range(self.tableLength)])

        self.searchRefreshPage(list)
        self.update()

    def searchTableD(self,sql):
        """
        hsj 根据条件查询信息，并返回界面
        :param select_condition: 列名
        :param content: 具体查询条件
        :return:
        """
        list = []
        db = openDB()
        query = QSqlQuery()
        q = QSqlQuery()
        sql2 = "SELECT distinct ProductNO From T_Product_New"
        query.exec(sql2)
        while query.next():
            ProductNO = query.value(0)
            sql3 = "select sum(InitCount) FROM T_Product_New %s ProductNO='%s' ORDER BY %s" % (
            sql, ProductNO, self.tableKey)
            sql1 = "SELECT %s,(%s)sum From %s %s ProductNO='%s' ORDER BY %s" % (
            self.slt, sql3, self.table, sql, ProductNO, self.tableKey)
            q.exec(sql1)
            while q.next():
                list.append([str(q.value(i)) for i in range(5)])

        self.searchRefreshPage(list)
        self.update()

    def getData(self):
        """
        获取所有数据
        :return:
        """
        results = []
        db = openDB()
        query = QSqlQuery()
        if self.table == "T_Product_New" and self.slt == "ProductID,ProductNO,ProductName,InitCount":
            q = QSqlQuery()
            sql2 = "SELECT distinct ProductNO From T_Product_New"
            query.exec(sql2)
            while query.next():
                ProductNO = query.value(0)
                sql3 = "select sum(InitCount) FROM T_Product_New WHERE ProductNO='%s' ORDER BY %s" % (ProductNO, self.tableKey)
                sql1 = "SELECT %s,(%s)sum From %s WHERE ProductNO='%s' ORDER BY %s" % (
                    self.slt, sql3, self.table, ProductNO, self.tableKey)
                q.exec(sql1)
                while q.next():
                    results.append([str(q.value(i)) for i in range(5)])
        elif self.table == "T_Product_New" and self.slt == "ProductID,ProductName,ProductNO,ReceiverDate,LifeTime,ToLifeDays" or self.table == "MaintenanceWay":
            if self.table == "MaintenanceWay":
                sql1 = "SELECT %s FROM %s ORDER BY %s" % (self.slt, self.table, self.tableKey)
            else:
                sql1 = "SELECT %s FROM %s WHERE LifeType = '时间' ORDER BY %s" % (self.slt, self.table, self.tableKey)
            query.exec(sql1)
            while query.next():
                dateStart = datetime.datetime.strptime(query.value(3), "%Y-%m-%d")
                life = int(query.value(4))
                Rlife = life - int(query.value(5))
                dateEnd = (dateStart + datetime.timedelta(days=life)).strftime("%Y-%m-%d")
                LRDate = dateStart + datetime.timedelta(days=Rlife)
                if datetime.datetime.now() > LRDate:
                    L = [str(query.value(i)) for i in range(0, 8)]
                    L[3] = dateEnd
                    results.append(L)
        elif self.table == "T_Product_New left join T_Out_Detail on T_Product_New.ProductID = T_Out_Detail.ProductID":
            sql1 = "SELECT %s,T_Out_Detail.ProductID FROM %s WHERE LifeType = '次数' GROUP BY T_Product_New.ProductID ORDER BY %s" % (self.slt, self.table,self.tableKey)
            query.exec(sql1)
            while query.next():
                counts = int(query.value(3))
                if query.value(6) == '':
                    counts -= 1
                life = int(query.value(4))
                Tlife = int(query.value(5))
                if life - counts < Tlife:
                    results.append([str(query.value(i)) for i in range(self.tableLength)])
        else:
            if self.table == "T_Out_Base,T_In_Detail,T_In_Base":
                sql = "SELECT ProductID,OutDate,InDate,T_In_Base.CreateID,InTechState FROM T_Out_Base,T_In_Detail,T_In_Base " \
                          "WHERE T_Out_Base.OutNO=T_In_Base.OutNO AND T_In_Detail.ID=T_In_Base.ID ORDER BY ProductID"
            elif self.table == "MaintenanceRecord":
                sql = "SELECT ProductNO,ProductName,ProductID,count(*) FROM MaintenanceRecord group by ProductID ORDER BY ProductNO,ProductID"
            elif self.table == "T_Out_Base,T_Out_Detail,T_Product_New":
                sql = "SELECT ProductNO,ProductName,T_Out_Detail.ProductID,OutDate,UsedID FROM T_Out_Base,T_Out_Detail,T_Product_New " \
                      "WHERE T_Out_Base.ID = T_Out_Detail.ID and T_Out_Detail.ProductID = T_Product_New.ProductID and IsReturn ='否' ORDER BY ProductNO,T_Out_Detail.ProductID"
            else:
                sql = "SELECT %s FROM %s ORDER BY %s" % (self.slt,self.table, self.tableKey)

            query.exec(sql)
            while(query.next()):
                results.append([query.value(i) for i in range(self.tableLength)])

        return results

    def update(self):
        self.beginResetModel()
        self.checkList = ['Unchecked' for i in range(len(self.data_list))]
        # print(self.data_list)
        self.endResetModel()

    def getTotalPage(self):
        """
        hsj 得到总页数
        :return:
        """
        return (len(self.totalData) -1) // self.perPageNum + 1

    def prePage(self):
        """
        上一页数据及页面更新
        :return:
        """
        self.currentPage = self.currentPage - 1
        self.setCurrentData()
        self.update()


    def nextPage(self):
        """
        hsj 下一页数据及页面更新
        :return:
        """
        self.currentPage = self.currentPage + 1
        self.setCurrentData()
        # print("---------------",len(self.data_list))
        self.update()

    def lastPage(self):
        """
        hsj 最后一页数据及页面更新
        :return:
        """
        self.currentPage = self.currentPage + 1
        self.data_list = self.totalData[self.currentPage * self.perPageNum:]
        self.update()

    def setCurrentData(self):
        """
        hsj 设置当前页码的数据
        :return:
        """
        self.data_list = self.totalData[self.currentPage * self.perPageNum:(self.currentPage + 1) * self.perPageNum]

    def refreshPage(self):
        """
        hsj 添加，删除后，刷新当前页内的信息
        :return:
        """
        self.totalData = self.getData()
        self.totalPage = self.getTotalPage()
        self.data_list = self.totalData[self.currentPage * self.perPageNum:(self.currentPage + 1) * self.perPageNum]

    def searchRefreshPage(self, list_data):
        """
        hsj 查询后更新界面
        :return:
        """
        self.totalData = list_data
        self.totalPage = self.getTotalPage()
        self.currentPage = 0
        self.initList()



    # hsj 下面是一般不需要调用，且不需要更改的方法
    def rowCount(self, QModelIndex):
        # print(len(self.data_list))
        return len(self.data_list)

    def columnCount(self, QModelIndex):
        return len(self.headerRow)

    def data(self, index, role):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return self.data_list[row][col]
        elif role == Qt.CheckStateRole:
            if col == 0:
                return Qt.Checked if self.checkList[row] == 'Checked' else Qt.Unchecked
        elif role == Qt.ToolTipRole:
            if col == 0:
                return self.checkList[row]
        elif role == Qt.TextAlignmentRole:
            return QVariant(Qt.AlignCenter)
        return QVariant()

    def setData(self, index, value, role):
        row = index.row()
        col = index.column()
        if role == Qt.CheckStateRole and col == 0:
            self.checkList[row] = 'Checked' if value == Qt.Checked else 'Unchecked'
            # print(self.checkList)
        return True

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable
        return Qt.ItemIsEnabled

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headerRow[section]

    def headerClick(self, isOn):
        self.update()
        self.beginResetModel()
        if isOn:
            self.checkList = ['Checked' for i in range(len(self.data_list))]
        else:
            self.checkList = ['Unchecked' for i in range(len(self.data_list))]
        self.endResetModel()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    tableView = QTableView()
    slt = "ProductID"
    headerRow = ["备注"]
    myModel = MySearchTableModelPIM("T_Product_New", headerRow, slt)
    tableView.setModel(myModel)
    header = CheckBoxHeader()
    tableView.setHorizontalHeader(header)
    header.clicked.connect(myModel.headerClick)
    tableView.showMaximized()
    tableView.show()
    a.exec_()