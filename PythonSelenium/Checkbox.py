import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Your_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

check_boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(check_boxes))
for checkbox in check_boxes:
    checkbox.click()  # This is way to click all the checkboxes
    assert checkbox.is_selected()  # This is to check if the checkbox is selected or not
driver.close()