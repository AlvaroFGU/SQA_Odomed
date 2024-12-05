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




    def test__create_new_recep(self):
        self.default_email = 'PACIENTE123333@GMAIL.COM'
        self.default_password = 'qwerty123@'
        self.default_prueba = 'Pruebafinal'
        self.default_pruebal = '9155694'
        self.default_pruebale = 'pruebaas@gmail.com'
        self.default_pruebales = '79575745'
        self.default_pruebalest = '10/15/2000'
        self.default_pruebaleste = 'Av.Silva'
        self.default_pruebalestet = 'qwerty@123'

        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[4]/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(self.default_email)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys(self.default_password)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(8)

        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[3]/a[4]").click()
        actual = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/h2").text
        esperado = "RECEPCIONISTAS"

        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"




        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Nombres']").send_keys(self.default_prueba)
        time.sleep(2)

        self.driver.find_element(By.XPATH,"//input[@placeholder='Apellidos']").send_keys(self.default_prueba)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='C.I.']").send_keys(self.default_pruebal)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys(self.default_pruebale)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Teléfono']").send_keys(self.default_pruebales)
        time.sleep(2)
        fecha_convertida = datetime.strptime(self.default_pruebalest, '%m/%d/%Y').strftime('%Y-%m-%d')
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys(fecha_convertida)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Dirección']").send_keys(self.default_pruebaleste)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Contraseña']").send_keys(self.default_pruebalestet)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@class='chakra-button css-nhals4']").click()
        time.sleep(4)
        actual = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/table/tbody/tr[5]/td[1]").text
        esperado = "Pruebafinal"
        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"

    def test_recep_edit(self):
        self.default_email = 'PACIENTE123333@GMAIL.COM'
        self.default_password = 'qwerty123@'
        self.default_prueba = 'Pruebafinaledit'
        self.default_prueba = 'Pruebafinaled'
        self.default_pruebal = '9155694'
        self.default_pruebale = 'pruebaas@gmail.com'
        self.default_pruebales = '79575745'
        self.default_pruebalest = '10/15/2000'
        self.default_pruebaleste = 'Av.Silva'
        self.default_pruebalestet = 'qwerty@123'
        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[4]/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(self.default_email)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys(self.default_password)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(8)

        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[3]/a[4]").click()
        actual = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/h2").text
        esperado = "RECEPCIONISTAS"

        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"

        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/table/tbody/tr[5]/td[5]/div/button[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/section/div/form/div/div[1]/div/input").send_keys(self.default_prueba)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/section/div/form/div/div[2]/div/input").send_keys(self.default_prueba)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/section/div/form/div/div[3]/div/input").send_keys(self.default_pruebal)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/section/div/form/div/div[4]/div/input").send_keys(self.default_pruebale)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/section/div/form/div/div[5]/div/input").send_keys(self.default_pruebales)
        time.sleep(2)
        fecha_convertida = datetime.strptime(self.default_pruebalest, '%m/%d/%Y').strftime('%Y-%m-%d')
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/section/div/form/div/div[6]/div/input").send_keys(fecha_convertida)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/section/div/form/div/div[7]/div/input").send_keys(self.default_pruebaleste)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//footer//child::button[contains(text(),'Guard')]").click()
        time.sleep(3)
        actual = self.driver.find_element(By.XPATH,"//*[contains(@class, 'chakra-alert__desc') and contains(@class, 'css-161kwbg')]").text
        esperado = "El recepcionista ha sido creado exitosamente."
        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"

    def test_recep_delete(self):
        self.default_email = 'PACIENTE123333@GMAIL.COM'
        self.default_password = 'qwerty123@'
        


        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[4]/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(self.default_email)
        self.driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys(self.default_password)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(8)

        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[3]/a[4]").click()
        actual = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/h2").text
        esperado = "RECEPCIONISTAS"

        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"


        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/table/tbody/tr[5]/td[5]/div/button[2]").click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())  
        alert = Alert(self.driver)
        alert.accept()  
        time.sleep(3)

        actual = self.driver.find_element(By.XPATH, "//*[contains(@class, 'chakra-alert__desc') and contains(@class, 'css-161kwbg')]").text
        esperado = "El recepcionista ha sido eliminado exitosamente."
        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"
        
    