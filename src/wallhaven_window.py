from os import path

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import wallhaven
import wall
import win_darkmode
import utils


class WallhavenWindow:
    def __init__(self, main_window):
        self.ui = main_window
        self.screenSize = QDesktopWidget().screenGeometry(0)
        self.image_path = None
        self.wh_instance = wallhaven.Wallhaven(self.screenSize.width(), self.screenSize.height())
        self.ui.whPhoto.setMaximumHeight(int(0.7 * self.screenSize.height()))
        self.ui.whPhoto.setMaximumWidth(int(0.99 * self.screenSize.width()))
        # self.ui.whSearchTextEdit.setMaximumWidth(
        #     int(0.15 * self.screenSize.width())
        # )
        self.ui.whNextWallButton.clicked.connect(self.next_wallpaper)
        self.ui.whWallpaperButton.clicked.connect(self.set_wallpaper)
        self.ui.whSaveButton.clicked.connect(self.save_wallpaper)

    def next_wallpaper(self):
        self.enable_wall_buttons(False)
        query = self.ui.whSearchTextEdit.toPlainText()
        is_general = self.ui.whGeneralCheck.isChecked()
        is_anime = self.ui.whAnimeCheck.isChecked()
        is_people = self.ui.whPeopleCheck.isChecked()
        is_sfw = self.ui.whSfwCheck.isChecked()
        is_sketchy = self.ui.whSketchyCheck.isChecked()
        is_nsfw = self.ui.whNsfwCheck.isChecked()
        sort = self.ui.whSortCombo.currentText()
        if self.valid_categories(is_general, is_anime, is_people) and self.valid_purity(
            is_sfw, is_sketchy, is_nsfw
        ):
            self.download_thread = WallhavenDownloadThread(
                self.wh_instance,
                query,
                is_general,
                is_anime,
                is_people,
                is_sfw,
                is_sketchy,
                is_nsfw,
                sort,
            )
            self.download_thread.signal.connect(self.display_wallpaper)
            self.download_thread.start()
        else:
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
                    self.image_path, self.wh_instance.image_extension
                ),
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
            if not utils.Helpers.insert_history(self.wh_instance.wallpaper_url, "wallhaven"):
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not add wall to the history.')

    def display_wallpaper(self, image_path):
        self.image_path = image_path
        self.ui.whPhoto.setPixmap(QtGui.QPixmap(self.image_path))
        self.ui.whPhoto.setScaledContents(True)
        self.enable_wall_buttons(True)

    def toggle_dark_mode(self):
        if self.ui.whDarkModeCheck.isChecked():
            win_darkmode.setDarkMode()
        else:
            win_darkmode.setLightMode()

    def valid_categories(self, is_general, is_anime, is_people):
        if not (is_general or is_anime or is_people):
            messagebox = QMessageBox()
            messagebox.setWindowTitle("Error!")
            messagebox.setText(
                "Choose atleast one option out of general, anime and people"
            )
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.exec_()
            return False
        else:
            return True

    def valid_purity(self, is_sfw, is_sketchy, is_nsfw):
        if not (is_sfw or is_sketchy or is_nsfw):
            messagebox = QMessageBox()
            messagebox.setWindowTitle("Error!")
            messagebox.setText("Choose atleast one option out of sfw, sketchy and nsfw")
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.exec_()
            return False
        else:
            return True

    def enable_wall_buttons(self, state):
        self.ui.whNextWallButton.setEnabled(state)
        self.ui.whSaveButton.setEnabled(state)
        self.ui.whWallpaperButton.setEnabled(state)


class WallhavenDownloadThread(QThread):
    signal = pyqtSignal(str)

    def __init__(
        self,
        wh_instance,
        query,
        is_general,
        is_anime,
        is_people,
        is_sfw,
        is_sketchy,
        is_nsfw,
        sort,
    ):
        QThread.__init__(self)
        self.wh_instance = wh_instance
        self.wh_instance.general = is_general
        self.wh_instance.anime = is_anime
        self.wh_instance.people = is_people
        self.wh_instance.sfw = is_sfw
        self.wh_instance.sketchy = is_sketchy
        self.wh_instance.nsfw = is_nsfw
        self.wh_instance.sort = sort
        if query and not query.isspace():
            self.wh_instance.query = query
        else:
            self.wh_instance.query = None

    def run(self):
        self.wh_instance.wallpapers()
        self.image_path = self.wh_instance.get_download_path()
        utils.Helpers.download_wall(
            self.image_path, self.wh_instance.wallpaper_url
        )
        self.signal.emit(self.image_path)
