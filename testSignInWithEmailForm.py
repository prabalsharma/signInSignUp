import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils import getSigninWithEmailForm
from utils import formsFiller
from utils import getSignInForm
from utils import getSignUpForm
from utils import signOut

class TestSignInWithEmailForm(unittest.TestCase):
    """Class to test sign-in with email"""

    formValues = formsFiller.formsFiller()

    def test_signInWithInvalidCreds(self):
        """Sign-in with invalid credentials"""
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

        signinForm, emailForm, passwordForm = getSignInForm.getSignInForm(simplepopup)

        emailForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signInWithInvalidCreds"]["email"])
        passwordForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signInWithInvalidCreds"]["password"])
        time.sleep(3)
        signInButton = signinForm.find_element_by_xpath(".//button[@class='green-button ladda-button signin-button ng-binding' and text() = 'Sign in']")
        signInButton.click()
        time.sleep(3)
        assert "Invalid login or password" in simplepopup.text
        driver.quit()

    def test_signInWithInvalidEmailFormat(self):
        """Sign-in with invalid email format"""
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

        signinForm, emailForm, passwordForm = getSignInForm.getSignInForm(simplepopup)

        emailForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signInWithInvalidEmailFormat"]["email"])
        passwordForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signInWithInvalidEmailFormat"]["password"])
        time.sleep(3)
        signInButton = signinForm.find_element_by_xpath(".//button[@class='green-button ladda-button signin-button ng-binding' and text() = 'Sign in']")
        signInButton.click()
        time.sleep(3)
        assert "This value should be a valid email." in simplepopup.text
        driver.quit()

    def test_signInWithValidCreds(self):
        """Sign-in with valid credentials"""
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

        signinForm, emailForm, passwordForm = getSignInForm.getSignInForm(simplepopup)

        emailForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signInWithValidCreds"]["email"])
        passwordForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signInWithValidCreds"]["password"])
        time.sleep(3)
        signInButton = signinForm.find_element_by_xpath(".//button[@class='green-button ladda-button signin-button ng-binding' and text() = 'Sign in']")
        signInButton.click()
        time.sleep(3)
        assert "Looks pretty empty, huh?" in driver.page_source

        signOut.signOut(driver)

        driver.quit()

    def test_signUpWithValidCreds(self):
        """Sign-up with valid credentials"""
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

        signUpForm, emailForm, passwordForm, confirmPass = getSignUpForm.getSignUpForm(simplepopup)

        emailForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithValidCreds"]["email"])
        passwordForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithValidCreds"]["password"])
        confirmPass.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithValidCreds"]["confirmPass"])
        time.sleep(3)
        signUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        signUpButton.click()
        time.sleep(3)
        assert "Welcome to News360" in driver.page_source

        signOut.signOut(driver)

        driver.quit()

    def test_signUpWithInvalidEmail(self):
        """Sign-up with invalid email format"""
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

        signUpForm, emailForm, passwordForm, confirmPass = getSignUpForm.getSignUpForm(simplepopup)

        emailForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithInvalidEmail"]["email"])
        passwordForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithInvalidEmail"]["password"])
        confirmPass.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithInvalidEmail"]["confirmPass"])
        time.sleep(3)
        signUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        signUpButton.click()
        time.sleep(3)
        assert "This value should be a valid email." in simplepopup.text

        driver.quit()

    def test_signUpWithNoConfirmPass(self):
        """Sign-up without filling confirm password field"""
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

        signUpForm, emailForm, passwordForm, confirmPass = getSignUpForm.getSignUpForm(simplepopup)

        emailForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithNoConfirmPass"]["email"])
        passwordForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithNoConfirmPass"]["password"])
        time.sleep(3)
        signUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        signUpButton.click()
        time.sleep(3)
        assert "This value is required." in simplepopup.text

        driver.quit()

    def test_signUpWithDiffConfirmPass(self):
        """Sign-up when password does not match confirm password value"""
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

        signUpForm, emailForm, passwordForm, confirmPass = getSignUpForm.getSignUpForm(simplepopup)

        emailForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithDiffConfirmPass"]["email"])
        passwordForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithDiffConfirmPass"]["password"])
        confirmPass.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithDiffConfirmPass"]["confirmPass"])
        time.sleep(3)
        signUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        signUpButton.click()
        time.sleep(3)
        assert "This value should be the same." in simplepopup.text

        driver.quit()

    def test_signUpWithPassLessThanSix(self):
        """Sign-up with password length less than six characters"""
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

        signUpForm, emailForm, passwordForm, confirmPass = getSignUpForm.getSignUpForm(simplepopup)

        emailForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithPassLessThanSix"]["email"])
        passwordForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithPassLessThanSix"]["password"])
        confirmPass.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithPassLessThanSix"]["confirmPass"])
        time.sleep(3)
        signUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        signUpButton.click()
        time.sleep(3)
        assert "This value is too short. It should have 6 characters or more." in simplepopup.text

        driver.quit()

    def test_signUpWithAllWrongFormat(self):
        """Sign-up by filling all forms with invalid format values"""
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

        signUpForm, emailForm, passwordForm, confirmPass = getSignUpForm.getSignUpForm(simplepopup)

        emailForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithAllWrongFormat"]["email"])
        passwordForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithAllWrongFormat"]["password"])
        confirmPass.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithAllWrongFormat"]["confirmPass"])
        time.sleep(3)
        signUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        signUpButton.click()
        time.sleep(3)
        assert "This value should be a valid email."and \
        "This value is too short. It should have 6 characters or more."and \
        "This value should be the same." in simplepopup.text

        driver.quit()

    def test_signUpWithExistingAccount(self):
        """Sign-up with existing account"""
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

        signUpForm, emailForm, passwordForm, confirmPass = getSignUpForm.getSignUpForm(simplepopup)

        emailForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithExistingAccount"]["email"])
        passwordForm.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithExistingAccount"]["password"])
        confirmPass.send_keys("%s"%TestSignInWithEmailForm.formValues["test_signUpWithExistingAccount"]["confirmPass"])
        time.sleep(3)
        signUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        signUpButton.click()
        time.sleep(3)
        assert "Invalid login or password" in simplepopup.text

        driver.quit()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSignInWithEmailForm)
unittest.TextTestRunner(verbosity=2).run(suite)