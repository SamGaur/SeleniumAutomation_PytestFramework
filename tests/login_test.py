import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
# driver.set_script_timeout(30)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH,   "//button[@type='submit']").click()

driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

time.sleep(5)
print("Test Completed")