from cx_Freeze import setup, Executable

setup(
    name="KustomPyper",
    version="1.0",
    description="Find and set random wallpapers from reddit as your desktop wallpaper",
    executables=[
        Executable("app.py", shortcutName="KustomPyper", shortcutDir="DesktopFolder")
    ],
)
