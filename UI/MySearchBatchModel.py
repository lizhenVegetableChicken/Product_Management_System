import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)

from Login_recorder import logToFile, getCurrentUserId
from Utils import openDB


class CheckBoxHeader(QHeaderView):
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


class MySearchTableModel(QAbstractTableModel):
    def __init__(self, table, headerRow, parent=None):
        """
        hsj 初始化TableModel
        :param table: 查询的表
        :param headerRow: 查询显示界面的标题
        :param parent:
        """

        super(MySearchTableModel, self).__init__(parent)

        self.table = table
        self.headerRow = headerRow
        self.tableLength = self.getcolumnCount() + 4
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

        # self.data_list = self.getData()
        # Keep track of which object are checked
        # self.headerRow = ["批次号", "ID", "产品编号", "交付日期", "交付单位", "交付人员", "接收单位", "接收人员", "创建人员ID", "创建时间", "修改人员ID", "修改时间", "备注"]

        self.checkList = ['Unchecked' for i in range(len(self.data_list))]

    def setTableInformation(self):
        """
        hsj 设置表相关信息
        :return:
        """
        if self.table == "T_Product_New":  # 黄帅杰开始
            self.tableKey = "ProductID"
            self.tableLength = 21
        elif self.table == "T_ProductComponent_New":
            self.tableKey = "ComponentID"
            self.tableLength = 14
            self.tableForeign = "T_Product_new"
            self.tableForeignKey = "ProductID"
            self.tableForeignKeyPosition = 5 # 在本表中是根据本表主键在外表中查询
            self.tableForeignLength = 14
        elif self.table == "T_Diagnose":
            self.tableKey = "FaultID"
            self.tableLength = 8
        elif self.table == "T_Product_Component":
            self.tableKey = "ID"
            # self.tabeLength = 17-4  # 黄帅杰结束
        elif self.table == "T_Out_Detail":  # 许帅开始
            self.tableKey = "ID"
            self.tableLength = 12
        elif self.table == "T_In_Detail":
            self.tableKey = "ID"
            self.tableLength = 13  # 许帅结束
        elif self.table =="T_Knowladge_Base_Mangement":#陈智卿开始
            self.tableKey="Num"
            # self.tableLength = 8
            self.tableForeign = "T_Knowladge_Base_Mangement"
            self.tableForeignKey = "Num"
            self.tableForeignKeyPosition = 0
            self.tableForeignLength = 9                #陈智卿结束
        elif self.table == "User":  # 刘敬楷开始
            self.tableKey = "UserId"
            self.tableLength = 5
        elif self.table == "Admin_Menu":
            self.tableKey = "ID"
            self.tableLength = 7  # 刘敬楷结束
        elif self.table == "MaintenanceRecord":  # 李振开始
            self.tableKey = "mrID"
            self.tableLength = 18
        elif self.table == "MaintenanceWay":
            self.tableKey = "MaintenanceWayID"
            self.tableLength = 18
            # 要查询的第二张表的名字
            # self.tableForeign = "Product"
            # self.tableForeignKey = "ProductID"
            # self.tableForeignKeyPosition = 2
            # self.tableForeignLength = 14  # 李振结束
        elif self.table== "T_Fault_Diagnosis":  # 薛程耀开始
            self.tableKey="batchNO"
            # self.tableLength = 5  # 薛程耀结束
        elif self.table == "Login_info":
            self.tableKey = "id"

    def initList(self):
            """
            hsj 初始化界面数据
            :return:
            """
            if len(self.totalData) <= self.perPageNum:
                self.data_list = self.totalData
            else:
                self.data_list = self.totalData[:self.perPageNum]

    def delete(self):
        """
        hsj 删除选中的数据
        :return:
        """
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                # sql = "DELETE FROM T_Product_BatchDetail WHERE BatchNO = '%s'" % (self.data_list[i][0])
                sql = "DELETE FROM %s WHERE %s = '%s'" % (self.table, self.tableKey,self.data_list[i][0])
                query.exec(sql)
                # sql = "DELETE FROM T_Product WHERE ProductNO = '%s'" % (self.data_list[i][2])
                # query.exec(sql)
                # sql = "DELETE FROM T_Product_Component WHERE ProductID = '%s'" % (self.data_list[i][2])
                # query.exec(sql)
        db.commit()
        self.refreshPage()

    def deleteProduct(self):
        """
        hsj 删除选中的产品，并且关联删除
        :return:
        """
        UserId = getCurrentUserId()
        logger = logToFile()

        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "DELETE FROM T_Product_New WHERE ProductID = '%s'" % (self.data_list[i][0])
                logger.info("用户："+str(UserId)+" 删除了 T_Product_New 表（产品信息表）中的产品ID为："+str(self.data_list[i][0])+"的数据项")
                #print(sql)
                query.exec(sql)
                sql = "DELETE FROM T_ProductComponent_New WHERE ProductID = '%s'" % (self.data_list[i][0])
                logger.info("用户：" + str(UserId) + " 删除 T_ProductComponent_New 表（产品组件表）中的产品ID为：" + str(self.data_list[i][0]) + "的数据项")
                print(sql)
                sql = "DELETE FROM MaintenanceWay WHERE ProductID = '%s'" % (self.data_list[i][0])
                logger.info("用户：" + str(UserId) + " 删除 MaintenanceWay 表（维保方式表）中的产品ID为：" + str(self.data_list[i][0]) + "的数据项")
                query.exec(sql)
        db.commit()
        self.refreshPage()

    def deleteCompoment(self):
        """
        hsj 删除选中的组件及关联删除
        :return:
        """
        UserId = getCurrentUserId()
        logger = logToFile()

        self.db = openDB()
        self.query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "DELETE FROM %s WHERE %s = '%s'" % (self.table, self.tableKey, self.data_list[i][0])
                self.query.exec(sql)
                logger.info("用户：" + str(UserId) + " 删除了 " + str(self.table) + " 表中的主键 " + str(self.tableKey) + " = " + str(self.data_list[i][0]) + "的组件，及其全部子组件")
                # sql = "DELETE FROM T_Product WHERE ProductNO = '%s'" % (self.data_list[i][2])
                # query.exec(sql)
                # sql = "DELETE FROM %s WHERE FatherID = '%s' AND ProductID = '%s'" % (self.table, self.data_list[i][0], self.data_list[i][1])
                self.deleteComponent_Sub(self.data_list[i][0])
                # print(sql)
                self.query.exec(sql)
                # sql = "DELETE FROM T_Product_Component WHERE ProductID = '%s'" % (self.data_list[i][2])
                # query.exec(sql)
        self.db.commit()

        self.refreshPage()

    def deleteComponent_Sub(self, fatherID):
        # 删除所有的子组件

        sql = "SELECT ComponentID FROM T_ProductComponent_New WHERE FatherID = '%s'" % (fatherID)
        self.query.exec(sql)
        list = []
        while (self.query.next()):
            list.append(self.query.value(0))
        for i in list:
            sql = "DELETE FROM T_ProductComponent_New WHERE ComponentID = '%s'" % (i)
            self.query.exec(sql)
            self.deleteComponent_Sub(i)

    def deleteMWByExactID(self, id):
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

    def deleteMRByExactID(self, id):
        """
        李振
        :return:
        """
        db = openDB()
        query = QSqlQuery()
        print("这里执行了：")
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "DELETE FROM MaintenanceRecord WHERE ProductID = '%s'" % id
                query.exec(sql)
        db.commit()
        self.refreshPage()

    def deleteMW(self):

        """
        李振
        :return:
        """
        db = openDB()
        query = QSqlQuery()
        print("这里执行了：")
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "DELETE FROM MaintenanceWay WHERE MaintenanceWayID = '%s'" % (self.data_list[i][0])
                query.exec(sql)
        db.commit()
        self.refreshPage()

    def deleteMR(self):
        """
        李振
        :return:
        """
        db = openDB()
        query = QSqlQuery()
        print("这里执行了：")
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "DELETE FROM MaintenanceRecord WHERE MrID = '%s'" % (self.data_list[i][0])
                query.exec(sql)
        db.commit()
        self.refreshPage()

    def deleteIn(self):
        """
        许帅 删除选中的入库信息，并且关联删除
        :return:
        """
        logger = logToFile()
        UserId = getCurrentUserId()

        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                global count
                global no
                sql = "SELECT ProductID,InCount FROM T_In_Detail WHERE InNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
                if query.next():
                    no = query.value(0)
                    count = query.value(1)
                sql = "UPDATE T_Product_New SET Count=Count-'%s' WHERE ProductID='%s'" % \
                      (int(count), no)
                query.exec(sql)
                sql = "DELETE FROM T_In_Detail WHERE InNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
                logger.info("用户：" + str(UserId) + " 删除了 T_In_Detail 表中入库编号为 "+ self.data_list[i][0]+" 的数据 "+ str(self.data_list[i]))
                sql = "DELETE FROM T_In_Base WHERE InNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
                logger.info("用户：" + str(UserId) + " 删除了 T_In_Base 表中入库编号为 "+ self.data_list[i][0]+" 的数据 "+str(self.data_list[i]))
        db.commit()
        self.refreshPage()

    def deleteOut(self):
        """
       许帅 删除选中的出库信息，并且关联删除
        :return:
        """
        logger = logToFile()
        UserId = getCurrentUserId()
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                global count
                global no
                sql = "SELECT ProductID,OutCount FROM T_Out_Detail WHERE OutNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
                if query.next():
                    no = query.value(0)
                    count = query.value(1)
                sql = "UPDATE T_Product_New SET Count=Count+'%s' WHERE ProductID='%s'" % \
                      (int(count), no)
                query.exec(sql)
                sql = "DELETE FROM T_Out_Detail WHERE OutNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
                logger.info("用户：" + str(UserId) + " 删除了 T_Out_Detail 表中出库编号为 "+ self.data_list[i][0]+" 的数据 "+ str(self.data_list[i]))
                sql = "DELETE FROM T_Out_Base WHERE OutNO = '%s'" % (self.data_list[i][0])
                query.exec(sql)
                logger.info("用户：" + str(UserId) + " 删除了 T_Out_Base 表中出库编号为 "+ self.data_list[i][0]+" 的数据 "+ str(self.data_list[i]))
        db.commit()
        self.refreshPage()

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

    def selectNum(self):
        """
        hsj 选中的行号
        :return:
        """
        n = 0
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                n = i
                break
        return n

    def getAllCheckedData(self):
        list = []
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "SELECT * FROM %s WHERE %s = '%s'" % (self.table, self.tableKey, self.data_list[i][0])
                query.exec(sql)
            if query.next():
                list000 = []
                for i in range (self.tableLength):
                    list000.append(query.value(i))
                list.append(list000)
        db.close()
        return list

    def selectSingleTable(self):
        """
        hsj 查询单个表信息
        :return:
        """
        list = []
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "SELECT * FROM %s WHERE %s = '%s'" % (self.table, self.tableKey, self.data_list[i][0])
                if self.table == "T_Out_Detail":
                    sql = "SELECT * FROM T_Out_Detail WHERE OutNO='%s'" % (self.data_list[i][0])
                if self.table == "T_In_Detail":
                    sql = "SELECT * FROM T_In_Detail WHERE InNO='%s'" % (self.data_list[i][0])
                query.exec(sql)
                break
        if query.next():
            list = [str(query.value(i)) for i in range(self.tableLength)]
        # print(list)
        return list

    def selectMultipleTable(self):
        """
        hsj 查询表多个信息
        :return:
        """
        list = []
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "SELECT * FROM %s WHERE %s = '%s'" % (self.table, self.tableKey, self.data_list[i][0])
                query.exec(sql)

                if query.next():
                    list.append([str(query.value(i)) for i in range(self.tableLength)])
        # print(list)
        return list

    def searchTable(self, select_condition, content):
        """
        hsj 根据条件查询信息，并返回界面
        :param select_condition: 列名
        :param content: 具体查询条件
        :return:
        """
        list = []
        db = openDB()
        query = QSqlQuery()
        sql = "SELECT * FROM %s WHERE %s LIKE '%%%s%%' ORDER BY %s" % (self.table, select_condition, content, self.tableKey)
        if self.table == "T_Out_Detail":
            sql = "SELECT T_Out_Detail.OutNO,ProductID,OutStorageNO,OutDate," \
                  "OutCount,RecorderID,UsedID,UsedDepartmentID FROM T_Out_Detail,T_Out_Base " \
                  "WHERE T_Out_Base.ID=T_Out_Detail.ID and T_Out_Detail.%s='%%%s%%'" % (select_condition, content)
        if self.table == "T_In_Detail":
            sql = "SELECT T_In_Detail.InNO,ProductID,InStorageNO,InDate,InCount," \
                  "InRecoder,OutNO FROM T_In_Detail,T_In_Base WHERE T_In_Detail.ID=T_In_Base.ID " \
                  "and T_In_Detail.%s='%%%s%%'" % (select_condition, content)
        if self.table == "T_Diagnose":
            sql = "SELECT FaultID, FaultName, ProductName, AnswerCount, KnowledgeID FROM %s WHERE %s LIKE '%%%s%%' ORDER BY %s" % (self.table, select_condition, content, self.tableKey)
        if self.table == "T_Product_New":
            sql = "SELECT ProductID, ProductName, ProductNO, BatchNO, Count, ReceiverDate, Receiver, ReceiverCompany, RegisterDate, Registerer, RegisterCompany FROM %s WHERE %s LIKE '%%%s%%' ORDER BY %s" % (self.table, select_condition, content, self.tableKey)
            # print(sql)
        elif self.table == "T_ProductComponent_New":
            sql = "SELECT ComponentID, ProductID, ComponentNO, ComponentName, FatherID, ComponentType, Count FROM %s WHERE %s LIKE '%%%s%%' ORDER BY %s" % (self.table, select_condition, content, self.tableKey)
        elif self.table == 'MaintenanceWay':
            sql = "SELECT MaintenanceWayID,MaintenanceWayName, ProductID, ProductName,ProductNO,Interva,AlterRule,RecentTime FROM %s WHERE %s LIKE '%%%s%%' ORDER BY %s" % (self.table, select_condition, content, self.tableKey)
        elif self.table == 'MaintenanceRecord':
            sql = "SELECT MrID,ProductID,ProductName,MwID, MwName," \
                  " MrTime, MrPart, MrLead, MrResult, Remark FROM %s WHERE %s LIKE '" \
                  "%%%s%%' ORDER BY %s" % (self.table, select_condition, content, self.tableKey)
        elif self.table == 'T_Knowladge_Base_Mangement':
            sql = "SELECT Num,Title, Source, Publisher, Rtime, Etime, Readrange, Content FROM %s WHERE %s LIKE '%%%s%%' ORDER BY %s" % (self.table, select_condition, content, self.tableKey)
        print(sql)
        query.exec(sql)
        while query.next():
            list.append([str(query.value(i)) for i in range(self.tableLength)])
        # print(list)
        self.searchRefreshPage(list)
        self.update()

    def getData(self):
        """
        获取所有数据
        :return:
        """
        results = []
        sql = "SELECT * FROM %s ORDER BY %s" % (self.table, self.tableKey)
        db = openDB()
        query = QSqlQuery()
        if self.table == "T_Product_New":
            sql = "SELECT ProductID, ProductName, ProductNO, BatchNO, Count, ReceiverDate, Receiver, ReceiverCompany, RegisterDate, Registerer, RegisterCompany FROM %s ORDER BY %s" % (self.table, self.tableKey)
            # print(sql)
        elif self.table == "T_ProductComponent_New":
            sql = "SELECT ComponentID, ProductID, ComponentNO, ComponentName, FatherID, ComponentType, Count FROM %s ORDER BY %s" % (
            self.table, self.tableKey)
        elif self.table == "T_Out_Detail":
            sql = "SELECT T_Out_Detail.OutNO,ProductID,OutStorageNO,OutDate," \
                  "OutCount,RecorderID,UsedID,UsedDepartmentID FROM T_Out_Detail,T_Out_Base " \
                  "WHERE T_Out_Base.ID=T_Out_Detail.ID ORDER BY T_Out_Detail.ID "
        elif self.table == "T_In_Detail":
            sql = "SELECT T_In_Detail.InNO,ProductID,InStorageNO,InDate,InCount," \
                  "InRecoder,OutNO FROM T_In_Detail,T_In_Base WHERE T_In_Detail.ID=T_In_Base.ID " \
                  "ORDER BY T_In_Detail.ID "
        elif self.table == "T_Diagnose":
            sql = "SELECT FaultID, FaultName, ProductName, AnswerCount, KnowledgeID FROM %s ORDER BY %s" % (self.table, self.tableKey)
        elif self.table == 'MaintenanceRecord':
            sql = 'SELECT MrID,ProductID,ProductName,MwID, MwName, MrTime, MrPart, ' \
                  'MrLead, MrResult, Remark FROM %s ORDER BY %s' % (self.table, self.tableKey)
        elif self.table == 'MaintenanceWay':
            sql = 'SELECT MaintenanceWayID,MaintenanceWayName, ProductID, ProductName,ProductNO,Interva,AlterRule,RecentTime FROM %s ORDER BY %s' % (
            self.table, self.tableKey)
        elif self.table == 'T_Knowladge_Base_Mangement':
            sql = "SELECT Num,Title, Source, Publisher, Rtime, Etime, Readrange, Content FROM %s ORDER BY %s" % (self.table, self.tableKey)

        # elif self.table == "T_Product_BatchDetail":
        #     sql = "SELECT BatchNO, ProductNO, DeliverDate, DeliverCompanyName, Deliverer, ReceiveCompanyName, Receiver, Remark, Document FROM %s ORDER BY %s" % (self.table, self.tableKey)
        #     # print(sql)
        # elif self.table == "T_Product":
        #     sql = "SELECT ProductNO, Life, StartDate, DaysBefore, IsUsedCountLimit, MaxUsedCount, HaveUsedCount, Remark FROM %s ORDER BY %s" % (self.table, self.tableKey)
        #     # print(sql)
        # elif self.table == "T_Product_Component":
        #     sql = "SELECT ID, ProductNO, ComponentName, ComponentTypeID, ParentID, IsLifeRemind, Life, StartDate, DaysBefore, IsUsedCountLimit, MaxUsedCount, HaveUsedCount, Remark FROM %s ORDER BY %s" % (self.table, self.tableKey)
        #     # self.tableLength = 8
        #     # print(sql)

        a = query.exec(sql)
        # print('a', a)
        while(query.next()):
            results.append([query.value(i) for i in range(self.tableLength)])
        # print(results)
        return results

        # 返回选择的所有数据项
    def getSelectedID(self):
        # 获取被选中产品的产品编号
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                return self.data_list[i][0], self.data_list[i][1]

    def getSelectedComponentID(self):
        # 获取被选中产品的产品编号
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                return self.data_list[i][0], self.data_list[i][1], self.data_list[i][3], self.data_list[i][5], self.data_list[i][6]

    def getAllCheckedData(self):
        list = []
        db = openDB()
        query = QSqlQuery()
        for i, isSelected in enumerate(self.checkList):
            if isSelected == "Checked":
                sql = "SELECT * FROM %s WHERE %s = '%s'" % (self.table, self.tableKey, self.data_list[i][0])
                query.exec(sql)
            if query.next():
                list000 = []
                for i in range (self.tableLength):
                    list000.append(query.value(i))
                list.append(list000)
        db.close()
        return list

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
        if self.data_list==[]:
            self.currentPage = self.currentPage if self.currentPage > 1 else 0
            self.data_list = self.totalData[(self.currentPage-1) * self.perPageNum:(self.currentPage + 1) * self.perPageNum]

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

    def getcolumnCount(self):
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
    headerRow = ["批次号", "ID", "产品编号", "交付日期", "交付单位", "交付人员", "接收单位", "接收人员", "创建人员ID", "创建时间", "修改人员ID", "修改时间", "备注"]
    myModel = MySearchTableModel("T_Product_New", ["ProductID"])
    tableView.setModel(myModel)
    header = CheckBoxHeader()
    tableView.setHorizontalHeader(header)
    header.clicked.connect(myModel.headerClick)
    tableView.showMaximized()
    tableView.show()
    a.exec_()