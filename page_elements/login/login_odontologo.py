from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

import time

class LoginPageOdo:
    def __init__(self, driver):
        self.driver = driver
        self.default_email = "GAA2025817@EST.UNIVALLE.EDU"
        self.default_password = "Qwerty123@"
        
    def esperar_elemento(self, by, locator, timeout=15, visible=True):
            wait = WebDriverWait(self.driver, timeout)
            try:
                return wait.until(EC.visibility_of_element_located((by, locator)))
            except TimeoutException:
                return None
            
    def enter_to_login(self):
        self.driver.find_element(By.XPATH, "//button[text() ='Ingresar']").click()
        self.esperar_elemento(By.XPATH, "//input[@type = 'email']")

    def ingresar_credenciales(self):
        email_field = self.driver.find_element(By.XPATH, "//input[@type = 'email']")
        email_field.clear()
        email_field.send_keys(self.default_email)
        password_field = self.driver.find_element(By.XPATH, "//input[@type = 'password']")
        password_field.clear()
        password_field.send_keys(self.default_password)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()

    def login(self):
        self.enter_to_login()
        self.ingresar_credenciales()
        self.esperar_elemento(By.XPATH, "//th[text()='NOMBRE COMPLETO']")
