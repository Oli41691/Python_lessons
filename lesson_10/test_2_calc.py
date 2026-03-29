import pytest
import allure
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    with allure.step("Запуск драйвера Chrome"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
    yield driver
    with allure.step("Закрытие драйвера Chrome"):
        driver.quit()

@allure.title("Тест сложения 7 + 8")
@allure.description("Тест проверяет выполнение сложения двух чисел и правильность результата.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver: 'WebDriver'):
    calc_page = CalcPage(driver)
    with allure.step("Открытие страницы калькулятора"):
        calc_page.open()

    with allure.step("Установка задержки 45 секунд"):
        calc_page.set_delay()

    with allure.step("Ввод числа 7"):
        calc_page.add_calc("7")

    with allure.step("Выбор операции сложения '+'"):
        calc_page.add_calc("+")

    with allure.step("Ввод числа 8"):
        calc_page.add_calc("8")

    with allure.step("Нажатие '=' для получения результата"):
        calc_page.add_calc("=")

    with allure.step("Проверка, что результат равен 15"):
        result_present = calc_page.wait_for_result("15")
        assert result_present, "Результат не соответствует ожидаемому значению '15'."
