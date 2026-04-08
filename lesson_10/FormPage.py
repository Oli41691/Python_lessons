from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:
    """
    Страница формы регистрации.

    Атрибуты:
        driver (WebDriver): экземпляр драйвера Selenium для взаимодействия с браузером.
        wait (WebDriverWait): объект ожидания стандартной продолжительности 5 секунд.
        fields (dict): словарь полей формы и их значения.
    """
    def __init__(self, driver: 'WebDriver'):
        """
        Инициализация страницы.

        :param driver: Экземпляр драйвера Selenium.
        :type driver: WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("Открытие страницы формы")
    def open(self) -> None:
        """
        Открывает страницу формы по URL.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )

    @allure.step("Заполнение формы")
    def fill_form(self)  -> None:
        """
        Заполняет все поля формы значениями из атрибута self.fields.
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Отправка формы")
    def submit_form(self) -> None:
        """
        Находит кнопку отправки и кликает по ней.
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    @allure.step("Получение класса поля по ID '{field_id}'")
    def get_field_class(self, field_id: str) -> str:
        """
        Возвращает значение атрибута class элемента по его id.

        :param field_id: id элемента.
        :type field_id: str
        :return: строка с классом элемента.
        :rtype: str
        """
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    @allure.step("Проверка, есть ли ошибка в поле 'zip-code'")
    def check_zip_code_error(self) -> bool:
        """
        Проверяет наличие класса 'alert-danger' у поля zip-code.

        :return: True, если есть ошибка, иначе False.
        :rtype: bool
        """
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверка успешности заполнения полей")
    def check_fields_success(self) -> bool:
        """
        Проверяет, что у всех полей есть класс 'success'.

        :return: True, если все поля успешны, иначе False.
        :rtype: bool
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Проверка формы на корректность и ошибки")
    def check_form_submission(self) -> None:
        """
        Выполняет проверки ошибок и успеха формы.
        """
        assert self.check_zip_code_error()
        assert self.check_fields_success()
