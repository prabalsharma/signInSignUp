import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getSignUpForm(simplepopup):
    """Gets objects for sign up form"""
    bHSignIn = simplepopup.find_element_by_xpath(".//div[@class='bHSignIn']")
    simpleauth =  bHSignIn.find_element_by_xpath(".//div[@class='simpleauth']")
    signinForm = simpleauth.find_element_by_xpath(".//form[@class='signin ng-pristine ng-valid']")
    gotoSingUpButton = signinForm.find_element_by_xpath(".//a[@class='signup ng-binding' and text() = 'Sign up']")
    gotoSingUpButton.click()
    time.sleep(3)
    
    signUpForm = simpleauth.find_element_by_xpath(".//form[@class='signup ng-pristine ng-valid']")
    emailForm = signUpForm.find_element_by_xpath(".//input[@class='email textbox']")
    passwordForm = signUpForm.find_element_by_xpath(".//input[@id='popuppassword']")
    confirmPass = signUpForm.find_element_by_xpath(".//input[@class='confirmpassword textbox']")
    return signUpForm, emailForm, passwordForm, confirmPass