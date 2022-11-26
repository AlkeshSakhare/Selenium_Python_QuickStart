import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url="https://www.selenium.dev/selenium/web/web-form.html"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get(url)
driver.find_element(By.XPATH,"//input[@id='my-text-id']").send_keys("This is text")
driver.find_element(By.XPATH,"//input[@name='my-password']").send_keys("password")
driver.find_element(By.XPATH,"//textarea[@name='my-textarea']").send_keys("This is textarea")

disabled_element=driver.find_element(By.XPATH,"//input[@placeholder='Disabled input']")
print("text is disabled: ",disabled_element.is_enabled())

readonly_element=driver.find_element(By.XPATH,"//input[@name='my-readonly']")
print("text is readonly and is it disabled: ", readonly_element.is_enabled())

time.sleep(1)
readonly_element.send_keys("Text changed")

dropdown_element=driver.find_element(By.NAME,"my-select")
select=Select(dropdown_element)
select.select_by_visible_text("Three")

time.sleep(5)