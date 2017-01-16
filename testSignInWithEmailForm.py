import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils import getSigninWithEmailForm

class TestSignInWithEmailForm(unittest.TestCase):

    # def setUp(self):
    #     self.driver = webdriver.Firefox()

    def test_signInWithInvalidCreds(self):
        #driver = self.driver
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)


        #simplepopup = self.simplepopup
        #print self.simplepopup.text
        bHSignIn = simplepopup.find_element_by_xpath(".//div[@class='bHSignIn']")
        #self.assertIn("Invalid login or password", bHSignIn.find_element_by_class_name('error-message message ng-binding'))
        #self.assertIn("Invalid login or password", simplepopup.text)
        simpleauth =  bHSignIn.find_element_by_xpath(".//div[@class='simpleauth']")
        signinForm = simpleauth.find_element_by_xpath(".//form[@class='signin ng-pristine ng-valid']")
        emailForm = signinForm.find_element_by_xpath(".//input[@class='email textbox']")
        passwordForm = signinForm.find_element_by_xpath(".//input[@class='password textbox']")
        #print simplepopup.text
        #print "*******************************************"
        emailForm.send_keys("YourUsername@gmail.com")
        passwordForm.send_keys("Pa55worD")
        time.sleep(3)
        signInButton = signinForm.find_element_by_xpath(".//button[@class='green-button ladda-button signin-button ng-binding' and text() = 'Sign in']")
        signInButton.click()
        time.sleep(3)
        #self.assertIn("Invalid login or password", simplepopup.text)
        print simplepopup.text
        assert "Invalid login or password" in simplepopup.text
        driver.quit()

    def test_signInWithInvalidEmailFormat(self):
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)


        #simplepopup = self.simplepopup
        #print self.simplepopup.text
        bHSignIn = simplepopup.find_element_by_xpath(".//div[@class='bHSignIn']")
        #self.assertIn("Invalid login or password", bHSignIn.find_element_by_class_name('error-message message ng-binding'))
        #self.assertIn("Invalid login or password", simplepopup.text)
        simpleauth =  bHSignIn.find_element_by_xpath(".//div[@class='simpleauth']")
        signinForm = simpleauth.find_element_by_xpath(".//form[@class='signin ng-pristine ng-valid']")
        emailForm = signinForm.find_element_by_xpath(".//input[@class='email textbox']")
        passwordForm = signinForm.find_element_by_xpath(".//input[@class='password textbox']")
        #print simplepopup.text
        #print "*******************************************"        
        emailForm.send_keys("YourUsername")
        passwordForm.send_keys("Pa55worD")
        time.sleep(3)
        signInButton = signinForm.find_element_by_xpath(".//button[@class='green-button ladda-button signin-button ng-binding' and text() = 'Sign in']")
        signInButton.click()
        time.sleep(3)
        #self.assertIn("Invalid login or password", simplepopup.text)
        print simplepopup.text
        assert "This value should be a valid email." in simplepopup.text
        driver.quit()

    def test_signInWithValidCreds(self):
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)


        #simplepopup = self.simplepopup
        #print self.simplepopup.text
        bHSignIn = simplepopup.find_element_by_xpath(".//div[@class='bHSignIn']")
        #self.assertIn("Invalid login or password", bHSignIn.find_element_by_class_name('error-message message ng-binding'))
        #self.assertIn("Invalid login or password", simplepopup.text)
        simpleauth =  bHSignIn.find_element_by_xpath(".//div[@class='simpleauth']")
        signinForm = simpleauth.find_element_by_xpath(".//form[@class='signin ng-pristine ng-valid']")
        emailForm = signinForm.find_element_by_xpath(".//input[@class='email textbox']")
        passwordForm = signinForm.find_element_by_xpath(".//input[@class='password textbox']")
        #print simplepopup.text
        #print "*******************************************"        
        emailForm.send_keys("signInSignUp@gmail.com")
        passwordForm.send_keys("signInSignUp")
        time.sleep(3)
        signInButton = signinForm.find_element_by_xpath(".//button[@class='green-button ladda-button signin-button ng-binding' and text() = 'Sign in']")
        signInButton.click()
        time.sleep(3)
        #print signInButton.text
        #print driver.page_source
        # #self.assertIn("Invalid login or password", simplepopup.text)
        # print simplepopup.text
        assert "Looks pretty empty, huh?" in driver.page_source

        """Sign Out"""
        driver.get("http://www.news360.com")
        loginSignout = driver.find_element_by_xpath("//a[@class='login-signout']")
        signoutButton = loginSignout.find_element_by_xpath(".//span[@ng-bind='::localization.landing_sign_out'and text() = 'Sign out']")
        signoutButton.click()
        time.sleep(3)

        driver.quit()

    def test_signUpWithValidCreds(self):
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

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
        emailForm.send_keys("dsfghfewrthyjkluy@gmail.com")
        passwordForm.send_keys("signInSignUp")
        confirmPass.send_keys("signInSignUp")
        time.sleep(3)
        singUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        singUpButton.click()
        time.sleep(3)
        assert "Welcome to News360" in driver.page_source

        """Sign Out"""
        driver.get("http://www.news360.com")
        loginSignout = driver.find_element_by_xpath("//a[@class='login-signout']")
        signoutButton = loginSignout.find_element_by_xpath(".//span[@ng-bind='::localization.landing_sign_out'and text() = 'Sign out']")
        signoutButton.click()
        time.sleep(3)

        driver.quit()

    def test_signUpWithInvalidEmail(self):
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

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
        emailForm.send_keys("dsfghfewrthyjkluy")
        passwordForm.send_keys("signInSignUp")
        confirmPass.send_keys("signInSignUp")
        time.sleep(3)
        singUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        singUpButton.click()
        time.sleep(3)
        assert "This value should be a valid email." in simplepopup.text

        driver.quit()

    def test_signUpWithNoConfirmPass(self):
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

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
        emailForm.send_keys("dsfghfewrthyjkluy@gmail.com")
        passwordForm.send_keys("signInSignUp")
        time.sleep(3)
        singUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        singUpButton.click()
        time.sleep(3)
        assert "This value is required." in simplepopup.text

        driver.quit()

    def test_signUpWithDiffConfirmPass(self):
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

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
        emailForm.send_keys("dsfghfewrthyjkluy@gmail.com")
        passwordForm.send_keys("signInSignUp")
        confirmPass.send_keys("different")
        time.sleep(3)
        singUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        singUpButton.click()
        time.sleep(3)
        assert "This value should be the same." in simplepopup.text

        driver.quit()

    def test_signUpWithPassLessThanSix(self):
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

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
        emailForm.send_keys("dsfghfewrthyjkluy@gmail.com")
        passwordForm.send_keys("123")
        confirmPass.send_keys("123")
        time.sleep(3)
        singUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        singUpButton.click()
        time.sleep(3)
        assert "This value is too short. It should have 6 characters or more." in simplepopup.text

        driver.quit()

    def test_signUpWithAllWrongFormat(self):
        driver = webdriver.Firefox()
        simplepopup = getSigninWithEmailForm.getSigninWithEmailForm(driver)

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
        emailForm.send_keys("dsfghfewrthyjkluy")
        passwordForm.send_keys("123")
        confirmPass.send_keys("1")
        time.sleep(3)
        singUpButton = signUpForm.find_element_by_xpath(".//button[@class='green-button ladda-button signup-button ng-binding' and text() = 'Sign up']")
        singUpButton.click()
        time.sleep(3)
        assert "This value should be a valid email."and \
        "This value is too short. It should have 6 characters or more."and \
        "This value should be the same." in simplepopup.text

        driver.quit()
        #simplepopup.find_element_by_class_name('error-message message ng-binding'))
        #username = signInWithEmail.find_element_by_class_name("email textbox")
        # username = driver.find_element_by_xpath("//input[@class='email textbox']")
        # print username
        # username = signInWithEmail.find_element_by_xpath(".//input[@class='email textbox']")
        # #print username.get_attribute('innerHTML')
        # print username
        # password = signInWithEmail.find_element_by_xpath("//input[@class='password textbox']")
        #username.send_keys("YourUsername")
        # password.send_keys("Pa55worD")
        # signIn = signInWithEmail.find_element_by_xpath("//button[@class='green-button ladda-button signin-button ng-binding' and text() = 'Sign in']")
        # signIn.click()
        # time.sleep(5)
        #self.assertIn("Sign in with email", driver.page_source)
        # self.assertIn("Python", driver.title)
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source

    # def tearDown(self):
    #     self.driver.quit()

#if __name__ == "__main__":
    #unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestSignInWithEmailForm)
unittest.TextTestRunner(verbosity=2).run(suite)