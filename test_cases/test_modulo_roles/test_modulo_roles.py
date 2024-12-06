from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestInterfaz:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')

    def teardown_method(self):
        self.driver.quit()
        print("Prueba completada")
   
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



    def test_roles_create_new_rol(self):
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

        self.driver.find_element(By.XPATH,"//button[@class='chakra-button css-betff9']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Nombre del rol']").send_keys(self.default_prueba)

        self.driver.find_element(By.XPATH,"//button[@class='chakra-accordion__button css-uttm9k']//child::div[contains(text(),'Roles')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@class='chakra-accordion__button css-uttm9k']//child::div[contains(text(),'Roles')]//parent::button//child::span[contains(text(),'Sele')]").click()
        time.sleep(8)
        actual = self.driver.find_element(By.XPATH,"///div[contains(@class,'css-161kwbg')]").text
        esperado = "PRUEBAROL"
        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"



    def test_roles_edit(self):
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



        self.driver.find_element(By.XPATH,"//td[contains(text(),'ODON')]//following-sibling::td//child::button[@class='chakra-button css-jn2gtv']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//strong[contains(text(),'Rol')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//strong[contains(text(),'Rol')]//ancestor::details//child::div//child::span[contains(text(),'Sele')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//footer//child::button[contains(text(),'Guard')]").click()
        time.sleep(3)
        actual = self.driver.find_element(By.XPATH,"//div[@class='chakra-alert__desc css-161kwbg']").text
        esperado = "El rol ha sido actualizado exitosamente."
        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"


    def test_roles_delete(self):
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

        self.driver.find_element(By.XPATH, "//button[@class='chakra-button css-jn2gtv']").click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present()) 
        alert = Alert(self.driver)
        alert.accept()  
        time.sleep(3)

        actual = self.driver.find_element(By.XPATH, "//div[@class='chakra-alert__desc css-161kwbg')]").text
        esperado = "El rol ha sido eliminado exitosamente."
        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"










        












