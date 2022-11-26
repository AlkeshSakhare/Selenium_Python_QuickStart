import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")
src=driver.find_element(By.XPATH,"//div[@id='draggable']")
des=driver.find_element(By.XPATH,"//div[@id='droppable']")

actions = ActionChains(driver)
actions.move_to_element(src).drag_and_drop(src,des).perform()