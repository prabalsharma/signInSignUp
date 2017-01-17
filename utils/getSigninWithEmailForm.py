import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getSigninWithEmailForm(driver):
    """Gets object for sign in with email form popup"""
    driver.get("https://news360.com/")
    startreading = driver.find_element_by_xpath("//a[@class='eNav startreading ng-binding']")
    startreading.click()
    time.sleep(3)
    signInWithEmail = driver.find_element_by_xpath("//a[@class='expand fancybox login-signin ng-binding']")
    signInWithEmail.click()
    time.sleep(3)
    simplepopup = driver.find_element_by_xpath("//div[@class='simplepopup expand']")
    return simplepopup
