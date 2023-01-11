import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver_services = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_services)
    yield driver
    driver.quit()
