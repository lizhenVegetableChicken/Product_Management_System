import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time
from PyQt5.QtSql import *


class AddProductWidget(QWidget):
    add_Product_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(AddProductWidget, self).__init__(parent)
        self.layout = QFormLayout()
        self._setUpUI()
        self.setWindowModality(Qt.WindowModal)


    def _setUpUI(self):
        """添加产品初始化UI"""
        self.setLayout(self.layout)
        self.setMaximumWidth(800)
        self.titleLabel = QLabel("添加产品")
        self.productIdLabel = QLabel("ID：")
        self.productModelIdLabel = QLabel("产品模型ID：")
        self.productNoLabel = QLabel("产品编号：")
        self.lifeLabel = QLabel("寿命：")
        self.startDateLabel = QLabel("寿命起始日期：")
        self.daysBeforeLabel = QLabel("寿命到期前多少天提醒：")
        self.isUsedCountLimitLabel = QLabel("是否使用次数限制：")
        self.maxUsedCountLabel = QLabel("最多使用次数：")
        self.haveUsedCountLabel = QLabel("已使用次数：")
        self.createIdLabel = QLabel("创建人员ID：")
        self.createTimeLabel = QLabel("创建时间：")
        self.updateIdLabel = QLabel("修改人员ID：")
        self.updateTimeLabel = QLabel("修改时间：")
        self.remarkLabel = QLabel("备注：")

        self.productIdEdit = QLineEdit()
        self.productModelIdEdit = QLineEdit()
        self.productNoEdit = QLineEdit()
        self.lifeEdit = QLineEdit()
        self.startDateEdit = QLineEdit()
        self.daysBeforeEdit = QLineEdit()
        self.isUsedCountLimitEdit = QLineEdit()
        self.maxUsedCountEdit = QLineEdit()
        self.haveUsedCountEdit = QLineEdit()
        self.createIdEdit = QLineEdit()
        self.createTimeEdit = QLineEdit()
        self.updateIdEdit = QLineEdit()
        self.updateTimeEdit = QLineEdit()
        self.remarkEdit = QLineEdit()

        self.confirmButton = QPushButton("提交")
        self.cancelButton = QPushButton("取消")

        # 设置标题水平剧中
        self.titleLabel.setAlignment(Qt.AlignHCenter)
        self.titleLabel.setStyleSheet("font-size:30px; font:bold; margin: 20px")
        self.layout.addRow(self.titleLabel)
        self.layout.addRow(self.productIdLabel, self.productIdEdit)
        self.layout.addRow(self.productModelIdLabel, self.productModelIdEdit)
        self.layout.addRow(self.productNoLabel, self.productNoEdit)
        self.layout.addRow(self.lifeLabel, self.lifeEdit)
        self.layout.addRow(self.startDateLabel, self.startDateEdit)
        self.layout.addRow(self.isUsedCountLimitLabel, self.isUsedCountLimitEdit)
        self.layout.addRow(self.maxUsedCountLabel, self.maxUsedCountEdit)
        self.layout.addRow(self.haveUsedCountLabel, self.haveUsedCountEdit)
        self.layout.addRow(self.createIdLabel, self.createIdEdit)
        self.layout.addRow(self.createTimeLabel, self.createTimeEdit)
        self.layout.addRow(self.updateIdLabel, self.updateIdEdit)
        self.layout.addRow(self.updateTimeLabel, self.updateTimeEdit)
        self.layout.addRow(self.remarkLabel, self.remarkEdit)
        self.confirmButton.setFixedSize(140, 32)
        self.cancelButton.setFixedSize(140, 32)
        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.confirmButton)
        layout.addWidget(self.cancelButton)
        widget.setLayout(layout)

        self.layout.addRow("", widget)


        self.layout.setVerticalSpacing(20)

        # self.addProductButton.clicked.connect(self.addProductButtonCicked)

    def confirmButtonClicked(self):
        ProductName = self.ProductNameEdit.text()
        ProductId = self.ProductIdEdit.text()
        authName = self.authNameEdit.text()
        ProductCategory = self.categoryComboBox.currentText()
        publisher = self.publisherEdit.text()
        publishTime = self.publishTime.text()
        addProductNum = self.addNumEdit.text()
        if (
                ProductName == "" or ProductId == "" or authName == "" or ProductCategory == "" or publisher == "" or publishTime == "" or addProductNum == ""):
            print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            addProductNum = int(addProductNum)
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('./db/ProductManagement.db')
            db.open()
            query = QSqlQuery()
            # 如果已存在，则update Product表的现存量，剩余可借量，不存在，则insert Product表，同时insert buyordrop表
            sql = "SELECT * FROM Product WHERE ProductId='%s'" % (ProductId)
            query.exec_(sql)
            if (query.next()):
                sql = "UPDATE Product SET NumStorage=NumStorage+%d,NumCanBorrow=NumCanBorrow+%d WHERE ProductId='%s'" % (
                    addProductNum, addProductNum, ProductId)
            else:
                sql = "INSERT INTO Product VALUES ('%s','%s','%s','%s','%s','%s',%d,%d,0)" % (
                    ProductName, ProductId, authName, ProductCategory, publisher, publishTime, addProductNum, addProductNum)
            query.exec_(sql)
            db.commit()
            # 插入droporinsert表
            timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            sql = "INSERT INTO buyordrop VALUES ('%s','%s',1,%d)" % (ProductId, timenow, addProductNum)
            query.exec_(sql)
            db.commit()
            print(QMessageBox.information(self, "提示", "添加书籍成功!", QMessageBox.Yes, QMessageBox.Yes))
            self.add_Product_success_signal.emit()
            self.close()
            self.clearEdit()
        return

    def clearEdit(self):
        self.ProductNameEdit.clear()
        self.ProductIdEdit.clear()
        self.authNameEdit.clear()
        self.addNumEdit.clear()
        self.publisherEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = AddProductWidget()
    mainMindow.show()
    sys.exit(app.exec_())
