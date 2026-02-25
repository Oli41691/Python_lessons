from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

def test_calc():
    driver.get(" https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.send_keys("45")

    driver.find_element_by_xpath("//*[text()='7']").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-outline-success").click()
    driver.find_element_by_xpath("//*[text()='8']").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-outline-warning").click()

    result_locator = "#screen" 
    WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, result_locator), "15"))

    # Получаем текст результата
    result_text = driver.find_element(By.CSS_SELECTOR, result_locator).text

    # Проверяем, что результат равен 15
    assert result_text == "15", f"Expected result to be 15, but got {result_text}"

    driver.quit()