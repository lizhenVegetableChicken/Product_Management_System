import sys
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem, QApplication, QDialog, QVBoxLayout, QMessageBox

from Utils import openDB


def getTreeData(productID, fatherID='无父组件'):
    db = openDB()
    query = QSqlQuery()
    sql = "Select ComponentID, ComponentName, ComponentType, Count From T_ProductComponent_New Where ProductID = '%s' and FatherID = '%s'" % (productID,fatherID)
    # sql = "Select * From T_ProductComponent_New"
    # print(sql)
    query.exec(sql)
    list = []
    while (query.next()):
        list.append([query.value(i) for i in range(4)])
    return list

def setTreeLevel(productID, current_level, root):
    for i in range(len(current_level)):
        levelOne = QTreeWidgetItem(root)
        for j in range(4):
            levelOne.setText(j, str(current_level[i][j]))
        second_level = getTreeData(productID=productID, fatherID=current_level[i][0])
        if second_level:
            setTreeLevel(productID, second_level, levelOne)

def getProductCount(productID):
    db = openDB()
    query = QSqlQuery()
    sql = "Select InitCount From T_Product_New Where ProductID = '%s'" % (productID)
    # sql = "Select * From T_ProductComponent_New"
    # print(sql)
    query.exec(sql)
    result = 0
    if query.next():
        result = query.value(0)
    return result

class TreeWidget(QDialog):
    def __init__(self, productID, productName, init_level=None, fatherID=None, componentType=None, count=None):
        super(TreeWidget, self).__init__()
        self.setWindowTitle('TreeWidget')
        self.tree = QTreeWidget()  # 实例化一个TreeWidget对象
        self.tree.setColumnCount(4)  # 设置部件的列数为2
        self.tree.setHeaderLabels(['产品/组件编号', '产品/组件名称', '类型', '数量'])  # 设置头部信息对应列的标识符
        self.productID = productID
        self.setFixedHeight(800)
        self.setFixedWidth(1200)

        self.tree.setColumnWidth(0, 300)
        self.tree.setColumnWidth(1, 300)
        self.tree.setColumnWidth(2, 300)
        self.tree.setColumnWidth(3, 300)
        productCount = getProductCount(productID)
        # 设置root为self.tree的子树，故root是根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, str(productID))  # 设置根节点的名称
        root.setText(1, str(productName))
        root.setText(2, '产品')
        root.setText(3, str(productCount))
        if not init_level:
            first_level = getTreeData(self.productID)
        else:
            first_level = init_level
            root.setText(0, str(fatherID))
            root.setText(2, str(componentType))
            root.setText(3, str(count))
        if first_level:
            self.isNone = False
            setTreeLevel(self.productID, first_level, root)
        else:
            QMessageBox.information(QDialog(), "提示！", "该产品暂无其他组件，请为其添加后查看！", QMessageBox.Yes, QMessageBox.Yes)
            self.isNone = True

        # 为root节点设置子结点
        # child1 = QTreeWidgetItem(root)
        # child1.setText(0, 'child1')
        # child1.setText(1, 'name1')
        # child2 = QTreeWidgetItem(root)
        # child2.setText(0, 'child2')
        # child2.setText(1, 'name2')
        # child3 = QTreeWidgetItem(root)
        # child3.setText(0, 'child3')
        # child4 = QTreeWidgetItem(child3)
        # child4.setText(0, 'child4')
        # child4.setText(1, 'name4')

        self.tree.addTopLevelItem(root)
        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)
        self.tree.expandAll()
