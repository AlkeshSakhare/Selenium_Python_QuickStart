from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = "https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/package-summary.html"
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(30)
driver.find_element(
    By.XPATH, "/html/body/header/nav/div[1]/div[2]/ul[1]/li[1]/a").click()

driver.switch_to.frame("packageListFrame")
driver.find_element(By.XPATH, "//a[text()='org.openqa.selenium']").click()
print("clicked org.openqa.selenium ")
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH, "//span[text()='WebDriver']").click()
print("clicked WebDriver")
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "//a[text()='Help']").click()
print("clicked HELP")
driver.switch_to.default_content()
driver.quit()
