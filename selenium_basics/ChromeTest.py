from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#driver=webdriver.Edge()
#driver=webdriver.Ie()
#driver = webdriver.Firefox()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(chrome_options=options)
driver.get("https://google.com")
driver.maximize_window()
search_tb=driver.find_element(By.NAME,"q")
search_tb.send_keys("Alkesh Sakhare")
search_tb.submit()