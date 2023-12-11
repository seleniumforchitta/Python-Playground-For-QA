from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Abhishek  _Mishra _D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

element = driver.find_element(By.ID, "mousehover")
action = ActionChains(driver)
driver.execute_script("arguments[0].scrollIntoView();", element)
action.move_to_element(element).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform() # RightClick
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()