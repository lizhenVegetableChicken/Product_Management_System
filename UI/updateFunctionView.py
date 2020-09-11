# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateFunctionView.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
# 刘敬楷
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QWidget

from Utils import openDB
from addUserView import AddUserWidget
from UI.Login_recorder import logToFile, getCurrentUserId

class updateFunctionWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 700)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(50, 20, 50, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.FunctionID = QtWidgets.QLineEdit(Dialog)
        self.FunctionID.setObjectName("FunctionID")
        self.FunctionID.setDisabled(True)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.FunctionID)
        self.Label_1 = QtWidgets.QLabel(Dialog)
        self.Label_1.setObjectName("Label_1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_1)
        self.ChineseName = QtWidgets.QLineEdit(Dialog)
        self.ChineseName.setObjectName("ChineseName")
        #self.ChineseName.setDisabled(True)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ChineseName)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.EnglishName = QtWidgets.QLineEdit(Dialog)
        self.EnglishName.setObjectName("EnglishName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.EnglishName)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.IsValid = QtWidgets.QLineEdit(Dialog)
        self.IsValid.setObjectName("IsValid")
        self.IsValid.setDisabled(True)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.IsValid)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.ChangeTime = QtWidgets.QLineEdit(Dialog)
        self.ChangeTime.setObjectName("ChangeTime")
        self.ChangeTime.setDisabled(True)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ChangeTime)
        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.ChangerID = QtWidgets.QLineEdit(Dialog)
        self.ChangerID.setObjectName("ChangerID")
        self.ChangerID.setDisabled(True)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ChangerID)
        self.Label_6 = QtWidgets.QLabel(Dialog)
        self.Label_6.setObjectName("Label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.remark = QtWidgets.QTextEdit(Dialog)
        self.remark.setObjectName("remark")
        self.remark.setDisabled(True)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.remark)
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
    #重设ui
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "更新业务信息"))
        self.Label.setText(_translate("Dialog", "业务ID："))
        self.Label_1.setText(_translate("Dialog", "中文名称："))
        self.Label_2.setText(_translate("Dialog", "英文名称："))
        self.Label_3.setText(_translate("Dialog", "是否可用："))
        self.Label_4.setText(_translate("Dialog", "修改时间："))
        self.Label_5.setText(_translate("Dialog", "修改人员ID："))
        self.Label_6.setText(_translate("Dialog", "备注："))
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
        新建界面的保存按钮事件
        :return:
        """
        functionId = self.FunctionID.text()
        chineseName = self.ChineseName.text()
        englishName = self.EnglishName.text()
        isValid = self.IsValid.text()
        changerTime = self.ChangeTime.text()
        changerId = self.ChangerID.text()
    #取消按钮事件
    def cancelButtonEvent(self, Dialog):
        """
        取消按钮事件
        :return:
        """
        logger = logToFile()
        UserId = getCurrentUserId()
        logger.info("用户：" + str(UserId) + " 点击取消按钮，取消了更新Admin_Menu表中数据")
        Dialog.close()
    #更新按钮事件
    def updateButtonEvent(self, queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """
        #修改前的数据
        result = queryModel.getData()
        checked_list = queryModel.checkList
        # 找到被选择的行数
        number = -1
        for i in range(len(checked_list)):
            if checked_list[i] == "Checked":
                number = i
        list = result[number]
        pre_functionId = list[0]
        pre_chineseName = list[1]
        pre_englishName = list[2]
        pre_isValid = list[3]
        pre_changeTime = list[4]
        pre_changerId = list[5]
        pre_remake = list[6]

        #先删除，以便检测
        queryModel.delete()
        #获取日志记录对象logger
        logger = logToFile()
        UserId = getCurrentUserId()

        functionId = self.FunctionID.text()
        chineseName = self.ChineseName.text()
        englishName = self.EnglishName.text()
        isValid = self.IsValid.text()
        import time
        changeTime = time.strftime("%Y-%m-%d %H:%M:%S")
        changerId = UserId  # 修改人ID
        remake = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if functionId== "" or chineseName== ""or remake=="":
            insert_sql = "INSERT INTO Admin_Menu VALUES ('%s','%s', '%s', '%s','%s','%s','%s')" % \
                         (pre_functionId, pre_chineseName, pre_englishName, pre_isValid, pre_changeTime, pre_changerId,pre_remake)
            db = openDB()
            query = QSqlQuery()
            query.exec(insert_sql)
            db.commit()
            db.close()
            logger.info("用户：" + str(UserId) + " 更新Admin_Menu表中数据失败（有字段为空）")
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，修改失败！", QMessageBox.Yes, QMessageBox.Yes))
            self.dialog.close()
            return
        else:
            #检测插入数据
            num = self.checkOn(functionId,chineseName,isValid,remake)
            #当返回0后取消则会删除当前选择数据，所以重新插入原数据的项
            if num == 0:
                insert_sql = "INSERT INTO Admin_Menu VALUES ('%s','%s', '%s', '%s','%s','%s','%s')" % \
                             (pre_functionId, pre_chineseName, pre_englishName, pre_isValid, pre_changeTime, pre_changerId, pre_remake)
                logger.info("用户：" + str(UserId) +" 更新Admin_Menu表中数据失败（业务ID/中文业务名称/权限，未通过检测）")
                self.query.exec(insert_sql)
                self.db.commit()
                self.dialog.close()
                return

            insert_sql = "INSERT INTO Admin_Menu VALUES ('%s','%s', '%s', '%s','%s','%s','%s')" % \
                         (functionId, chineseName, englishName, isValid, changeTime,changerId,remake)
            self.query.exec(insert_sql)
            self.db.commit()
            logger.info("用户：" + str(UserId) + " 更新 Admin_Menu 表中数据成功。"+"新数据为["+str(functionId)+","+str(chineseName)+","+str(englishName)+","+str(isValid)+","+str(changeTime)+","+str(changerId)+"]")
            confirm = QMessageBox.information(QDialog(), "提示", "业务信息更新成功！（在下次登录时可显示）", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.dialog.close()
    #检验输入，合理性
    def checkOn(self,functionId,chineseName,isValid,remark):
        """
        检查业务ID和权限ID是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM Admin_Menu WHERE ID = '%s'" % functionId
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.warning(QDialog(), "警告", "此业务ID已存在，请更换后重新添加！", QMessageBox.Yes, QMessageBox.Yes))
            return 0

        sql = "SELECT * FROM Admin_Menu WHERE ChineseName = '%s'" % chineseName
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.warning(QDialog(), "警告", "此业务名称已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0

        if (isValid != "true") and (isValid != "false"):
            print(QMessageBox.warning(QDialog(), "警告", "是否启用仅为true或false，请检查后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0

        sql = "SELECT * FROM Admin_Menu WHERE 备注 = '%s'" % remark
        self.query.exec(sql)
        if not self.query.next():
            print(QMessageBox.warning(QDialog(), "警告", "此业务备注分类非规定项，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        return 1
    #更新数据
    def updateData(self, list, queryModel):
        """
        修改用户信息
        :param list:
        :return:
        """
        self.label.setText("修改业务信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda:self.updateButtonEvent(queryModel))
        self.FunctionID.setText(list[0])
        self.ChineseName.setText(list[1])
        self.EnglishName.setText(list[2])
        self.IsValid.setText(list[3])
        self.ChangeTime.setText(list[4])
        self.ChangerID.setText(list[5])
        self.remark.setText(list[6])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = AddUserWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())