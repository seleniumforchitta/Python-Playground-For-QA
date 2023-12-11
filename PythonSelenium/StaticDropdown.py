from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Abhishek  _Mishra _D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# driver.find_element_by_name("name").send_keys("Abhishek  Mishra ")
driver.find_element(By.CSS_SELECTOR, "input[name='name']:nth-child(2)").send_keys("Abhishek  Mishra ")
driver.find_element(By.NAME, "email").send_keys("seleniumforrama@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Hanuman@123")
# select class provide the methods to handle the options in dropdown.
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)
# dropdown.select_by_value("") - We can't use this as there is no Value tag
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()  # Submit
# Printing the alert message below.
print(driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text)
driver.close()
