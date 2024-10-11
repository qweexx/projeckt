
from search_client_window import Search_Client

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Add_Order(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1222, 543)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 1201, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 70, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(1060, 20, 151, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(1060, 70, 151, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_3.clicked.connect(self.search_client_window)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Добавить заказ"))
        self.pushButton_2.setText(_translate("Dialog", "Добавить товар"))
        self.pushButton_3.setText(_translate("Dialog", "Найти клиента"))
        self.pushButton_4.setText(_translate("Dialog", "Добавить клиента"))


    def add_order_data(self):
        table_column = ["ID", "Процесс", "Дата заказа", "Имя клиента", "Контакты", "Адресс", "Имя сотрудника",
                        "Стоимость"]
        self.tableWidget.setColumnCount(len(table_column))
        self.tableWidget.setHorizontalHeaderLabels(table_column)
        self.tableWidget.setRowCount(1)

    def search_client_window(self):
        self.search_client = QtWidgets.QDialog()
        self.ui = Search_Client()
        self.ui.setupUi(self.search_client)
        self.ui.client_data()
        self.search_client.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Add_Order()
    ui.setupUi(Dialog)
    ui.add_order_data()
    Dialog.show()
    sys.exit(app.exec_())
