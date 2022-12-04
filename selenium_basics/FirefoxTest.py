from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService

url = "http://the-internet.herokuapp.com/login"
# prevent creating geckodriver.log file
service = FirefoxService(log_path='nul')
driver = webdriver.Firefox(service=service)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get(url)
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("username")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
driver.save_screenshot("./screenshot/image.png")
driver.quit()
