from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_admin import LoginPageAdmin
from page_elements.pacientes.paciente import ModuloPaciente
import time

class TestModulo:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:3000/')
        time.sleep(1)
        self.login_page = LoginPageAdmin(self.driver)
        self.paciente = ModuloPaciente(self.driver)
        self.login_page.login(True)

    def teardown_method(self):
        self.driver.quit()

    def taest_contenido_inicio(self):
        actual = self.paciente.encabezado()
        esperada = "PACIENTES"
        assert esperada == actual, f"ERROR, actual {actual}, esperado: {esperada}"
    
    def test_crear_paciente(self):
        self.paciente.boton_crear()
        self.paciente.llenar_form_crear(True)
        self.paciente.enviar_form()
        creado = self.paciente.verificar_pacientecreado()
        assert creado, f'El paciente no se creo correctamente'
    
    def test_ver_historial(self):
        self.paciente.boton_historial()
        esperado = self.paciente.text_datos_personales()
        assert esperado, f'El boton de datos personales no se ve'
    
    def test_historial_navbar_historial(self):
        self.paciente.boton_historial()
        self.paciente.nav_bar_historial()

    def test_historial_navbar_tratamientos(self):
        self.paciente.boton_historial()
        self.paciente.nav_bar_tratamientos()

    def test_historial_navbar_prescripciones(self):
        self.paciente.boton_historial()
        self.paciente.nav_bar_prescripciones()

    def test_editar_datos_personales(self):
        self.paciente.boton_historial()
        mensaje = self.paciente.editar_datos_personales()
        assert mensaje, f'El mensaje de exito no se muestra'