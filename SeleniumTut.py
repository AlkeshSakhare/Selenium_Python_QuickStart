# install python packages
# pip install -U selenium
# pip install -U pytest
# pip install -U openpyxl
# pip install -U requests
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

# Launch browsers
driver = webdriver.Chrome()
driver = webdriver.Edge()
driver = webdriver.Ie()
driver = webdriver.Firefox()

# Chrome options

options = webdriver.ChromeOptions()
# Prevent closing chrome browsers
options.add_experimental_option("detach", True)
# Prevent console logging devtools
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Navigate to URL
url = "https://google.com"
driver.get(url)

# Maximize window
driver.maximize_window()

# Locate Element

driver.find_element(By.NAME, 'q')

# Implicit Wait
driver.implicitly_wait(20)

# Explicit Wait

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, 'someid')))


# Actions

actions = ActionChains(driver)
element = driver.find_element(By.ID, "q")
actions.click(element)

# Select

select = Select(element)
select.select_by_index(1)
select.select_by_visible_text("Text")
select.select_by_value("value")

# Switch window
driver.switch_to.window("WindowName")

# Switch to alert
alert_ob = driver.switch_to.alert
alert_ob.accept()  # accept
alert_ob.dismiss()  # dismiss
alert_ob.send_keys("This will be enterd to prompt")  # enter text in prompt
alert_msg = alert_ob.text()  # get text from alert

# Get Page Source
driver.page_source

# Navigations
driver.forward()
driver.back()

# TakeScreenshots
driver.save_screenshot("./screenshot/image.png")

# Get inner Text
element.text

# Thread.sleep

time.sleep(2)  # no. should be in seconds

# download mime type: https://www.sitepoint.com/mime-types-complete-list/
