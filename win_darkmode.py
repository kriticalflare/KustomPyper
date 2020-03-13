import winreg

# Path to the required registry 
REG_PATH = 'Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize'

def get_reg(name):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ) as registry_key:
            value, regtype = winreg.QueryValueEx(registry_key, name)
            return value
    except WindowsError:
        return None

def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE) as registry_key:
        # use winreg.REG_DWORD as it covers both the cases for us
            winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value) 
            return True
    except WindowsError:
        return False

def setDarkMode():
    set_reg('AppsUseLightTheme', 0)
    set_reg('SystemUsesLightTheme', 0)

def setLightMode():
    set_reg('AppsUseLightTheme', 1)
    set_reg('SystemUsesLightTheme', 1)

    
def toggleDarkMode():
    isDarkMode = get_reg('AppsUseLightTheme') or get_reg('SystemUsesLightTheme')
    print(isDarkMode)
    print(type(isDarkMode))
    if isDarkMode == 0:
        set_reg('AppsUseLightTheme', 1)
        set_reg('SystemUsesLightTheme', 1)
    else: 
        set_reg('AppsUseLightTheme', 0)
        set_reg('SystemUsesLightTheme', 0)


if __name__ == "__main__":
    toggleDarkMode()
    