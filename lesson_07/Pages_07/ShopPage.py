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

    def add_info(self, info_type, value):
        if info_type == "first_name":
            element_id = "first-name"
        elif info_type == "last_name":
            element_id = "last-name"
        elif info_type == "postal_code":
            element_id = "postal-code"
        elif info_type == ".cart_button":
            button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart_button")))
            button.click()
            return self
        else:
            raise ValueError(f"Unknown info_type: {info_type}")

        self.wait.until(EC.presence_of_element_located((By.ID, element_id))).send_keys(value)

    def get_total(self):
        total_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label'))
        ).text
        return total_text
