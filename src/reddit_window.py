from os import path

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import reddit
import wall
import win_darkmode
import utils


class RedditWindow:
    def __init__(self, main_window):
        self.ui = main_window
        self.image_path = None
        self.reddit_instance = reddit.Reddit()
        self.ui.redditNextWallButton.clicked.connect(self.next_wallpaper)
        self.ui.redditWallpaperButton.clicked.connect(self.set_wallpaper)
        self.ui.redditSaveButton.clicked.connect(self.save_wallpaper)
        self.screenSize = QDesktopWidget().screenGeometry(0)
        self.ui.redditPhoto.setMaximumHeight(int(0.7 * self.screenSize.height()))
        self.ui.redditPhoto.setMaximumWidth(int(0.99 * self.screenSize.width()))
        self.ui.redditSearchTextEdit.setMaximumWidth(
            int(0.15 * self.screenSize.width())
        )

    def next_wallpaper(self):
        self.enable_wall_buttons(False)
        query = self.ui.redditSearchTextEdit.toPlainText()
        subreddit = self.ui.redditSubredditCombo.currentText()
        category = self.ui.redditCategoryCombo.currentText()
        limit = self.ui.redditLimitCombo.currentText()
        limit = int(limit)
        self.download_thread = DownloadThread(
            self.reddit_instance, subreddit, category, limit, query
        )
        self.download_thread.signal.connect(self.display_wallpaper)
        self.download_thread.start()

    def display_wallpaper(self, image_path):
        self.image_path = image_path
        self.ui.redditPhoto.setPixmap(QtGui.QPixmap(self.image_path))
        self.ui.redditPhoto.setScaledContents(True)
        self.enable_wall_buttons(True)

    def save_wallpaper(self):
        if self.image_path is None:
            messagebox = QMessageBox()
            messagebox.setWindowTitle("Wallpaper not found!")
            messagebox.setText("Choose a wallpaper to set")
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.exec_()
        else:
            wall.saveWall(
                self.image_path,
                utils.Helpers.saved_wall_path(
                    self.image_path, self.reddit_instance.get_image_extension()
                ),
            )
            messagebox = QMessageBox()
            messagebox.setWindowTitle("Wallpaper saved!")
            messagebox.setText("Wallpaper saved in User's Pictures folder")
            messagebox.setIcon(QMessageBox.Information)
            messagebox.exec_()

    def toggle_darkmode(self):
        if self.ui.redditDarkModeCheck.isChecked():
            win_darkmode.setDarkMode()
        else:
            win_darkmode.setLightMode()

    def enable_wall_buttons(self, state):
        self.ui.redditNextWallButton.setEnabled(state)
        self.ui.redditSaveButton.setEnabled(state)
        self.ui.redditWallpaperButton.setEnabled(state)

    def set_wallpaper(self):
        if self.image_path is None:
            messagebox = QMessageBox()
            messagebox.setWindowTitle("Wallpaper not found!")
            messagebox.setText("Choose a wallpaper to set")
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.exec_()
        else:
            self.toggle_darkmode()
            wall.changeBG(self.image_path)


class DownloadThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, reddit_instance, subreddit, category, limit, query):
        QThread.__init__(self)
        self.reddit_instance = reddit_instance
        self.reddit_instance.set_category(category)
        self.reddit_instance.set_subreddit(subreddit)
        self.reddit_instance.set_limit(limit)
        if query and not query.isspace():
            self.reddit_instance.set_search_query(query)

    # run method gets called when we start the thread
    def run(self):
        self.reddit_instance.next_wallpaper()
        self.image_path = self.reddit_instance.get_download_path()
        utils.Helpers.download_wall(self.image_path, self.reddit_instance.wallpaper_url)
        self.signal.emit(self.image_path)
