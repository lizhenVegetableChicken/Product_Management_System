import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import hashlib
from PyQt5.QtSql import *

from UI.Login_recorder import insert_info, update_currentLoginState
from Utils import openDB


class SignInWidget(QWidget):
    is_admin_signal = pyqtSignal()
    is_User_signal = pyqtSignal(str)

    def __init__(self):
        super(SignInWidget, self).__init__()
        self.resize(900, 600)
        self.setWindowTitle("决策支持系统")
        self.setUpUI()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("./images/junjian.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def setUpUI(self):
        self.Vlayout = QVBoxLayout(self)
        self.Vlayout1 = QVBoxLayout()
        self.Hlayout2 = QHBoxLayout()
        self.formlayout = QFormLayout()

        self.label1 = QLabel("用户名: ")
        labelFont = QFont()
        labelFont.setPixelSize(16)
        lineEditFont = QFont()
        lineEditFont.setPixelSize(16)
        self.label1.setFont(labelFont)
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setFixedHeight(32)
        self.lineEdit1.setFixedWidth(180)
        self.lineEdit1.setFont(lineEditFont)
        self.lineEdit1.setMaxLength(10)

        self.formlayout.addRow(self.label1, self.lineEdit1)

        self.label2 = QLabel("密  码: ")
        self.label2.setFont(labelFont)


        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setFixedHeight(32)
        self.lineEdit2.setFixedWidth(180)
        self.lineEdit2.setMaxLength(16)

        # 设置验证
        reg = QRegExp("PB[0~9]{8}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        # self.lineEdit1.setValidator(pValidator)

        reg = QRegExp("[a-zA-z0-9]+$")
        pValidator.setRegExp(reg)
        self.lineEdit2.setValidator(pValidator)

        passwordFont = QFont()
        passwordFont.setPixelSize(10)
        self.lineEdit2.setFont(passwordFont)

        self.lineEdit2.setEchoMode(QLineEdit.Password)
        self.formlayout.addRow(self.label2, self.lineEdit2)
        self.signIn = QPushButton("登 录")
        self.signIn.setFixedWidth(100)
        self.signIn.setFixedHeight(30)
        self.signIn.setFont(labelFont)
        self.formlayout.addRow("", self.signIn)

        self.label = QLabel()
        pe = QPalette();
        pe.setColor(QPalette.WindowText,Qt.red)
        self.label.setPalette(pe)
        self.label.setText("决策支持系统")
        fontlabel = QFont()
        fontlabel.setPixelSize(50)
        fontlabel.setBold(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(fontlabel)
        self.Vlayout1.addWidget(self.label, Qt.AlignCenter)

        self.widget1 = QWidget()
        self.widget1.setLayout(self.Vlayout1)

        # self.lab =QLabel()
        # self.lab.setMaximumSize(1000,600)
        # self.lab.setPixmap(QPixmap("./images/lnj.jpg"))
        # self.Vlayout1.addWidget(self.lab,0,Qt.AlignHCenter)

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.8)
        self.label2.setGraphicsEffect(op)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.8)
        self.label1.setGraphicsEffect(op)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.8)
        self.lineEdit1.setGraphicsEffect(op)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.8)
        self.lineEdit2.setGraphicsEffect(op)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.8)
        self.signIn.setGraphicsEffect(op)



        self.widget2 = QWidget()
        self.widget2.setFixedWidth(300)
        self.widget2.setFixedHeight(150)
        self.widget2.setLayout(self.formlayout)

        self.Hlayout2.addWidget(self.widget2, Qt.AlignCenter)

        self.widget = QWidget()
        self.widget.setLayout(self.Hlayout2)
        self.Vlayout.addWidget(self.widget1)
        self.Vlayout.addWidget(self.widget, Qt.AlignTop)

        self.widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget1.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget2.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        self.signIn.clicked.connect(self.signInCheck2)
        self.lineEdit2.returnPressed.connect(self.signInCheck2)
        self.lineEdit1.returnPressed.connect(self.signInCheck2)

    # Zgg 删除了User表格中的Name字段
    def signInCheck2(self):
        UserId = self.lineEdit1.text()
        password = self.lineEdit2.text()
        if (UserId == "" or password == ""):
            print(QMessageBox.warning(self, "警告", "用户名和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes))
            return
        # 打开数据库连接
        db = openDB()
        query = QSqlQuery()
        sql = "SELECT * FROM User WHERE UserId='%s'" % (UserId)
        query.exec_(sql)
        db.close()

        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        if (not query.next()):
            print(QMessageBox.information(self, "提示", "该账号不存在!", QMessageBox.Yes, QMessageBox.Yes))
        else:
            if (UserId == query.value(0) and hl.hexdigest() == query.value(1)):
                import time
                #更新当前登录用户的状态
                update_currentLoginState()
                #插入当前登录用户项
                insert_info(UserId)
                #登录日志
                from Login_recorder import logToFile
                logger = logToFile()
                logger.info("用户："+str(UserId)+" 登录系统")
                # 如果是管理员
                if (query.value(2)==1):
                    self.is_admin_signal.emit()
                else:
                    self.is_User_signal.emit(UserId)
            else:
                print(QMessageBox.information(self, "提示", "密码错误!", QMessageBox.Yes, QMessageBox.Yes))
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = SignInWidget()
    mainMindow.show()
    sys.exit(app.exec_())
