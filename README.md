
Preconditions:

Ubuntu 14 Desktop version
($ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 14.04.5 LTS
Release:	14.04
Codename:	trusty
)

Python 2.7.x 
($ python --version
Python 2.7.6)
sudo apt-get install python

Install selenium:
sudo apt install python-pip
pip install --upgrade pip
sudo pip install selenium 
(selenium 3.0.2) 

Install geckodriver:
wget https://github.com/mozilla/geckodriver/releases/download/v0.13.0/geckodriver-v0.13.0-linux64.tar.gz Extract it and copy the driver to /usr/local/bin and make it executable (chmod +x geckodriver)

Firfox installed

Signed out for www.news360.com on Firefox

Run tests:

python testSignInWithEmailForm.py

Rerun the tests:

Replace all "dsfujhiwqjeoijpwqepo@gmail.com" with another valid email in formsFiller.yaml

Note: test_signInWithValidCreds - Sign-in with valid credentials is using email: signInSignUp@gmail.com and requires it to be a new account with everything empty as it looks for message "Looks pretty empty, huh?" for positive test. So if you change the value please do it with a new account with everything empty.
