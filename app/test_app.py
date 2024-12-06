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
    time.sleep(10)
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


def test_create_cita(appium_driver):
    login(appium_driver, "PACIENTE@GMAIL.COM", "qwerty123@")
    menu_button = appium_driver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Abrir panel lateral de navegación']")
    menu_button.click()
    time.sleep(5)
    appointments_tab = appium_driver.find_element(By.XPATH, "//androidx.appcompat.widget.LinearLayoutCompat[@resource-id='com.example.odomedapp:id/nav_gallery']")
    appointments_tab.click()
    time.sleep(5)
    apponts_galery= appium_driver.find_element(By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.example.odomedapp:id/recyclerViewUsers']")
    linear_layouts = apponts_galery.find_elements(By.CLASS_NAME, "android.widget.LinearLayout")
    initial_count = len(linear_layouts)
    create_appoint_button = appium_driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='com.example.odomedapp:id/btnCrearCita']")
    create_appoint_button.click()
    time.sleep(4)
    appoint_button= appium_driver.find_element(By.XPATH,"//android.widget.TextView[@resource-id='com.example.odomedapp:id/fechaTextView']")
    appoint_button.click()
    time.sleep(3)
    aceptal_fecha= appium_driver.find_element(By.XPATH,"//android.widget.Button[@resource-id='android:id/button1']")
    aceptal_fecha.click()
    time.sleep(20)
    hora_spinner = appium_driver.find_element(By.XPATH,"//android.widget.Spinner[@resource-id='com.example.odomedapp:id/horarioSpinner']")
    hora_spinner.click()
    time.sleep(3)
    selected_hora =appium_driver.find_element(By.XPATH,"(//android.widget.TextView[@resource-id='com.example.odomedapp:id/text_horario'])[1]")
    selected_hora.click()
    time.sleep(3)
    guardar_button= appium_driver.find_element(By.XPATH,"//android.widget.Button[@resource-id='com.example.odomedapp:id/guardarButton']")
    guardar_button.click()
    time.sleep(5)
    linear_layouts_after = apponts_galery.find_elements(By.CLASS_NAME, "android.widget.LinearLayout")
    final_count = len(linear_layouts_after)
    assert final_count+1 == initial_count + 1, "NO se cREO LA CITA ESTUUUUUPIDO."
def test_delete_cita(appium_driver):
    login(appium_driver, "PACIENTE@GMAIL.COM", "qwerty123@")
    menu_button = appium_driver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Abrir panel lateral de navegación']")
    menu_button.click()
    time.sleep(5)
    appointments_tab = appium_driver.find_element(By.XPATH, "//androidx.appcompat.widget.LinearLayoutCompat[@resource-id='com.example.odomedapp:id/nav_gallery']")
    appointments_tab.click()
    time.sleep(5)
    apponts_galery = appium_driver.find_element(By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.example.odomedapp:id/recyclerViewUsers']")
    linear_layouts = apponts_galery.find_elements(By.CLASS_NAME, "android.widget.LinearLayout")
    initial_count = len(linear_layouts)
    boton_cancel_cita = appium_driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='com.example.odomedapp:id/btnCancelar']")
    boton_cancel_cita.click()
    time.sleep(2)
    boton_conf_ca = appium_driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='com.example.odomedapp:id/btnConfirmar']")
    boton_conf_ca.click()
    time.sleep(10)
    linear_layouts_after = apponts_galery.find_elements(By.CLASS_NAME, "android.widget.LinearLayout")
    final_count = len(linear_layouts_after)
    assert final_count == initial_count - 1, "No se eliminó la cita correctamente."
def test_ver_historial(appium_driver):
    login(appium_driver, "PACIENTE@GMAIL.COM", "qwerty123@")
    menu_button = appium_driver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Abrir panel lateral de navegación']")
    menu_button.click()
    time.sleep(5)
    appointments_tab = appium_driver.find_element(By.XPATH, "//android.widget.CheckedTextView[@resource-id='com.example.odomedapp:id/design_menu_item_text' and @text='Historial de Citas']")
    appointments_tab.click()
    time.sleep(5)
    histo_tab=appium_driver.find_element(By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.example.odomedapp:id/recyclerViewUsers']")
    assert histo_tab.is_displayed()
def test_logout(appium_driver):
    login(appium_driver, "PACIENTE@GMAIL.COM", "qwerty123@")
    menu_button = appium_driver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Abrir panel lateral de navegación']")
    menu_button.click()
    time.sleep(5)
    logOUT_B=appium_driver.find_element(By.XPATH,"//android.widget.CheckedTextView[@resource-id='com.example.odomedapp:id/design_menu_item_text' and @text='Cerrar Sesión']")
    logOUT_B.click()
    assert logOUT_B.is_displayed()