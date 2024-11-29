from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from page_elements.login.login_recepcionista import LoginPageRecep
from selenium.webdriver import Keys, ActionChains

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

    def test_crear_paciente(self):
        self.driver.find_element(By.XPATH, "//h2//following-sibling::button").click()
        time.sleep(0.5)
        nomPacient= "Raul Alejandro"
        self.driver.find_element(By.XPATH, "//input[@placeholder='Nombres']").send_keys(f"{nomPacient}")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Apellidos']").send_keys("Hernandez")
        self.driver.find_element(By.XPATH, "//input[@placeholder='C.I.']").send_keys("471258369")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("pcnt1test@google.com")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Teléfono']").send_keys("71234568")
        self.driver.find_element(By.XPATH, "//input[@type='date']").send_keys("03-mar-2003")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Dirección']").send_keys("Calle testeo, 4332")
        self.driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)
        self.driver.find_element(By.XPATH, "//body").send_keys(Keys.SPACE)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']").send_keys("Qwerty123@")
        self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Codigo')]").send_keys("Rp123456")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Alergias']").clear()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Alergias']").send_keys("Productos altos en ph")
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Antecedentes Médicos']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@placeholder = 'Antecedentes Médicos']").send_keys("SI")







