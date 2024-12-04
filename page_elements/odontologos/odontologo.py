from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_odontologo import LoginPageOdo
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


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
def genera_num():
    numeros = list(range(1, 2))
    numRan = str(random.choice(numeros)) 
    return numRan
def genera_num_diag():
    numeros = list(range(1, 2))
    numRan = str(random.choice(numeros)) 
    return numRan

class Odontologo:
    def __init__(self, driver):
        self.driver = driver
        self.email_user_test = genera_username()
        self.ci_user_test = genera_ci()
        self.num_data = genera_num()
        self.ci_esperado = 00000
    
    def esperar_elemento(self, by, locator, timeout=15, visible=True):
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.visibility_of_element_located((by, locator)))
        except TimeoutException:
            return None

    def ingresar_form_crear_paciente(self):
        self.driver.find_element(By.XPATH, "//h2//following-sibling::button").click()

    def llenar_form_crear_paciente(self):
        self.ingresar_form_crear_paciente()
        nomPacient= "Raul Alejandro"
        self.driver.find_element(By.XPATH, "//input[@placeholder='Nombres']").send_keys(f"{nomPacient}")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Apellidos']").send_keys("Hernandez")
        self.driver.find_element(By.XPATH, "//input[@placeholder='C.I.']").send_keys(f"{self.ci_user_test}")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(f"{self.email_user_test}")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Teléfono']").send_keys("71234568")
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("2003-03-03")
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
        time.sleep(7)


    def buscar_paciente_creado_byCi(self):
        self.driver.find_element(By.XPATH, "//input[@value]").send_keys(f"{self.ci_user_test}")
        time.sleep(1)
        
    def crear_nuevo_paciente(self):
        self.llenar_form_crear_paciente()
        self.buscar_paciente_creado_byCi()
        actual = self.driver.find_element(By.XPATH, "//td[2]").text
        return actual
    
    def ingresar_info_paciente(self):
        
        self.ci_esperado = self.driver.find_element(By.XPATH, f"//tr[{self.num_data}]//td[2]").text
        self.driver.find_element(By.XPATH, f"//tr[{self.num_data}]//button").click()
        self.esperar_elemento(By.XPATH, "//header[text()='HISTORIAL ODONTOLOGICO DEL PACIENTE']")
        
    # def verif_pcnt_datosPersonales(self):
    #     actual = self.driver.find_element(By.XPATH, "//strong[text()='CI:']//parent::p").text
    #     return actual
    
    def ingresar_datos_per(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, f"//p//following-sibling::button[contains(text(), 'PERSONALES')]").click()
        
    def editar_datos_personales_paciente(self):
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, f"//label[contains(text(), 'C.I.')]//following-sibling::input").clear()
        self.driver.find_element(By.XPATH, f"//label[contains(text(), 'C.I.')]//following-sibling::input").send_keys(f"{self.ci_user_test}")
        self.driver.find_element(By.XPATH, f"//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, f"//header//following-sibling::button").click()
    
    def editar_paciente(self):
        self.ingresar_info_paciente()
        self.ingresar_datos_per()
        self.editar_datos_personales_paciente()
        time.sleep(5)
        self.actual = self.driver.find_element(By.XPATH, f"//tr[{self.num_data}]//td[2]").text
        return self.actual

    def verificar_paciente_seleccionado(self):
        self.ingresar_info_paciente()
        time.sleep(4)
        self.actual = self.driver.find_element(By.XPATH, "//strong[text()='CI:']//parent::p").text
        return self.actual

    def editar_paciente_datos_clinicos(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//p//following-sibling::button[contains(text(), 'CLÍNICOS')]").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//label[text()='Alergias']//following-sibling::input").clear()
        self.driver.find_element(By.XPATH, "//label[text()='Alergias']//following-sibling::input").send_keys("Test Alergias")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
    
    def editar_datos_clinicos(self):
        self.ingresar_info_paciente()
        self.editar_paciente_datos_clinicos()
        time.sleep(4)
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        return self.actual
    
    def ingresar_btn_historial(self):
        esperaElem = self.esperar_elemento(By.XPATH, "//button[text()='HISTORIAL CLINICO']")        
        self.driver.find_element(By.XPATH, "//button[text()='HISTORIAL CLINICO']").click()
        
    def editar_datos_historial(self):
        self.ingresar_info_paciente()
        self.ingresar_btn_historial()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'EDITAR DATOS')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//textarea").clear()
        self.driver.find_element(By.XPATH, "//textarea").send_keys("Nota Test")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        time.sleep(0.5)
        return self.actual
        
    def crear_nuevo_diagnostico(self):
        self.ingresar_info_paciente()
        self.ingresar_btn_historial()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'CREAR NUEVO DIAG')]").click()
        self.driver.find_element(By.XPATH, "//label[contains(text(),'Nombre')]//following-sibling::input").send_keys("Dato Test Diagnostico")
        self.driver.find_element(By.XPATH, "//textarea").send_keys("Dato Test Diagnostico")
        self.driver.find_element(By.XPATH, "//footer//button[1]").click()
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        time.sleep(0.5)
        return self.actual
        
    def editar_diagnostico(self):
        self.ingresar_info_paciente()
        self.ingresar_btn_historial()
        esperaElem = self.esperar_elemento(By.XPATH, f"//div[@class='css-cjp7tt'][{genera_num_diag()}]//button[text()='EDITAR DIAGNOSTICO']")
        esperaElem.click()
        self.driver.find_element(By.XPATH, f"//textarea").clear()
        self.driver.find_element(By.XPATH, f"//textarea").send_keys("Descripcion Test")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        time.sleep(0.5)
        return self.actual

    def eliminar_diagnostico(self):
        self.ingresar_info_paciente()
        self.ingresar_btn_historial()
        esperaElem = self.esperar_elemento(By.XPATH, f"//div[@class='css-cjp7tt'][{genera_num_diag()}]//button[2]")
        esperaElem.click()
        alerta = self.driver.switch_to.alert
        time.sleep(0.5)
        alerta.accept()
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        time.sleep(0.5)
        return self.actual
    
    def ingresar_btn_tratamientos(self):
        esperaElem = self.esperar_elemento(By.XPATH, "//button[text()='HISTORIAL CLINICO']")        
        self.driver.find_element(By.XPATH, "//button[text()='TRATAMIENTOS']").click()
        
    def crear_tratamiento(self):
        self.ingresar_info_paciente()
        self.ingresar_btn_tratamientos()
        self.driver.find_element(By.XPATH, "//button[text()='CREAR NUEVO TRATAMIENTO']").click()
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Nombre')]//following-sibling::input").send_keys("Dato Test")
        self.driver.find_element(By.XPATH, "//textarea").send_keys("Dato Test")
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("2024-12-12")
        self.driver.find_element(By.XPATH, "//input[@type='number']").send_keys("500")
        self.driver.find_element(By.XPATH, "//button[text()='Crear']").click()
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        time.sleep(0.5)
        return self.actual
    
    def editar_tratamiento(self):
        self.ingresar_info_paciente()
        self.ingresar_btn_tratamientos()
        esperaElem = self.esperar_elemento(By.XPATH, f"//div[@class='css-1kqiu9f'][{genera_num_diag()}]//button[1]")
        esperaElem.click()
        self.driver.find_element(By.XPATH, "//textarea").clear()
        self.driver.find_element(By.XPATH, "//textarea").send_keys("Dato Test Tratamiento")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        time.sleep(0.5)
        return self.actual
    
    def eliminar_tratamiento(self):
        self.ingresar_info_paciente()
        self.ingresar_btn_tratamientos()
        esperaElem = self.esperar_elemento(By.XPATH, f"//div[@class='css-1kqiu9f'][{genera_num_diag()}]//button[2]")
        esperaElem.click()
        alerta = self.driver.switch_to.alert
        time.sleep(0.5)
        alerta.accept()
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        time.sleep(0.5)
        return self.actual
    
    def ingresar_btn_prescripcion(self):
        esperaElem = self.esperar_elemento(By.XPATH, "//button[text()='HISTORIAL CLINICO']")        
        self.driver.find_element(By.XPATH, "//button[text()='PRESCRIPCIÓNES']").click()
        
    def crear_prescripcion(self):
        self.ingresar_info_paciente()
        self.ingresar_btn_prescripcion()
        self.driver.find_element(By.XPATH, "//button[text()='CREAR NUEVA PRESCRIPCIÓN']").click()
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Nombre')]//following-sibling::input").send_keys("Dato Prescripcion Test")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Dosis')]//following-sibling::input").send_keys("Dato Prescripcion Test")
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("2024-12-12")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'lista')]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Crear']").click()
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        time.sleep(0.5)
        return self.actual
        
    def editar_prescripcion(self):
        self.ingresar_info_paciente()
        self.ingresar_btn_prescripcion()
        esperaElem = self.esperar_elemento(By.XPATH, f"//div[@class='css-1kqiu9f'][{genera_num_diag()}]//button[1]")
        esperaElem.click()
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Dosis')]//following-sibling::input").clear()
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Dosis')]//following-sibling::input").send_keys("Dato Prescripcion Edit Test")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        time.sleep(0.5)
        return self.actual
    
    def eliminar_prescripcion(self):
        self.ingresar_info_paciente()
        self.ingresar_btn_prescripcion()
        esperaElem = self.esperar_elemento(By.XPATH, f"//div[@class='css-1kqiu9f'][{genera_num_diag()}]//button[2]")
        esperaElem.click()
        alerta = self.driver.switch_to.alert
        time.sleep(0.5)
        alerta.accept()
        esperaElem = self.esperar_elemento(By.XPATH, "//div[contains(@class,'chakra-alert__title')]")
        self.actual = esperaElem.text
        time.sleep(0.5)
        return self.actual