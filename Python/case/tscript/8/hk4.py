from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.baidu.com")

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='chat-textarea']")))
search_box.clear()
search_box.send_keys("江西软件职业技术大学")
search_button = wait.until(EC.element_to_be_clickable((By.ID, "chat-submit-button")))
search_button.click()

link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "江西软件职业技术大学")))
link.click()

driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
department_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "学校概况")))
department_link.click()


time.sleep(5)

driver.quit()
