import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def signOut(driver):    
    driver.get("http://www.news360.com")
    loginSignout = driver.find_element_by_xpath("//a[@class='login-signout']")
    signoutButton = loginSignout.find_element_by_xpath(".//span[@ng-bind='::localization.landing_sign_out'and text() = 'Sign out']")
    signoutButton.click()
    time.sleep(3)