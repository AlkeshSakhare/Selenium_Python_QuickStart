import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

path = os.getcwd()
url = "https://file-examples.com/index.php/sample-documents-download/sample-doc-download/"


def chrome_setup():
    prefs = {"download.default_directory": path}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    return driver


def edge_setup():
    prefs = {"download.default_directory": path}
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Edge(options=options)
    return driver


def firefox_setup():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", path)
    profile.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "application/msword")
    driver = webdriver.Firefox(options=profile)
    return driver


#driver = chrome_setup()
#driver = edge_setup()
driver = firefox_setup()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(url)
driver.find_element(By.XPATH, "//a[text()='Download sample DOC file']").click()
time.sleep(2)

driver.switch_to.frame("aswift_3")
driver.switch_to.frame("ad_iframe")
close_btn = driver.find_element(By.XPATH, "//span[text()='Close']")
close_btn.click()
time.sleep(10)

print("File downloaded")
