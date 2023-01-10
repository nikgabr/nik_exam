import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime
from os import path, makedirs
import logging
from conftest import log_path, screenshot_path
url = "https://st-dev.scrdairy.com"
username =  "admin"
password =  "frodo"
farm_id = "AP5830293"

LOGGER = logging.getLogger(__name__)

class TestSenseHub:

    def setup_method(self):
        if not path.exists(screenshot_path):
            makedirs(screenshot_path)
        if not path.exists(log_path):
            makedirs(log_path)

    def test_sense_hub(self):

        browser = webdriver.Chrome()
        browser.get(url)
        browser.maximize_window()
        WebDriverWait(browser, 120).until( EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        username_element = browser.find_element(By.XPATH, "//input[@name='username']")
        username_element.send_keys(username)
        password_element = browser.find_element(By.XPATH, "//input[@name='password']")
        password_element.send_keys(password)
        farm_id_element = browser.find_element(By.XPATH, "//input[@name='farmId']")
        farm_id_element.send_keys(farm_id)
        login_button = browser.find_element(By.XPATH, "//input[@value='Login']")
        login_button.click()
        WebDriverWait(browser, 120).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@sh-id='header_search_toggleSearch']")))

        if browser.find_elements(By.XPATH, "//*[text()=' Premium Application Trial ']"):
            browser.find_element(By.XPATH, "//*[text()=' Ok, Got it ']").click()
        browser.find_element(By.XPATH, "//div[@sh-id='header_search_toggleSearch']").click() # search button

        WebDriverWait(browser, 120).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Tag / Animal / Group']")))
        browser.find_element(By.XPATH, "//input[@placeholder='Tag / Animal / Group']").send_keys("0004")
        sleep(3)
        browser.find_element(By.XPATH, "//input[@placeholder='Tag / Animal / Group']").send_keys(Keys.ENTER)
        sleep(3)
        browser.find_element(By.XPATH, "//span[@sh-id='search_result_entry_0004']").click()
        WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Heat']")))
        sleep(3)
        browser.find_element(By.XPATH, "//a[text()='Heat']").click()
        sleep(3)
        time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        browser.save_screenshot(f'{screenshot_path}{time}_my_screenshot.png')

    def teardown_method(self):
        pass
