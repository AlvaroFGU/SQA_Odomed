from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_recepcionista import LoginPageRecep
from selenium.webdriver import Keys, ActionChains

import time
import string
import random

class TestModulo:
    def genera_username(self):
        alfabeto = list(string.ascii_lowercase)
        numeros = list(range(1000, 10000))
        user = ''.join([random.choice(alfabeto) for i in range(3)])  
        number = str(random.choice(numeros)) 
        username = user + number + "@google.com"  
        return username
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')
        time.sleep(0.5)
        self.login_page = LoginPageRecep(self.driver)
        self.login_page.login()
        time.sleep(10)
        self.usuario_generado = self.genera_username()


    def teardown_method(self):
        self.driver.quit()
        print("Prueba finalizada")


    def test_crear_paciente(self):
        self.driver.find_element(By.XPATH, "//h2//following-sibling::button").click()
        time.sleep(0.5)
        nomPacient= "Raul Alejandro"
        self.driver.find_element(By.XPATH, "//input[@placeholder='Nombres']").send_keys(f"{nomPacient}")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Apellidos']").send_keys("Hernandez")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='C.I.']").send_keys("471258369")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(f"{self.usuario_generado}")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Teléfono']").send_keys("71234568")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("03-mar-2003")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Dirección']").send_keys("Calle testeo, 4332")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']").send_keys("Qwerty123@")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Codigo')]").send_keys("Rp123456")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Alergias']").clear()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Alergias']").send_keys("Productos altos en ph")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Antecedentes Médicos']").clear()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Antecedentes Médicos']").send_keys("SI")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//select").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//option[@value ='1']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Notas Generales']").clear()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Notas Generales']").send_keys("SI")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//footer//button[1]").click()
        time.sleep(8)








