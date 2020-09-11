import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time
from PyQt5.QtSql import *


class AddProductDialog(QDialog):
    add_Product_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(AddProductDialog, self).__init__(parent)
        self.layout = QFormLayout()
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)

    # def setUpUI_O(self):
    #     # 书名，书号，作者，分类，添加数量.出版社,出版日期
    #     # 书籍分类：哲学类、社会科学类、政治类、法律类、军事类、经济类、文化类、教育类、体育类、语言文字类、艺术类、历史类、地理类、天文学类、生物学类、医学卫生类、农业类
    #     ProductCategory = ["哲学", "社会科学", "政治", "法律", "军事", "经济", "文化", "教育", "体育", "语言文字", "艺术", "历史"
    #         , "地理", "天文学", "生物学", "医学卫生", "农业"]
    #     self.resize(1200, 600)
    #     self.layout = QFormLayout()
    #     self.setLayout(self.layout)
    #
    #     # Label控件
    #     # self.titlelabel = QLabel("添加产品")
    #     self.productNameLabel = QLabel("产品名：")
    #     # self.ProductIdLabel = QLabel("产品代号:")
    #     self.productBatchNOLabel = QLabel("批次号；")
    #     # self.categoryLabel = QLabel("技术文档:")
    #     self.productNOLabel = QLabel("产品编号；")
    #     self.deliverDateLabel = QLabel("交付日期；")
    #     self.deliverCompanyNameLabel = QLabel("交付单位；")
    #     self.delivererLabel = QLabel("交付者；")
    #     self.receiveCompanyNameLabel = QLabel("接收单位：")
    #     self.receiverLable = QLabel("接收者：")
    #     self.createIdLabel = QLabel("创建人员ID：")
    #     self.createTimeLable = QLabel("创建时间：")
    #     # 存放地点
    #     # 存储环境
    #     # 存储时间
    #     # 产品状态
    #     # 出入库信息
    #     self.lifeLabel = QLabel("寿命(天)：")
    #     self.startDateLabel = QLabel("寿命起始日期：")
    #     self.daysBeforeLabel = QLabel("寿命到期前多少天提醒：")
    #
    #     # button控件
    #     self.addProductButton = QPushButton("添 加")
    #
    #     # lineEdit控件
    #     self.productNameEdit = QLineEdit()
    #     # self.ProductIdLabel = QLabel("产品代号:")
    #     self.productBatchNOEdit = QLineEdit()
    #     # self.categoryLabel = QLabel("技术文档:")
    #     self.productNOEdit = QLineEdit()
    #     self.deliverDateEdit = QLineEdit()
    #     self.deliverCompanyNameEdit = QLineEdit()
    #     self.delivererEdit = QLineEdit()
    #     self.receiveCompanyNameEdit = QLineEdit()
    #     self.receiverEdit = QLineEdit()
    #     self.createIdEdit = QLineEdit()
    #     self.createTimeEdit = QLineEdit()
    #     # 存放地点
    #     # 存储环境
    #     # 存储时间
    #     # 产品状态
    #     # 出入库信息
    #     self.lifeEdit = QLineEdit()
    #     self.startDateEdit = QLineEdit()
    #     self.daysBeforeEdit = QLineEdit()
    #
    #
    #
    #
    #     # self.ProductNameEdit = QLineEdit()
    #     # self.ProductIdEdit = QLineEdit()
    #     # self.authNameEdit = QLineEdit()
    #     # self.categoryComboBox = QComboBox()
    #     # self.categoryComboBox.addItems(ProductCategory)
    #     # self.publisherEdit = QLineEdit()
    #     # self.publishTime = QDateTimeEdit()
    #     # self.publishTime.setDisplayFormat("yyyy-MM-dd")
    #     # # self.publishDateEdit = QLineEdit()
    #     # self.addNumEdit = QLineEdit()
    #     #
    #     # self.ProductNameEdit.setMaxLength(10)
    #     # self.ProductIdEdit.setMaxLength(6)
    #     # self.authNameEdit.setMaxLength(10)
    #     # self.publisherEdit.setMaxLength(10)
    #     # self.addNumEdit.setMaxLength(12)
    #     # self.addNumEdit.setValidator(QIntValidator())
    #
    #     # 添加进formlayout
    #     # self.layout.addRow("", self.titlelabel)
    #     self.layout.addRow(self.productNameLabel, self.productNameEdit)
    #     self.layout.addRow(self.productBatchNOLabel, self.productBatchNOEdit)
    #     self.layout.addRow(self.deliverDateLabel, self.deliverDateEdit)
    #     self.layout.addRow(self.deliverCompanyNameLabel, self.deliverCompanyNameEdit)
    #     self.layout.addRow(self.delivererLabel, self.delivererEdit)
    #     self.layout.addRow(self.receiveCompanyNameLabel, self.receiveCompanyNameEdit)
    #     self.layout.addRow(self.receiverLable, self.receiverEdit)
    #     self.layout.addRow(self.createIdLabel, self.createIdEdit)
    #     self.layout.addRow(self.createTimeLable, self.createTimeEdit)
    #     self.layout.addRow(self.lifeLabel, self.lifeEdit)
    #     self.layout.addRow(self.startDateLabel, self.startDateEdit)
    #     self.layout.addRow(self.daysBeforeLabel, self.daysBeforeEdit)
    #     self.layout.addRow("", self.addProductButton)
    #
    #     # 设置字体
        font = QFont()
    #     font.setPixelSize(20)
    #     # self.titlelabel.setFont(font)
    #     font.setPixelSize(14)
    #     # Label设置字体
    #     self.productNameLabel.setFont(font)
    #     self.productBatchNOLabel.setFont(font)
    #     self.deliverDateLabel.setFont(font)
    #     self.deliverCompanyNameLabel.setFont(font)
    #     self.delivererLabel.setFont(font)
    #     self.receiveCompanyNameLabel.setFont(font)
    #     self.receiverLable.setFont(font)
    #     self.createIdLabel.setFont(font)
    #     self.createTimeLable.setFont(font)
    #     self.lifeLabel.setFont(font)
    #     self.startDateLabel.setFont(font)
    #     self.daysBeforeLabel.setFont(font)
    #     # 编辑框设置字体
    #     self.productNameEdit.setFont(font)
    #     self.productBatchNOEdit.setFont(font)
    #     self.deliverDateEdit.setFont(font)
    #     self.deliverCompanyNameEdit.setFont(font)
    #     self.delivererEdit.setFont(font)
    #     self.receiveCompanyNameEdit.setFont(font)
    #     self.receiverEdit.setFont(font)
    #     self.createIdEdit.setFont(font)
    #     self.createTimeEdit.setFont(font)
    #     self.lifeEdit.setFont(font)
    #     self.startDateEdit.setFont(font)
    #     self.daysBeforeEdit.setFont(font)
    #
    #
    #     # button设置
    #     font.setPixelSize(16)
    #     self.addProductButton.setFont(font)
    #     self.addProductButton.setFixedHeight(32)
    #     self.addProductButton.setFixedWidth(140)
    #
    #     # 设置间距
    #     # self.titlelabel.setMargin(8)
    #     self.layout.setVerticalSpacing(10)
    #
    #     self.addProductButton.clicked.connect(self.addProductButtonCicked)

    def setUpUI(self):
        self.resize(600, 600)
        self.setLayout(self.layout)

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


        self.layout.setVerticalSpacing(20)

        # self.addProductButton.clicked.connect(self.addProductButtonCicked)


    def addProductButtonCicked(self):
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
    mainMindow = AddProductDialog()
    mainMindow.show()
    sys.exit(app.exec_())
