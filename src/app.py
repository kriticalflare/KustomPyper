import sys
import sqlite3

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

from gui import Ui_MainWindow
import reddit_window
import unsplash_window
import bing_window
import wallhaven_window
import history_window


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show_reddit_page()
        """ Moving the next two lines to the reddit window init results in the following warning 
        QWindowsWindow::setGeometry: Unable to set geometry 1920x1080+0+29 (frame: 1938x1127-9-9) on QWidgetWindow/"MainWindowWindow" 
        on " \\\.\DISPLAY1". Resulting geometry: 1920x1001+0+29 """
        self.screenSize = QDesktopWidget().screenGeometry(0)
        self.setMinimumSize(self.screenSize.width(), self.screenSize.height())
        self.pageRedditAction.triggered.connect(self.show_reddit_page)
        self.pageUnsplashAction.triggered.connect(self.show_unsplash_page)
        self.pageBingAction.triggered.connect(self.show_bing_page)
        self.pageWallHavenAction.triggered.connect(self.show_wallhaven_page)
        self.aboutAction.triggered.connect(self.show_about_page)
        self.helpAction.triggered.connect(self.open_help_url)
        self.historyAction.triggered.connect(self.show_history_page)
        self.init_history_db()
        self.showMaximized()

    def show_reddit_page(self):
        self.pageStackWidget.setCurrentIndex(0)

    def show_unsplash_page(self):
        self.pageStackWidget.setCurrentIndex(1)

    def show_bing_page(self):
        self.pageStackWidget.setCurrentIndex(2)

    def show_wallhaven_page(self):
        self.pageStackWidget.setCurrentIndex(3)

    def show_about_page(self):
        self.pageStackWidget.setCurrentIndex(4)

    def show_history_page(self):
        self.pageStackWidget.setCurrentIndex(5)

    def open_help_url(self):
        url = QUrl("https://github.com/kriticalflare/KustomPyper/blob/master/README.md")
        if not QtGui.QDesktopServices.openUrl(url):
            QMessageBox.warning(
                self,
                "Open Url",
                "Could not open https://github.com/kriticalflare/KustomPyper/",
            )

    def init_history_db(self):
        conn = sqlite3.connect("wall_history.db")
        c = conn.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS history(wallpaper TEXT PRIMARY KEY,source TEXT)"
        )
        c.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv)
        arg = sys.argv[1]
        if arg == "--no-gui":
            print("yas")
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    RedditWindow = reddit_window.RedditWindow(MainWindow)
    UnsplashWindow = unsplash_window.UnsplashWindow(MainWindow)
    BingWindow = bing_window.BingWindow(MainWindow)
    WallhaveWindow = wallhaven_window.WallhavenWindow(MainWindow)
    HistoryWindow = history_window.HistoryWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
