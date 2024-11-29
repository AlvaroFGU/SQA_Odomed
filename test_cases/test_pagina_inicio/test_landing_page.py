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

    def button_about(self):

        self.driver.find_element(By.XPATH, "//p[contains(text(),'Acerca ')]//parent::div[@class='css-1cu9hd1']//child::p[contains(text(),'Acerca')]").click()
        time.sleep(2)

        actual = self.driver.find_element(By.XPATH, "//p[contains(text(),'en la atención personalizada para cada paciente. Ofrecemos una amplia gama de servicios, que incluyen')]//parent::div//child::p[@class='chakra-text css-rszk63']").text
        esperada = "en la atención personalizada para cada paciente. Ofrecemos una amplia gama de servicios, que incluyen tratamientos preventivos"


        assert esperada in actual, f"ERROR, actual {actual}, esperado: {esperada}"

    def button_service(self):
        self.driver.find_elemnt(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[3]/button").click()
        actual = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[3]/button").text()
        time.sleep(2)
        esperado = "ofrecemos una amplia gama de servicios dentales para satisfacer todas tus necesidades de salud bucal"
        assert esperado in actual,f"ERROR, actual {actual}, esperado: {esperado}"

    

    def bun_ser(self):
        self.driver.find_elemnt(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[3]/button").click()
        actual = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div[3]/button").text()
        time.sleep(2)
        esperado = "ofrecemos una amplia gama de servicios dentales para satisfacer todas tus necesidades de salud bucal"
        assert esperado in actual,f"ERROR, actual {actual}, esperado: {esperado}"

    

