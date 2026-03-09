from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        
    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    def set_delay(self):
        delay_element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_element.clear()
        delay_element.send_keys("45")

    def add_calc(self, value):
        button = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//span[text()='{value}']"))
        )
        button.click()

    def wait_for_result(self, expected_text, timeout=45):
        try:
            WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_text)
        )
            return True
        except:
            return False
