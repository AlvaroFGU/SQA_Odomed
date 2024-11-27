from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_recepcionista import LoginPageRecep
import time

class TestModulo:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')
        time.sleep(0.5)
        self.login_page = LoginPageRecep(self.driver)
        self.login_page.login()
        time.sleep(15)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba finalizada")

    def test_verify_contenido_inicio(self):
        actual = self.driver.find_element(By.XPATH, "//h2").text
        esperada = "PACIENTES"
        assert esperada == actual, f"ERROR, actual {actual}, esperado: {esperada}"
