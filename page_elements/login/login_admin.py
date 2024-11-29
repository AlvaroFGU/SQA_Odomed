from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

import time

class LoginPageAdmin:
    def __init__(self, driver):
        self.driver = driver
        self.def_email = 'PACIENTE123333@GMAIL.COM'
        self.def_contra = 'qwerty123@'

    def ingresar(self):
        self.driver.find_element(By.XPATH, "//button[text() ='Ingresar']").click()
        time.sleep(1)

    def email(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(self.def_email)
        
    def contra_correcta(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys(self.def_contra)

    def contra_incorrecta(self):
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys('hola')

    def enviar(self):
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        
    def llenar_form(self, bien):
        self.ingresar()
        self.email()
        if bien:
            self.contra_correcta()
        else:
            self.contra_incorrecta()

    def login(self, bien):
        self.llenar_form(bien)
        self.enviar()
        time.sleep(10)
    
    def logo_visible(self):
        try:
            logo = self.driver.find_element(By.XPATH, "//img[@alt='OdontoMed Logo']").is_displayed()
        except:
            logo = False
        finally:        
            return logo
    
    def cerrar_sesion(self):
        self.driver.find_element(By.XPATH, "//*[@aria-label = ' avatar']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@aria-orientation]//child::button[text() = 'Cerrar sesión']").click()
        time.sleep(1)

    def titulo(self):
        try:
            titulo = self.driver.find_element(By.XPATH, "//p[text() = 'BIENVENIDO A ODOMED']").is_displayed()
        except:
            titulo = False
        finally:
            return titulo

    def olvidar_contraseña(self, bien):
        self.driver.find_element(By.XPATH, "//button[text() = '¿Olvidaste tu contraseña?']").click()
        time.sleep(1)
        if bien:
            self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys('gaa2025817@est.univalle.edu')
        else:
            self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys('emailinvalido@est.univalle.edu')
        self.driver.find_element(By.XPATH, "//button[text()= 'Enviar Código de Recuperación']").click()
        time.sleep(10)
        
    def ver_cod(self):
        try:
            titulo_cod = self.driver.find_element(By.XPATH, "//p[text()= 'Verificar Código']").is_displayed()
        except:
            titulo_cod = False
        finally:
            return titulo_cod
        
    def ver_contra(self):
        self.driver.find_element(By.XPATH, "//button[@class= 'chakra-button css-1xgetim']").click()
        esperado = 'Ocultar'
        actual = self.driver.find_element(By.XPATH, "//button[@class= 'chakra-button css-1xgetim']").text
        time.sleep(1)
        if actual == esperado:
            return True
        else:
            return False
        
    
        

