from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_odontologo import LoginPageOdo
from page_elements.odontologos.odontologo import Odontologo
from selenium.webdriver import Keys, ActionChains

import time
import string
import random

class TestPaciente:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')
        time.sleep(0.5)
        self.login_page = LoginPageOdo(self.driver)
        self.login_page.login()
        self.odo_page = Odontologo(self.driver)
        time.sleep(8)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba finalizada")

    def test_crear_paciente(self):
        self.odo_page.ingresar_form_crear_paciente()
        self.odo_page.llenar_form_crear_paciente()
        self.odo_page.enviar_formulario_paciente()
        actual = self.odo_page.buscar_paciente_creado()
        esperado = self.odo_page.ci_user_test
        assert actual in esperado, f"ERROR, esperado: {esperado}, actual: {actual}"





