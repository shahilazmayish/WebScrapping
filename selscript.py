from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://www.daraz.com.bd/")

search=driver.find_element_by_class_name("search-box__input--O34g")
search.send_keys("Shirt")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "c1_t2i"))
    )
    products= main.find_elements_by_class_name("c3e8SH")
    for product in products:
        Name=product.find_element_by_class_name("c16H9d")
        Price=product.find_element_by_class_name("c13VH6")
        print(Name.text)
        print(Price.text)
    
finally:
    driver.quit()
  
