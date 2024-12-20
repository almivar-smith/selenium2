import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bleach
import os
import time  # Importamar "el retraso" sempre bé de lag

class TestWebApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Configura el navegador abans de començar els tests"""
        # Detectem si estem en un entorn local o en GitHub Actions
        if os.environ.get('CI') == 'true':
            print("Entorn de GitHub Actions detectat: s'executarà en mode headless.")
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            cls.driver = webdriver.Chrome(options=options)
        else:
            print("Entorn local detectat: s'executarà amb interfície gràfica.")
            cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        """Tanca el navegador després de completar els tests"""
        cls.driver.quit()

    def test_suma_correcta(self):
        """Prova que la calculadora faci la suma correctament (5 + 3 = 8)"""
        print("\n\n====> TEST 1 ================")
        self.driver.get("http://localhost:5000")  # Ajusta aquesta URL segons sigui necessari
        number_field_1 = self.driver.find_element(By.NAME, "number1")
        number_field_2 = self.driver.find_element(By.NAME, "number2")
        submit_button = self.driver.find_element(By.XPATH, '//input[@type="submit"]')

        # Omplim els camps amb valors
        number_field_1.send_keys("5")
        number_field_2.send_keys("3")
        submit_button.click()

        # Esperem que es mostri el resultat
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        result = self.driver.find_element(By.TAG_NAME, "body").text
        print(f"funcio suma --> (5 + 3 = 8)")  # Detall de la suma

        # Netegem el resultat per evitar etiquetes HTML i altres elements
        result_clean = bleach.clean(result)

        # Verifiquem que el resultat de la suma sigui correcte
        self.assertIn("Resultat: 8", result_clean)

        print("test_suma_correcta OK")  # Mensaje de éxito

        # Afegim un delay de 2 segons abans del següent test
        time.sleep(2)

    def test_validacio_campos_vacios(self):
        """Prova que es mostri el missatge d'error si falten camps al formulari"""
        print("\n\n====> TEST 2 ================")
        self.driver.get("http://localhost:5000")  # Ajusta aquesta URL segons sigui necessari
        number_field_1 = self.driver.find_element(By.NAME, "number1")
        number_field_2 = self.driver.find_element(By.NAME, "number2")
        submit_button = self.driver.find_element(By.XPATH, '//input[@type="submit"]')

        # Deixem els camps en blanc
        number_field_1.clear()
        number_field_2.clear()
        submit_button.click()

        # Esperem que es mostri el missatge d'error
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        result = self.driver.find_element(By.TAG_NAME, "body").text
        print("funcio error --> Camps buits")  # Detall del error

        # Netegem el resultat per evitar etiquetes HTML i altres elements
        result_clean = bleach.clean(result)

        # Verifiquem que es mostri el missatge d'error
        self.assertIn("¡Els 2 camps són obligatoris!", result_clean)

        print("test_validacio_campos_vacios OK")  # Missatge de èxit

        # Afegim un delay de 2 segons abans del següent test
        time.sleep(2)

    def test_validacio_dades_no_numeriques(self):
        """Prova que es mostri el missatge d'error si es posen dades no numèriques"""
        print("\n\n====> TEST 3 ================")
        self.driver.get("http://localhost:5000")  # Ajusta aquesta URL segons sigui necessari
        number_field_1 = self.driver.find_element(By.NAME, "number1")
        number_field_2 = self.driver.find_element(By.NAME, "number2")
        submit_button = self.driver.find_element(By.XPATH, '//input[@type="submit"]')

        # Omplim els camps amb text en lloc de números
        number_field_1.send_keys("a")
        number_field_2.send_keys("b")
        submit_button.click()

        # Esperem que es mostri el missatge d'error
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        result = self.driver.find_element(By.TAG_NAME, "body").text
        print("funcio error --> Dades no numèriques")  # Detall del error

        # Netegem el resultat per evitar etiquetes HTML i altres elements
        result_clean = bleach.clean(result)

        # Ara, verifiquem que el missatge conté la part clau
        self.assertIn("¡Si us plau!", result_clean)
        self.assertIn("només números", result_clean)
        self.assertIn("només números válids!", result_clean)  # Comprovem que estigui amb 'v'

        print("test_validacio_dades_no_numeriques OK")  # Missatge de èxit

        # Afegim un delay de 2 segons abans de finalitzar
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
