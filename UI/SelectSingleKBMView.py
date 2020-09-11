

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QHeaderView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

class SelectrKnowledgeBase(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(532, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
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
        self.NumLabel = QtWidgets.QLabel(Form)
        self.NumLabel.setObjectName("NumLabel")
        self.Num = QtWidgets.QLineEdit(Form)
        self.Num.setObjectName("Num")
        self.Num.setEnabled(False)
        self.TitleLabel = QtWidgets.QLabel(Form)
        self.TitleLabel.setObjectName("TitleLabel")
        self.Title = QtWidgets.QLineEdit(Form)
        self.Title.setObjectName("Title")
        self.Title.setEnabled(False)
        self.SourceLabel = QtWidgets.QLabel(Form)
        self.SourceLabel.setObjectName("SourceLabel")
        self.Source = QtWidgets.QLineEdit(Form)
        self.Source.setObjectName("Source")
        self.Source.setEnabled(False)
        self.PublisherLabel = QtWidgets.QLabel(Form)
        self.PublisherLabel.setObjectName("PublisherLabel")
        self.Publisher = QtWidgets.QLineEdit(Form)
        self.Publisher.setObjectName("Publisher")
        self.Publisher.setEnabled(False)
        self.RtimeLabel = QtWidgets.QLabel(Form)
        self.RtimeLabel.setObjectName("RtimeLabel")
        self.Rtime = QtWidgets.QLineEdit(Form)
        self.Rtime.setObjectName("Rtime")
        self.Rtime.setEnabled(False)
        self.ReadrangeLabel = QtWidgets.QLabel(Form)
        self.ReadrangeLabel.setObjectName("ReadrangeLabel")
        self.Readrange = QtWidgets.QLineEdit(Form)
        self.Readrange.setObjectName("Readrange")
        self.Readrange.setEnabled(False)
        self.ContentLabel = QtWidgets.QLabel(Form)
        self.ContentLabel.setObjectName("ContentLabel")
        self.Content = QtWidgets.QTextEdit(Form)
        self.Content.setObjectName("Content")
        self.Content.setEnabled(False)
        self.EtimeLabel = QtWidgets.QLabel(Form)
        self.EtimeLabel.setObjectName("EtimeLabel")
        self.Etime = QtWidgets.QLineEdit(Form)
        self.Etime.setObjectName("Etime")
        self.Etime.setEnabled(False)

        # self.remarkLabel = QtWidgets.QLabel(Form)
        # self.remarkLabel.setObjectName("remarkLabel")
        # self.remark = QtWidgets.QTextEdit(Form)
        # self.remark.setObjectName("remark")
        # self.remark.setEnabled(False)
        # self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.remarkLabel)
        # self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.remark)

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

        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "查看知识信息"))
        self.NumLabel.setText(_translate("Form", "序号："))
        self.TitleLabel.setText(_translate("Form", "标题："))
        self.SourceLabel.setText(_translate("Form", "来源："))
        self.PublisherLabel.setText(_translate("Form", "发布人："))
        self.RtimeLabel.setText(_translate("Form", "发布时间："))
        self.EtimeLabel.setText(_translate("Form", "过期时间："))
        self.ReadrangeLabel.setText(_translate("Form", "阅读范围："))
        self.ContentLabel.setText(_translate("Form", "内容："))
        # self.remarkLabel.setText(_translate("Form", "备注："))


    def setData(self, list):
        """
        czq 设置单个产品查询结果
        :param list: 单个查询结果
        :return:
        """
        self.Num.setText(str(list[0]))
        self.Title.setText(str(list[1]))
        self.Source.setText(str(list[2]))
        self.Publisher.setText(str(list[3]))
        self.Rtime.setText(str(list[4]))
        self.Etime.setText(str(list[5]))
        self.Readrange.setText(str(list[6]))
        self.Content.setText(str(list[7]))
        # self.remark.setText(str(list[8]))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = SelectrKnowledgeBase()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
