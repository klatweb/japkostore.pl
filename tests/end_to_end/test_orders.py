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
    @pytest.mark.case
    def test_iphone_case_order(self):
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
        time.sleep(1)

        iphone_category_list = driver.find_element(By.XPATH, "/html//main[@id='main-content']/div[@class='elementor "
                                                             "elementor-9020101 elementor-bc-flex-widget']/div["
                                                             "@class='elementor-inner']/div["
                                                             "@class='elementor-section-wrap']/section/div/div/div["
                                                             "1]/div/div[@class='elementor-widget-wrap']/section["
                                                             "1]//div[@class='elementor-row']/div//div["
                                                             "@class='elementor-element elementor-element-8e08a4d "
                                                             "elementor-widget elementor-widget-pkmodules']//section["
                                                             "@class='ps_categorytree relative']//div["
                                                             "@class='category-tree']/ul/li[2]/ul/li[1]/span/span/span")
        iphone_category_list.click()
        time.sleep(1)

        case_category_list = driver.find_element(By.XPATH, "/html//main[@id='main-content']/div[@class='elementor "
                                                           "elementor-9020101 elementor-bc-flex-widget']/div["
                                                           "@class='elementor-inner']/div["
                                                           "@class='elementor-section-wrap']/section/div/div/div["
                                                           "1]/div/div[@class='elementor-widget-wrap']/section["
                                                           "1]//div[@class='elementor-row']/div//div["
                                                           "@class='elementor-element elementor-element-8e08a4d "
                                                           "elementor-widget elementor-widget-pkmodules']//section["
                                                           "@class='ps_categorytree relative']//div["
                                                           "@class='category-tree']/ul/li[2]/ul/li[1]/div/ul/li["
                                                           "1]/span/span/span")
        case_category_list.click()

        iphone_case_link = driver.find_element(By.XPATH, "/html//main[@id='main-content']/div[@class='elementor "
                                                         "elementor-9020101 elementor-bc-flex-widget']/div["
                                                         "@class='elementor-inner']/div["
                                                         "@class='elementor-section-wrap']/section/div/div/div["
                                                         "1]/div/div[@class='elementor-widget-wrap']/section[1]//div["
                                                         "@class='elementor-row']/div//div[@class='elementor-element "
                                                         "elementor-element-8e08a4d elementor-widget "
                                                         "elementor-widget-pkmodules']//section["
                                                         "@class='ps_categorytree relative']//div["
                                                         "@class='category-tree']/ul/li[2]/ul/li[1]/div/ul//a["
                                                         "@href='https://japkostore.pl/31-etui']")

        iphone_case_link.click()
        time.sleep(1)

        iphone_14_pro_decoded_case = driver.find_element(By.XPATH, "/html//div[@id='js-product-list']/div/article["
                                                                   "2]/div/div/div[@class='elementor "
                                                                   "elementor-1010000 "
                                                                   "elementor-bc-flex-widget']//div["
                                                                   "@class='elementor-section-wrap']/section/div/div["
                                                                   "@class='elementor-row']/div//section//div["
                                                                   "@class='elementor-row']/div//div["
                                                                   "@class='elementor-element "
                                                                   "elementor-element-70be420 elementor-widget "
                                                                   "elementor-widget-pkminiaturetitle']//a["
                                                                   "@href='https://japkostore.pl/iphone-14-pro/93"
                                                                   "-decoded-obudowa-ochronna-do-iphone-14-pro"
                                                                   "-kompatybilna-z-magsafe-olive-8720593005832.html']")
        iphone_14_pro_decoded_case.click()

        add_to_basket_button = driver.find_element(By.XPATH, "/html//form[@id='add-to-cart-or-refresh']//button["
                                                             "@class='custom-add-to-cart']/span["
                                                             "@class='custom-button-text']")
        add_to_basket_button.click()

        time.sleep(2)
        order_button = driver.find_element(By.XPATH, "//*[@id='blockcart-modal']/div/div/div[2]/div/div[2]/div/a")
        order_button.click()

        order_final_button = driver.find_element(By.XPATH, "/html//section[@id='main']/div[@class='cart-grid "
                                                           "row']//a[@href='https://japkostore.pl/zamówienie']")
        order_final_button.click()

        next_button_address = driver.find_element(By.XPATH, "//*[@id='checkout-addresses-step']/div/div/form/div["
                                                            "2]/button")
        next_button_address.click()

        next_button_delivery = driver.find_element(By.XPATH, "//*[@id='js-delivery']/button")
        next_button_delivery.click()

        terms_and_conditions_checkbox_payments = driver.find_element(By.XPATH, "//*[@id='conditions_to_approve["
                                                                               "terms-and-conditions]']")
        terms_and_conditions_checkbox_payments.click()
        time.sleep(2)

        submit_button_summary = driver.find_element(By.XPATH, "/html/body/div[1]/section/div/section/div[1]/section["
                                                              "4]/div/div[3]/div[1]/button")
        submit_button_summary.click()

        driver.delete_all_cookies()
