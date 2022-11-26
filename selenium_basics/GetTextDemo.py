from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url="http://the-internet.herokuapp.com/abtest"
driver.get(url)
driver.maximize_window()
element =driver.find_element(By.CSS_SELECTOR,"div[class='example'] p")
text_value=element.text
print("text value is: ",text_value)