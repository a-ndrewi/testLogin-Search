from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
import sys
print(sys.path)
sys.path.insert(0, "D:\\AUTOMATION\\addtocart_framework\\page")
print(sys.path)
from websitePage import *


class websiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_website(self):
        websitetest = webTest(self.driver)
        websitetest.goToSite()
        websitetest.setUsername()
        websitetest.setPassword()
        websitetest.clickLogin()
        websitetest.shoppingCart()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#shopping_cart_container > a")))

        websitetest.returnToHomepage1()
        
        websitetest.firstItem()
        websitetest.addToCart()
        websitetest.returnToHomepage()
        websitetest.secondItem()
        websitetest.addToCart2()
        websitetest.test_mobile_view()

    def test_page_load(self):
        start_time = time.time()
        self.driver.get("https://www.saucedemo.com/")
        load_time = time.time() - start_time
        self.assertTrue(load_time < 5, "Page load time is too slow")  

    def tearDown(self):
        import time
        time.sleep(10)
        self.driver.quit()   

if __name__ == "__main__":
    unittest.main()