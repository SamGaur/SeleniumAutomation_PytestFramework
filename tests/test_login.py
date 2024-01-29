import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestLogin():
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        # driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        time.sleep(5)
        print("Test Completed")

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_logout(self, test_setup):
        driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()


#### Other way more towards Selenium

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pytest
#
#
# class TestLogin:
#     @pytest.fixture(scope="session")
#     def test_setup(self):
#         global driver
#         # Uncomment the line below and provide the correct path if needed
#         driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
#         driver.implicitly_wait(5)
#         driver.maximize_window()
#         yield
#         driver.quit()
#         print("Test Completed")
#
#     def test_login(self, test_setup):
#         driver.get("https://opensource-demo.orangehrmlive.com/")
#         driver.find_element(By.NAME, "username").send_keys("Admin")
#         driver.find_element(By.NAME, "password").send_keys("admin123")
#         driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
#     def test_logout(self, test_setup):
#         # Use an explicit wait instead of time.sleep()
#         dropdown = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']"))
#         )
#         dropdown.click()
#
#         # Use an explicit wait instead of time.sleep()
#         logout_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']"))
#         )
#         logout_button.click()