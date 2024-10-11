from DataBase.database import db
from add_order_window import Add_Order

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1510, 845)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 60, 1401, 711))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 1201, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(1220, 50, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(1220, 10, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 50, 151, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView = QtWidgets.QListView(self.widget)
        self.listView.setGeometry(QtCore.QRect(1220, 90, 171, 192))
        self.listView.setObjectName("listView")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(1230, 100, 141, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setGeometry(QtCore.QRect(1230, 130, 141, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(1230, 160, 141, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tabWidget.currentChanged.connect(self.change_tab)
        self.pushButton.clicked.connect(self.change_order)
        self.pushButton_2.clicked.connect(self.add_order)
        self.pushButton_3.clicked.connect(self.save_order)

        self.lineEdit.textChanged.connect(self.search_order)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Изменить заказ"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить заказ"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Поиск по заказам"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить"))
        self.checkBox.setText(_translate("MainWindow", "Processing"))
        self.checkBox_3.setText(_translate("MainWindow", "Completed"))
        self.checkBox_2.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Продажи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Приемка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Перемещение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Списание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Клиенты"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Товары/Склады"))

    def load_first_tab(self):
        orders = db.get_orders_with_full_fill_data()

        table_column = ["ID", "Процесс", "Дата заказа", "Имя клиента", "Контакты", "Адрес", "Имя сотрудника", "Стоимость"]

        self.tableWidget.setRowCount(len(orders))
        self.tableWidget.setColumnCount(len(orders[0]))

        self.tableWidget.setHorizontalHeaderLabels(table_column)

        for i, order in enumerate(orders):
            for j, value in enumerate(order):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))

    def search_order(self):

        search_text = self.lineEdit.text()
        results_search = db.search_order(search_text)
        self.tableWidget.clearContents()

        self.tableWidget.setRowCount(len(results_search))

        for i, row in enumerate(results_search):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
    def change_tab(self, index):
        print(f"Current Tab Index: {index}")
        print(self.tabWidget.currentIndex())

    def add_order(self):
        self.add_order = QtWidgets.QDialog()
        self.ui = Add_Order()
        self.ui.setupUi(self.add_order)
        self.ui.add_order_data()
        self.add_order.show()

    def change_order(self):
        print('Open window for change order')

    def save_order(self):
        print('Save order')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.load_first_tab()
    MainWindow.show()
    sys.exit(app.exec_())
