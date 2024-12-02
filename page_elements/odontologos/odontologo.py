from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_odontologo import LoginPageOdo
from selenium.webdriver import Keys, ActionChains
import pytest
import time
import string
import random

def genera_username():
    alfabeto = list(string.ascii_lowercase)
    numeros = list(range(1000, 10000))
    user = ''.join([random.choice(alfabeto) for i in range(3)])  
    number = str(random.choice(numeros)) 
    username = user + number + "@google.com"  
    return username
    
def genera_ci():
    numeros = list(range(1000000, 99999999))
    ci = str(random.choice(numeros)) 
    return ci

class Odontologo:
    def __init__(self, driver):
        self.driver = driver
        self.email_user_test = genera_username()
        self.ci_user_test = genera_ci()

    def ingresar_form_crear_paciente(self):
        self.driver.find_element(By.XPATH, "//h2//following-sibling::button").click()
        time.sleep(0.5)

    def llenar_form_crear_paciente(self):
        nomPacient= "Raul Alejandro"
        self.driver.find_element(By.XPATH, "//input[@placeholder='Nombres']").send_keys(f"{nomPacient}")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Apellidos']").send_keys("Hernandez")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='C.I.']").send_keys(f"{self.ci_user_test}")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(f"{self.email_user_test}")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Teléfono']").send_keys("71234568")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("03-03-2003")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Dirección']").send_keys("Calle testeo. 4332")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)
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
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Antecedentes Médicos']").send_keys("SI")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//select").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//option[@value ='1']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Notas Generales']").clear()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Notas Generales']").send_keys("SI")

    def enviar_formulario_paciente(self):
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//footer//button[1]").click()
        time.sleep(6)

    def buscar_paciente_creado(self):
        self.driver.find_element(By.XPATH, "//input[@value]").send_keys(f"{self.ci_user_test}")
        time.sleep(1)
        actual = self.driver.find_element(By.XPATH, "//td[2]").text
        return actual