import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Abhishek  _Mishra _D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://sso.teachable.com/secure/9521/identity/login/password")

email = "demo@gmail.com"

driver.find_element(By.LINK_TEXT, "Forgot Password").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)
output = driver.find_element(By.XPATH, "//p[@class='bodySmallSemiBold']/output").text
assert email == output
driver.close()
