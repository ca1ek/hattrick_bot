from selenium.selenium import selenium

__author__ = 'ca1ek'

import selenium
from selenium import webdriver
from time import sleep
import random

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
        print("No username file")
        browser.quit()
        exit()
    print("0")
    login = f.read().split(" ")
    print("0.5")
    username.send_keys(login[0])
    print("0.55")
    password.send_keys(login[1])
    print("0.6")
    button.click() #FAIL
    print("0.7")
    # now on the main page
    print("1")
    my_club = browser.find_element_by_xpath('.//*[@id=\'myClubLink\']')
    print("2")
    my_club.click()
    print("3")
    # now on the my club page

    while True:
        try:
            challenges = browser.find_element_by_partial_link_text('Wyzwania')
            challenges.click()
            break
        except selenium.common.exceptions.NoSuchElementException:
            print("it works just half the time for some reason, trying again")
    # now on the challenges page
    try:
        pool = browser.find_element_by_xpath('.//*[@id=\'ctl00_ctl00_CPContent_CPSidebar_btnShowPoolSettings\']')
        pool.click()
        # now on challenge settings page
        button = browser.find_element_by_xpath('.//*[@id=\'ctl00_ctl00_CPContent_CPMain_btnPoolSettingsSave\']')
        button.click()
    except selenium.common.exceptions.NoSuchElementException:
        print("pool thingy not found, not a problem")
    # now on challenge settings page
    # IGNORE
    #   button = browser.find_element_by_xpath('.//*[@id=\'ctl00_ctl00_CPContent_CPMain_btnPoolSettingsSave\']')
    #   button.click()
    # IGNORE
    # now added to the pool
    while True:
        try:
            matches = browser.find_element_by_xpath('.//*[@id=\'matchesLink\']')
            matches.click()
            break
        except:
            print("Matches link not found for some reason, retrying")
    # now on matches page
    while True:
        try: # trying to find a match
            match = browser.find_element_by_xpath(
                './/*[@id=\'mainBody\']/table/tbody/tr[td[2]/img[contains(@class, \'matchFriendly\')]]/td[7]/a/img')
            match.click()
            break
        except selenium.common.exceptions.NoSuchElementException:
            print("no match found yet, retrying in about 11-13 mintues")
            sleep(600 + random.randint(60, 180))

    # now on the match selection stuffs page
    button = browser.find_element_by_xpath('.//*[@id=\'lineups\']')
    button.click()
    # lineups menu is now open
    button = browser.find_element_by_xpath('.//*[@id=\'ui-id-5\']/span')
    button.click()
    # now in saved lineups selection
    button = browser.find_element_by_xpath('.//*[@id=\'savedlineup_8240059\']')
    button.click()
    # saved lineup now select
    button = browser.find_element_by_xpath('.//*[@id=\'send\']')
    button.click()
    # lineup now set


    browser.quit()
except:
    pass
    browser.quit()
