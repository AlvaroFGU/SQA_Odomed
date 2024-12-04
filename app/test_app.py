import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="function")
def appium_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "11.0"
    options.device_name = "4x45h6u4zt5dinnz"
    options.app = "C:\\Users\\braya\\Downloads\\base.apk"

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()


def login(driver, email: str, password: str):
    time.sleep(2)
    email_field = driver.find_element(By.ID, "com.example.odomedapp:id/emailEditText")
    email_field.send_keys(email)

    password_field = driver.find_element(By.ID, "com.example.odomedapp:id/passwordEditText")
    password_field.send_keys(password)

    login_button = driver.find_element(By.ID, "com.example.odomedapp:id/loginButton")
    login_button.click()
    time.sleep(5)


def test_login(appium_driver):
    login(appium_driver, "PACIENTE@GMAIL.COM", "qwerty123@")
    landing_element = appium_driver.find_element(By.XPATH, "//android.widget.TextView[@text='Inicio']")
    assert landing_element.is_displayed(), "El usuario no pudo iniciar sesión correctamente."


def test_create_appointment(appium_driver):
    login(appium_driver, "PACIENTE@GMAIL.COM", "qwerty123@")
    menu_button = appium_driver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Abrir panel lateral de navegación']")
    menu_button.click()
    time.sleep(5)
    appointments_tab = appium_driver.find_element(By.XPATH, "//androidx.appcompat.widget.LinearLayoutCompat[@resource-id='com.example.odomedapp:id/nav_gallery']")
    appointments_tab.click()
    time.sleep(5)
    create_appointment_button = appium_driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='com.example.odomedapp:id/btnCrearCita']")
    create_appointment_button.click()
    time.sleep(4)
    assert create_appointment_button.is_displayed(), "No se pudo crear la cita correctamente."
