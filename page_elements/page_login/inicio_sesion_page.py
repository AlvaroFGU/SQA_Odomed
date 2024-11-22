# Aquí se incluirán los pasos específicos o comunes para poder interactuar con los elementos de la página
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class LoginPage:
   def __init__(self, driver):
      self.driver = driver 
   def inicio_sesion_admin(self):
      self.driver.find_element(By.XPATH, "//button[text() = 'Ingresar']").click()
      time.sleep(1)
      self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys('PACIENTE123333@GMAIL.COM')
      self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys('qwerty123@')
      self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
      time.sleep(10)

