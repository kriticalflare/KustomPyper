# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.u.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 846)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 9, 1121, 501))
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.wallpaperButton = QtWidgets.QPushButton(self.centralwidget)
        self.wallpaperButton.setGeometry(QtCore.QRect(940, 750, 121, 28))
        self.wallpaperButton.setObjectName("wallpaperButton")
        self.nextWallButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextWallButton.setGeometry(QtCore.QRect(790, 750, 111, 28))
        self.nextWallButton.setObjectName("nextWallButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(800, 550, 101, 20))
        self.label.setObjectName("label")
        self.subredditComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.subredditComboBox.setGeometry(QtCore.QRect(942, 550, 151, 22))
        self.subredditComboBox.setEditable(True)
        self.subredditComboBox.setObjectName("subredditComboBox")
        self.subredditComboBox.addItem("")
        self.subredditComboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 26))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.photo.setText(_translate("MainWindow", "Set a random wallpaper from reddit!"))
        self.wallpaperButton.setText(_translate("MainWindow", "Set as wallpaper"))
        self.nextWallButton.setText(_translate("MainWindow", "Next wallpaper"))
        self.label.setText(_translate("MainWindow", "Subreddit : "))
        self.subredditComboBox.setItemText(0, _translate("MainWindow", "wallpapers"))
        self.subredditComboBox.setItemText(1, _translate("MainWindow", "amoledbackgrounds"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
