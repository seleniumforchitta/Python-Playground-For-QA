import document as document
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("headless")

service_obj = Service("C:/Your_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_Options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("screen.png")