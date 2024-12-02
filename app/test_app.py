

from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "11.0"
options.device_name = "Xiaomi Redmi Note 8 Pro"
options.app="C:\\Users\\braya\\Downloads\\base.apk"

driver = webdriver.Remote("http://localhost:4723", options=options)

try:
    print("Conexión exitosa con Appium.")
finally:
    driver.quit()
