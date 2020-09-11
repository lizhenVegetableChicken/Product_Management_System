import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from ShowDiagnoseResult import ShowDiagnoseResultWidget
from Utils import openDB


class StartDiagnoseWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(774, 231)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(50, 30, 50, 50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.productName = QtWidgets.QComboBox(Dialog)
        self.productName.setObjectName("productName")
        self.horizontalLayout.addWidget(self.productName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.confirmButton = QtWidgets.QPushButton(Dialog)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_2.addWidget(self.confirmButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.bindButton()
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.addProductName()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "开始诊断"))
        self.label_2.setText(_translate("Dialog", "请选择要诊断的产品："))
        self.confirmButton.setText(_translate("Dialog", "确认"))
        self.cancelButton.setText(_translate("Dialog", "取消"))


    def addProductName(self):
        try:
            db = openDB()
            query = QSqlQuery()
            productName_list = list()
            # if not self.productName.hasFocus():
            sql = "SELECT DISTINCT ProductName From T_Diagnose"
            # print(sql)
            query.exec(sql)
            while query.next():
                productName_list.append(query.value(0))
            # print(mwid_list)
            for i in productName_list :
                self.productName.addItem(str(i))
        except Exception as e:
            print(e)

    def bindButton(self):
        self.cancelButton.clicked.connect(self.cancelButtonEvent)
        self.confirmButton.clicked.connect(self.confirmButtonEvent)

    def cancelButtonEvent(self):
        """
        取消按钮事件
        :return:
        """
        self.dialog.close()

    def confirmButtonEvent(self):
        """
        确定按钮事件
        :return:
        """
        question = ""
        answer = ""
        self.lastAnswer = ""
        self.product = self.productName.currentText()  # 保存查询的产品
        max = self.selectQuestionMaxLength()
        self.dialog.close()
        if max == 0:
            QMessageBox.information(QDialog(), "提示", "该产品暂无故障诊断树，请先建立故障树后再查询！", QMessageBox.Yes, QMessageBox.Yes)
            return
        question = self.selectQuestion(max, answer)
        for i in range(1, max+1):
            # question = self.selectQuestion(max, answer)
            question_list = question.split("？")
            question_current = question_list[i-1]
            # a = 0
            if i == 1:
                a = QMessageBox.question(QDialog(),"问题", str(i) + ". " +question_current + "？", QMessageBox.Yes, QMessageBox.No)
            else:
                # question_current_no, question_current_content = question_current.split("；")
                # if question_current_no == self.lastAnswer:
                #     a = QMessageBox.question(QDialog(),"问题", str(i) + ". " +question_current_content, QMessageBox.Yes, QMessageBox.No)
                # else:
                #     QMessageBox.
                # question_current_no, question_current_content = question_current.split("；")
                # a = QMessageBox.question(QDialog(),"问题", str(i) + ". " +question_current_content, QMessageBox.Yes, QMessageBox.No)
                a = QMessageBox.question(QDialog(), "问题", str(i) + ". " + question_current, QMessageBox.Yes,
                                         QMessageBox.No)
            if a == QMessageBox.Yes:
                answer += "是；"
                # self.lastAnswer = "是"
            else:
                answer += "否；"
                # self.lastAnswer = "否"
            result = self.matchAnswer(answer)
            if result == 1:
                self.getResolveMethod()
                w = ShowDiagnoseResultWidget()
                dialog = QDialog()
                w.setupUi(dialog)
                w.setShowData(self.result_list)
                dialog.exec()
                return
            elif result == -1:
                break
        QMessageBox.information(QDialog(), "提示", "未知故障，手工查明后，可以建立完善该产品的故障树分支！", QMessageBox.Yes, QMessageBox.Yes)
        return



    def selectQuestion(self, questionLength, answer):
        db = openDB()
        question_str = ""
        query = QSqlQuery()
        if answer == "":
            # print(1111)
            sql = "SELECT Question FROM T_Diagnose WHERE ProductName = '%s' AND AnswerCount = '%s'" % (self.product, questionLength)
        else:
            sql = """SELECT Question FROM T_Diagnose WHERE ProductName = '%s' AND AnswerCount = '%s' AND Answer LIKE '%s'""" % (self.product, questionLength, answer[:-1] + "%")
            # print(sql)
        # print(sql)
        query.exec(sql)
        if query.next():
            question_str = query.value(0)
        return question_str

    def selectQuestionMaxLength(self):
        """
        获取问题的最多次数
        :return:
        """
        db = openDB()
        maxLength = 0
        query = QSqlQuery()
        sql = "SELECT Max(AnswerCount) FROM T_Diagnose WHERE ProductName = '%s'" % (self.product)
        #print(sql)
        query.exec(sql)
        if query.next():
            maxLength = query.value(0)
            #print(maxLength)
        return int(maxLength)

    def matchAnswer(self, answer):
        db = openDB()
        maxLength = 0
        query = QSqlQuery()
        sql = "SELECT FaultName, KnowledgeID FROM T_Diagnose WHERE ProductName = '%s' and Answer = '%s'" % (self.product, answer[:-1])
        query.exec(sql)
        if query.next():
            self.result_list = [query.value(0), query.value(1)]
            return 1
        else:
            sql = "SELECT FaultName, KnowledgeID FROM T_Diagnose WHERE ProductName = '%s' and Answer LIKE '%s%%'" % (
            self.product, answer[:-1])
            query.exec(sql)
            if query.next():
                return 0
            return -1

    def getResolveMethod(self):
        db = openDB()
        query = QSqlQuery()
        sql = "SELECT Content FROM T_Knowladge_Base_Mangement WHERE Num = '%s' " % (self.result_list[1])
        query.exec(sql)
        if query.next():
            self.result_list[1] = query.value(0)
        else:
            self.result_list[1] = "知识库ID对应的数据不存在"



if  __name__ == "__main__":
    app = QApplication(sys.argv)
    w = StartDiagnoseWidget()
    dialog = QDialog()
    w.setupUi(dialog)
    dialog.exec()
