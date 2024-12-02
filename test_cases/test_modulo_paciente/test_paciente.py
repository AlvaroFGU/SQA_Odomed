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

    def test_contenido_inicio(self):
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
        esperado = self.paciente.nav_bar_historial()
        assert esperado, f'El encabezado de historial no se ve'

    def test_historial_navbar_tratamientos(self):
        self.paciente.boton_historial()
        esperado = self.paciente.nav_bar_tratamientos()
        assert esperado, f'El encabezado de tratamientos no se ve'

    def test_historial_navbar_prescripciones(self):
        self.paciente.boton_historial()
        esperado = self.paciente.nav_bar_prescripciones()
        assert esperado, f'El encabezado de prescripciones no se ve'

    def test_editar_datos_personales(self):
        self.paciente.boton_historial()
        mensaje = self.paciente.editar_datos_personales()
        assert mensaje, f'El mensaje de exito no se muestra'

    def test_editar_datos_clinicos(self):
        self.paciente.boton_historial()
        mensaje = self.paciente.editar_datos_clinicos()
        assert mensaje, f'El mensaje de exito no se muestra'

    def test_descargar_historial(self):
        mensaje = self.paciente.descargar_historial()
        assert mensaje, f'El mensaje de exito no se muestra'
        
    def test_editar_datos_historial(self):
        mensaje = self.paciente.editar_datos_historial()
        assert mensaje, f'El mesanje de exito no se muestra'

    def test_crear_daignostico(self):
        mensaje = self.paciente.crear_diagnostico()
        assert mensaje, f'El mensaje de exito no se muestra'
    
    def test_editar_daignostico(self):
        mensaje = self.paciente.editar_diagnostico()
        assert mensaje, f'El mensaje de exito no se muestra'
        
    def test_eliminar_diagnostico(self):
        mensaje = self.paciente.eliminar_diagnostico()
        assert mensaje, f'El mensaje de exito no se muestra'

    def test_crear_tratamiento(self):
        mensaje = self.paciente.crear_tratamiento()
        assert mensaje, f'El mensaje de exito no se muestra'

    def test_editar_tratamiento(self):
        mensaje = self.paciente.editar_tratamiento()
        assert mensaje, f'El mensaje de exito no se muestra'

    def test_eliminar_tratamiento(self):
        mensaje = self.paciente.eliminar_tratamiento()
        assert mensaje, f'El mensaje de exito no se muestra'

    def test_crear_prescripcion(self):
        mensaje = self.paciente.crear_prescripcion()
        assert mensaje, f'El mensaje de exito no se muestra'

    def test_editar_prescripcion(self):
        mensaje = self.paciente.editar_prescripcion()
        assert mensaje, f'El mensaje de exito no se muestra'

    def test_eliminar_prescripcion(self):
        mensaje = self.paciente.eliminar_prescripcion()
        assert mensaje, f'El mensaje de exito no se muestra'