from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class TestInterfaz:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')

    def teardown_method(self):
        self.driver.quit()
        print("Prueba completada")


    def test_paciente_button(self):
        self.default_email = 'PACIENTE123333@GMAIL.COM'
        self.default_password = 'qwerty123@'
        self.default_prueba = 'Pruebafinal'


        self.driver.find_element(By.XPATH,"//button[@class='chakra-button css-164ku12']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(self.default_email)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys(self.default_password)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(8)

        self.driver.find_element(By.XPATH,"//p[contains(text(),'PACIENTES')]").click()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH,"//h2[contains(text(),'PACIENTES')]").text
        esperado = "PACIENTES"

        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"

        
   
    def test_odonto_button(self):
        self.default_email = 'PACIENTE123333@GMAIL.COM'
        self.default_password = 'qwerty123@'
        self.default_prueba = 'Pruebafinal'


        self.driver.find_element(By.XPATH,"//button[@class='chakra-button css-164ku12']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(self.default_email)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys(self.default_password)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(8)

        self.driver.find_element(By.XPATH,"//p[contains(text(),'ODO')]").click()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH,"//h2[contains(text(),'ODO')]").text
        esperado = "ODONTÓLOGOS"

        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"

    def test_roles_button(self):
        self.default_email = 'PACIENTE123333@GMAIL.COM'
        self.default_password = 'qwerty123@'
        self.default_prueba = 'Pruebafinal'


        self.driver.find_element(By.XPATH,"//button[@class='chakra-button css-164ku12']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(self.default_email)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys(self.default_password)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(8)

        self.driver.find_element(By.XPATH,"//P[contains(text(),'ROL')]").click()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH,"//h2[contains(text(),'ROL')]").text
        esperado = "ROLES"
        
        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"
    
    def test_recep_button(self):
        self.default_email = 'PACIENTE123333@GMAIL.COM'
        self.default_password = 'qwerty123@'
        self.default_prueba = 'Pruebafinal'


        self.driver.find_element(By.XPATH,"//button[@class='chakra-button css-164ku12']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(self.default_email)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys(self.default_password)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(8)

        self.driver.find_element(By.XPATH,"//P[contains(text(),'RECEP')]").click()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH,"//h2[contains(text(),'RECEP')]").text
        esperado = "RECEPCIONISTAS"

        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"
    
    def test_citas_button(self):
        self.default_email = 'PACIENTE123333@GMAIL.COM'
        self.default_password = 'qwerty123@'
        self.default_prueba = 'Pruebafinal'


        self.driver.find_element(By.XPATH,"//button[@class='chakra-button css-164ku12']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(self.default_email)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys(self.default_password)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(8)

        self.driver.find_element(By.XPATH,"//P[contains(text(),'CIT')]").click()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH,"//P[contains(text(),'CIT')]").text
        esperado = "CITAS"

        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"





        


        


