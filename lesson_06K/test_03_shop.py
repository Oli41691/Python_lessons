from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

EXPECTED_TOTAL = "$58.29"

driver = webdriver.Firefox()

def test_shop():
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.implicitly_wait(5)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "shopping_cart_link").click()
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'first-name'))).send_keys("Olga")
    driver.find_element(By.ID, "last-name").send_keys("Prikhodko")
    driver.find_element(By.ID, "postal-code").send_keys("198332")
    driver.find_element(By.ID, "continue").click()

    total_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label'))
    ).text

    print(f"Итоговая стоимость: {total_text}")

    assert total_text == f"Total: {EXPECTED_TOTAL}", f"Ожидалось {EXPECTED_TOTAL}, но получено {total_text}"
    
    driver.quit()
    