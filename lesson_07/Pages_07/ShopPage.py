from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.fields = {
            'user-name': "standard_user",
            'password': "secret_sauce",
        }
        self.wait = WebDriverWait(driver, 10)
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.total_label = (By.CLASS_NAME, 'summary_total_label')

    def open(self):
        self.driver.get(
            "https://www.saucedemo.com"
            )

    def login(self):
        for field, value in self.fields.items():
            self.driver.find_element(By.ID, field).send_keys(value)
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()

    def add_product(self, product_id):
        self.driver.find_element(By.ID, product_id).click()   

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    def proceed_checkout(self, timeout=10):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    def fill_form(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name)).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
    
    def get_total(self):
        total_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.total_label)).text
        return total_text
