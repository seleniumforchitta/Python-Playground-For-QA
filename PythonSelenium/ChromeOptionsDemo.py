from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("--start-maximized")

# Headless Browser - When we don't want to open the browser. but want execute everything without opening browser and get the result in the end. Headless takes less RAM & it is faster to execute. Below is the code
chrome_Options.add_argument("headless")

# Certification errors can be ignored using ChromeOptions
chrome_Options.add_argument("--ignore-certificate-errors")

# How to give chrome option knowledge to driver. Like below
service_obj = Service("C:/Abhishek  _Mishra _D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_Options)


driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
print(driver.title)
