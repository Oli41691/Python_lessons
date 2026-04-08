from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ShopPage:
    """
    Страница интернет-магазина с функционалом авторизации, добавления товаров, оформления заказа.
    
    Атрибуты:
        driver (WebDriver): экземпляр драйвера Selenium.
        wait (WebDriverWait): объект для ожидания элементов.
        fields (dict): словарь логина и пароля.
        локаторы (расширение для удобства): локаторы элементов страницы.
    """
    def __init__(self, driver: 'WebDriver'):
        """
        Инициализация объекта страницы.
        
        :param driver: Экземпляр драйвера Selenium.
        :type driver: WebDriver
        """
        self.driver = driver
        self.fields = {
            'user-name': "standard_user",
            'password': "secret_sauce",
        }
        self.wait = WebDriverWait(driver, 10)
        
        # Локаторы элементов страницы
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.total_label = (By.CLASS_NAME, 'summary_total_label')

    @allure.step("Открытие главной страницы магазина")
    def open(self) -> None:
        """
        Открывает главную страницу магазина.
        """
        self.driver.get(
            "https://www.saucedemo.com"
            )

    @allure.step("Авторизация: ввод логина и пароля")
    def login(self) -> None:
        """
        Выполняет авторизацию, заполняя логин и пароль из self.fields и кликая кнопку входа.
        """
        for field, value in self.fields.items():
            self.driver.find_element(By.ID, field).send_keys(value)
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()

    @allure.step("Добавление товара по ID: {product_id}")
    def add_product(self, product_id: str) -> None:
        """
        Добавляет товар по его ID.
        
        :param product_id: id товара.
        :type product_id: str
        """
        self.driver.find_element(By.ID, product_id).click()   

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит в корзину, кликая по ссылке.
        """
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    @allure.step("Переход к оформлению заказа")
    def proceed_checkout(self, timeout: int = 10) -> None:
        """
        Нажимает кнопку "Checkout" чтобы перейти к оформлению заказа.
        
        :param timeout: время ожидания в секундах.
        :type timeout: int
        """
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    @allure.step("Заполнение формы оформления заказа: {first_name} {last_name}, {postal_code}")
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму заказа и продолжает.
        
        :param first_name: имя.
        :type first_name: str
        :param last_name: фамилия.
        :type last_name: str
        :param postal_code: почтовый индекс.
        :type postal_code: str
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name)).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
    
    @allure.step("Получение итоговой суммы заказа")
    def get_total(self) -> str:
        """
        Возвращает текст итоговой суммы заказа.
        
        :return: текст с суммой.
        :rtype: str
        """
        total_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.total_label)).text
        return total_text
