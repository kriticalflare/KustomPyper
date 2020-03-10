import ctypes
import os

directory = os.getcwd()

def changeBG(image):
    # print(directory)
    image_path = directory + "\\" + image
    # print(image_path)  
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path , 0)
    return

if __name__ == "__main__":
    print('Not a standalone program')

