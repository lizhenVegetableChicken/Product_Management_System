import sys

import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QStackedWidget

from PyQt5.QtCore import QSize, Qt

from FaultDiagnosis import FaultDiagnosis
from FunctionManageView import FunctionManageWidget
from InStorageView import InStorageWidget
from LifeReminder import LifeReminder
from MR_SearchMRView import SelectMRWidget
from Maintenance import Maintenance
from OutInputDBTimes import OutInputDBTimes
from OutStorageView import OutStorageWidget
from ProductDeliveryRegistration import ProductDeliveryRegistration
from ProductInventory import ProductInventory
from SearchMWView import SearchMWWidget
from UI.AddProductView import AddProductWidget
from UI.KnowledgeBaseManage import KnowledgeBaseManage
from UI.SearchProductBatchDetailView import SelectProductBatchDetailWidget
from Thread.SearchProductBatchThread import SearchProductBatchDetailThread
from UI.SearchProductComponentTypeView import SearchProductComponentTypeWidget
from UI.SearchProductComponentView import SearchProductComponentWidget
from UI.SearchProductView import SelectProductWidget
from UserManageView import UserManageWidget
from Utils import openDB


class AdminHome(QWidget):
    """登录后的主界面，该界面采用侧边栏+内容区相结合的方式"""
    def __init__(self):
        super(AdminHome, self).__init__()
        # 设置窗口大小和标题
        # self.resize(900, 600)
        self.setWindowTitle("欢迎使用产品管理系统")
        # 导入QListWidget的qss样式
        with open("./QListWidgetQSS.qss", 'r') as f:
            self.list_style = f.read()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        # 左侧选项表
        # self.left_widget = QListWidget()
        # self.left_widget.setStyleSheet(self.list_style)

        self.create_bar_navigation()
        widget = QWidget()
        layout_1 = QVBoxLayout()
        layout_1.addWidget(self.left_widget)
        widget.setLayout(layout_1)
        self.main_layout.addWidget(widget)
        # 右侧内容区
        self.right_widget = QStackedWidget(self)
        self.main_layout.addWidget(self.right_widget)
        # 刷新查询批次界面
        # self.table_thread = SearchProductBatchDetailThread()
        # self.table_thread.update_date.connect(self.updateSearchProductBatchDetailWidget)
        # self.table_thread.start()
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        self.resize(self.width, self.height)
        self.showMaximized()
        self.__setUpUI()

    def create_bar_navigation(self):
        self.left_widget = QTreeWidget()
        self.left_widget.setHeaderLabel("左侧导航栏")
        self.left_widget.setColumnCount(1)
        self.setMaximumWidth(300)

        icon_size = QSize(100, 30)
        self.left_widget.setIconSize(icon_size)

        data = self.getBarList()
        self.create_bar_list(data)
        self.left_widget.itemClicked.connect(self.itemClicked)

    def getBarList(self):
        bar_list_item = []
        bar_list_1 = ["产品批次查询", "产品信息新建", "产品组件查询", "组件类型查询"]
        bar_list_2 = ['产品入库', '产品出库', '产品出入库']
        bar_list_item.append(bar_list_1)
        bar_list_item.append(bar_list_2)
        return bar_list_item

    def create_bar_list(self, data):
        for item in data:
            item1 = QTreeWidgetItem(self.left_widget)
            for item_item in item:
                item1_1 = QTreeWidgetItem(item1)
                item1_1.setText(0, item_item)
            self.left_widget.addTopLevelItem(item1)

    def itemClicked(self, item, column):
        # 获得父节点
        parent = item.parent()

        index_top = 0
        index_row = -1

        if parent is None:
            index_top = self.left_widget.indexOfTopLevelItem(item)
        else:
            index_top = self.left_widget.indexOfTopLevelItem(parent)
            index_row = parent.indexOfChild(item)

        data = [0, 4, 7]
        if index_row != -1:
            self.display(data[index_top] + index_row)
            # print(data[index_top] + index_row)


    def __setUpUI(self):
        """加载界面UI"""
        # # list和右边窗口的index对应绑定
        # self.left_widget.currentRowChanged.connect(self.display)
        # # 去掉边框
        # self.left_widget.setFrameShape(QListWidget.NoFrame)
        # # 隐藏滚动条
        # self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['产品批次查询', '产品信息新建', '产品组件查询', '组件类型查询', '产品入库', '产品出库', '产品出入库', '维修保养', '产品交付登记', '产品库存', '寿命到期提醒', '知识库管理', '维护方式管理', '维护记录管理', '故障诊断与处理', '业务管理', '用户管理']
        # 根据list_str设置对应UI
        url_list = ["self.setSearchBatchView",                  #1
                    "self.setSearchProductView",                #2
                    "self.setSearchProductConponentView",       #3
                    "self.setSearchProductConponentTypeView",   #4
                    "self.setInStorageView",
                    "self.setOutStorageView",
                    "self.setOutInputDBTimes",                  #6
                    "self.setMaintenance",                      #7
                    "self.setProductDeliveryRegistration",      #8
                    "self.setProductInventory",
                    "self.setLifeReminder",
                    "self.setKnowledgeBaseManageWidget",        #5
                    "self.setMaintenanceWayView",               #8
                    "self.setMaintenanceRecordView",            #9
                    "self.FaultDiagnosis",
                    "self.setFunctionManageView",
                    "self.setUserManageView" ]               #12

        for i in range(len(list_str)):
            # # 左侧选项的添加
            # self.item = QListWidgetItem(list_str[i], self.left_widget)
            # self.item.setSizeHint(QSize(30, 60))
            # self.item.setTextAlignment(Qt.AlignCenter)
            # 根据对应函数设置右侧显示内容
            eval(url_list[i] + "()")

    # def __setUpUI(self):
    #     """加载界面UI"""
    #     # list和右边窗口的index对应绑定
    #     self.left_widget.currentRowChanged.connect(self.display)
    #     # 去掉边框
    #     self.left_widget.setFrameShape(QListWidget.NoFrame)
    #     # 隐藏滚动条
    #     self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    #     self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    #
    #     #list_str = ['产品批次查询', '产品信息新建', '产品组件查询', '组件类型查询', '出库信息管理', '信息统计', '维护方式管理', '维护记录管理', '故障诊断与处理', '知识库管理', '用户管理']
    #     list_str = list()
    #     #链接数据库
    #     db = openDB()
    #     #查询出isvalid为true的项显示
    #     q = QSqlQuery()
    #     #当isvalid为false时，list对应窗口会出错
    #     sql_code = "SELECT ChineseName FROM Admin_Menu WHERE IsValid = '%s'" % "true"
    #     if q.exec_(sql_code):
    #         while q.next():
    #             string = q.value(0)
    #             list_str.append(string)
    #
    #     #出现问题，很奇怪，list_str与url_list不对应
    #     # 根据list_str设置对应UI
    #     #url_list = ["self.setSearchBatchView", "self.setSearchProductView", "self.setSearchProductConponentView", "self.setSearchProductConponentTypeView", "self.setKnowledgeBaseManageWidget", "self.test", "self.test", "self.test", "self.test", "self.test", "self.test", "self.test"]
    #     url_list = ["self.setSearchBatchView",                  #1
    #                 "self.setSearchProductView",                #2
    #                 "self.setSearchProductConponentView",       #3
    #                 "self.setSearchProductConponentTypeView",   #4
    #                 "self.setOutInputDBTimes",                  #6
    #                 "self.setMaintenance",                      #7
    #                 "self.setProductDeliveryRegistration",      #8
    #                 "self.setProductInventory",
    #                 "self.setLifeReminder",
    #                 "self.setKnowledgeBaseManageWidget",        #5
    #                 "self.test",                                #6
    #                 "self.test",                                #7
    #                 "self.test",                                #8
    #                 "self.test",                                #9
    #                 "self.setUserManageView",                   #10
    #                 "self.setKnowledgeBaseManageWidget",        #11
    #                 "self.setFunctionManageView"]               #12
    #     db.close()
    #     for i in range(len(list_str)):
    #         # 左侧选项的添加
    #         self.item = QListWidgetItem(list_str[i], self.left_widget)
    #         self.item.setSizeHint(QSize(30, 60))
    #         self.item.setTextAlignment(Qt.AlignCenter)
    #         # 根据对应函数设置右侧显示内容
    #         #print(i)
    #         #print(url_list[i] + "()")
    #         eval(url_list[i] + "()")


    def display(self, i):
        # print(self.right_widget.widget(i))
        # self.a.queryModel.update()
        # self.b.queryModel.update()
        # self.c.queryModel.update()
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

    def setSearchBatchView(self):
        """设置产品批次查询的UI"""
        self.a = SelectProductBatchDetailWidget()
        self.setRightWidget1(self.a)

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
        #print(11111)
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
        self.d = ProductDeliveryRegistration()
        self.setRightWidget1(self.d)

    def setProductInventory(self):
        '''产品库存'''
        self.i = ProductInventory()
        self.setRightWidget1(self.i)

    def setLifeReminder(self):
        '''寿命到期提醒'''
        self.l = LifeReminder()
        self.setRightWidget1(self.l)

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
        self.k = FaultDiagnosis()
        self.setRightWidget1(self.k)
        #print("设置故障诊断界面")


    def test(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = AdminHome()
    mainMindow.show()
    sys.exit(app.exec_())


