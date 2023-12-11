import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/CHITTARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
# driver.find_element_by_name("name").send_keys("Chittaranjan Swain")
driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
print(len(countries))

for country in countries:
    print(country.text)
    if country.text == "India":
        country.click()
        break

assert driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value") == "India"
# When you update/input value dynamically through script, then we can't extract that using
# .text() method, we have to use .get_attribute("value")
driver.close()
