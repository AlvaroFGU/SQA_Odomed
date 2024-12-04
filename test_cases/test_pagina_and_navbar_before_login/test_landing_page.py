from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestInterfaz:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')

    def teardown_method(self):
        self.driver.quit()
        print("Prueba completada")

    def test_verify_reload_logo(self):
        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[2]/a").click()
        time.sleep(2)
        modal_reload = self.driver.find_element(By.XPATH,"//p[contains(text(),'Acerca ')]//parent::div[@class='css-1cu9hd1']//child::p[contains(text(),'Acerca')]")
        assert modal_reload, "ERROR: El Modal no se recargo correctamente"
    def test_verify_About_button(self):
        self.driver.find_element(By.XPATH, "//p[contains(text(),'Acerca ')]//parent::div[@class='css-1cu9hd1']//child::p[contains(text(),'Acerca')]").click()

        modal = self.driver.find_element(By.XPATH, "//*[@id='chakra-modal-:r1:']")
        assert modal, "ERROR: El modal no se abrió correctamente."

        time.sleep(2)

        actual = self.driver.find_element(By.XPATH, "//p[contains(text(),'en la atención personalizada para cada paciente. Ofrecemos una amplia gama de servicios, que incluyen')]//parent::div//child::p[@class='chakra-text css-rszk63']").text
        esperada = "en la atención personalizada para cada paciente. Ofrecemos una amplia gama de servicios, que incluyen tratamientos preventivos"
        assert esperada in actual, f"ERROR, actual: {actual}, esperado: {esperada}"

        self.driver.find_element(By.XPATH, "//*[@id='chakra-modal-:r1:']/button").click()
        time.sleep(3)

        modal_closed = not self.driver.find_elements(By.XPATH, "//*[@id='chakra-modal-:r1:']")
        assert modal_closed, "ERROR: El modal no se cerró correctamente."

    def test_verify_Servicios_button(self):
        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[3]/button").click()
        actual = self.driver.find_element(By.XPATH,"//*[@id='services-section']/div/div/div/div[1]/p").text
        time.sleep(4)
        esperado = "ofrecemos una amplia gama de servicios dentales para satisfacer todas tus necesidades de salud bucal"
        assert esperado in actual,f"ERROR, actual {actual}, esperado: {esperado}"

    def test_verify_Contacto_button(self):
        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[3]/p[2]").click()
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH,"//*[@id='chakra-modal--body-:r2:']")
        assert modal, "ERROR: El modal no se abrió correctamente."

        actual = self.driver.find_element(By.XPATH, "//*[@id='chakra-modal--body-:r2:']/p[2]").text
        esperado = "Correo electrónico"
        assert esperado in actual, f"ERROR, actual: {actual}, esperado: {esperado}"

        self.driver.find_element(By.XPATH, "//*[@id='chakra-modal-:r2:']/button").click()

        time.sleep(3)

        modal_closed = not self.driver.find_elements(By.XPATH, "//*[@id='chakra-modal-:r2:']")
        assert modal_closed, "ERROR: El modal no se cerró correctamente."
    
    def test_verify_Explore_Services(self):

        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/button").click()
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH,"//*[@id='services-section']/div/div/div/div[2]/ul/li[6]").text
        esperado= "-"
        assert esperado in actual, f"Error, Actual: {actual}, esperado: {esperado}"
    

        


