from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

gecko_driver_path = r"C:\Users\user\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe"

service = Service(gecko_driver_path)

driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/login")

input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

input_field.send_keys("Sky")

time.sleep(2)

input_field.clear()

input_field.send_keys("Pro")

time.sleep(2)

driver.quit()

driver.quit()