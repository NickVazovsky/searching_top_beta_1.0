from selenium import webdriver  # Import selenium web driver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
def get_screen():
    browser = webdriver.Firefox('#!/bin/sh')
    browser.get('http://mospolytech.ru/')
    browser.save_screenshot('screenie.png')
    browser.quit()