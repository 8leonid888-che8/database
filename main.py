import sys

from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QWidget, QTableView, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName("coffee.sqlite")
        db.open()
        view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)
        self.setGeometry(300, 100, 650, 450)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())