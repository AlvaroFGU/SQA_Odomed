from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

import time

class LoginPageOdo:
    def __init__(self, driver):
        self.driver = driver
        self.default_email = "GAA2025817@EST.UNIVALLE.EDU"
        self.default_password = "Qwerty123@"

    def enter_to_login(self):
        self.driver.find_element(By.XPATH, "//button[text() ='Ingresar']").click()
        time.sleep(1)

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