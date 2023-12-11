from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/CHITTARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
# we have to sort the webtable(veg/fruit name). Below are the steps -
# Click on the column header
# Collect all the veggie names -> BrowserSortedVeggieList
# Sort the veggieList -> new sorted List
# Check - BrowserSortedVeggieList == new sorted List
BrowserSortedVeggieList = []
driver.find_element(By.XPATH, "//span[normalize-space()='Veg/fruit name']").click()
veggieXpathListNew = driver.find_elements(By.XPATH, "//table[@class='table table-bordered']/tbody/tr/td[1]")
for veggie1 in veggieXpathListNew:
    BrowserSortedVeggieList.append(str(veggie1.text))
veggieList = BrowserSortedVeggieList.copy()
print("veggieList = ", veggieList)
BrowserSortedVeggieList.sort()
print("BrowserSortedVeggieList = ", BrowserSortedVeggieList)
assert veggieList == BrowserSortedVeggieList
driver.close()
