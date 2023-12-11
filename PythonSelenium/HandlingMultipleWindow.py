from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/ramARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()

window_list = driver.window_handles
# window_handle method will get all the window IDs opened by the driver

driver.switch_to.window(window_list[1])  # Pass the window ID of the child window
assert "New Window" == driver.find_element(By.TAG_NAME, "h3").text
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

driver.switch_to.window(window_list[0])  # Switching back to parent window
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
