import ctypes
import os
import winpath

def temp_download_dir():
    return winpath.get_local_appdata() + "\\Programs\\KustomPyper"


def changeBG(image):
    # print(directory)
    image_path =  image
    # print(image_path)  
   
    # Constant for setting the desktop wallpaper
    SPI_SETDESKWALLPAPER = 20
    # Constant for making the wallpaper persist across reboots
    SPIF_UPDATEINIFILE = 1
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path , SPIF_UPDATEINIFILE)
    return

if __name__ == "__main__":
    print('Not a standalone program')

