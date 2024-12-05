from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page_elements.login.login_admin import LoginPageAdmin
import time

def actual_espera(actual, esperado):
    assert actual == esperado, f'Error: actual: {actual}, esperado {esperado}' 

class TestLogin:
   def setup_method(self):
      self.driver = webdriver.Chrome()
      self.driver.get('http://localhost:3000/')
      time.sleep(0.5)
      self.login_page = LoginPageAdmin(self.driver)
      self.actual = True
      
   def teardown_method(self):
      self.driver.quit()

   def test_inicio_sesion(self):
      self.login_page.login(True)
      logo = self.login_page.logo_visible()
      actual_espera(self.actual, logo)

   def test_inicio_sesion_mal(self):
      self.login_page.llenar_form(False)
      self.login_page.enviar()
      time.sleep(5)
      logo = self.login_page.logo_visible()
      actual_espera(not self.actual, logo)

   def test_cerrar_sesion(self):
      self.login_page.login(True)
      self.login_page.cerrar_sesion()
      boton_ingresar = self.login_page.titulo()
      actual_espera(self.actual, boton_ingresar)

   def test_recuperar_contrasenia(self):
      self.login_page.ingresar()
      self.login_page.olvidar_contraseña(True)
      titulo_cod = self.login_page.ver_cod()
      actual_espera(self.actual, titulo_cod)

   def test_recuperar_contrasenia_mal(self):
      self.login_page.ingresar()
      self.login_page.olvidar_contraseña(False)
      titulo_cod = self.login_page.ver_cod()
      actual_espera(not self.actual, titulo_cod)
   
   def test_ver_contra(self):
      self.login_page.ingresar()
      contra = self.login_page.ver_contra()
      actual_espera(self.actual, contra)
