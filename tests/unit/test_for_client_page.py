import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


class TestForClientPage:

    @pytest.mark.positive
    @pytest.mark.for_client_page
    def test_deliveries_page(self):
        driver.get("https://japkostore.pl/")

        my_account_link = driver.find_element(By.XPATH, "//div[@class='pk-myaccount']")
        my_account_link.click()

        my_account_button = driver.find_element(By.XPATH, "//div[@class='tab-content']/a")
        time.sleep(2)
        my_account_button.click()

        email_input = driver.find_element(By.XPATH, "//div[@class='form-group row']/div[1]/div[1]/div[1]/div[1]/input["
                                                    "@name='email']")
        email_input.send_keys("stevenberry84@op.pl")

        password_input = driver.find_element(By.XPATH, "//div[@class='form-group row']/div[1]/div[1]/div[1]/div["
                                                       "1]/input[@name='password']")
        password_input.send_keys("g238rIJIudkjabj@19Njnja")

        login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary form-control-submit']")
        login_button.click()

        deliveries_link = driver.find_element(By.XPATH, "//*[@id='footer']/div/div/div/section/div/div/div["
                                                        "2]/div/div/div[2]/div/div/div/ul/li/a")
        deliveries_link.click()

        delivery_page_title = driver.title
        expected_delivery_title = "Dostawy w JapkoStore"

        assert delivery_page_title == expected_delivery_title, "Incorrect page title. Expected: {" \
                                                               "expected_delivery_page_title}, " \
                                                               "actual: {driver.title}"

        driver.delete_all_cookies()

    @pytest.mark.positive
    @pytest.mark.for_client_page
    def test_store_regulations_page(self):
        driver.get("https://japkostore.pl/")

        my_account_link = driver.find_element(By.XPATH, "//div[@class='pk-myaccount']")
        my_account_link.click()

        my_account_button = driver.find_element(By.XPATH, "//div[@class='tab-content']/a")
        time.sleep(2)
        my_account_button.click()

        email_input = driver.find_element(By.XPATH, "//div[@class='form-group row']/div[1]/div[1]/div[1]/div[1]/input["
                                                    "@name='email']")
        email_input.send_keys("stevenberry84@op.pl")

        password_input = driver.find_element(By.XPATH, "//div[@class='form-group row']/div[1]/div[1]/div[1]/div["
                                                       "1]/input[@name='password']")
        password_input.send_keys("g238rIJIudkjabj@19Njnja")

        login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary form-control-submit']")
        login_button.click()

        store_regulations_link = driver.find_element(By.XPATH, "//*[@id='footer']/div/div/div/section/div/div/div["
                                                               "3]/div/div/div[2]/div/div/div/ul/li[2]/a")
        store_regulations_link.click()

        store_regulations_page_title = driver.title
        expected_store_regulations_page_title = "Regulamin sklepu"

        assert store_regulations_page_title == expected_store_regulations_page_title, "Incorrect page title. " \
                                                                                      "Expected: {" \
                                                                                      "expected_store_regulations_page_title}, " \
                                                                                      "actual: {driver.title}"

        driver.delete_all_cookies()

    @pytest.mark.positive
    @pytest.mark.for_client_page
    def test_payments_page(self):
        driver.get("https://japkostore.pl/")

        my_account_link = driver.find_element(By.XPATH, "//div[@class='pk-myaccount']")
        my_account_link.click()

        my_account_button = driver.find_element(By.XPATH, "//div[@class='tab-content']/a")
        time.sleep(2)
        my_account_button.click()

        email_input = driver.find_element(By.XPATH, "//div[@class='form-group row']/div[1]/div[1]/div[1]/div[1]/input["
                                                    "@name='email']")
        email_input.send_keys("stevenberry84@op.pl")

        password_input = driver.find_element(By.XPATH, "//div[@class='form-group row']/div[1]/div[1]/div[1]/div["
                                                       "1]/input[@name='password']")
        password_input.send_keys("g238rIJIudkjabj@19Njnja")

        login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary form-control-submit']")
        login_button.click()

        payments_link = driver.find_element(By.XPATH,
                                            "//*[@id='footer']/div/div/div/section/div/div/div[3]/div/div/div["
                                            "2]/div/div/div/ul/li[3]/a")
        payments_link.click()

        payments_page_title = driver.title
        expected_payments_page_title = "Płatności"

        assert payments_page_title == expected_payments_page_title, "Incorrect page title. Expected: {" \
                                                                    "expected_payments_page_title}, " \
                                                                    "actual: {driver.title}"

        driver.delete_all_cookies()
