import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options

url = "https://file-examples.com/index.php/sample-documents-download/sample-doc-download/"


def chrome_setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Chrome(options=options)
    return driver


def edge_setup():
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Edge(options=options)
    return driver


def firefox_setup():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    return driver


driver = chrome_setup()
#driver = edge_setup()
#driver = firefox_setup()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(url)
print(driver.title)  # Sample .doc and .docx download | File Examples Download
