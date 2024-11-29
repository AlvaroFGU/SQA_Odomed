from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

import time

class ModuloPaciente:
    def __init__(self, driver):
        self.driver = driver
        self.email_def = 'test1@gmail.com'
        self.ci_def = '1234567' 

    def encabezado(self):
        actual = self.driver.find_element(By.XPATH, "//h2").text
        return actual
    
    def boton_crear(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[text() = 'CREAR NUEVO PACIENTE']").click()
        time.sleep(1)
    
    def llenar_form_crear(self, bien):
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Nombres']").send_keys('Nombre test')
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Apellidos']").send_keys('Apellido test')
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'C.I.']").send_keys(self.ci_def)
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Email']").send_keys(self.email_def)
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Teléfono']").send_keys('77553300')
        if bien:
            self.driver.find_element(By.XPATH, "//input[@type= 'date']").send_keys('01-01-1995')
        else:
            self.driver.find_element(By.XPATH, "//input[@type= 'date']").send_keys('31-12-2025')
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Dirección']").send_keys('AV Software quality assurance')
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Contraseña']").send_keys('qwerty123@')
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Codigo de Seguro Médico']").send_keys('sqa123456')
        self.driver.find_element(By.XPATH, "//select").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//option[2]").click()
        time.sleep(5)
    
    def enviar_form(self):
        self.driver.find_element(By.XPATH, "//button[text() = 'Crear Paciente']").click()
        time.sleep(10)
    
    def verificar_pacientecreado(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'BUSCAR PACIENTE...']").send_keys(self.email_def)
        actual = self.email_def.upper()
        esperado = self.driver.find_element(By.XPATH, "//tr//td[3]").text
        if actual == esperado:
            return  True
        return False

    

        
    
        

