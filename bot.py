__author__ = 'ca1ek'

import selenium
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://hattrick.org')

username = browser.find_element_by_xpath('.//*[@id=\'txtUserName\']')
password = browser.find_element_by_xpath('.//*[@id=\'txtPassword\']')
button = browser.find_element_by_xpath('.//*[@id=\'butLogin\']')

f = open('user.txt', 'r')

login = f.read().split(" ")

username.send_keys(login[0])
password.send_keys(login[1])
button.click()