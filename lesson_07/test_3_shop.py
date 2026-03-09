import pytest
from selenium import webdriver
from Pages_07.ShopPage import ShopPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_shop(driver):
    EXPECTED_TOTAL = "$58.29"
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.login()
    shop_page.add_product("add-to-cart-sauce-labs-backpack")
    shop_page.add_product("add-to-cart-sauce-labs-bolt-t-shirt")
    shop_page.add_product("add-to-cart-sauce-labs-onesie")
    shop_page.go_to_cart()
    shop_page.proceed_checkout()
    shop_page.fill_form("Olga", "Prikhodko", "198332")
    total_text = shop_page.get_total()

    print(f"Итоговая стоимость: {total_text}")
    assert total_text == "Total: $58.29"