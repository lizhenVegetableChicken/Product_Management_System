import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from Login_recorder import logToFile, getCurrentUserId
from Utils import openDB


class AddFaultWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(789, 668)
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
        self.formLayout.setContentsMargins(50, 30, 50, 50)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.faultID = QtWidgets.QLineEdit(Dialog)
        self.faultID.setObjectName("faultID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.faultID)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.faultName = QtWidgets.QLineEdit(Dialog)
        self.faultName.setObjectName("faultName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.faultName)
        self.Label_3 = QtWidgets.QLabel(Dialog)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.productName = QtWidgets.QLineEdit(Dialog)
        self.productName.setObjectName("productName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.productName)
        self.label_count = QtWidgets.QLabel(Dialog)
        self.label_count.setObjectName("label_count")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_count)
        self.answerCount = QtWidgets.QSpinBox(Dialog)
        self.answerCount.setObjectName("answerCount")
        self.answerCount.setMaximum(99)
        self.answerCount.setMinimum(1)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.answerCount)
        self.Label_4 = QtWidgets.QLabel(Dialog)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.question = QtWidgets.QTextEdit(Dialog)
        self.question.setMinimumSize(QtCore.QSize(0, 250))
        self.question.setObjectName("question")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.question)
        self.Label_5 = QtWidgets.QLabel(Dialog)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.answer = QtWidgets.QLineEdit(Dialog)
        self.answer.setObjectName("answer")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.answer)
        # self.label_count = QtWidgets.QLabel(Dialog)
        # self.label_count.setObjectName("label_count")
        # self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.Label_6 = QtWidgets.QLabel(Dialog)
        self.Label_6.setObjectName("Label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.knowledgeID = QtWidgets.QComboBox(Dialog)
        self.knowledgeID.setObjectName("knowledgeID")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.knowledgeID)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.conserveButton = QtWidgets.QPushButton(Dialog)
        self.conserveButton.setObjectName("conserveButton")
        self.horizontalLayout.addWidget(self.conserveButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.bindButton(Dialog)
        self.getKnowledgeID()
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # self.answerCount.chan

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新建故障分支"))
        self.Label.setText(_translate("Dialog", "故障编号："))
        self.Label_2.setText(_translate("Dialog", "故障名称："))
        self.Label_3.setText(_translate("Dialog", "适用产品:"))
        self.label_count.setText(_translate("Dialog", "决策分支深度:"))
        self.Label_4.setText(_translate("Dialog", "故障树节点内容："))
        self.Label_5.setText(_translate("Dialog", "故障树节点答案："))
        self.Label_6.setText(_translate("Dialog", "解决方案编号："))
        self.conserveButton.setText(_translate("Dialog", "保存"))
        self.cancelButton.setText(_translate("Dialog", "取消"))
        self.faultID.setText(self.getFaultID())
        self.faultID.setDisabled(True)
        self.question.setPlaceholderText("输入说明：每个问题直接必须用？分割，所以需要严格按照格式输入。\n请按照如下格式录入信息：\n问题一？问题二？问题三？\n比如：\n电视机是否正常通电？电视机显示是否正确？电视机声音是否正常？")
        self.answer.setPlaceholderText("输入格式：问题一答案；问题二答案\t比如：是；否；是")
    def bindButton(self, Dialog):
        self.conserveButton.clicked.connect(lambda: self.conserveButtonEvent(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelButtonEvent(Dialog))
        self.answerCount.valueChanged.connect(self.answerCountEvent)
        self.productName.textChanged.connect(self.productNameEvent)

    def answerCountEvent(self):
        try:
            db = openDB()
            query = QSqlQuery()
            if self.answerCount.hasFocus():
                sql = "SELECT Question, Answer From T_Diagnose WHERE AnswerCount = '%s' AND ProductName = '%s'" % (self.answerCount.text(), self.productName.text())
                query.exec(sql)
                if query.next():
                    question = query.value(0)
                    answer = query.value(1)
                    #             self.productName.setText(productname)
                    self.question.setText(question)
                    self.answer.setText(answer[:-1])
        except Exception as e:
            print(e)

    def productNameEvent(self):
        # print(1111)
        try:
            db = openDB()
            query = QSqlQuery()
            # if not self.answerCount.hasFocus():
            sql = "SELECT Question, Answer From T_Diagnose WHERE AnswerCount = '%s' AND ProductName = '%s'" % (
            self.answerCount.text(), self.productName.text())
            query.exec(sql)
            if query.next():
                question = query.value(0)
                answer = query.value(1)
                #             self.productName.setText(productname)
                self.question.setText(question)
                self.answer.setText(answer[:-1])
        except Exception as e:
            print(e)

    def cancelButtonEvent(self, Dialog):
        """
        取消按钮事件
        :return:
        """
        Dialog.close()

    def getFaultID(self):
        max_no = ''
        db = openDB()
        q = QSqlQuery()
        date_str = QDate.currentDate().toString("yyyyMMdd")
        sql = "SELECT FaultID FROM T_Diagnose WHERE ID=(SELECT MAX(ID) FROM T_Diagnose)"
        if q.exec(sql):
            while q.next():
                max_no = q.value(0)
        db.close()
        if date_str > max_no[1:9]:
            return 'G' + date_str + '001'
        else:
            return 'G' + str(int(max_no[1:]) + 1)

    def getKnowledgeID(self):
        try:
            db = openDB()
            query = QSqlQuery()
            knowledgeID_list = list()
            if not self.knowledgeID.hasFocus():
                sql = "SELECT Num FROM T_Knowladge_Base_Mangement"
                # print(sql)
                query.exec(sql)
                while query.next():
                    knowledgeID_list.append(query.value(0))
            # print(mwid_list)
            for i in knowledgeID_list:
                self.knowledgeID.addItem(str(i))
        except Exception as e:
            print(e)

    def conserveButtonEvent(self, Dialog):
        """
        hsj 新建产品界面的保存按钮事件
        :return:
        """
        logger = logToFile()
        UserId = getCurrentUserId()
        faultID = self.faultID.text()
        faultName = self.faultName.text()
        productName = self.productName.text()
        question_str = self.question.toPlainText()
        question = question_str.replace("?", "？").replace(",", "，")
        answer_str = self.answer.text()
        if answer_str.endswith("；") or answer_str.endswith(";"):
            answer_str = answer_str[:-1]
        answer = answer_str.replace(";", "；")
        answers = answer.split("；")
        answerCount = len(answers)
        if self.answerCount.text() != str(answerCount):
            QMessageBox.information(QDialog(), "提示", "输入的问题答案和决策树深度不匹配！", QMessageBox.Yes, QMessageBox.Yes)
            return
        knowledgeID = self.knowledgeID.currentText()


        # 如果必要的信息都不为空
        if productName == "" or faultName == "":
            logger.info("用户：" + str(UserId) + " 新建故障树分支失败（必要信息为空）")
            print(QMessageBox.warning(QDialog(), "警告", "有字段为空，添加失败！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            self.db = openDB()
            self.query = QSqlQuery()
            insert_sql = "INSERT INTO T_Diagnose VALUES (null, '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %\
                         (faultID, faultName, productName, question, answer, answerCount, knowledgeID)
            print(insert_sql)
            self.query.exec_(insert_sql)
            self.db.commit()
            logger.info("用户：" + str(UserId) + " 新建故障树分支成功！数据为：[" +
                        str(faultID) + "," + str(faultName) + "," + str(productName) + "," +
                        str(question) + "," + str(answer) + "," + str(answerCount) + "," + str(knowledgeID) + "]")
            confirm = QMessageBox.information(QDialog(), "提示", "故障树分支新建成功！", QMessageBox.Yes, QMessageBox.Yes)
            if confirm == QMessageBox.Yes:
                Dialog.close()

    def updateData(self, list, queryModel):
        """
        修改产品批次信息
        :param list:
        :return:
        """
        self.pre_list = list
        list = list[1:]
        self.label.setText("修改故障分支信息")
        self.conserveButton.disconnect()
        self.conserveButton.clicked.connect(lambda :self.updateButtonEvent(queryModel))
        self.faultID.setText(list[0])
        self.faultID.setDisabled(True)
        self.faultName.setText(list[1])
        self.productName.setText(list[2])
        self.question.setText(list[3])
        self.answer.setText(list[4])
        self.answerCount.setValue(int(list[5]))
        self.knowledgeID.setCurrentText(list[6])

    def showData(self, list, queryModel):
        self.updateData(list, queryModel)
        self.label.setText("详细故障分支信息")
        self.faultID.setDisabled(True)
        self.faultName.setDisabled(True)
        self.productName.setDisabled(True)
        self.question.setDisabled(True)
        self.answer.setDisabled(True)
        self.knowledgeID.setDisabled(True)
        self.conserveButton.setVisible(False)
        self.cancelButton.setVisible(False)
        self.answerCount.setDisabled(True)

    def updateButtonEvent(self, queryModel):
        """
        更新界面按钮事件
        :param queryModel:
        :return:
        """
        faultID = self.faultID.text()
        faultName = self.faultName.text()
        productName = self.productName.text()
        question_str = self.question.toPlainText()
        question = question_str.replace("?", "？")
        answer_str = self.answer.text()
        if answer_str.endswith("；") or answer_str.endswith(";"):
            answer_str = answer_str[:-1]
        answer = answer_str.replace(";", "；")
        answers = answer.split("；")
        answerCount = len(answers)

        logger = logToFile()
        UserId = getCurrentUserId()

        if self.answerCount.text() != str(answerCount):
            QMessageBox.information(QDialog(), "提示", "输入的问题答案和决策树深度不匹配！", QMessageBox.Yes, QMessageBox.Yes)
            return
        knowledgeID = self.knowledgeID.currentText()

        self.db = openDB()
        self.query = QSqlQuery()
        update_sql = "UPDATE T_Diagnose SET (FaultName, ProductName, Question, Answer, Answercount, KnowledgeID) = " \
                     "('%s', '%s','%s','%s','%s','%s') WHERE FaultID = '%s'" % \
                     (faultName, productName, question, answer, answerCount, knowledgeID, faultID)
        print(update_sql)
        self.query.exec(update_sql)
        self.db.commit()
        logger.info("用户：" + str(UserId) + " 修改故障树分支成功！数据为：[" +
                    str(faultID) + "," + str(faultName) + "," + str(productName) + "," +
                    str(question) + "," + str(answer) + "," + str(answerCount) + "," + str(knowledgeID) + "]")
        confirm = QMessageBox.information(QDialog(), "提示", "故障分支更改成功！", QMessageBox.Yes, QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            self.dialog.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QDialog()
    w = AddFaultWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
