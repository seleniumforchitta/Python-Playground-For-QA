from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service


# Chrome driver - It needs a service
service_obj = Service("C:/CHITTARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# service_obj = Service("C:/CHITTARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/geckodriver")
# driver = webdriver.Firefox(service=service_obj)
# service_obj = Service("C:/CHITTARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/msedgedriver")
# driver = webdriver.Edge(service=service_obj)
driver.maximize_window()  # To maximize the window
driver.get("https://courses.rahulshettyacademy.com/")
print(driver.title)  # Captures the Title
url1 = driver.title
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)  # Captures the Title
url2 = driver.title
print(driver.current_url)
assert url1 != url2
driver.minimize_window()  # To minimize the current window.
driver.back()  # Coming back to the previously loaded page
driver.refresh()  # Refresh the loaded page
print(driver.title, driver.current_url)

driver.close()
