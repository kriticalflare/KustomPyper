import ctypes
import os
import winpath
import shutil


def temp_download_dir():
    path = winpath.get_local_appdata() + "\\Programs\\KustomPyper"
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def history_db_dir(db_name):
    path = temp_download_dir() + f"\\{db_name}.db"
    # print(path)
    return path


def saveWall(image_path, imagetitle):
    path = winpath.get_my_pictures() + "\\KustomPyper"
    if not os.path.exists(path):
        os.mkdir(path)
    shutil.copyfile(image_path, path + f"\\{imagetitle}")


def changeBG(image):
    # print(directory)
    image_path = image
    # print(image_path)

    # Constant for setting the desktop wallpaper
    SPI_SETDESKWALLPAPER = 20
    # Constant for making the wallpaper persist across reboots
    SPIF_UPDATEINIFILE = 1
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE
    )
    return


if __name__ == "__main__":
    print("Not a standalone program")
