import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


class TestPositiveScenarios:

    @pytest.mark.login
    def test_positive_login(self):
        driver.get("https://japkostore.pl/")

        my_account_link = driver.find_element(By.XPATH, "//div[@class='pk-myaccount']")
        my_account_link.click()

        my_account_button = driver.find_element(By.XPATH, "//div[@class='tab-content']/a")
        time.sleep(2)
        my_account_button.click()

        email_input = driver.find_element(By.XPATH, "//div[@class='form-group row']/div[1]/div[1]/div[1]/div[1]/input["
                                            "@name='email']")
        email_input.send_keys("stevenberry84@op.pl")

        password_input = driver.find_element(By.XPATH, "//div[@class='form-group row']/div[1]/div[1]/div[1]/div[1]/input["
                                               "@name='password']")
        password_input.send_keys("g238rIJIudkjabj@19Njnja")

        login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary form-control-submit']")
        login_button.click()

        logout_button = driver.find_element(By.XPATH, "//a[@class='btn']")
        assert logout_button.is_displayed(), "Logout button is not displayed"
