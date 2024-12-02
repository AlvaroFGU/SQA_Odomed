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
    
class ModuloPaciente:
    def __init__(self, driver):
        self.driver = driver
        self.email_def = genera_username()
        self.ci_def = genera_ci() 

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

    def boton_historial(self):
        self.driver.find_element(By.XPATH, "//button[@class = 'chakra-button css-jn2gtv'][1]").click()
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//header"))
        )

    def text_datos_personales(self):
        try:
            boton = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//button[text()= 'DATOS PERSONALES']"))
            )
            return boton.is_displayed()
        except:
            return False
    
    def nav_bar_historial(self):
        self.driver.find_element(By.XPATH, "//button[text()= 'HISTORIAL CLINICO']").click()
        try:
            boton = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//button[text()= 'EDITAR DATOS DEL HISTORIAL']"))
            )
            return boton.is_displayed()
        except:
            return False
                
    def nav_bar_tratamientos(self):
        self.driver.find_element(By.XPATH, "//button[text()= 'TRATAMIENTOS']").click()
        try:
            boton = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//button[text()= 'CREAR NUEVO TRATAMIENTO']"))
            )
            return boton.is_displayed()
        except:
            return False
            
    def nav_bar_prescripciones(self):
        self.driver.find_element(By.XPATH, "//button[text()= 'PRESCRIPCIÓNES']").click()
        try:
            boton = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//button[text()= 'CREAR NUEVA PRESCRIPCIÓN']"))
            )
            return boton.is_displayed()
        except:
            return False
    
    def editar_datos_personales(self):
        self.driver.find_element(By.XPATH, "//button[text()= 'EDITAR DATOS PERSONALES']").click()
        time.sleep(1)
        dir = self.driver.find_element(By.XPATH, "//label[text() = 'Dirección']//following-sibling::input")
        dir.clear()
        dir.send_keys('Edicion sqa')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        try:
            mensaje = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Datos personales actualizados.']"))
            )
            return mensaje.is_displayed()
        except:
            return False
        
    def editar_datos_clinicos(self):
        self.driver.find_element(By.XPATH, "//button[text()= 'EDITAR DATOS CLÍNICOS']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@placeholder = 'Ingrese alergias']").send_keys(genera_ci())
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        try:
            mensaje = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Paciente actualizado.']"))
            )
            return mensaje.is_displayed()
        except:
            return False
        
    def descargar_historial(self):
        self.boton_historial()
        boton = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//button[text() = 'DESCARGAR HISTORIAL']"))
            )
        boton.click()
        try:
            mensaje = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Descarga exitosa']"))
            )
            return mensaje.is_displayed()
        except:
            return False
        
    def wait_locator(self, locator):
        try:
            elemento = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
            return elemento.is_displayed()
        except:
            return False
        
    def editar_datos_historial(self):
        self.boton_historial()
        self.driver.find_element(By.XPATH, "//button[text()= 'HISTORIAL CLINICO']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text() = 'EDITAR DATOS DEL HISTORIAL']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//textarea").send_keys('editado')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        return self.wait_locator("//div[text() = 'Historial actualizado.']")
    
    def crear_diagnostico(self):
        self.boton_historial()
        self.driver.find_element(By.XPATH, "//button[text()= 'HISTORIAL CLINICO']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text() = 'CREAR NUEVO DIAGNOSTICO']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input").send_keys('prueba sqa')
        self.driver.find_element(By.XPATH, "//textarea").send_keys('descripcion sqa')
        self.driver.find_element(By.XPATH, "//button[text() = 'Crear']").click()
        return self.wait_locator("//div[text() = 'Diagnóstico creado.']")

    def editar_diagnostico(self):
        self.boton_historial()
        self.driver.find_element(By.XPATH, "//button[text()= 'HISTORIAL CLINICO']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//p[text() = 'PRUEBA SQA'][1]//following-sibling::button[text()]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//textarea").send_keys(' editado')
        self.driver.find_element(By.XPATH, "//button[text() = 'Guardar']").click()
        return self.wait_locator("//div[text() = 'Diagnóstico actualizado.']")

    def eliminar_diagnostico(self):
        self.boton_historial()
        self.driver.find_element(By.XPATH, "//button[text()= 'HISTORIAL CLINICO']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//p[text() = 'PRUEBA SQA'][1]//following-sibling::button[@class = 'chakra-button css-17gj2bt']").click()
        time.sleep(1)
        alert = Alert(self.driver)
        alert.accept()
        return self.wait_locator("//div[text() = 'Diagnostico eliminado.']")

    def crear_tratamiento(self):
        self.boton_historial()
        self.driver.find_element(By.XPATH, "//button[text()= 'TRATAMIENTOS']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text() = 'CREAR NUEVO TRATAMIENTO']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id = 'field-:rh:']").send_keys('Tratamiento sqa')
        self.driver.find_element(By.XPATH, "//textarea").send_keys('descripcion sqa')
        self.driver.find_element(By.XPATH, "//input[@type= 'date']").send_keys('15-12-2024')
        self.driver.find_element(By.XPATH, "//input[@type= 'number']").send_keys('100')
        self.driver.find_element(By.XPATH, "//button[text() = 'Crear']").click()
        return self.wait_locator("//div[text() = 'Tratamiento creado.']")

    def editar_tratamiento(self):
        self.boton_historial()
        self.driver.find_element(By.XPATH, "//button[text()= 'TRATAMIENTOS']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//p[text() = 'EN CURSO'][1]//following-sibling::button[text()]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@type  = 'date']").send_keys('15-12-2024')
        self.driver.find_element(By.XPATH, "//textarea").send_keys(' editado')
        self.driver.find_element(By.XPATH, "//button[text() = 'Guardar']").click()
        return self.wait_locator("//div[text() = 'Tratamiento actualizado.']")

    def eliminar_tratamiento(self):
        self.boton_historial()
        self.driver.find_element(By.XPATH, "//button[text()= 'TRATAMIENTOS']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//p[text() = 'TRATAMIENTO SQA'][1]//following-sibling::button[@class = 'chakra-button css-17gj2bt']").click()
        time.sleep(1)
        alert = Alert(self.driver)
        alert.accept()
        return self.wait_locator("//div[text() = 'Tratamiento eliminado.']")
    
    def crear_prescripcion(self):
        self.boton_historial()
        self.driver.find_element(By.XPATH, "//button[text()= 'PRESCRIPCIÓNES']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text() = 'CREAR NUEVA PRESCRIPCIÓN']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name = 'nombre_medicamento']").send_keys('medicamento sqa 1')
        self.driver.find_element(By.XPATH, "//input[@name = 'dosis']").send_keys('dosis sqa')
        self.driver.find_element(By.XPATH, "//input[@name= 'fecha_fin']").send_keys('15-12-2024')
        self.driver.find_element(By.XPATH, "//button[text() = 'Añadir a la lista']").click()
        self.driver.find_element(By.XPATH, "//input[@name = 'nombre_medicamento']").send_keys('medicamento sqa 2')
        self.driver.find_element(By.XPATH, "//input[@name = 'dosis']").send_keys('dosis sqa')
        self.driver.find_element(By.XPATH, "//input[@name= 'fecha_fin']").send_keys('15-12-2024')
        self.driver.find_element(By.XPATH, "//button[text() = 'Añadir a la lista']").click()
        self.driver.find_element(By.XPATH, "//input[@name = 'nombre_medicamento']").send_keys('medicamento sqa 3')
        self.driver.find_element(By.XPATH, "//input[@name = 'dosis']").send_keys('dosis sqa')
        self.driver.find_element(By.XPATH, "//input[@name= 'fecha_fin']").send_keys('15-12-2024')
        self.driver.find_element(By.XPATH, "//button[text() = 'Añadir a la lista']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class = 'chakra-button css-1wqgnr1'][1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text() = 'Crear']").click()
        return self.wait_locator("//div[text() = 'Prescripcion creado.']")

    def editar_prescripcion(self):
        self.boton_historial()
        self.driver.find_element(By.XPATH, "//button[text()= 'PRESCRIPCIÓNES']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text() = 'EDITAR PRESCRIPCIÓN'][1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//label[text() = 'Dosis']//following-sibling::input").send_keys(' editado')
        self.driver.find_element(By.XPATH, "//button[text() = 'Guardar']").click()
        return self.wait_locator("//div[text() = 'Prescripción actualizada']")

    def eliminar_prescripcion(self):
        self.boton_historial()
        self.driver.find_element(By.XPATH, "//button[text()= 'PRESCRIPCIÓNES']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class = 'chakra-button css-17gj2bt'][1]").click()
        time.sleep(1)
        alert = Alert(self.driver)
        alert.accept()
        return self.wait_locator("//div[text() = 'Medicamento eliminado.']")

    def eliminar_paciente(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//thead"))
        )
        self.driver.find_element(By.XPATH, "//button[text() = 'SIGUIENTE']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class = 'chakra-button css-spmwho'][1]").click()
        time.sleep(1)
        alert = Alert(self.driver)
        alert.accept()
        return self.wait_locator("//div[text() = 'Paciente eliminado.']")

    def paginacion(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//thead"))
        )
        self.driver.find_element(By.XPATH, "//button[text() = 'SIGUIENTE']").click()
        return self.wait_locator("//button[@class = 'chakra-button css-spmwho'][1]")

