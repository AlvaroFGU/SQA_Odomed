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
        self.ingresar_form_crear_paciente()
        nomPacient= "Raul Alejandro"
        self.driver.find_element(By.XPATH, "//input[@placeholder='Nombres']").send_keys(f"{nomPacient}")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Apellidos']").send_keys("Hernandez")
        self.driver.find_element(By.XPATH, "//input[@placeholder='C.I.']").send_keys(f"{self.ci_user_test}")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(f"{self.email_user_test}")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Teléfono']").send_keys("71234568")
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("03")
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("03")
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys(Keys.ARROW_RIGHT)
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("2003")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Dirección']").send_keys("Calle testeo. 4332")
        self.driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)
        self.driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']").send_keys("Qwerty123@")
        self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Codigo')]").send_keys("Rp123456")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Alergias']").send_keys("Productos altos en ph")
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Antecedentes Médicos']").send_keys("SI")
        self.driver.find_element(By.XPATH, "//select").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//option[@value ='1']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Notas Generales']").send_keys("SI")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//footer//button[1]").click()
        time.sleep(10)

    def buscar_paciente_creado_byCi(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@value]").send_keys(f"{self.ci_user_test}")
        time.sleep(1)
        
    
    def verif_pcnt_creado(self):
        actual = self.driver.find_element(By.XPATH, "//td[2]").text
        return actual
    
    def ingresar_a_infPcnt(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'css-jn2gtv')]").click()
        time.sleep(7)
        
    def verif_pcnt_datosPersonales(self):
        actual = self.driver.find_element(By.XPATH, "//strong[text()='CI:']//parent::p").text
        return actual
    
    