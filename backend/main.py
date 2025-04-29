from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Remote(
    command_executor=os.getenv("SELENIUM_URL", "http://selenium:4444/wd/hub"),
    options=options
)

driver.get("https://www.google.com/")
print(driver.title)
driver.quit()
