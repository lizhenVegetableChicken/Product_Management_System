import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog


class ShowDiagnoseResultWidget(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(843, 508)
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
        self.formLayout.setContentsMargins(75, 30, 75, -1)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(Dialog)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.diagnoseResult = QtWidgets.QLineEdit(Dialog)
        self.diagnoseResult.setObjectName("diagnoseResult")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.diagnoseResult)
        self.Label_2 = QtWidgets.QLabel(Dialog)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.resolveMethod = QtWidgets.QTextEdit(Dialog)
        self.resolveMethod.setMinimumSize(QtCore.QSize(0, 250))
        self.resolveMethod.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.resolveMethod)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.confirmButton = QtWidgets.QPushButton(Dialog)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout.addWidget(self.confirmButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.confirmButton.clicked.connect(self.confirmButtonEvent)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "诊断结果"))
        self.Label.setText(_translate("Dialog", "诊断结果："))
        self.Label_2.setText(_translate("Dialog", "解决方法："))
        self.confirmButton.setText(_translate("Dialog", "确定"))

    def setShowData(self, result_list):
        self.diagnoseResult.setText(result_list[0])
        self.diagnoseResult.setDisabled(True)
        self.resolveMethod.setText(result_list[1])
        self.resolveMethod.setDisabled(True)

    def confirmButtonEvent(self):
        self.dialog.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ShowDiagnoseResultWidget()
    dialog = QDialog()
    w.setupUi(dialog)
    dialog.exec()
