import qdarkstyle
import sys

import qdarkstyle
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import QSize, Qt

from FaultDiagnosis import FaultDiagnosis
from InStorageView import InStorageWidget
from LifeReminder import LifeReminder
from MaintenanceReminder import MaintenanceReminder
from SearchFaultView import SelectFaultWidget
from SearchMRView import SelectMRWidget
from Maintenance import Maintenance
from OutInputDBTimes import OutInputDBTimes
from OutStorageView import OutStorageWidget
from ProductDeliveryRegistration import ProductDeliveryRegistration
from ProductInventory import ProductInventory
from SearchMWView import SearchMWWidget
from UI.AddProductView import AddProductWidget
from UI.KnowledgeBaseManage import KnowledgeBaseManage
from UI.SearchProductBatchDetailView import SelectProductBatchDetailWidget
from UI.SearchProductComponentTypeView import SearchProductComponentTypeWidget
from UI.SearchProductComponentView import SearchProductComponentWidget
from UI.SearchProductView import SelectProductWidget

from UI.UserManageView import UserManageWidget
from LnfoManageView import LnfoManageWidget
from UI.FunctionManageView import FunctionManageWidget

from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QTreeWidget, QTreeWidgetItem,
                             QGroupBox, QStackedWidget)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize

class AdminHome(QWidget):
    def __init__(self):
        super(AdminHome, self).__init__()
        self.setMinimumHeight(600);
        self.setMinimumWidth(800);
        self.setWindowTitle("决策支持系统")
        ##main_layout.setMargin(5)
        ##main_layout.setSpace(5)
        with open("./leftMenuStyle.qss", 'r', encoding='utf-8') as f:
            self.list_style = f.read()
        self.creat_main_layout()
        self.creat_bar_navigation()
        self.creat_left_box()
        self.setStyleSheet(self.list_style)

    def get_bar_list(self):
        bar_list_item = []
        self.data = []

        from Utils import openDB
        db = openDB()
        query = QSqlQuery()

        bar_list_firstItem = []
        sql_first = "SELECT DISTINCT 备注 FROM Admin_Menu"
        query.exec_(sql_first)
        while (query.next()):
            bar_list_firstItem.append(query.value(0))
        db.commit()

        bar_list_1_inter = []
        sql_1 = "SELECT ChineseName FROM Admin_Menu WHERE 备注 = '%s'" % bar_list_firstItem[0]
        query.exec(sql_1)
        while (query.next()):
            bar_list_1_inter.append(query.value(0))
        db.commit()

        bar_list_2_inter = []
        sql_2 = "SELECT ChineseName FROM Admin_Menu WHERE 备注 = '%s'" % bar_list_firstItem[1]
        query.exec(sql_2)
        while (query.next()):
            bar_list_2_inter.append(query.value(0))
        db.commit()

        bar_list_3_inter = []
        sql_3 = "SELECT ChineseName FROM Admin_Menu WHERE 备注 = '%s'" % bar_list_firstItem[2]
        query.exec(sql_3)
        while (query.next()):
            bar_list_3_inter.append(query.value(0))
        db.commit()

        bar_list_4_inter = []
        sql_4 = "SELECT ChineseName FROM Admin_Menu WHERE 备注 = '%s'" % bar_list_firstItem[3]
        query.exec(sql_4)
        while (query.next()):
            bar_list_4_inter.append(query.value(0))
        db.commit()
        db.close()

        bar_list_1 = []
        bar_list_1.append(bar_list_firstItem[0])
        bar_list_1.append(bar_list_1_inter)

        bar_list_2 = []
        bar_list_2.append(bar_list_firstItem[1])
        bar_list_2.append(bar_list_2_inter)

        bar_list_3 = []
        bar_list_3.append(bar_list_firstItem[2])
        bar_list_3.append(bar_list_3_inter)

        bar_list_4 = []
        bar_list_4.append(bar_list_firstItem[3])
        bar_list_4.append(bar_list_4_inter)

        # bar_list_1 = ["产品信息管理",["产品批次查询", "产品信息查询", "产品组件查询", "组件类型查询",  '产品入库', '产品出库', '产品出入库', '维修保养', '产品交付登记', '产品库存', '寿命到期提醒'，‘维修保养提醒’]]
        # bar_list_2 = ["预防性维修保养管理",['维护方式管理', '维护记录管理']]
        # bar_list_3 = ["故障诊断与知识库管理", ['故障诊断与处理', '知识库管理']]
        # bar_list_4 = ["系统管理", ['业务管理', '用户管理', '日志管理']]
        len1 = len(bar_list_1[1])
        len2 = len(bar_list_2[1]) + len1
        len3 = len(bar_list_3[1]) + len2
        self.data = [0, len1, len2, len3]
        bar_list_item.append(bar_list_1)
        bar_list_item.append(bar_list_2)
        bar_list_item.append(bar_list_3)
        bar_list_item.append(bar_list_4)
        # print(bar_list_item)
        return bar_list_item

    def creat_main_layout(self):
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

    def creat_bar_list(self, data):

        for item in data:
            item_1 = QTreeWidgetItem(self.left_widget)
            item_1.setText(0, item[0])
            ##item_1.setText(0,item[0])
            ## 设置节点的打开/关闭状态下的不同的图片
            icon = QIcon()
            ##节点打开状态
            icon.addPixmap(QPixmap("./Images/" + self.item_iamges[item[0]] + ".png"), QIcon.Normal, QIcon.On)
            item_1.setIcon(0, icon)

            for item_item in item[1]:
                item_1_1 = QTreeWidgetItem(item_1);
                icon = QIcon()
                ##节点打开状态
                icon.addPixmap(QPixmap("./Images/" + self.item_iamges[item_item] + ".png"), QIcon.Normal, QIcon.On)
                item_1_1.setIcon(0, icon)
                item_1_1.setText(0, item_item)
            self.left_widget.addTopLevelItem(item_1);

    def creat_bar_navigation(self):
        data = self.get_bar_list()
        # 获取item_iamages字典 key-value,key为业务名称，value为图标的名称
        self.item_iamges = {
            # 产品信息管理
            data[0][0]: "1",
            data[0][1][0]: "batchsearch",
            data[0][1][1]: "batchsearch",
            data[0][1][2]: "产品出库",
            data[0][1][3]: "产品入库",
            data[0][1][4]: "产品出入库",
            data[0][1][5]: "维修保养",
            data[0][1][6]: "维修记录",
            data[0][1][7]: "产品出入库",
            data[0][1][8]: "寿命到期提醒",
            data[0][1][9]: "寿命到期提醒",
            # 预防性维修保养管理
            data[1][0]: "维修保养",
            data[1][1][0]: "维修方式",
            data[1][1][1]: "维修记录",
            # 故障诊断与知识库管理
            data[2][0]: "故障诊断",
            data[2][1][0]: "故障诊断",
            data[2][1][1]: "知识库管理",
            # 系统管理
            data[3][0]: "用户管理",
            data[3][1][0]: "业务管理",
            data[3][1][1]: "用户管理",
            data[3][1][2]: "维修记录"
        }
        self.left_widget = QTreeWidget()
        self.left_widget.setMinimumWidth(300)
        self.left_widget.setHeaderLabel("左侧导航栏")
        self.left_widget.setColumnCount(1)
        self.left_widget.setMaximumWidth(150)
        self.left_widget.setFocusPolicy(Qt.NoFocus)
        # self.left_widget.setRootIsDecorated(False)

        icon_size = QSize(20, 20)
        self.left_widget.setIconSize(icon_size)

        ##如果treewidget就一列，该列的宽度默认等于treewidget的宽度,两列以上的话才起作用.
        ##self. left_widget.setColumnWidth(0,100);
        # data = self.get_bar_list()
        self.creat_bar_list(data)
        self.main_layout.addWidget(self.left_widget)
        ## QModelIndex
        ##self. left_widget.doubleClicked.connect(self.showModelSelected)
        ## QTreeWidgetItem
        # self. left_widget.itemDoubleClicked.connect(self.showSelected)
        self.left_widget.itemClicked.connect(self.showSelected)

    ## itemObj:QTreeWidgetItem
    def showSelected(self, item, column):
        # 获得父节点
        parent = item.parent()

        index_top = 0
        index_row = -1

        if parent is None:
            index_top = self.left_widget.indexOfTopLevelItem(item)
        else:
            index_top = self.left_widget.indexOfTopLevelItem(parent)
            index_row = parent.indexOfChild(item)

        if index_row != -1:
            self.display(self.data[index_top] + index_row)

    def creat_left_box(self):
        self.right_widget = QStackedWidget(self)
        self.main_layout.addWidget(self.right_widget)
        self.__setUpUI()

    def __setUpUI(self):
        """加载界面UI"""

        # list_str = ['产品批次查询', '产品信息新建', '产品组件查询', '组件类型查询', '产品入库', '产品出库', '产品出入库', '维修保养', '产品交付登记', '产品库存', '寿命到期提醒', '维护方式管理', '维护记录管理', '故障诊断与处理', '知识库管理', '业务管理', '用户管理']
        # 根据list_str设置对应UI
        url_list = [
                    "self.setSearchProductView",            # 1产品信息创建
                    "self.setSearchProductConponentView",   # 2产品组件管理
                    "self.setOutStorageView",               # 3产品出库
                    "self.setInStorageView",                # 4产品入库
                    "self.setOutInputDBTimes",              # 5产品出入库
                    "self.setMaintenance",                  # 6维修保养记录
                    "self.setProductDeliveryRegistration",  # 7产品交付登记
                    "self.setProductInventory",             # 8产品库存
                    "self.setLifeReminder",                 # 9寿命到期提醒
                    "self.setMaintenanceReminder",          # 10维修保养提醒

                    "self.setMaintenanceRecordView",        # 11维修记录
                    "self.setMaintenanceWayView",           # 12维修方式

                    "self.FaultDiagnosis",                  # 13故障诊断
                    "self.setKnowledgeBaseManageWidget",    # 14知识库管理

                    "self.setFunctionManageView",           # 15业务管理
                    "self.setUserManageView",               # 16用户管理
                    "self.setLnfoManageView"]               # 17日志管理

        for i in range(len(url_list)):
            eval(url_list[i] + "()")
        self.right_widget.setCurrentIndex(8)

    def display(self, i):
        # print(self.right_widget.widget(i))
        self.d.queryModel.refreshPage()
        self.d.queryModel.update()
        self.km.queryModel.refreshPage()
        self.km.queryModel.update()
        self.h.queryModel.refreshPage()
        self.h.queryModel.update()
        self.l.queryModel.refreshPage()
        self.h.queryModel.update()
        self.mm.queryModel.refreshPage()
        self.mm.queryModel.update()
        self.l.queryModel.refreshPage()
        self.l.queryModel.update()
        self.right_widget.setCurrentIndex(i)

    def setRightWidget(self, layout):
        """
        设置右部QStackWidget中的内容
        :param layout: 含有相应视图的右部布局
        :return:
        """
        widget = QWidget()
        widget.setLayout(layout)
        self.right_widget.addWidget(widget)

    def setRightWidget1(self, myWidget):
        """
        设置右部QStackWidget中的内容
        :param layout: 含有相应视图的右部布局
        :return:
        """
        widget = QWidget()
        myWidget.setupUi(widget)
        self.right_widget.addWidget(widget)

    def addProductView(self):
        """产品信息添加的UI"""
        self.tt = AddProductWidget()
        self.setRightWidget1(self.tt)

    # def setSearchBatchView(self):
    #     """设置产品批次查询的UI"""
    #     self.a = SelectProductBatchDetailWidget()
    #     self.setRightWidget1(self.a)

    def setSearchProductView(self):
        """设置产品查询的UI"""
        self.b = SelectProductWidget()
        self.setRightWidget1(self.b)

    def setSearchProductConponentTypeView(self):
        """设置产品组件类型查询的UI"""
        self.c = SearchProductComponentTypeWidget()
        self.setRightWidget1(self.c)

    def setSearchProductConponentView(self):
        """设置产品组件查询的UI"""
        self.d = SearchProductComponentWidget()
        self.setRightWidget1(self.d)

    def setInStorageView(self):
        """设置入库管理的UI"""
        self.r = InStorageWidget()
        self.setRightWidget1(self.r)

    def setOutStorageView(self):
        """设置出库管理的UI"""
        self.s = OutStorageWidget()
        self.setRightWidget1(self.s)

    def setKnowledgeBaseManageWidget(self):
        """设置知识库管理UI"""
        self.e = KnowledgeBaseManage()
        self.setRightWidget1(self.e)

    # 设置右侧的业务管理功能
    def setFunctionManageView(self):
        self.f = FunctionManageWidget()
        self.setRightWidget1(self.f)

    # 设置右侧的用户管理界面
    def setUserManageView(self):
        self.e = UserManageWidget()
        self.setRightWidget1(self.e)
        # print("UserManageWidget初始化完成")

    def updateSearchProductBatchDetailWidget(self):
        """
        更新产品批次查询的视图
        :return:
        """
        # self.myWidget.update()
        self.myWidget.queryModel.update()

    def setOutInputDBTimes(self):
        '''产品出入库'''
        self.o = OutInputDBTimes()
        self.setRightWidget1(self.o)

    def setMaintenance(self):
        '''维修保养'''
        self.m = Maintenance()
        self.setRightWidget1(self.m)

    def setProductDeliveryRegistration(self):
        '''产品交付登记'''
        self.km = ProductDeliveryRegistration()
        self.setRightWidget1(self.km)

    def setProductInventory(self):
        '''产品库存'''
        self.i = ProductInventory()
        self.setRightWidget1(self.i)

    def setLifeReminder(self):
        '''寿命到期提醒'''
        self.l = LifeReminder()
        self.setRightWidget1(self.l)

    def setMaintenanceReminder(self):
        '''维保到期提醒'''
        self.mm = MaintenanceReminder()
        self.setRightWidget1(self.mm)

    def setMaintenanceWayView(self):
        """设置维保方式的UI"""
        self.h = SearchMWWidget()
        self.setRightWidget1(self.h)

    def setMaintenanceRecordView(self):
        """设置维保方式的UI"""
        self.j = SelectMRWidget()
        self.setRightWidget1(self.j)

    def FaultDiagnosis(self):
        """
        xcy 设置故障诊断界面
        :return:
        """
        self.k = SelectFaultWidget()
        self.setRightWidget1(self.k)
        #print("设置故障诊断界面")

    def setLnfoManageView(self):
        self.z = LnfoManageWidget()
        self.setRightWidget1(self.z)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = AdminHome()
    window.show()
    sys.exit(app.exec_())