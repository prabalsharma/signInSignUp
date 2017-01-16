#import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getSigninWithEmailForm(driver):
    driver.get("https://news360.com/")
    #driver.find_element_by_xpath("/html/body/div/a[@class=`eNav startreading ng-binding']")
    startreading = driver.find_element_by_xpath("//a[@class='eNav startreading ng-binding']")
    startreading.click()
    time.sleep(3)
    #self.assertIn("Sign in with email", driver.page_source)
    signInWithEmail = driver.find_element_by_xpath("//a[@class='expand fancybox login-signin ng-binding']")
    signInWithEmail.click()
    time.sleep(3)
    #print signInWithEmail
    #print signInWithEmail.get_attribute('innerHTML')

    simplepopup = driver.find_element_by_xpath("//div[@class='simplepopup expand']")
    #print self.simplepopup.text
    #print simplepopup.get_attribute()
    return simplepopup
