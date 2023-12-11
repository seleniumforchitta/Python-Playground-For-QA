import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/ramARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID, "fromCity").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='From']").send_keys("del")
time.sleep(5) # Implicit wait doesn't work for find_elements
# Here we are searching in the FROM, with "del" and fetching all suggestions coming below it
cities = driver.find_elements(By.CSS_SELECTOR, "p[class*='blackText']")
# Lets store it in a list of webelements
# In the above syntax "blackText" is common across all the cities coming under suggestion
# Now below is the way to find the count
print("Total Count of cities", len(cities))
for city in cities:
    print(city.text)
    if city.text == "Agra, India":
        city.click()
        break # Use break coz if it found the Del Rio in 3rd iteration then rest iteration will not be done
# Now we will select TO option
driver.find_element(By.CSS_SELECTOR, "input[placeholder='To']").send_keys("mum")
time.sleep(5)
cities = driver.find_elements(By.CSS_SELECTOR, "p[class*='blackText']")
for city in cities:
    print(city.text)
    if city.text == "Mumbai, India":
        city.click()
        break
driver.close()
