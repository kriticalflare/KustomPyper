from cx_Freeze import setup, Executable 

setup(name = "KustomPyper" , 
	version = "0.1" , 
	description = "Find and set random wallpapers from reddit as your desktop wallpaper" , 
	executables = [Executable("gui.py", shortcutName='Pywall', shortcutDir= "DesktopFolder")]) 