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
        self.subredditLabel = QtWidgets.QLabel(self.centralwidget)
        self.subredditLabel.setGeometry(QtCore.QRect(800, 550, 101, 20))
        self.subredditLabel.setObjectName("subredditLabel")
        self.subredditComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.subredditComboBox.setGeometry(QtCore.QRect(942, 550, 151, 22))
        self.subredditComboBox.setEditable(True)
        self.subredditComboBox.setObjectName("subredditComboBox")
        self.subredditComboBox.addItem("")
        self.subredditComboBox.addItem("")
        self.categoryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.categoryComboBox.setGeometry(QtCore.QRect(940, 590, 151, 22))
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.categoryLabel.setGeometry(QtCore.QRect(800, 590, 91, 16))
        self.categoryLabel.setObjectName("categoryLabel")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "KustomPyper"))
        self.photo.setText(_translate("MainWindow", "Set a random wallpaper from reddit!"))
        self.wallpaperButton.setText(_translate("MainWindow", "Set as wallpaper"))
        self.nextWallButton.setText(_translate("MainWindow", "Next wallpaper"))
        self.subredditLabel.setText(_translate("MainWindow", "Subreddit : "))
        self.subredditComboBox.setItemText(0, _translate("MainWindow", "wallpapers"))
        self.subredditComboBox.setItemText(1, _translate("MainWindow", "amoledbackgrounds"))
        self.categoryComboBox.setItemText(0, _translate("MainWindow", "hot"))
        self.categoryComboBox.setItemText(1, _translate("MainWindow", "rising"))
        self.categoryComboBox.setItemText(2, _translate("MainWindow", "new"))
        self.categoryComboBox.setItemText(3, _translate("MainWindow", "top"))
        self.categoryComboBox.setItemText(4, _translate("MainWindow", "controversial"))
        self.categoryLabel.setText(_translate("MainWindow", "Category :"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
