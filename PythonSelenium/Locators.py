from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/ramARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_css_selector("input[name='name']:nth-child(2)").send_keys("ramaranjan Swain")
# This was the old style. Now By class is available, So we can use below.
driver.find_element(By.CSS_SELECTOR, "input[name='name']:nth-child(2)").send_keys("ramaranjan Swain")
# This above CSS is same as (//input[@name='name'])[1] - When we have multiple results in CSS we use nth-child()
driver.find_element(By.NAME, "email").send_keys("seleniumforrama@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Hanuman@123")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[value='option1']").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
# Printing the alert message below.
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(message)
# Lets do assertion
assert "Success" in message
if "Success" in message:
    print("Test case is Passed !")
# //*[contains(@class,'alert-success')]    - Xpath using RegEx
# [class*='alert-success']      -  CSSselector using RegEx
driver.close()
