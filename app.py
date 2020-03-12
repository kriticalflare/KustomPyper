import os.path
import sys
from os import path

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

from gui import Ui_MainWindow
import wall
import reddit


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.image_path = None
        self.reddit_instance = reddit.Reddit()
        self.nextWallButton.clicked.connect(self.nextWallpaper)
        self.wallpaperButton.clicked.connect(self.setWallpaper)

    def nextWallpaper(self):
        subreddit = self.subredditComboBox.currentText()
        category = self.categoryComboBox.currentText()
        limit = self.limitComboBox.currentText()
        limit = int(limit)
        self.reddit_instance.setCategory(category)
        self.reddit_instance.setSubreddit(subreddit)
        self.reddit_instance.setLimit(limit)
        self.reddit_instance.nextWallpaper()
        self.image_path = self.reddit_instance.download_path()
        self.reddit_instance.download_wall()
        self.photo.setPixmap(QtGui.QPixmap(self.image_path))
        self.photo.setScaledContents(True)
        
    def setWallpaper(self):
        if self.image_path is None:
            messagebox = QMessageBox()
            messagebox.setWindowTitle('Wallpaper not found!')
            messagebox.setText('Choose a wallpaper to set')
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.exec_()
        else: 
            wall.changeBG(self.image_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
