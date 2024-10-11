from DataBase.database import db

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Search_Client(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(969, 563)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 951, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 500, 951, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(572, 30, 381, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit.textChanged.connect(self.search_client)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "Выбрать клиента"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Введите Фамилию/Имя клиента"))

    def client_data(self):
        clients = db.get_client_table()

        self.tableWidget.setRowCount(len(clients))
        self.tableWidget.setColumnCount(len(clients[0]))
        table_column = ["ID", "Фамилия", "Имя", "Телефон", "Email", "Адрес", "Кол. заказов"]
        self.tableWidget.setHorizontalHeaderLabels(table_column)

        for i, client in enumerate(clients):
            for j, value in enumerate(client):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))

    def search_client(self):

        search_text = self.lineEdit.text()
        results_search = db.search_client(search_text)
        self.tableWidget.clearContents()

        self.tableWidget.setRowCount(len(results_search))

        for i, row in enumerate(results_search):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Search_Client()
    ui.setupUi(Dialog)
    ui.client_data()
    Dialog.show()
    sys.exit(app.exec_())
