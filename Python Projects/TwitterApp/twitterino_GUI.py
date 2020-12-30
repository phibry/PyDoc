from PyQt5 import QtCore, QtGui, QtWidgets
from twitterino import *
import matplotlib.pyplot as plt

class Ui_Dialog(twitterwinnerino):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 1112)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 411, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 460, 411, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 534, 409, 41))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 310, 411, 70))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 570, 411, 521))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 210, 411, 70))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.layoutWidget3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 110, 411, 70))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.connectMethods()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Twitterwinnerino KPR"))
        self.pushButton.setText(_translate("Dialog", "Refresh"))
        self.pushButton_2.setText(_translate("Dialog", "Winners of Twitterino"))
        self.label_3.setText(_translate("Dialog", "Display"))
        self.label_4.setText(_translate("Dialog", "Number of Winners"))
        self.textBrowser.setText(_translate("Dialog", "Welcome to Twitterwinnerino!"))
        self.label_2.setText(_translate("Dialog", "#Hashtag 2"))
        self.label.setText(_translate("Dialog", "#Hashtag 1"))
        
    def keyPressEvent(self, event):
    #press ESCAPE to quit the application
        key = event.key()
        if key == Qt.Key_Escape:
            self.app.quit()

    def connectMethods(self):
        self.pushButton.clicked.connect(self.refresherino)
        self.pushButton_2.clicked.connect(self.winnerButton)
 
    def getHashtag_1(self):
        self.hash_1 = str(self.lineEdit.text())
        return(self.hash_1)

    def getHashtag_2(self):
        self.hash_2 = str(self.lineEdit_2.text())
        return(self.hash_2)

    def getCount(self):
        self.count = int(self.lineEdit_3.text())
        return(self.count)

    def winnerButton(self):
        self.hashtagerino_1(self.getHashtag_1())
        self.hashtagerino_2(self.getHashtag_2())
        self.counterino(self.getCount())        
        self.winnerprint = self.winnerino()
        if isinstance(self.winnerprint, list):
            self.textBrowser.append("The winners are:")
            for i in range(len(self.winnerprint)):
                self.textBrowser.append(str(self.winnerprint[i]))
            
        else:
            self.textBrowser.append(str(self.winnerprint))
        plt.close()
        self.appenddict()

    def refresherino(self):
#        self.appenddict()
        self.refreshGUI()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

