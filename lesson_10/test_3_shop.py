import pytest
import allure
from selenium import webdriver
from ShopPage import ShopPage


@pytest.fixture
def driver():
    """
    Фикстура открытия браузера и его закрытия.
    """
    with allure.step("Запуск браузера"):
        driver = webdriver.Firefox()
    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()

@allure.title("Процесс покупки товара в интернет-магазине")
@allure.description("Тест авторизации, добавления товара, оформления заказа и проверки общей суммы.")
@allure.feature("Покупка товаров")
@allure.title("Проверка полного сценария покупки")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_purchase_flow(driver: 'WebDriver'):
    EXPECTED_TOTAL = "$58.29"
    shop_page = ShopPage(driver)

    with allure.step("Открытие страницы магазина"):
        shop_page.open()

    with allure.step("Авторизация пользователя"):
        shop_page.login()

    with allure.step("Добавление товаров в корзину"):
        shop_page.add_product("add-to-cart-sauce-labs-backpack")
        shop_page.add_product("add-to-cart-sauce-labs-bolt-t-shirt")
        shop_page.add_product("add-to-cart-sauce-labs-onesie")

    with allure.step("Переход в корзину"):
        shop_page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        shop_page.proceed_checkout()

    with allure.step("Заполнение формы заказа"):
        shop_page.fill_form("Olga", "Prikhodko", "198332")

    with allure.step("Получение итоговой суммы заказа"):
        total_text = shop_page.get_total()

    @allure.step("Проверка итоговой суммы")
    def get_total(self) -> str:
        """
        Возвращает текст итоговой суммы заказа.
        
        :return: текст с суммой.
        :rtype: str
        """
        total_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.total_label)).text
        return total_text

    print(f"Итоговая стоимость: {total_text}")
    assert total_text == "Total: $58.29"
