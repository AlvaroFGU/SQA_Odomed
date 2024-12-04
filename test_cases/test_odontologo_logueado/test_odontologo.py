from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_odontologo import LoginPageOdo
from page_elements.odontologos.odontologo import Odontologo
from selenium.webdriver import Keys, ActionChains

import time
import string
import random

class TestCita:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')
        time.sleep(0.5)
        self.login_page = LoginPageOdo(self.driver)
        self.login_page.login()
        self.odo_page = Odontologo(self.driver)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba finalizada")
    
    def test_verificar_info_odontologo_logueado(self):
        actual = self.odo_page.verificar_info_odontologo_logueado()
        esperado = self.login_page.default_email
        assert esperado in actual, f"ERROR, esperado: {esperado}, actual: {actual}"
        
    def test_verificar_restriccion_modulo_odontologo(self):
        actual = self.odo_page.verificar_restriccion_modulo_odontologo()
        esperado = "Acceso Denegado"
        assert esperado in actual, f"ERROR, esperado: {esperado}, actual: {actual}"
        
    def test_verificar_restriccion_modulo_recepcionista(self):
        actual = self.odo_page.verificar_restriccion_modulo_recepcionista()
        esperado = "Acceso Denegado"
        assert esperado in actual, f"ERROR, esperado: {esperado}, actual: {actual}"