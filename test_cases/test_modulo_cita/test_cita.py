from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_admin import LoginPageAdmin
from page_elements.citas.cita import ModuloCitas
import time

def actual_espera(actual, esperado):
    assert actual == esperado or actual in esperado, f'Error: actual: {actual}, esperado {esperado}' 


class TestModulo:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:3000/')
        time.sleep(1)
        self.login_page = LoginPageAdmin(self.driver)
        self.cita = ModuloCitas(self.driver)
        self.login_page.login(True)
        self.actualb = True
        self.actual = 'exitosamente'

    def teardown_method(self):
        self.driver.quit()

    def test_ver_citas(self):
        citas = self.cita.ver_citas()
        actual_espera(self.actualb, citas)

    def test_filtro_odontologo(self):
        filtro = self.cita.fitro_odontologo()
        actual_espera(self.actualb, filtro)

    def test_filtro_fecha(self):
        filtro = self.cita.filtro_fecha()
        actual_espera(self.actualb, filtro)

    def test_editar_cita(self):
        mensaje = self.cita.editar_cita()
        actual_espera(self.actual, mensaje)

    def test_filtro_estado(self):
        filtro = self.cita.filtro_estado()
        actual_espera(self.actualb, filtro)
    
    def test_eliminar_cita(self):
        mensaje = self.cita.eliminar_cita()
        actual_espera(self.actual, mensaje)


