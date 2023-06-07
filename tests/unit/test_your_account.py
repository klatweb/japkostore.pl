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


class TestYourAccountPage:

    @pytest.mark.positive
    @pytest.mark.your_account_page
    def test_information_page(self):
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

        information_link = driver.find_element(By.XPATH, "//div[@class='links']/a[@id='identity-link']")
        information_link.click()

        information_page_title = driver.title
        expected_information_page_title = "Dane osobiste"
        assert information_page_title == expected_information_page_title, "Incorrect page title. Expected: {" \
                                                                          "expected_information_page_title}, " \
                                                                          "actual: {driver.title}"

        driver.delete_all_cookies()

    @pytest.mark.positive
    @pytest.mark.your_account_page
    def test_addresses_page(self):
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

        addresses_link = driver.find_element(By.XPATH, "//div[@class='links']/a[@id='addresses-link']")
        addresses_link.click()

        addresses_page_title = driver.title
        expected_addresses_page_title = "Adresy"
        assert addresses_page_title == expected_addresses_page_title, "Incorrect page title. Expected: {" \
                                                                      "expected_addresses_page_title}, " \
                                                                      "actual: {driver.title}"

        driver.delete_all_cookies()

    @pytest.mark.positive
    @pytest.mark.your_account_page
    def test_order_history_page(self):
        driver.get("https://japkostore.pl/")

        my_account_link = driver.find_element(By.XPATH, "//div[@class='pk-myaccount']")
        my_account_link.click()

        my_account_button = driver.find_element(By.XPATH, "//div[@class='tab-content']/a")
        time.sleep(2)
        my_account_button.click()

        email_input = driver.find_element(By.XPATH,
                                          "//div[@class='form-group row']/div[1]/div[1]/div[1]/div[1]/input["
                                          "@name='email']")
        email_input.send_keys("stevenberry84@op.pl")

        password_input = driver.find_element(By.XPATH, "//div[@class='form-group row']/div[1]/div[1]/div[1]/div["
                                                       "1]/input[@name='password']")
        password_input.send_keys("g238rIJIudkjabj@19Njnja")

        login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary form-control-submit']")
        login_button.click()

        order_history_and_details_link = driver.find_element(By.XPATH,
                                                             "//div[@class='links']/a[@id='history-link']")
        order_history_and_details_link.click()

        order_history_and_details_page_title = driver.title
        expected_order_history_and_details_title = "Historia zamówień"
        assert order_history_and_details_page_title == expected_order_history_and_details_title, "Incorrect page title. " \
                                                                                                 "Expected: {" \
                                                                                                 "expected_order_history_and_details_title}, " \
                                                                                                 "actual: {driver.title}"

        driver.delete_all_cookies()

    @pytest.mark.positive
    @pytest.mark.your_account_page
    def test_credit_slips_page(self):
        driver.get("https://japkostore.pl/")

        my_account_link = driver.find_element(By.XPATH, "//div[@class='pk-myaccount']")
        my_account_link.click()

        my_account_button = driver.find_element(By.XPATH, "//div[@class='tab-content']/a")
        time.sleep(2)
        my_account_button.click()

        email_input = driver.find_element(By.XPATH,
                                          "//div[@class='form-group row']/div[1]/div[1]/div[1]/div[1]/input["
                                          "@name='email']")
        email_input.send_keys("stevenberry84@op.pl")

        password_input = driver.find_element(By.XPATH, "//div[@class='form-group row']/div[1]/div[1]/div[1]/div["
                                                       "1]/input[@name='password']")
        password_input.send_keys("g238rIJIudkjabj@19Njnja")

        login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary form-control-submit']")
        login_button.click()

        credit_slips_link = driver.find_element(By.XPATH,
                                                "//div[@class='links']/a[@id='order-slips-link']")
        credit_slips_link.click()

        credit_slips_page_title = driver.title
        expected_credit_slips_title = "Historia zamówień"
        assert credit_slips_page_title == expected_credit_slips_title, "Incorrect page title. " \
                                                                       "Expected: {" \
                                                                       "expected_credit_slips_title}, " \
                                                                       "actual: {driver.title}"

        driver.delete_all_cookies()
