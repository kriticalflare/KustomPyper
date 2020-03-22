from datetime import datetime
from os import path

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import reddit
import wall
import win_darkmode


class RedditWindow():

    def __init__(self, main_window):
        self.ui = main_window
        self.image_path = None
        self.reddit_instance = reddit.Reddit()
        self.ui.redditNextWallButton.clicked.connect(self.nextWallpaper)
        self.ui.redditWallpaperButton.clicked.connect(self.setWallpaper)
        self.ui.redditSaveButton.clicked.connect(self.saveWallpaper)
        self.ui.helpAction.triggered.connect(self.openHelpUrl)
        self.screenSize = QDesktopWidget().screenGeometry(0)
        self.ui.redditPhoto.setMaximumHeight(int(0.7 * self.screenSize.height()))
        self.ui.redditPhoto.setMaximumWidth(int(0.99 * self.screenSize.width()))
        self.ui.redditSearchTextEdit.setMaximumWidth(int(0.15 * self.screenSize.width()))
    
    def nextWallpaper(self):
        self.enableWallButtons(False)
        query = self.ui.redditSearchTextEdit.toPlainText()
        subreddit = self.ui.redditSubredditCombo.currentText()
        category = self.ui.redditCategoryCombo.currentText()
        limit = self.ui.redditLimitCombo.currentText()
        limit = int(limit)
        self.download_thread = DownloadThread(self.reddit_instance,subreddit,category,limit,query)
        self.download_thread.signal.connect(self.displayWallpaper)
        self.download_thread.start()

    def displayWallpaper(self,image_path):
        self.image_path = image_path
        self.ui.redditPhoto.setPixmap(QtGui.QPixmap(self.image_path))
        self.ui.redditPhoto.setScaledContents(True)
        self.enableWallButtons(True)

    def saveWallpaper(self):
        if self.image_path is None:
            messagebox = QMessageBox()
            messagebox.setWindowTitle('Wallpaper not found!')
            messagebox.setText('Choose a wallpaper to set')
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.exec_()
        else: 
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            timestamp = int(timestamp)
            wall.saveWall(self.image_path, "KustomPyper_" + str(timestamp) + self.reddit_instance.getImageExtension())
            messagebox = QMessageBox()
            messagebox.setWindowTitle('Wallpaper saved!')
            messagebox.setText("Wallpaper saved in User's Pictures folder")
            messagebox.setIcon(QMessageBox.Information)
            messagebox.exec_()
        
    def toggleDarkMode(self):
        if self.ui.darkModeCheckBox.isChecked():
            win_darkmode.setDarkMode()
        else:
            win_darkmode.setLightMode()

    def enableWallButtons(self,state):
        self.ui.redditNextWallButton.setEnabled(state)
        self.ui.redditSaveButton.setEnabled(state)
        self.ui.redditWallpaperButton.setEnabled(state)

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

    def openHelpUrl(self):
        url = QUrl('https://github.com/kriticalflare/KustomPyper/blob/master/README.md')
        if not QtGui.QDesktopServices.openUrl(url):
            QMessageBox.warning(self, 'Open Url', 'Could not open https://github.com/kriticalflare/KustomPyper/')

class DownloadThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self,reddit_instance,subreddit,category,limit,query):
        QThread.__init__(self)
        self.reddit_instance = reddit_instance
        self.reddit_instance.setCategory(category)
        self.reddit_instance.setSubreddit(subreddit)
        self.reddit_instance.setLimit(limit)
        if (query and not query.isspace()): 
            self.reddit_instance.setSearchQuery(query)   
        

    # run method gets called when we start the thread
    def run(self):
        self.reddit_instance.nextWallpaper()
        self.image_path = self.reddit_instance.downloadPath()
        self.reddit_instance.downloadWall()
        self.signal.emit(self.image_path)
