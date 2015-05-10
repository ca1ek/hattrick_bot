from selenium.selenium import selenium

__author__ = 'ca1ek'

import selenium
from selenium import webdriver

try:
    browser = webdriver.Firefox()
    browser.get('http://hattrick.org/Startpage2.aspx')
    browser.set_window_size(1280, 720)

    username = browser.find_element_by_xpath('.//*[@id=\'txtUserName\']')
    password = browser.find_element_by_xpath('.//*[@id=\'txtPassword\']')
    button = browser.find_element_by_xpath('.//*[@id=\'butLogin\']')
    try:
        f = open('user.txt', 'r')
    except IOError:
        browser.quit()
        exit()

    login = f.read().split(" ")

    username.send_keys(login[0])
    password.send_keys(login[1])
    button.click()
    # now on the main page
    my_club = browser.find_element_by_xpath('.//*[@id=\'myClubLink\']')
    my_club.click()
    # now on the my club page

    while True:
        try:
            challenges = browser.find_element_by_partial_link_text('Wyzwania')
            challenges.click()
            break
        except selenium.common.exceptions.NoSuchElementException:
            print("it works just half the time for some reason, trying again")
    # now on the challenges page
    add_to_pool = browser.find_element_by_xpath('.//*[@id=\'ctl00_ctl00_CPContent_CPSidebar_btnShowPoolSettings\']')
    add_to_pool.click()

    browser.quit()
except:
    browser.quit()
    pass
