# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
#from page_elements.page_login.inicio_sesion_page import LoginPage

class TestLogin:
   def setup_method(self):
      self.driver = webdriver.Chrome()
      self.driver.get('http://localhost:3000/')
      time.sleep(1)

   def teardown_method(self):
      self.driver.quit()

   def test_inicio_sesion(self):
      self.driver.find_element(By.XPATH, "//button[text() = 'Ingresar']").click()
      time.sleep(1)
      self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys('PACIENTE123333@GMAIL.COM')
      self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys('qwerty123@')
      self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
      time.sleep(10)
      logo = self.driver.find_element(By.XPATH, "//img[@alt='OdontoMed Logo']").is_displayed()
      assert logo, f'El logo de la pagina de administrador no se encontro'

   def test_cerrar_sesion(self):
      self.driver.find_element(By.XPATH, "//button[text() = 'Ingresar']").click()
      time.sleep(1)
      self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys('PACIENTE123333@GMAIL.COM')
      self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys('qwerty123@')
      self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
      time.sleep(10)
      self.driver.find_element(By.XPATH, "//*[@aria-label = ' avatar']").click()
      time.sleep(1)
      self.driver.find_element(By.XPATH, "//div[@aria-orientation]//child::button[text() = 'Cerrar sesión']").click()
      time.sleep(1)
      boton_ingresar = self.driver.find_element(By.XPATH, "//button[text() = 'Ingresar']").is_displayed()
      assert boton_ingresar, f'El boton ingresar de la pagina de inicio no se encontro'

   #def test_inicio_sesion(self):
   #   inicio_sesion = LoginPage(self.driver)
   #   inicio_sesion.inicio_sesion_admin()      
   #   time.sleep(10)
   #   logo = self.driver.find_element(By.XPATH, "//img[@alt='OdontoMed Logo']")
   #   assert logo, f'El logo de la pagina de administrador no se encontro'

      

