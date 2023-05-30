import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://japkostore.pl/")

my_account_link = driver.find_element(By.XPATH, "//div[@class='pk-myaccount']")
my_account_link.click()

my_account_button = driver.find_element(By.XPATH, "//div[@class='tab-content']/a")
time.sleep(2)
my_account_button.click()
