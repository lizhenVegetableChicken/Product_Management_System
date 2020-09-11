import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QTableView, QHeaderView, QMessageBox, QDialog, QWidget, QApplication

from UI.MySearchBatchModelPIM import CheckBoxHeader, MySearchTableModelPIM


class MySearchWidgetPIM(object):
    # 俞欣
    def __init__(self):

        # 搜索关键列的列表 一般大小为3
        self.select_conditions = []
        # 在setupUi中进行重写
        self.queryModel = MySearchTableModelPIM("T_Product_BatchDetail", ["BatchNO"],"ProductName,ProductCode,ProductNOS,Counts")
        self.totalPageLabel = QtWidgets.QLabel()
        self.totalPageLabel.setObjectName("totalPageLabel")

        self.jumpEdit = QtWidgets.QLineEdit()
        self.jumpEdit.setMaximumSize(QtCore.QSize(50, 50))

    def setupUi(self, Form):
        pass

    def retranslateUi(self, Form):
        pass

    def updateUI(self):
        """
        hsj 跳转的后更新
        :return:
        """
        self.totalPageLabel.setText("/  " + str(self.queryModel.totalPage) + "  页")
        self.jumpEdit.setText(str(self.queryModel.currentPage + 1))

    def bindButton(self):
        """
        hsj 绑定按钮
        :return:
        """
        pass

    '''def deleteButtonEvent(self):
        """
        hsj 删除批次按钮绑定事件
        :return:
        """
        # print(self.queryModel.checkList.count("Checked"))
        # 如果没有选中数据，则提示无数据
        if self.queryModel.checkList.count("Checked") == 0:
            QMessageBox.warning(QDialog(), "警告", "没有数据被选中，请选中后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return
        a = QMessageBox.information(QDialog(), "提示", "是否确认删除？", QMessageBox.Yes, QMessageBox.No)
        if a == QMessageBox.No:
            return
        self.queryModel.delete()
        self.queryModel.update()'''

    '''def addButtonEvent(self, Widget):
        """
        hsj 新建产品批次
        :param Widget: 要显示的窗体
        :return:
        """
        form = QDialog()
        w = Widget
        w.setupUi(form)
        form.show()
        a = form.exec_()
        # 如果对话框关闭，则对查询数据进行更行
        if a == 0:
            self.queryModel.refreshPage()
            self.queryModel.update()
            self.updateUI()'''

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

    '''def updateButtonEvent(self, Widget):
        """
        hsj 修改产品批次信息
        :param Widget: 要显示的窗体
        :return:
        """
        # 判断复选框是否只选中一个
        a = self.isCorrect()
        if a == 0:
            return
        result = self.queryModel.selectSingleTable()
        batchDialog = Widget
        form = QDialog()
        batchDialog.setupUi(form)
        batchDialog.updateData(result, self.queryModel)
        form.show()
        a = form.exec()
        # 如果对话框关闭，则对查询数据进行更行
        if a == 0:
            self.queryModel.refreshPage()
            self.queryModel.update()
'''
    def preButtonEvent(self):
        """
        hsj 上一页按钮事件
        :return:
        """
        if self.queryModel.currentPage == 0:
            QMessageBox.information(QDialog(), "提示", "已经是第一页！", QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            self.queryModel.prePage()
            self.queryModel.update()
            self.updateUI()

    def nextButtonEvent(self):
        """
        hsj 下一页按钮事件
        :return:
        """
        if (self.queryModel.currentPage + 1) == self.queryModel.totalPage:
            QMessageBox.information(QDialog(), "提示", "已经是最后一页！", QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            self.queryModel.nextPage()
            self.queryModel.update()
            self.updateUI()

    def jumpButtonEvent(self):
        """
        hsj 跳转按钮事件
        :return:
        """
        objectPage = self.jumpEdit.text()
        if not objectPage.isdigit():
            QMessageBox.information(QDialog(), "提示", "跳转输入的不是数字，请正确填写后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            objectPage = int(objectPage)
            if objectPage <= 0 or objectPage > self.queryModel.totalPage:
                QMessageBox.information(QDialog(), "提示", "跳转输入超出范围，请正确填写后重试！", QMessageBox.Yes, QMessageBox.Yes)
                return
            else:
                self.queryModel.currentPage = objectPage - 1
                self.queryModel.setCurrentData()
                self.queryModel.update()
                self.updateUI()

    '''def searchButtonEvent2(self):
        """
        hsj 输入查询条件查询按钮事件
        加一个日期修正函数
        :return:
        """
        content = []

        if self.dateEdit.text() != "":
            content.append(self.dateEdit.text())
        if self.dateEdit_2.text() != "":
            content.append(self.dateEdit_2.text())
        if self.searchEdit.text() != "":
            content.append(self.searchEdit.text())

        if content == "":
            print(111)
            self.queryModel.refreshPage()
            self.queryModel.update()
        else:
            # n = self.comboBox.currentIndex()
            if len(content) == 1 and self.searchEdit.text() == "":
                if self.dateEdit.text() != "":
                    sql = "WHERE %s >= '%s'" % (
                        self.select_conditions[0], content[0])
                else:
                    sql = "WHERE %s <= '%s'" % (
                        self.select_conditions[0], content[0])
            elif len(content) == 2:
                if self.searchEdit.text() == "":
                    sql = "WHERE %s >= '%s' and %s <= '%s'" % (
                        self.select_conditions[0], content[0], self.select_conditions[0], content[1])
                elif self.dateEdit_2.text() == "":
                    sql = "WHERE %s >= '%s' and %s == '%s'" % (
                        self.select_conditions[0], content[0], self.select_conditions[1], content[1])
                else:
                    sql = "WHERE %s <= '%s' and %s == '%s'" % (
                        self.select_conditions[0], content[0], self.select_conditions[1], content[1])
            elif len(content) == 3:
                sql = "WHERE %s >= '%s' and %s <= '%s' and %s = '%s'" % (
                    self.select_conditions[0], content[0], self.select_conditions[0], content[1],
                    self.select_conditions[1], content[2])

        #if self.comboBox = true:
         #   n = self.comboBox.currentIndex()

        #self.queryModel.searchTable(sql)
                # self.queryModel.searchTable(self.select_conditions[0], content[0])
            # if len(content)
            # self.queryModel.searchTable(self.select_conditions[0], self.select_conditions[1],content[0],content[1],content[2])
            # self.queryModel.searchTable(self.select_conditions,content)
            # sql = "SELECT * FROM %s WHERE %s = '%s' ORDER BY %s" % (
            # self.table, select_condition, content, self.tableKey)
            self.updateUI()'''

    """
    def searchButtonEvent3(self):
       
        hsj 输入查询条件查询按钮事件
        加一个日期修正函数
        加一个是否选择条件
        :return:
        """

            #self.updateUI()

    '''def searchButtonEvent(self):
        """
        hsj 输入查询条件查询按钮事件
        没有日期的查询
        :return:
        """
        content =self.searchEdit.text()
        n = self.comboBox.currentIndex()

        if content == "":
            if n==0:
                print(111)
                self.queryModel.refreshPage()
                self.queryModel.update()
            elif n==1:

        else:
            if n==0:
                sql = "WHERE %s = '%s'" % (self.select_conditions,content)
                self.updateUI()
            elif n==1:
                sql = "WHERE %s = '%s'" % (self.select_conditions, content)
                self.updateUI()
            self.queryModel.searchTable(sql)'''
    def isCorrect(self):
        """
        hsj 判断复选框是否选中一个数据
        :return:
        """
        if self.queryModel.checkList.count("Checked") == 0:
            QMessageBox.warning(QDialog(), "警告", "没有数据被选中，请选中后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return 0
        elif self.queryModel.checkList.count("Checked") > 1:
            QMessageBox.warning(QDialog(), "警告", "数据过多，请选中一条后重试！", QMessageBox.Yes, QMessageBox.Yes)
            return 0
        else:
            return 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = MySearchWidgetPIM()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
