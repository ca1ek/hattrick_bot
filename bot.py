__author__ = 'ca1ek'

import selenium
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://hattrick.org')

login = browser.find_element_by_xpath('.//*[@id=\'txtUserName\']')
password = browser.find_element_by_xpath('.//*[@id=\'txtPassword\']')

login.send_keys("login")
password.send_keys("password")