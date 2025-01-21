import pytest
from selenium import webdriver
from POM_Class.Login import loginPage

class TestLogin:
    def test_login(self):
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(5)
        driver.maximize_window()

        lp=loginPage(driver)

        lp.setUserName("shrutimahajan1626@gmail.com")
        lp.setUserPasswd("shruti")
        lp.click_button()

        act_title=driver.title
        assert act_title=="My account - My Shop"

