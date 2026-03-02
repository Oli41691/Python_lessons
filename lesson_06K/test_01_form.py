import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_submission(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.NAME, "zip-code")))

    classes_zip = zip_code_element.get_attribute("class")
    assert "alert-danger" in classes_zip, "Zip-code не выделен классом alert-danger"

    fields = {
    "first-name": "First Name",
    "last-name": "Last Name",
    "address": "Address",
    "e-mail": "E-mail",
    "phone": "Phone",
    "city": "City",
    "country": "Country",
    "job-position": "Job Position",
    "company": "Company"
    }
    
    for name_attr, description in fields.items():
        element = driver.find_element(By.NAME, name_attr)
        classes = element.get_attribute("class")
        assert "alert-success" in classes, f"{description} не выделен классом alert-success"
            
    print("All assertions passed.")
