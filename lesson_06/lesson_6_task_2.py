from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

input_field.send_keys("SkyPro")

button = driver.find_element(By.ID, "updatingButton")

button.click()

updated_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "updatingButton"))
    )

text = updated_button.text

print(text)

driver.quit()
