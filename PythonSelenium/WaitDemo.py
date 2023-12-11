import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Your_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.implicitly_wait(5)
# Wait  until 5 seconds if object is not displayed. This steps is globally apllied to all the steps in our code
# Global Wait - If the object is displayed after 2 seconds, then it will not wait for 5 seconds.
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4) # Imp - Implicit wait will not work for find_elements. Because it waits till it return blank list
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
product_count = len(products)
assert product_count == 3
for product in products:
    product.find_element(By.XPATH, "div/button").click()
# Here product was the parent element and "add to cart" was a child
# So we did parent to child chaining here
# Now all the searched products are selected. Now we will go to cart.
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# Now we will click "Proceed to Checkout using -
"""CSS: Selecting text nodes (as with XPath’s text()) - 
in XPath you can select the <div> element with //div[text()="bananas"]. 
Question: Is there a CSS equivalent? Answer: No, it’s not possible to do the same with CSS. CSS 
selectors only work on elements, not on the text nodes they contain. """
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Now we have landed in the next page. Now we will enter the promocode "rahulshettyacademy"

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,".promoCode")))
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()  # Clicking on Apply

wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,"span.promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)  # Promo code Applied Successfully

driver.close()
