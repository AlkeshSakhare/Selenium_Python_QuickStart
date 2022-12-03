import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = "http://the-internet.herokuapp.com/javascript_alerts"
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(20)

# alert accepted with entered text
driver.find_element(By.XPATH, "//*[text()='Click for JS Prompt']").click()
alert_popup = driver.switch_to.alert
alert_popup.send_keys("Alert accepted.")
time.sleep(2)
alert_popup.accept()
time.sleep(2)


# alert dismissed
driver.find_element(By.XPATH, "//*[text()='Click for JS Prompt']").click()
alert_popup = driver.switch_to.alert
alert_popup.send_keys("Alert accepted.")
time.sleep(2)
alert_popup.dismiss()
time.sleep(2)
driver.quit()
