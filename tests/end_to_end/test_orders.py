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


class TestOrders:

    @pytest.mark.positive
    @pytest.mark.menu_page
    @pytest.mark.iphone
    def test_orders(self):
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

        menu_link = driver.find_element(By.XPATH, "/html//header[@id='header']/div["
                                                  "@class='mobile-header-wrapper']/div[@class='elementor "
                                                  "elementor-43010000 elementor-bc-flex-widget']/div["
                                                  "@class='elementor-inner']/div/section[2]/div/div["
                                                  "@class='elementor-row']/div//div[@class='elementor-element "
                                                  "elementor-element-42fc8996 elementor-widget "
                                                  "elementor-widget-pkmenu']//span[.='Menu']")

        menu_link.click()

        main_page_link = driver.find_element(By.XPATH, "//ul[@id='top-menu']//a["
                                                       "@href='https://japkostore.pl/2-strona-glowna']/span")

        main_page_link.click()





        driver.delete_all_cookies()
