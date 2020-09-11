# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddKnowledgeBase.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtCore import Qt, QDateTime, QDate
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QHeaderView
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QDialog
from Login_recorder import getCurrentUserId, logToFile
from Utils import openDB


class AddKBMWidge(object):
    def setupUi(self, Form):
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(600, 700)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(80, 20, 50, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.NumLabel = QtWidgets.QLabel(Form)
        self.NumLabel.setObjectName("NumLabel")
        self.NumLabel.hide()
        self.Num = QtWidgets.QLineEdit(Form)
        self.Num.setObjectName("Num")
        self.Num.setMinimumHeight(30)
        self.Num.hide()
        self.TitleLabel = QtWidgets.QLabel(Form)
        self.TitleLabel.setObjectName("TitleLabel")
        self.Title = QtWidgets.QLineEdit(Form)
        self.Title.setObjectName("Title")
        self.Title.setMinimumHeight(30)
        self.SourceLabel = QtWidgets.QLabel(Form)
        self.SourceLabel.setObjectName("SourceLabel")
        self.Source = QtWidgets.QLineEdit(Form)
        self.Source.setMinimumHeight(30)
        self.Source.setObjectName("Source")
        self.PublisherLabel = QtWidgets.QLabel(Form)
        self.PublisherLabel.setObjectName("PublisherLabel")
        self.Publisher = QtWidgets.QLineEdit(Form)
        self.Publisher.setMinimumHeight(30)
        self.Publisher.setObjectName("Publisher")
        self.Publisher.setText(str(getCurrentUserId()))
        self.RtimeLabel = QtWidgets.QLabel(Form)
        self.RtimeLabel.setObjectName("RtimeLabel")
        self.Rtime = QtWidgets.QDateEdit(Form)
        self.Rtime.setMinimumHeight(30)
        self.Rtime.setObjectName("Rtime")
        self.Rtime.setDisplayFormat("yyyy-MM-dd")
        self.Rtime.setMinimumDate(QDate(2015, 1, 1))
        self.Rtime.setDate(QDate.currentDate())
        self.Rtime.setMaximumDate(QDate(2199, 1, 1))
        self.Rtime.setCalendarPopup(True)
        self.ReadrangeLabel = QtWidgets.QLabel(Form)
        self.ReadrangeLabel.setObjectName("ReadrangeLabel")
        self.Readrange = QtWidgets.QLineEdit(Form)
        self.Readrange.setMinimumHeight(30)
        self.Readrange.setObjectName("Readrange")
        self.ContentLabel = QtWidgets.QLabel(Form)
        self.ContentLabel.setObjectName("ContentLabel")
        self.Content = QtWidgets.QTextEdit(Form)
        self.Content.setMinimumHeight(30)
        self.Content.setObjectName("Content")
        self.EtimeLabel = QtWidgets.QLabel(Form)
        self.EtimeLabel.setObjectName("EtimeLabel")
        self.Etime = QtWidgets.QDateEdit(Form)
        self.Etime.setMinimumHeight(30)
        self.Etime.setObjectName("Etime")
        self.Etime.setDisplayFormat("yyyy-MM-dd")
        self.Etime.setMinimumDate(QDate(2015, 1, 1))
        self.Etime.setDate(QDate.currentDate())
        self.Etime.setMaximumDate(QDate(2199, 1, 1))
        self.Etime.setCalendarPopup(True)
        # self.remarkLabel = QtWidgets.QLabel(Form)
        # self.remarkLabel.setObjectName("remarkLabel")
        # self.remark = QtWidgets.QTextEdit(Form)
        # self.remark.setObjectName("remark")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.NumLabel)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Num)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.TitleLabel)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Title)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.SourceLabel)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Source)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.PublisherLabel)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Publisher)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.RtimeLabel)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Rtime)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.EtimeLabel)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Etime)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.ReadrangeLabel)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Readrange)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.ContentLabel)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Content)
        # self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.remarkLabel)
        # self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.remark)


        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Form)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.bindButton(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.click=0

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "新增知识信息"))
        self.NumLabel.setText(_translate("Form", "序号："))
        self.TitleLabel.setText(_translate("Form", "标题："))
        self.SourceLabel.setText(_translate("Form", "来源："))
        self.PublisherLabel.setText(_translate("Form", "发布人："))
        self.RtimeLabel.setText(_translate("Form", "发布时间："))
        self.EtimeLabel.setText(_translate("Form", "过期时间："))
        self.ReadrangeLabel.setText(_translate("Form", "阅读范围："))
        self.ContentLabel.setText(_translate("Form", "内容："))
        # self.remarkLabel.setText(_translate("Form", "备注："))
        self.conserveButton.setText(_translate("Form", "保存"))
        self.cancelButton.setText(_translate("Form", "取消"))

    def bindButton(self, Form):
        """
        czq 按钮绑定事件
        :param Dialog: 弹窗本身
        :return:
        """
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Form))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Form))

    def conserveButtonEvent(self, Form):
        """
        hsj 新建产品组件界面的保存按钮事件
        :return:
        """
        Num = self.Num.text()
        Title = self.Title.text()
        Source = self.Source.text()
        Publisher = getCurrentUserId()
        Rtime = self.Rtime.text()
        Etime = self.Etime.text()
        Readrange = self.Readrange.text()
        Content = self.Content.toPlainText()

        logger = logToFile()
        UserId = getCurrentUserId()

        # remark = self.remark.toPlainText()

        # 如果必要的信息都不为空
        if  Title == "" or Source == "" or Publisher == "" or Readrange == "" or Content == "" or Etime == "":
            logger.info("用户：" + str(UserId) + " 新建知识库数据失败（必要信息为空）")
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            num = self.checkOn(Num)
            if num == 0:
                logger.info("用户：" + str(UserId) + " 新建知识库数据失败（添加信息未通过检测）")
                revert_sql = "INSERT INTO T_Knowladge_Base_Mangement VALUES (null, '%s', '%s'," \
                                                                             " '%s', '%s', '%s', " \
                                                                             "'%s', '%s')" \
                             % (Title, Source, Publisher, Rtime, Etime, Readrange, Content)
                self.query.exec(revert_sql)
                self.db.commit()
                return
            insert_sql = "INSERT INTO T_Knowladge_Base_Mangement VALUES (null, '%s', '%s'," \
                                                                         " '%s', '%s', '%s', " \
                                                                         "'%s', '%s')" \
                         % (Title, Source, Publisher, Rtime, Etime, Readrange, Content)
            self.query.exec(insert_sql)
            self.db.commit()

            logger.info("用户：" + str(UserId) + " 新建知识库数据成功！数据为：[" +
                        str(Title) + "," + str(Source) + "," + str(Publisher) + "," +
                        str(Rtime) + "," + str(Etime) + "," + str(Readrange) + "," + str(Content) + "]")
            confirm = QMessageBox.information(QDialog(), "提示", "新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                Form.close()

    def cancelButtonEvent(self, Form):
        """
        取消按钮事件
        :return:
        """
        Form.close()

    def updateButtonEvent(self, queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """

        #print(('shank'))
        Num = self.Num.text()
        Title = self.Title.text()
        Source = self.Source.text()
        Publisher = getCurrentUserId()
        Rtime = self.Rtime.text()
        Etime = self.Etime.text()
        Readrange = self.Readrange.text()
        Content = self.Content.toPlainText()
        # remark = self.remark.toPlainText()

        queryModel.delete()

        logger = logToFile()
        UserId = getCurrentUserId()

        # 如果必要的信息都不为空
        if Title == "" or Source == "" or Publisher == "" or Readrange == "" or Content == "" or Etime == "":
            print(QMessageBox.information(QDialog(), "提示", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))

            return
        else:
            num = self.checkOn(Num)
            if num == 0:
                return
            insert_sql = "INSERT INTO T_Knowladge_Base_Mangement VALUES ('%s', '%s', '%s'," \
                                                                        " '%s', '%s', '%s', " \
                                                                        "'%s', '%s')" \
                         % (Num,Title, Source, Publisher, Rtime, Etime, Readrange, Content)
            self.query.exec(insert_sql)
            self.db.commit()
            logger.info("用户：" + str(UserId) + " 修改知识库数据成功！数据为：[" +
                        str(Title) + "," + str(Source) + "," + str(Publisher) + "," +
                        str(Rtime) + "," + str(Etime) + "," + str(Readrange) + "," + str(Content) + "]")
            confirm = QMessageBox.information(QDialog(), "提示", "更改成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                self.form.close()

    def checkOn(self, Num):
        """
        检查序号是否合理
        :return:
        """
        self.db = openDB()
        self.query = QSqlQuery()
        sql = "SELECT * FROM T_Knowladge_Base_Mangement WHERE Num = '%s'" % Num
        self.query.exec(sql)
        if self.query.next():
            print(QMessageBox.information(QDialog(), "提示", "序号已存在，请更换后重试！", QMessageBox.Yes, QMessageBox.Yes))
            return 0
        self.query.exec(sql)
        return 1

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        self.NumLabel.show()
        self.Num.show()

        self.pre_list = list
        self.label.setText("修改知识信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda: self.updateButtonEvent(queryModel))
        self.Num.setText(str(list[0]))
        self.Title.setText(str(list[1]))
        self.Source.setText(str(list[2]))
        self.Publisher.setText(str(list[3]))
        self.Rtime.setDate(QDate.fromString(str(list[4]), 'yyyy-MM-dd'))
        self.Etime.setDate(QDate.fromString(str(list[5]), 'yyyy-MM-dd'))
        self.Readrange.setText(str(list[6]))
        self.Content.setText(str(list[7]))
        # self.remark.setText(str(list[8]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = AddKBMWidge()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
