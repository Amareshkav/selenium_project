import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLog import Loggen



class Test_001_LoginPage:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger1 = Loggen.loggen()

    def test_homePage_title(self, setUp):
        self.logger1.info("************* Test_001_Login *****************")
        self.logger1.info("************* Verifying HomePage Title *****************")
        self.driver = setUp
        self.driver.get(self.base_url)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.logger1.info("************* Home Page title is Passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger1.info("************* Home Page title is Failed *****************")
            assert False

    def test_login(self, setUp):
        self.logger1.info("************* Verifying LoginPage Title *****************")
        self.driver = setUp
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger1.info("************* Login Page title is Passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_LoginPageTitle.png")
            self.logger1.info("************* Login Page title is Failed *****************")
            assert False
