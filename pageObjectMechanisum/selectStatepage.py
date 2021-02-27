from selenium.webdriver.common.by import By


class selectstate:
    def __init__(self, driver):
        self.driver = driver

    inputbox = (By.ID, "country")
    stateList = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    tickbox =   (By.CSS_SELECTOR, "[class*=checkbox]")
    successbtn = (By.CSS_SELECTOR, "input[class*='btn-success']")
    alert = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def textbox(self):
        return self.driver.find_element(*selectstate.inputbox)

    def Statelist(self):
        return self.driver.find_element(*selectstate.stateList)

    def Tickbox(self):
        return self.driver.find_element(*selectstate.tickbox)

    def Successbtn(self):
        return self.driver.find_element(*selectstate.successbtn)

    def Alert(self):
        return self.driver.find_element(*selectstate.alert)