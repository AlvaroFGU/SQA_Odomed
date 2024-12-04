from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_odontologo import LoginPageOdo
from page_elements.odontologos.odontologo import Odontologo
from selenium.webdriver import Keys, ActionChains

import time
import string
import random

class TestPaciente:
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

    # def test_crear_paciente(self):
    #     actual = self.odo_page.crear_nuevo_paciente()
    #     esperado = self.odo_page.ci_user_test
    #     assert actual in esperado, f"ERROR, esperado: {esperado}, actual: {actual}"

    # def test_editar_datos_personales(self):
    #     actual = self.odo_page.editar_paciente()
    #     esperado = self.odo_page.ci_user_test
    #     assert esperado in actual, f"ERROR: actual:{actual}, esperado:{esperado}"
        
    # def test_verificar_info_paciente_seleccionado(self):
    #     actual = self.odo_page.verificar_paciente_seleccionado()
    #     esperado = self.odo_page.ci_esperado
    #     assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"
    
    # def test_editar_datos_clinicos(self):
    #     actual = self.odo_page.editar_datos_clinicos()
    #     esperado = "Paciente actualizado"
    #     assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"
    
    # def test_editar_datos_historial(self):
    #     actual = self.odo_page.editar_datos_historial()
    #     esperado = "Historial actualizado"
    #     assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"
        
    # def test_crear_nuevo_diagnostico(self):
    #     actual = self.odo_page.crear_nuevo_diagnostico()
    #     esperado = "Diagnóstico creado"
    #     assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"

    # def test_editar_diagnostico(self):
    #     actual = self.odo_page.editar_diagnostico()
    #     esperado = "Diagnóstico actualizado"
    #     assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"

    # def test_eliminar_diagnostico(self):
    #     actual = self.odo_page.eliminar_diagnostico()
    #     esperado = "Diagnostico eliminado"
    #     assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"
    
    # def test_crear_tratamiento(self):
    #     actual = self.odo_page.crear_tratamiento()
    #     esperado = "Tratamiento creado"
    #     assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"
        
    # def test_editar_tratamiento(self):
    #     actual = self.odo_page.editar_tratamiento()
    #     esperado = "Tratamiento actualizado"
    #     assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"
        
    # def test_eliminar_tratamiento(self):
    #     actual = self.odo_page.eliminar_tratamiento()
    #     esperado = "Tratamiento eliminado"
    #     assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"
        
    # def test_crear_prescripcion(self):
    #     actual = self.odo_page.crear_prescripcion()
    #     esperado = "Prescripcion creado"
    #     assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"
        
    def test_editar_prescripcion(self):
        actual = self.odo_page.editar_prescripcion()
        esperado = "Prescripción actualizada"
        assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"
    
    def test_eliminar_prescripcion(self):
        actual = self.odo_page.eliminar_prescripcion()
        esperado = "Medicamento eliminado"
        assert esperado in actual, f"ERROR: actual: {actual}, esperado: {esperado}"