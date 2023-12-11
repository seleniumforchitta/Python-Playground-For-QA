from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

validateText = "rama"
service_obj = Service("C:/ramARANJAN _SWAIN_D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validateText)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
# You have to switch to alert mode, if you want to (fetch the text/do any opeartion) present in Alert
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert validateText in alertText # To check substring inside a string
alert.accept()
# Now clicking on the confirm button - Use of Dismiss()
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()
driver.close()
