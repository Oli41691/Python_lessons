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
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_submission():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR, ".first-name").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, ".last-name").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, ".address").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, ".e-mail").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, ".phone").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, ".zip-code").send_keys("")
    driver.find_element(By.CSS_SELECTOR, ".city").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, ".country").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, ".job-position").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, ".company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    driver.implicitly_wait(5)

    zipcode_field = driver.find_element(By.NAME, "zip-code")
    assert "error" in zipcode_field.get_attribute("class"), "Zip code field is not highlighted in red."

    fields = ["first-name", "last-name", "address", "email", "phone", "city", "country", "job-position", "company"]
    for field_name in fields:
            field = driver.find_element(By.NAME, field_name)
            assert "success" in field.get_attribute("class"), f"{field_name} field is not highlighted in green."
            
    print("All assertions passed.")
