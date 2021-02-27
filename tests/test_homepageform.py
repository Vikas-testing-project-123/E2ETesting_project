import pytest
from TestData.homepageformdata import homepagedata
from pageObjectMechanisum.homePage import homePage
from utilities.Baseclass import Baseclass


class Testhomepageform(Baseclass):
    def test_homepage(self, getdata):
        log = self.getlogger()
        home = homePage(self.driver)

        #home.Name().send_keys(getdata[0])# for tuple data type

        home.Name().send_keys(getdata["Firstname"])
        log.info("First name is entered")

        home.Email().send_keys(getdata["Email"])
        log.info("Email is entered")

        home.Password().send_keys(getdata["Password"])
        log.info("The password is entered")

        home.Tick().click()
        self.selectvisibletext("Male")
        home.Status().click()
        home.Dateofbirth().send_keys("20-05-1998")
        home.Button().click()
        alert = home.Alert().text
        assert "success" in alert
        self.driver.refresh()

    #@pytest.fixture(params=[("Vikash", "Email", "Test12345"),("Archa" ,"arc", "Test12345")])#Send data in tuple datatype
    #@pytest.fixture(params=[{"Firstname":"Vikash", "Email":"Email", "Password":"Test12345"},{"Firstname":"Archa" ,"Email":"arc", "Password":"Test12345"}])

    @pytest.fixture(params=homepagedata.test_homepage_data)
    def getdata(self, request):
        return request.param
