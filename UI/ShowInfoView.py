# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowInfoView.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate,QDateTime
from PyQt5.QtWidgets import QApplication,QWidget,QDateTimeEdit
import os
import sys


class ShowInfoWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1050, 650)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(29, 9, 1000, 600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        #网格布局
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        # 日期选择框
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(),self.gridLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365 * 3))
        self.dateEdit.setCalendarPopup(True)
        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)
        #下拉列表
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        num = self.getLogsItems()
        self.comboBox.setMaxVisibleItems(num)
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)

        #日志显示框
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 1)
        self.textEdit.setReadOnly(True)

        #按钮
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)


        self.bindButton()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "系统日志查询"))
        self.pushButton.setText(_translate("Form", "显示日志"))

    def bindButton(self):
        self.pushButton.clicked.connect(lambda:self.showFileButtonClicked())
        self.dateEdit.dateTimeChanged.connect(lambda:self.getLogsItems())
    #显示日志按钮点击事件
    def showFileButtonClicked(self):
        self.textEdit.clear()
        path =os.path.abspath(os.getcwd())
        filename = self.comboBox.currentText()
        if not filename:
            self.textEdit.append("这一天没有产生日志")
            return
        filepath = path+"/logs/"+filename
        try:
            with open(filepath,"r",encoding='utf-8') as f:
                count = 1;
                data = f.readline()
                while data:
                    if data:
                        datalist = data.split("-",4)
                        self.textEdit.append("第"+str(count)+"条日志:"+datalist[1]+"/"+datalist[2]+datalist[4])
                        count = count+1
                        data = f.readline()
                    else:
                        self.textEdit.append(filename+"文件为空")
        except FileNotFoundError:
            self.textEdit.append("找不到"+filename+"文件")
    #获取要显示在下拉框中的日志文件名
    def getLogsItems(self):
        path = str(os.path.abspath(os.getcwd()))+"/logs"
        data = self.getChoisedTimeInfoFileData()
        for root,dirs,files in os.walk(path):
            self.comboBox.clear()
        for i in files:
            fileNameList = i.split("-")
            filename = fileNameList[0]+"-"+fileNameList[1]+"-"+fileNameList[2]
            if filename == data:
                self.comboBox.addItem(i)
        return len(files)
    #获取当前选择的日期的文件日期
    def getChoisedTimeInfoFileData(self):
        date = self.dateEdit.text()
        return str(date)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = ShowInfoWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())