from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Abhishek  _Mishra _D_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radio_buttons = driver.find_elements(By.XPATH, "//input[@name='radioButton']")
print(len(radio_buttons))
for radiobutton in radio_buttons:
    if radiobutton.get_attribute("value") == "radio3":
        # Here we have used get_attribute to find a particular element
        radiobutton.click()  # This is way to click all the checkboxes
        assert radiobutton.is_selected()
        # This is to check if the checkbox is selected or not
radio_buttons[2].click() # We can use if we know the sequence will not change
driver.close()