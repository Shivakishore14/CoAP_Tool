from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(476, 631)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.etPort = QtGui.QTextEdit(self.tab)
        self.etPort.setGeometry(QtCore.QRect(130, 60, 181, 31))
        self.etPort.setObjectName(_fromUtf8("etPort"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 60, 65, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.columnViewPathsAndVal = QtGui.QColumnView(self.tab)
        self.columnViewPathsAndVal.setGeometry(QtCore.QRect(10, 120, 421, 151))
        self.columnViewPathsAndVal.setObjectName(_fromUtf8("columnViewPathsAndVal"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 290, 65, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 330, 65, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 65, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.etIp = QtGui.QTextEdit(self.tab)
        self.etIp.setGeometry(QtCore.QRect(130, 20, 181, 31))
        self.etIp.setObjectName(_fromUtf8("etIp"))
        self.etPath = QtGui.QTextEdit(self.tab)
        self.etPath.setGeometry(QtCore.QRect(90, 290, 281, 31))
        self.etPath.setObjectName(_fromUtf8("etPath"))
        self.etResponse = QtGui.QTextEdit(self.tab)
        self.etResponse.setGeometry(QtCore.QRect(90, 330, 281, 81))
        self.etResponse.setObjectName(_fromUtf8("etResponse"))
        self.btnAdd = QtGui.QPushButton(self.tab)
        self.btnAdd.setGeometry(QtCore.QRect(170, 420, 92, 28))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.etLogsServer = QtGui.QTextEdit(self.tab)
        self.etLogsServer.setGeometry(QtCore.QRect(10, 460, 431, 111))
        self.etLogsServer.setObjectName(_fromUtf8("etLogsServer"))
        self.btnStartStopServer = QtGui.QPushButton(self.tab)
        self.btnStartStopServer.setGeometry(QtCore.QRect(340, 20, 81, 71))
        self.btnStartStopServer.setObjectName(_fromUtf8("btnStartStopServer"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 65, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.etUrl = QtGui.QTextEdit(self.tab_2)
        self.etUrl.setGeometry(QtCore.QRect(100, 50, 341, 31))
        self.etUrl.setObjectName(_fromUtf8("etUrl"))
        self.rbGet = QtGui.QRadioButton(self.tab_2)
        self.rbGet.setGeometry(QtCore.QRect(60, 110, 110, 25))
        self.rbGet.setObjectName(_fromUtf8("rbGet"))
        self.rbPost = QtGui.QRadioButton(self.tab_2)
        self.rbPost.setGeometry(QtCore.QRect(220, 110, 110, 25))
        self.rbPost.setObjectName(_fromUtf8("rbPost"))
        self.etRequestContent = QtGui.QTextEdit(self.tab_2)
        self.etRequestContent.setGeometry(QtCore.QRect(100, 160, 341, 121))
        self.etRequestContent.setObjectName(_fromUtf8("etRequestContent"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 65, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 360, 241, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.etLogsClient = QtGui.QTextEdit(self.tab_2)
        self.etLogsClient.setGeometry(QtCore.QRect(20, 390, 411, 171))
        self.etLogsClient.setObjectName(_fromUtf8("etLogsClient"))
        self.btnSendRqquest = QtGui.QPushButton(self.tab_2)
        self.btnSendRqquest.setGeometry(QtCore.QRect(170, 310, 121, 31))
        self.btnSendRqquest.setObjectName(_fromUtf8("btnSendRqquest"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "CoAP tool", None))
        self.label.setText(_translate("Form", "Port", None))
        self.label_2.setText(_translate("Form", "Path", None))
        self.label_3.setText(_translate("Form", "Response", None))
        self.label_4.setText(_translate("Form", "Ip", None))
        self.btnAdd.setText(_translate("Form", "Add", None))
        self.btnStartStopServer.setText(_translate("Form", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Server", None))
        self.label_5.setText(_translate("Form", "URL", None))
        self.rbGet.setText(_translate("Form", "Get", None))
        self.rbPost.setText(_translate("Form", "Post", None))
        self.label_6.setText(_translate("Form", "Content", None))
        self.label_7.setText(_translate("Form", "Response From server", None))
        self.btnSendRqquest.setText(_translate("Form", "Send Request", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Client", None))






if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
