from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

import time

class LoginPageRecep:
    def __init__(self, driver):
        self.driver = driver
        self.default_email = "RECEP@GMAIL.COM"
        self.default_password = "qwerty123@"

    def enter_to_login(self):
        self.driver.find_element(By.XPATH, "//button[text() ='Ingresar']").click()
        time.sleep(2)

    def enter_email(self):
        email_field = self.driver.find_element(By.XPATH, "//input[@type = 'email']")
        email_field.clear()
        email_field.send_keys(self.default_email)

    def enter_password(self):
        password_field = self.driver.find_element(By.XPATH, "//input[@type = 'password']")
        password_field.clear()
        password_field.send_keys(self.default_password)

    def submit(self):
        login_button = self.driver.find_element(By.XPATH, "//button[@type = 'submit']")
        login_button.click()

    def login(self):
        self.enter_to_login()
        self.enter_email()
        self.enter_password()
        self.submit()