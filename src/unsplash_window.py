
from os import path

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import unsplash
import wall
import win_darkmode
import utils


class UnsplashWindow:
    def __init__(self, main_window):
        self.ui = main_window
        self.screenSize = QDesktopWidget().screenGeometry(0)
        self.image_path = None
        self.unsplash_instance = unsplash.Unsplash(
            self.screenSize.width(), self.screenSize.height()
        )
        self.ui.unsplashPhoto.setMaximumHeight(int(0.7 * self.screenSize.height()))
        self.ui.unsplashPhoto.setMaximumWidth(int(0.99 * self.screenSize.width()))
        self.ui.unsplashSearchTextEdit.setMaximumWidth(
            int(0.15 * self.screenSize.width())
        )
        self.ui.unsplashNextWallButton.clicked.connect(self.next_wallpaper)
        self.ui.unsplashWallpaperButton.clicked.connect(self.set_wallpaper)
        self.ui.unsplashSaveButton.clicked.connect(self.save_wallpaper)

    def next_wallpaper(self):
        self.enable_wall_buttons(False)
        query = self.ui.unsplashSearchTextEdit.toPlainText()
        if self.ui.unsplashFeaturedCheck.isChecked():
            is_featured = True
        else:
            is_featured = False

        self.download_thread = UnsplashDownloadThread(
            self.unsplash_instance, is_featured, query
        )
        self.download_thread.signal.connect(self.display_wallpaper)
        self.download_thread.start()

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
                    self.image_path, 
                    self.unsplash_instance.get_image_extension()
                    )
            )
            messagebox = QMessageBox()
            messagebox.setWindowTitle("Wallpaper saved!")
            messagebox.setText("Wallpaper saved in User's Pictures folder")
            messagebox.setIcon(QMessageBox.Information)
            messagebox.exec_()

    def set_wallpaper(self):
        if self.image_path is None:
            messagebox = QMessageBox()
            messagebox.setWindowTitle("Wallpaper not found!")
            messagebox.setText("Choose a wallpaper to set")
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.exec_()
        else:
            self.toggle_dark_mode()
            wall.changeBG(self.image_path)
            if not utils.Helpers.insert_history(self.unsplash_instance.wallpaper_url, "unsplash"):
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not add wall to the history.')

    def display_wallpaper(self, image_path):
        self.image_path = image_path
        self.ui.unsplashPhoto.setPixmap(QtGui.QPixmap(self.image_path))
        self.ui.unsplashPhoto.setScaledContents(True)
        self.enable_wall_buttons(True)

    def toggle_dark_mode(self):
        if self.ui.unsplashDarkModeCheck.isChecked():
            win_darkmode.setDarkMode()
        else:
            win_darkmode.setLightMode()

    def enable_wall_buttons(self, state):
        self.ui.unsplashNextWallButton.setEnabled(state)
        self.ui.unsplashSaveButton.setEnabled(state)
        self.ui.unsplashWallpaperButton.setEnabled(state)

class UnsplashDownloadThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, unsplash_instance,is_featured, query):
        QThread.__init__(self)
        self.unsplash_instance = unsplash_instance
        self.unsplash_instance.set_featured(is_featured)
        if query and not query.isspace():
            self.unsplash_instance.set_query(query)

    def run(self):
        self.unsplash_instance.get_unsplash_pic()
        print(self.unsplash_instance.wallpaper_url)
        self.image_path = self.unsplash_instance.get_download_path()
        utils.Helpers.download_wall(self.image_path,self.unsplash_instance.wallpaper_url)
        self.signal.emit(self.image_path)
