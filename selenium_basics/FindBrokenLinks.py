import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://www.deadlinkcity.com/"
driver = webdriver.Edge()
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(20)
linkList = driver.find_elements(By.TAG_NAME, "a")
print("No of links: ", len(linkList))
for i in linkList:
    print(i.get_attribute("href"))


links = []

for i in linkList:
    url = i.get_attribute('href')
    try:
        req = requests.get(url)
    except:
        None
    if req.status_code <= 400:
        links.append(url)

print("No of broken links: ", len(links))
print("broken links: ", links)
driver.quit()
