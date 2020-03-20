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
import win_darkmode


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.image_path = None
        self.reddit_instance = reddit.Reddit()
        self.nextWallButton.clicked.connect(self.nextWallpaper)
        self.wallpaperButton.clicked.connect(self.setWallpaper)
        self.screenSize = QDesktopWidget().screenGeometry(0)
        self.setMinimumSize(self.screenSize.width(),self.screenSize.height())
        self.photo.setMaximumHeight(int(0.7 * self.screenSize.height()))
        self.photo.setMaximumWidth(int(0.99 * self.screenSize.width()))
        self.showMaximized()

    def nextWallpaper(self):
        self.nextWallButton.setEnabled(False)
        subreddit = self.subredditComboBox.currentText()
        category = self.categoryComboBox.currentText()
        limit = self.limitComboBox.currentText()
        limit = int(limit)
        self.download_thread = DownloadThread(self.reddit_instance,subreddit,category,limit)
        self.download_thread.signal.connect(self.displayWallpaper)
        self.download_thread.start()

    def displayWallpaper(self,image_path):
        self.image_path = image_path
        self.photo.setPixmap(QtGui.QPixmap(self.image_path))
        self.photo.setScaledContents(True)
        self.nextWallButton.setEnabled(True)

        
    def toggleDarkMode(self):
        if self.darkModeCheckBox.isChecked():
            win_darkmode.setDarkMode()
        else:
            win_darkmode.setLightMode()

    def setWallpaper(self):
        if self.image_path is None:
            messagebox = QMessageBox()
            messagebox.setWindowTitle('Wallpaper not found!')
            messagebox.setText('Choose a wallpaper to set')
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.exec_()
        else: 
            self.toggleDarkMode()
            wall.changeBG(self.image_path)

class DownloadThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self,reddit_instance,subreddit,category,limit):
        QThread.__init__(self)
        self.reddit_instance = reddit_instance
        self.reddit_instance.setCategory(category)
        self.reddit_instance.setSubreddit(subreddit)
        self.reddit_instance.setLimit(limit)
        

    # run method gets called when we start the thread
    def run(self):
        self.reddit_instance.nextWallpaper()
        self.image_path = self.reddit_instance.downloadPath()
        self.reddit_instance.downloadWall()
        self.signal.emit(self.image_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
