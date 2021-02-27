from selenium.webdriver.common.by import By

from pageObjectMechanisum.checkoutPage import checkoutPage


class PLP:
    def __init__(self, driver):
        self.driver = driver

    # products = (By.XPATH, "//app-card-list/app-card/div")

    checkout = (By.XPATH, "//div/ul/li/a")

    # def Products(self):
    #     return self.driver.find_element(*PLP.products)

    def checkoutplp(self):
        self.driver.find_element(*PLP.checkout).click()
        checkout = checkoutPage(self.driver)
        return checkout
