from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    text_box_usernameId = "Email"
    text_box_passwordId = "Password"
    login_xpath = "//button[text() = 'Log in']"
    logout_text = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.text_box_usernameId).clear()
        self.driver.find_element(By.ID, self.text_box_usernameId).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.text_box_passwordId).clear()
        self.driver.find_element(By.ID, self.text_box_passwordId).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_text).click()




