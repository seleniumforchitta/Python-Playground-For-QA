from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Your_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# Click on the shop icon
driver.find_element(By.LINK_TEXT,"Shop").click()

# Search all the blackberry products that is there in the webpage
# Now selecting the blocks of all the products available in that page
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        # Add item to cart
        product.find_element(By.XPATH, "div[2]/button").click()
        # you can give div/button as well as button is unique in the 2 Divs
        print("Item added to cart.")
# Click checkout button
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

# Click on the final checkout button
driver.find_element(By.CSS_SELECTOR, "button.btn-success").click()

# Give your delivery location - It is an auto suggestive dropdown
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")

# Wait for India to be visible in the dropdown
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
# Click on India
driver.find_element(By.LINK_TEXT, "India").click()

# Click on checkbox
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()

# Click on Purchase
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Print Success message and check
successText = driver.find_element(By.CSS_SELECTOR, "div.alert-success").text
print(successText)
assert "Success! Thank you!" in successText

# Take Screen Shot
driver.get_screenshot_as_file("screen.png")
driver.close()
