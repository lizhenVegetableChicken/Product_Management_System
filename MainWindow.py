import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
import qdarkstyle

from Login_recorder import update_currentLoginState
from SignIn import SignInWidget
from SignUp import SignUpWidget
import sip
from UI.Login_recorder import update_currentLoginState,getCurrentUserId,logToFile
from AdminHome import AdminHome
#from UserHome import UserHome
from ChangePasswordDialog import ChangePasswordDialog


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.widget = SignInWidget()

        #self.resize(900, 600)

        self.setWindowTitle("决策支持系统")
        self.setCentralWidget(self.widget)
        bar = self.menuBar()
        self.Menu = bar.addMenu("菜单栏")

        self.signUpAction = QAction("注册", self)
        self.signInAction = QAction("登录", self)
        self.ChangePasswordAction =QAction("修改密码",self)
        #self.signInAction = QAction("登录", self)
        self.quitSignInAction = QAction("退出登录", self)
        self.quitAction = QAction("退出系统", self)
        self.Menu.addAction(self.signUpAction)
        self.Menu.addAction(self.signInAction)
        self.Menu.addAction(self.ChangePasswordAction)
        #self.Menu.addAction(self.signInAction)
        self.Menu.addAction(self.quitSignInAction)
        self.Menu.addAction(self.quitAction)

        #self.signUpAction.setEnabled(True)
        # Zgg
        self.signUpAction.setEnabled(True)
        self.ChangePasswordAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(False)
        self.widget.is_admin_signal.connect(self.adminSignIn)
        self.widget.is_User_signal[str].connect(self.UserSignIn)
        self.Menu.triggered[QAction].connect(self.menuTriggered)

        # Zgg 全屏
        # self.showFullScreen()
        #self.showMaximized()
        self.showMaximized()

    def adminSignIn(self):
        sip.delete(self.widget)
        self.widget = AdminHome()
        self.setCentralWidget(self.widget)
        self.ChangePasswordAction.setEnabled(False)
        self.signUpAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)

    def UserSignIn(self, UserId):
        sip.delete(self.widget)
        #
        self.widget = AdminHome()
        self.setCentralWidget(self.widget)

        # Zgg 普通用户登陆后可以修改密码
        self.ChangePasswordAction.setEnabled(True)
        #self.signUpAction.setEnabled(True)
        # Zgg 普通用户无法注册
        self.signUpAction.setEnabled(False)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(True)

    def menuTriggered(self, q):
        UserId = getCurrentUserId()
        if(q.text()=="修改密码"):
            logger = logToFile()
            logger.info("用户: " +str(UserId) +" 进入修改用户密码页面")
            changePsdDialog = ChangePasswordDialog(self)
            changePsdDialog.show()
            changePsdDialog.exec()
        if (q.text() == "注册"):
            sip.delete(self.widget)
            self.widget = SignUpWidget(self)
            self.setCentralWidget(self.widget)
            #self.widget.User_signup_signal[str].connect(self.UserSignIn)
            self.signUpAction.setEnabled(False)
            self.ChangePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(True)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "退出登录"):
            logger = logToFile()
            logger.info("用户：" + str(UserId) + " 退出登录")
            update_currentLoginState()
            sip.delete(self.widget)
            self.close()
            self.widget = SignInWidget()
            self.__init__()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            #self.widget.is_User_signal[str].connect(self.UserSignIn)
            self.signUpAction.setEnabled(True)
            self.ChangePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "登录"):
            sip.delete(self.widget)
            self.widget = SignInWidget()
            self.setCentralWidget(self.widget)
            self.widget.is_admin_signal.connect(self.adminSignIn)
            self.widget.is_User_signal[str].connect(self.UserSignIn)
            self.signUpAction.setEnabled(True)
            self.ChangePasswordAction.setEnabled(True)
            self.signInAction.setEnabled(False)
            self.quitSignInAction.setEnabled(False)
        if (q.text() == "退出系统"):
            update_currentLoginState()
            qApp = QApplication.instance()
            qApp.quit()
            logger = logToFile()
            logger.info("用户：" + str(UserId) + " 退出系统")
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Main()
    mainMindow.show()
    sys.exit(app.exec_())