import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """Повертає екземпляр драйвера Chrome для тестування."""
    chrome_options = Options()
    # chrome_options.add_argument("--windows-size=1920,1080")

    # Налаштування драйвера через Service
    service = Service(ChromeDriverManager().install())


    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()  # Закриває браузер після тесту


