
from selenium.webdriver.common.by import By

from pageObjectMechanisum.plpPage import PLP


class homePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.ID, "exampleInputPassword1")
    tick = (By.ID, "exampleCheck1")
    gend = (By.ID, "exampleFormControlSelect1")
    status = (By.ID, "inlineRadio1")
    DOB = (By.CSS_SELECTOR, "input[name='bday']")
    button = (By.CSS_SELECTOR, "input[class='btn btn-success']")
    alert = (By.CSS_SELECTOR, "div[class*='alert-dismissible']")

    def Name(self):
        return self.driver.find_element(*homePage.name)

    def Email(self):
        return self.driver.find_element(*homePage.email)

    def Password(self):
        return self.driver.find_element(*homePage.password)

    def Tick(self):
        return self.driver.find_element(*homePage.tick)

    def Gend(self):
        return self.driver.find_element(*homePage.gend)

    def Status(self):
        return self.driver.find_element(*homePage.status)

    def Dateofbirth(self):
        return self.driver.find_element(*homePage.DOB)

    def Button(self):
        return self.driver.find_element(*homePage.button)

    def Alert(self):
        return self.driver.find_element(*homePage.alert)

    def shopButton(self):
        self.driver.find_element(*homePage.shop).click()
        plpPage=PLP(self.driver)
        return plpPage

