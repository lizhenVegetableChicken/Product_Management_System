# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addUserView.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import hashlib
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDialog
from UI.Login_recorder import logToFile,getCurrentUserId
from Utils import openDB

class AddUserWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 600)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(50, 20, 50, 10)
        self.formLayout.setSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.UserID = QtWidgets.QLineEdit(Dialog)
        self.UserID.setObjectName("UserID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.UserID)
        self.pswLabel = QtWidgets.QLabel(Dialog)
        self.pswLabel.setObjectName("pswLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pswLabel)
        self.PSW = QtWidgets.QLineEdit(Dialog)
        self.PSW.setObjectName("PSW")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.PSW)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.rightID = QtWidgets.QLineEdit(Dialog)
        self.rightID.setObjectName("rightID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rightID)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.changeDate = QtWidgets.QLineEdit(Dialog)
        self.changeDate.setObjectName("changeDate")
        self.changeDate.setDisabled(True)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.changeDate)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.changerID = QtWidgets.QLineEdit(Dialog)
        self.changerID.setObjectName("changerID")
        self.changerID.setDisabled(True)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.changerID)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Dialog)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.bindButton(Dialog)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    #重设UI
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "新建用户"))
        self.label.setText(_translate("Dialog", "新建用户"))
        self.Label.setText(_translate("Dialog", "用户ID："))
        self.pswLabel.setText(_translate("Dialog", "用户密码："))
        self.Label_2.setText(_translate("Dialog", "权限ID："))
        self.Label_3.setText(_translate("Dialog", "修改时间："))
        self.Label_3.setDisabled(True)
        self.Label_4.setText(_translate("Dialog", "修改人ID："))
        self.Label_4.setDisabled(True)
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))
    #绑定按钮事件
    def bindButton(self,Dialog):
        """
        按钮绑定事件
        :param
        Dialog: 弹窗本身
        :return:
        """
        #print("保存按钮点击")
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Dialog))
    #保存按钮事件
    def conserveButtonEvent(self, Dialog):
        """
        hsj 新建批次界面的保存按钮事件
        :return:
        """
        userID = self.UserID.text()
        psw = self.PSW.text()
        #加密psw
        hl = hashlib.md5()
        hl.update(psw.encode(encoding="utf-8"))
        encoded_psw = hl.hexdigest()
        rightID = self.rightID.text()
        #获取日志logger对象
        logger = logToFile()
        UserId = getCurrentUserId()

        # 如果必要的信息都不为空
        if userID == "" or psw == "" or rightID == "":
            logger.info("用户：" + str(UserId) +" 新建User表数据失败（必要信息为空）")
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            #检测用户Id和权限Id
            num = self.checkOn(userID,rightID)
            if num == 0:
                logger.info("用户：" + str(UserId) + " 新建User表数据失败（用户ID或权限ID，未通过检测）")
                return
            import time
            changeDate = time.strftime("%Y-%m-%d %H:%M:%S")
            changerId = UserId #修改人id

            insert_sql = "INSERT INTO User VALUES ('%s','%s','%s','%s', '%s')" \
                         % (userID,encoded_psw,rightID,changeDate,changerId)
            self.query.exec(insert_sql)
            self.db.commit()
            logger.info("用户：" + str(UserId) + " 新建了一条User表数据"+"新数据为：["+str(userID)+" ,"+str(encoded_psw)+" ,"+str(rightID)+" ,"+str(changeDate)+" ,"+str(changerId)+"]")
            confirm = QMessageBox.information(QDialog(), "提示", "用户新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                Dialog.close()
    #取消按钮事件
    def cancelButtonEvent(self, Dialog):
        """
        取消按钮事件
        :return:
        """
        Dialog.close()
    #更新按钮事件
    def updateButtonEvent(self, queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """
        #第一次点击出错后，修改数据正确后，后再保存会删除下一行
        #解决方案，在第一次出错后直接关闭dialog
        queryModel.delete()
        userID = self.UserID.text()
        #加密psw
        psw = self.PSW.text()
        hl = hashlib.md5()
        hl.update(psw.encode(encoding='utf-8'))
        #加密后的psw
        encoded_psw = hl.hexdigest()
        rightID = self.rightID.text()
        #获取日志logger对象，以及UserId
        logger = logToFile()
        UserId = getCurrentUserId()

        # 如果必要的信息都不为空
        if userID== "" or psw== "" or rightID == "" :
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，修改失败！", QMessageBox.Yes, QMessageBox.Yes))
            revert_sql = "INSERT INTO User VALUES ('%s','%s', '%s', '%s','%s')" % \
                         (self.pre_list[0], self.pre_list[1], self.pre_list[2], self.pre_list[3], self.pre_list[4])
            db = openDB()
            query = QSqlQuery()
            query.exec(revert_sql)
            db.commit()
            db.close()
            logger.info("用户：" + str(UserId) + " 更新User表中数据失败（重要字段信息为空）")
            self.dialog.close()
            return
        else:
            #检测userID和rightID
            num = self.checkOn(userID,rightID)
            if num == 0:
                revert_sql = "INSERT INTO User VALUES ('%s','%s', '%s', '%s','%s')" % \
                             (self.pre_list[0], self.pre_list[1], self.pre_list[2], self.pre_list[3], self.pre_list[4])
                self.query.exec(revert_sql)
                self.db.commit()
                logger.info("用户：" + str(UserId) + " 更新User表中数据失败（用户ID或权限Id，未通过检测）")
                self.dialog.close()
                return

            import time
            changeDate = time.strftime("%Y-%m-%d %H:%M:%S")
            changerId = UserId   #修改人ID
            insert_sql = "INSERT INTO User VALUES ('%s','%s', '%s', '%s','%s')" % \
                         (userID, encoded_psw, rightID, changeDate, changerId)
            self.query.exec(insert_sql)
            self.db.commit()
            logger.info("用户：" + str(UserId) + " 更新User表中数据成功,新数据为：["+str(userID)+","+str(encoded_psw)+","+str(rightID)+","+str(changeDate)+","+str(changerId)+"]")
            confirm = QMessageBox.information(QDialog(), "提示", "用户信息更新成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()
    #检验输入，合理性
    def checkOn(self,userID,rightID):
        """
        检查用户ID和权限ID是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM User WHERE UserId = '%s'" % userID
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.warning(QDialog(), "警告", "此用户ID已存在，请更换后重新添加！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        # 如果权限id不为0或1，则提示不能保存
        if (rightID != "1") and (rightID != "0"):
            print(QMessageBox.warning(QDialog(), "警告", "权限ID仅为0或1，请检查后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1
    #更新数据
    def updateData(self, list, queryModel):
        """
        修改用户信息
        :param list:
        :return:
        """
        self.pre_list = list
        self.label.setText("修改用户信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda:self.updateButtonEvent(queryModel))
        self.UserID.setText(list[0])
        self.PSW.setText(list[1])
        self.rightID.setText(list[2])
        self.changeDate.setText(list[3])
        self.changerID.setText(list[4])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = AddUserWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())