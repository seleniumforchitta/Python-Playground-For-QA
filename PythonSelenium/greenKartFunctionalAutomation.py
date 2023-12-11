import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

Veggies_Selected = []  # Declaring the empty string to fetch the Product Names from search
Veggies_inCart = []  # Declaring the empty string to fetch the Product Names in Cart
service_obj = Service("C:/Your_Drive/STUDY/Software/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
product_count = len(products)
assert product_count == 3
# We will use products as a parent xpath & will find-out veg name & add-to-cart from products xpath
for product in products:
    Veggies_Selected.append(product.find_element(By.XPATH, "h4").text)
    # product is already an element to go to product name we just have to give the extra path from product
    # And we are adding each element to the list - Veggies_Selected
    product.find_element(By.XPATH, "div/button").click()
print(Veggies_Selected)

# Now all the searched products are selected. Now we will go to cart.
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# Now we will click "Proceed to Checkout using -
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Now we have landed in the next page. Now we will enter the promocode "rahulshettyacademy"
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,".promoCode")))

# Now before giving the promocode, we will fetch all the selected products present in cart with the one's we selected
# before.
veggies = driver.find_elements(By.XPATH, "//p[@class='product-name']")
for veg in veggies:
    Veggies_inCart.append(veg.text)
print(Veggies_inCart)

# Now we will compare the products selected with products in Cart
assert Veggies_Selected == Veggies_inCart
print("Veggies_Selected is equal to Veggies_inCart !")

# Verify if Price decreases on discount. This code is to check Discounted Price < Actual Price. So get the Discounted price before applying promo code
originalAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()  # Clicking on Apply

wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,"span.promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)  # Promo code Applied Successfully

# This code is to check Discounted Price after applying promo code and comapring with original amount
discountedAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
assert float(discountedAmount) < float(originalAmount)
print("Discounted price - ", float(discountedAmount), " is less than the original amount - ", float(originalAmount))

# Verify if sum of the price of products in checkout page matches with the Total Amount
amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")
# Here we have used parent to child traversal to get the last column data in the web table
SumTotal = 0.0
for amount in amounts:
    SumTotal = SumTotal+float(amount.text)

totalAmount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
assert float(totalAmount) == SumTotal
print("Sum of the price of products in checkout page - ", SumTotal, " is equal to the total Amount - ", float(totalAmount))

driver.close()
