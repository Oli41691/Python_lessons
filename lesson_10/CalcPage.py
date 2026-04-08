from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    """
    Страница калькулятора.

    Атрибуты:
        driver (WebDriver): Экземпляр драйвера Selenium для взаимодействия с браузером.
    """


    def __init__(self, driver: 'WebDriver'):
        self.driver = driver
        """
        Инициализация объекта страницы.

        :param driver: экземпляр драйвера Selenium.
        :type driver: WebDriver
        """
    
    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self, delay: str = "45") -> None:
        """
        Устанавливает задержку работы калькулятора.

        :param delay: задержка в секундах, по умолчанию "45".
        :type delay: str
        """
        delay_element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_element.clear()
        delay_element.send_keys("45")

    @allure.step("Нажатие кнопки с значением '{value}'")
    def add_calc(self, value: str) -> None:
        """
        Нажимает кнопку калькулятора с указанным значением.

        :param value: значение кнопки для нажатия, например "7", "+" или "=".
        :type value: str
        """
        button = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//span[text()='{value}']"))
        )
        button.click()

    @allure.step("Ожидание появления текста '{expected_text}' в дисплее")
    def wait_for_result(self, expected_text: str, timeout: int = 45) -> bool:
        """
        Ожидает появления текста результата в элементе дисплея.

        :param expected_text: ожидаемый текст результата.
        :param timeout: время ожидания в секундах, по умолчанию 45 секунд.
        :type expected_text: str
        :type timeout: int
        :return: True, если текст появился до истечения таймаута, иначе False.
        :rtype: bool
        """
        try:
            WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_text)
        )
            return True
        except:
            return False
