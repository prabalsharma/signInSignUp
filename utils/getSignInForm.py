import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getSignInForm(simplepopup):
    """Gets objects for sign in form"""
    bHSignIn = simplepopup.find_element_by_xpath(".//div[@class='bHSignIn']")
    simpleauth =  bHSignIn.find_element_by_xpath(".//div[@class='simpleauth']")
    signinForm = simpleauth.find_element_by_xpath(".//form[@class='signin ng-pristine ng-valid']")
    emailForm = signinForm.find_element_by_xpath(".//input[@class='email textbox']")
    passwordForm = signinForm.find_element_by_xpath(".//input[@class='password textbox']")
    return signinForm, emailForm, passwordForm