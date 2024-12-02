from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_admin import LoginPageAdmin
from page_elements.citas.cita import ModuloCitas
import time

class TestModulo:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:3000/')
        time.sleep(1)
        self.login_page = LoginPageAdmin(self.driver)
        self.cita = ModuloCitas(self.driver)
        self.login_page.login(True)

    def teardown_method(self):
        self.driver.quit()

    def test_ver_citas(self):
        citas = self.cita.ver_citas()
        assert citas, f'El listado de citas no se muestra'

    def test_filtro_odontologo(self):
        filtro = self.cita.fitro_odontologo()
        assert filtro, f'El filtro no funciono correctamente'

    def test_filtro_fecha(self):
        filtro = self.cita.filtro_fecha()
        assert filtro, f'El filtro no funciono correctamente'

    def test_editar_cita(self):
        mensaje = self.cita.editar_cita()
        assert mensaje, f'El mensaje de exito no se muestra'

    def test_filtro_estado(self):
        filtro = self.cita.filtro_estado()
        assert filtro, f'El filtro no funciono correctamente'
    
    def test_eliminar_cita(self):
        mensaje = self.cita.eliminar_cita()
        assert mensaje, f'El mensaje de exito no se muestra'


