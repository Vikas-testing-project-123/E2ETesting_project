import time
from pageObjectMechanisum.homePage import homePage
from utilities.Baseclass import Baseclass


class TestOne(Baseclass):
    def test_e2e(self):
        log = self.getlogger()
        # home page
        home = homePage(self.driver)
        plpPage = home.shopButton()
        log.info("Shop button is clicked")

        #PLP Page start
        products = self.driver.find_elements_by_xpath("//app-card-list/app-card/div")

        for product in products:
            productTitle = product.find_element_by_xpath("div/h4")
            ptitle = productTitle.text
            log.info("Product titles:" + ptitle)
            if ptitle == "Blackberry":
                product.find_element_by_xpath("div[@class='card-footer']/button").click()
                break

        checkout = plpPage.checkoutplp()

        # Checkout page

        title = checkout.producttitle().text
        assert title == "Blackberry"
        State = checkout.checkoutButton()

        # selectStatepage

        State.textbox().send_keys("Ind")

        self.waitbylinktest("India")
        countries = self.driver.find_elements_by_xpath("//div[@class='suggestions']/ul/li/a")
        print(len(countries))
        for country in countries:
            if country.text == "India":
                country.click()
                break

        time.sleep(2)
        State.Tickbox().click()
        log.info("Checkbox is clicked")

        time.sleep(2)
        State.Successbtn().click()
        log.info("Success button is clicked")
        Alert_text = State.Alert().text
        assert "Success" in Alert_text
