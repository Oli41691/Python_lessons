import pytest
from selenium import webdriver
from Pages_07.CalcPage import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calc(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.set_delay()
    calc_page.add_calc("7")
    calc_page.add_calc("+")
    calc_page.add_calc("8")
    calc_page.add_calc("=")
    result_present = calc_page.wait_for_result("15")
    assert result_present, "The result is not correct."
