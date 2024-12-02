from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


import time
import string
import random

def genera_username():
    alfabeto = list(string.ascii_lowercase)
    numeros = list(range(1000, 10000))
    user = ''.join([random.choice(alfabeto) for i in range(3)])  
    number = str(random.choice(numeros)) 
    username = user + number + "@gmail.com"  
    return username

def genera_ci():
    numeros = list(range(100000, 99999999))  
    number = str(random.choice(numeros)) 
    username = number  
    return username
    
class ModuloCitas:
    def __init__(self, driver):
        self.driver = driver
        
    def wait_locator(self, locator):
        try:
            elemento = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
            return elemento.is_displayed()
        except:
            return False
        
    def wait_locator_s(self, locator):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
        except:
            return False
        
    def ver_citas(self):
        self.driver.find_element(By.XPATH, "//p[text() = 'CITAS']").click()
        return self.wait_locator("//tr[1]")
        
    def fitro_odontologo(self):
        self.driver.find_element(By.XPATH, "//p[text() = 'CITAS']").click()
        self.wait_locator_s("//tr[1]")
        self.driver.find_element(By.XPATH, "//option[text() = 'SELECCIONAR ODONTOLOGO']//parent::select").click()
        odontologo = self.driver.find_element(By.XPATH, "//option[text() = 'SELECCIONAR ODONTOLOGO']//following-sibling::option[1]")
        odontologo.click()
        nombre = odontologo.text
        lista = self.driver.find_elements(By.XPATH, "//tr//td[4]")
        for i in lista:
            if i.text != nombre:
                return False
        return True
        
    def filtro_fecha(self):
        self.driver.find_element(By.XPATH, "//p[text() = 'CITAS']").click()
        self.wait_locator_s("//tr[1]")
        fecha = self.driver.find_element(By.XPATH, "//input")
        fecha.send_keys('15-12-2024')
        fecha_text = fecha.get_attribute('value')
        lista = self.driver.find_elements(By.XPATH, "//tr//td[1]")
        for i in lista:
            if i.text != fecha_text:
                return False
        return True

    def filtro_estado(self):
        self.driver.find_element(By.XPATH, "//p[text() = 'CITAS']").click()
        self.wait_locator_s("//tr[1]")
        self.driver.find_element(By.XPATH, "//option[text() = 'SELECCIONAR ESTADO DE CITA']//parent::select").click()
        odontologo = self.driver.find_element(By.XPATH, "//option[text() = 'SELECCIONAR ESTADO DE CITA']//following-sibling::option[1]")
        odontologo.click()
        estado = odontologo.text
        lista = self.driver.find_elements(By.XPATH, "//tr//td[5]")
        for i in lista:
            if i.text != estado:
                return False
        return True
    
    def editar_cita(self):
        self.driver.find_element(By.XPATH, "//p[text() = 'CITAS']").click()
        self.wait_locator_s("//tr[1]")
        self.driver.find_element(By.XPATH, "//td//button[@class = 'chakra-button css-jn2gtv'][1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//option[text() = 'Selecciona un paciente']//parent::select").click()
        self.wait_locator_s("//option[text() = 'Selecciona un paciente']//following-sibling::option[1]")
        self.driver.find_element(By.XPATH, "//option[text() = 'Selecciona un paciente']//following-sibling::option[1]").click()
        self.driver.find_element(By.XPATH, "//option[text() = 'Programada']//parent::select").click()
        self.driver.find_element(By.XPATH, "//option[text() = 'Programada']").click()
        self.driver.find_element(By.XPATH, "//button[text() = 'Guardar']").click()
        return self.wait_locator("//div[text() = 'Cita actualizada.']")

    def eliminar_cita(self):
        self.driver.find_element(By.XPATH, "//p[text() = 'CITAS']").click()
        self.wait_locator_s("//tr[1]")
        self.driver.find_element(By.XPATH, "//td//button[@class = 'chakra-button css-jn2gtv'][1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//option[text() = 'Selecciona un paciente']//parent::select").click()
        self.wait_locator_s("//option[text() = 'Selecciona un paciente']//following-sibling::option[1]")
        self.driver.find_element(By.XPATH, "//option[text() = 'Selecciona un paciente']//following-sibling::option[1]").click()
        self.driver.find_element(By.XPATH, "//option[text() = 'Programada']//parent::select").click()
        self.driver.find_element(By.XPATH, "//option[text() = 'Cancelada']").click()
        self.driver.find_element(By.XPATH, "//button[text() = 'Guardar']").click()
        self.wait_locator_s("//div[text() = 'Cita actualizada.']")
        time.sleep(10)
        self.wait_locator_s("//tr[1]")
        self.driver.find_element(By.XPATH, "//td//button[@class = 'chakra-button css-spmwho'][1]").click()
        time.sleep(1)
        alert = Alert(self.driver)
        alert.accept()
        return self.wait_locator("//div[text() = 'Cita eliminada.']")



