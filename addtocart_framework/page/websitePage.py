from selenium.webdriver.common.by import By
from assertpy import assert_that, soft_assertions
from selenium import webdriver

class webTest:
    def __init__(self, driver):
        self.driver = driver

    def goToSite(self):
        self.driver.get("https://www.saucedemo.com")

    def setUsername(self):
        username = self.driver.find_element(By.ID, "user-name")
        username.clear()
        username.send_keys("performance_glitch_user")

    def setPassword(self):
        password = self.driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("secret_sauce")

    def clickLogin(self):
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()

    def shoppingCart(self):
        cartButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        cartButton.click()

    def returnToHomepage1(self):
        returntohomepage1 = self.driver.find_element(By.ID, "continue-shopping")
        returntohomepage1.click()
                                         
    def firstItem(self):
        firstitem1 = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
        firstitem1.click()

    def addToCart(self):    
        addtocart = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart")
        addtocart.click()

    def returnToHomepage(self):
        returntohomepage = self.driver.find_element(By.ID, "back-to-products")
        returntohomepage.click()

    def secondItem(self):
        seconditem = self.driver.find_element(By.CSS_SELECTOR, "#item_5_title_link > div")
        seconditem.click()

    def addToCart2(self):
        addtocart2 = self.driver.find_element(By.ID, "add-to-cart")
        addtocart2.click()

    def test_mobile_view(self):
        testmobileview = self.driver.set_window_size(375, 667)

    