from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window
driver.get_screenshot_as_file("screenshot/before.png")
driver.find_element(By.NAME,"q").send_keys("Alkesh Sakhare")
driver.find_element(By.NAME,"q").submit()
driver.save_screenshot("screenshot/afterented.png")