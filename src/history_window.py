import sqlite3

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class HistoryWindow:
    def __init__(self, main_window):
        self.ui = main_window
        self.ui.historyClearButton.clicked.connect(self.clear_history)
        self.ui.historyRefreshButton.clicked.connect(self.refresh_history)
        self.tableWidget = self.ui.historyTableWidget
        self.refresh_history()

    def clear_history(self):
        try:
            conn = sqlite3.connect("wall_history.db")
            c = conn.cursor()
            c.execute("DELETE FROM history ")
            conn.commit()
            c.close()
            conn.close()
            self.refresh_history()
        except Exception:
            QMessageBox.warning(
                QMessageBox(), "Error", "Could not add wall to the history."
            )

    def refresh_history(self):
        connection = sqlite3.connect("wall_history.db")
        query = "SELECT * FROM history"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QTableWidgetItem(str(data))
                )
        connection.close()
        self.tableWidget.resizeColumnsToContents()
