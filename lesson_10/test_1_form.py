import pytest
from selenium import webdriver
from FormPage import FormPage
import allure


@pytest.fixture
def driver():
    with allure.step("Запуск драйвера Chrome"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
    yield driver
    with allure.step("Закрытие драйвера Chrome"):
        driver.quit()

@allure.title("Тест заполнения и отправки формы")
@allure.description("Тест заполняет форму, отправляет её и проверяет отображение ошибок и успехов.")
@allure.feature("Форма регистрации")

@allure.title("Процесс заполнения и проверки формы")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver: 'WebDriver'):
    form_page = FormPage(driver)

    with allure.step("Открытие страницы формы"):
        form_page.open()

    with allure.step("Заполнение формы значениями по умолчанию"):
        form_page.fill_form()

    with allure.step("Отправка формы"):
        form_page.submit_form()

    with allure.step("Проверка ошибок и успеха формы"):
        form_page.check_form_submission()
