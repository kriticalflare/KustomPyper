
from os import path

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import bing
import wall
import win_darkmode
import utils

class BingWindow:
    def __init__(self, main_window):
        self.ui = main_window
        self.screenSize = QDesktopWidget().screenGeometry(0)
        self.image_path = None
        self.bing_instance = bing.Bing()
        self.ui.bingPhoto.setMaximumHeight(int(0.7 * self.screenSize.height()))
        self.ui.bingPhoto.setMaximumWidth(int(0.99 * self.screenSize.width()))
        self.ui.bingNextWallButton.clicked.connect(self.next_wallpaper)
        self.ui.bingWallpaperButton.clicked.connect(self.set_wallpaper)
        self.ui.bingSaveButton.clicked.connect(self.save_wallpaper)

    def next_wallpaper(self):
        self.enable_wall_buttons(False)
        country = self.ui.bingCountryCombo.currentText()
        self.download_thread = BingDownloadThread(self.bing_instance, country)
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
                    self.bing_instance.get_image_extension()
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
            if not utils.Helpers.insert_history(self.bing_instance.wallpaper_url,"bing"):
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not add wall to the history.')

    def display_wallpaper(self, image_path):
        self.image_path = image_path
        self.ui.bingPhoto.setPixmap(QtGui.QPixmap(self.image_path))
        self.ui.bingPhoto.setScaledContents(True)
        self.enable_wall_buttons(True)

    def toggle_dark_mode(self):
        if self.ui.bingDarkModeCheck.isChecked():
            win_darkmode.setDarkMode()
        else:
            win_darkmode.setLightMode()

    def enable_wall_buttons(self, state):
        self.ui.bingNextWallButton.setEnabled(state)
        self.ui.bingSaveButton.setEnabled(state)
        self.ui.bingWallpaperButton.setEnabled(state)

class BingDownloadThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, bing_instance, country):
        QThread.__init__(self)
        self.bing_instance = bing_instance
        self.bing_instance.set_country(country)

    def run(self):
        self.bing_instance.get_wallpapers()
        self.image_path = self.bing_instance.get_download_path()
        utils.Helpers.download_wall(self.image_path, self.bing_instance.wallpaper_url)
        self.signal.emit(self.image_path)
