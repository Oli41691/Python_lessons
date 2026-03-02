from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_calc(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    result = WebDriverWait(driver, 54).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#result"), "15")
    )
    assert result, "The result is not correct."
