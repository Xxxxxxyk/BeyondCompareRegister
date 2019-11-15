import win32api
import win32con

key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,'Software\\Scooter Software\\Beyond Compare 4',0, win32con.KEY_ALL_ACCESS)
# value = win32api.RegQueryValue(key,'')
# value = win32api.RegQueryValueEx(key,'CacheID')
win32api.RegDeleteValue(key,'CacheID')
# print(value)
win32api.RegCloseKey(key)