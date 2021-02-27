from selenium.webdriver.common.by import By

from pageObjectMechanisum.selectStatepage import selectstate


class checkoutPage:
    def __init__(self, driver):
        self.driver = driver

    checkout = (By.XPATH, "//td/button[@class='btn btn-success']")
    productTitle = (By.XPATH, "//h4[@class='media-heading']/a")

    def producttitle(self):
        return self.driver.find_element(*checkoutPage.productTitle)

    def checkoutButton(self):
        self.driver.find_element(*checkoutPage.checkout).click()
        State = selectstate(self.driver)
        return State