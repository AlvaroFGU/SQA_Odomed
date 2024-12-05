from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_admin import LoginPageAdmin
from page_elements.pacientes.paciente import ModuloPaciente
import time

def actual_espera(actual, esperado):
    assert actual == esperado or actual in esperado, f'Error: actual: {actual}, esperado {esperado}' 


class TestModulo:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:3000/')
        time.sleep(1)
        self.login_page = LoginPageAdmin(self.driver)
        self.paciente = ModuloPaciente(self.driver)
        self.login_page.login(True)
        self.actual = 'exitosamente'
        self.actualb = True

    def teardown_method(self):
        self.driver.quit()

    def test_contenido_inicio(self):
        actual = self.paciente.encabezado()
        esperada = "PACIENTES"
        assert esperada == actual, f"ERROR, actual {actual}, esperado: {esperada}"
    
    def test_crear_paciente(self):
        self.paciente.boton_crear()
        self.paciente.llenar_form_crear(True)
        self.paciente.enviar_form()
        creado = self.paciente.verificar_pacientecreado()
        actual_espera(self.actualb, creado)
    
    def test_ver_historial(self):
        self.paciente.boton_historial()
        esperado = self.paciente.text_datos_personales()
        actual_espera(self.actualb, esperado)
    
    def test_historial_navbar_historial(self):
        self.paciente.boton_historial()
        esperado = self.paciente.nav_bar_historial()
        actual_espera(self.actualb, esperado)

    def test_historial_navbar_tratamientos(self):
        self.paciente.boton_historial()
        esperado = self.paciente.nav_bar_tratamientos()
        actual_espera(self.actualb, esperado)

    def test_historial_navbar_prescripciones(self):
        self.paciente.boton_historial()
        esperado = self.paciente.nav_bar_prescripciones()
        actual_espera(self.actualb, esperado)

    def test_editar_datos_personales(self):
        self.paciente.boton_historial()
        mensaje = self.paciente.editar_datos_personales()
        actual_espera(self.actualb, mensaje)

    def test_editar_datos_clinicos(self):
        self.paciente.boton_historial()
        mensaje = self.paciente.editar_datos_clinicos()
        actual_espera(self.actualb, mensaje)

    def test_descargar_historial(self):
        mensaje = self.paciente.descargar_historial()
        actual_espera(self.actualb, mensaje)
        
    def test_editar_datos_historial(self):
        mensaje = self.paciente.editar_datos_historial()
        actual_espera(self.actual, mensaje)

    def test_crear_diagnostico(self):
        mensaje = self.paciente.crear_diagnostico()
        actual_espera(self.actual, mensaje)
    
    def test_editar_diagnostico(self):
        mensaje = self.paciente.editar_diagnostico()
        actual_espera(self.actual, mensaje)
        
    def test_eliminar_diagnostico(self):
        mensaje = self.paciente.eliminar_diagnostico()
        actual_espera(self.actual, mensaje)

    def test_crear_tratamiento(self):
        mensaje = self.paciente.crear_tratamiento()
        actual_espera(self.actual, mensaje)

    def test_editar_tratamiento(self):
        mensaje = self.paciente.editar_tratamiento()
        actual_espera(self.actual, mensaje)

    def test_eliminar_tratamiento(self):
        mensaje = self.paciente.eliminar_tratamiento()
        actual_espera(self.actual, mensaje)

    def test_crear_prescripcion(self):
        mensaje = self.paciente.crear_prescripcion()
        actual_espera(self.actual, mensaje)

    def test_editar_prescripcion(self):
        mensaje = self.paciente.editar_prescripcion()
        actual_espera(self.actual, mensaje)

    def test_eliminar_prescripcion(self):
        mensaje = self.paciente.eliminar_prescripcion()
        actual_espera(self.actual, mensaje)

    def test_paginacion(self):
        pagina = self.paciente.paginacion()
        actual_espera(self.actualb, pagina)

    def test_eliminar_paciente(self):
        mensaje = self.paciente.eliminar_paciente()
        actual_espera(self.actual, mensaje)

    
