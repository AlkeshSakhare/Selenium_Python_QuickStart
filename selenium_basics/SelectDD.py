from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = "https://itera-qa.azurewebsites.net/home/automation"
driver = webdriver.Edge()
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(30)
selectdd = driver.find_element(By.XPATH, "//*[@class='custom-select']")
selectddList = Select(selectdd)
allOptions = selectddList.options  # get options
for i in allOptions:
    print(i.text)  # printing option
driver.quit()
