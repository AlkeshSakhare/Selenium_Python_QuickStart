import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = "https://mail.rediff.com/cgi-bin/login.cgi"
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(30)
usernameTxB = driver.find_element(By.ID, 'login1')
signInBtn = driver.find_element(By.NAME, "proceed")
nameValue = "Alkesh"
time.sleep(2)
# highlight element with dashed border
driver.execute_script(
    "arguments[0].style.border='5px dashed red'", usernameTxB)
time.sleep(2)
# removing highlighted border
driver.execute_script("arguments[0].style.border=''", usernameTxB)
time.sleep(2)
# highlight element with solid border
driver.execute_script("arguments[0].style.border='5px solid red'", usernameTxB)
time.sleep(2)
# removing highlighted border
driver.execute_script("arguments[0].style.border=''", usernameTxB)
# enter text into element
driver.execute_script(
    "arguments[0].setAttribute('value', '" + nameValue + "')", usernameTxB)
time.sleep(2)
# click to element
driver.execute_script("arguments[0].click()", signInBtn)
time.sleep(2)
alert_1 = driver.switch_to.alert
print(alert_1.text)
alert_1.accept()
driver.quit()
