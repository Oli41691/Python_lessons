from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

gecko_driver_path = r"C:\Users\user\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe"

service = Service(gecko_driver_path)

driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/login")

input_field = driver.find_element(By.CSS_SELECTOR, "input[name='username']")

input_field.send_keys("tomsmith")

input_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

input_field.send_keys("SuperSecretPassword!")

button = driver.find_element(By.CLASS_NAME, "radius")

button.click()

time.sleep(2)

success_message = driver.find_element(By.CSS_SELECTOR, '.flash.success')
print(success_message.text)

driver.quit()