import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
from PyQt5.QtSql import *
import time


class DropProductDialog(QDialog):
    drop_Product_successful_signal=pyqtSignal()

    def __init__(self, parent=None):
        super(DropProductDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("删除书籍")

    def setUpUI(self):
        # 书名，书号，作者，分类，添加数量.出版社,出版日期
        # 书籍分类：哲学类、社会科学类、政治类、法律类、军事类、经济类、文化类、教育类、体育类、语言文字类、艺术类、历史类、地理类、天文学类、生物学类、医学卫生类、农业类
        ProductCategory = ["哲学", "社会科学", "政治", "法律", "军事", "经济", "文化", "教育", "体育", "语言文字", "艺术", "历史"
            , "地理", "天文学", "生物学", "医学卫生", "农业"]
        self.resize(300, 400)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel("删除书籍")
        self.ProductNameLabel = QLabel("书    名:")
        self.ProductIdLabel = QLabel("书    号:")
        self.authNameLabel = QLabel("作    者:")
        self.categoryLabel = QLabel("分    类:")
        self.publisherLabel = QLabel("出 版 社:")
        self.publishDateLabel = QLabel("出版日期:")
        self.dropNumLabel = QLabel("数    量:")

        # button控件
        self.dropProductButton = QPushButton("删  除")

        # lineEdit控件
        self.ProductNameEdit = QLineEdit()
        self.ProductIdEdit = QLineEdit()
        self.authNameEdit = QLineEdit()
        self.categoryComboBox = QComboBox()
        self.categoryComboBox.addItems(ProductCategory)
        self.publisherEdit = QLineEdit()
        self.publishTime = QLineEdit()
        # self.publishDateEdit = QLineEdit()
        self.dropNumEdit = QLineEdit()

        self.ProductNameEdit.setMaxLength(10)
        self.ProductIdEdit.setMaxLength(6)
        self.authNameEdit.setMaxLength(10)
        self.publisherEdit.setMaxLength(10)
        self.dropNumEdit.setMaxLength(12)
        self.dropNumEdit.setValidator(QIntValidator())

        # 添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.ProductNameLabel, self.ProductNameEdit)
        self.layout.addRow(self.ProductIdLabel, self.ProductIdEdit)
        self.layout.addRow(self.authNameLabel, self.authNameEdit)
        self.layout.addRow(self.categoryLabel, self.categoryComboBox)
        self.layout.addRow(self.publisherLabel, self.publisherEdit)
        self.layout.addRow(self.publishDateLabel, self.publishTime)
        self.layout.addRow(self.dropNumLabel, self.dropNumEdit)
        self.layout.addRow("", self.dropProductButton)

        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titlelabel.setFont(font)
        font.setPixelSize(14)
        self.ProductNameLabel.setFont(font)
        self.ProductIdLabel.setFont(font)
        self.authNameLabel.setFont(font)
        self.categoryLabel.setFont(font)
        self.publisherLabel.setFont(font)
        self.publishDateLabel.setFont(font)
        self.dropNumLabel.setFont(font)

        self.ProductNameEdit.setFont(font)
        self.ProductNameEdit.setReadOnly(True)
        self.ProductNameEdit.setStyleSheet("background-color:#363636")
        self.ProductIdEdit.setFont(font)
        self.authNameEdit.setFont(font)
        self.authNameEdit.setReadOnly(True)
        self.authNameEdit.setStyleSheet("background-color:#363636")
        self.publisherEdit.setFont(font)
        self.publisherEdit.setReadOnly(True)
        self.publisherEdit.setStyleSheet("background-color:#363636")
        self.publishTime.setFont(font)
        self.publishTime.setStyleSheet("background-color:#363636")
        self.categoryComboBox.setFont(font)
        self.categoryComboBox.setStyleSheet("background-color:#363636")
        self.dropNumEdit.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.dropProductButton.setFont(font)
        self.dropProductButton.setFixedHeight(32)
        self.dropProductButton.setFixedWidth(140)

        # 设置间距
        self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)

        self.dropProductButton.clicked.connect(self.dropProductButtonClicked)
        self.ProductIdEdit.textChanged.connect(self.ProductIdEditChanged)

    def ProductIdEditChanged(self):
        ProductId = self.ProductIdEdit.text()
        if (ProductId == ""):
            self.ProductNameEdit.clear()
            self.publisherEdit.clear()
            self.authNameEdit.clear()
            self.dropNumEdit.clear()
            self.publishTime.clear()
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/ProductManagement.db')
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM Product WHERE ProductId='%s'" % (ProductId)
        query.exec_(sql)
        # 查询对应书号，如果存在就更新form
        if (query.next()):
            self.ProductNameEdit.setText(query.value(0))
            self.authNameEdit.setText(query.value(2))
            self.categoryComboBox.setCurrentText(query.value(3))
            self.publisherEdit.setText(query.value(4))
            self.publishTime.setText(query.value(5))
        return

    def dropProductButtonClicked(self):
        ProductId = self.ProductIdEdit.text()
        dropNum = 0
        if (self.dropNumEdit.text() == ""):
            print(QMessageBox.warning(self, "警告", "删除数目为空，请检查输入，操作失败"), QMessageBox.Yes, QMessageBox.Yes)
            return
        dropNum = int(self.dropNumEdit.text())
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/ProductManagement.db')
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM Product WHERE ProductId='%s'" % (ProductId)
        query.exec_(sql)
        if (query.next()):
            if (dropNum > query.value(7) or dropNum < 0):
                print(QMessageBox.warning(self, "警告", "最多可删除%d本，请检查输入" % (query.value(7)), QMessageBox.Yes,
                                          QMessageBox.Yes))
                return
        # 更新Product表和BuyorDrop表
        # 如果drop书目和当前库存相同，则直接删除Product记录（这里先默认当前所有书都在库存中）
        if (dropNum == query.value(6)):
            sql = "DELETE  FROM Product WHERE ProductId='%s'" % (ProductId)
        else:
            sql = "UPDATE Product SET NumStorage=NumStorage-%d,NumCanBorrow=NumCanBorrow-%d WHERE ProductId='%s'" % (
                dropNum, dropNum, ProductId)
        query.exec_(sql)
        db.commit()

        timenow = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "INSERT INTO buyordrop VALUES ('%s','%s',0,%d)" % (ProductId, timenow, dropNum)
        query.exec_(sql)
        db.commit()
        print(QMessageBox.information(self, "提示", "淘汰书籍成功!", QMessageBox.Yes, QMessageBox.Yes))
        self.drop_Product_successful_signal.emit()
        self.close()
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = DropProductDialog()
    mainMindow.show()
    sys.exit(app.exec_())
