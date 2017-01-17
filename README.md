
###Preconditions:

#####1.Ubuntu 14.04.5/ 16.04.1 Desktop version
```
($ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 14.04.5 LTS
Release:	14.04
Codename:	trusty
)
```

#####2.Python 2.7.6 / 2.7.12
```
($ python --version
Python 2.7.6)
```
`sudo apt-get install python`

#####3.Install selenium:
`sudo apt install python-pip`
`pip install --upgrade pip`
`sudo pip install selenium`
(selenium 3.0.2) 

#####4.Install pyyaml:
`sudo pip install pyyaml`

#####5.Install geckodriver:
`wget https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz` Extract it and copy the driver to /usr/local/bin and make it executable (chmod +x geckodriver)
```
tar -xvzf geckodriver-v0.11.1-linux64.tar.gz
rm geckodriver-v0.11.1-linux64.tar.gz
chmod +x geckodriver
sudo cp geckodriver /usr/local/bin/
```

#####6.Firfox installed

#####7.Signed out for www.news360.com on Firefox

###Run tests:

`python testSignInWithEmailForm.py`

###Rerun the tests:

Replace all "dsfujhiwqjeoijpwqepo@gmail.com" with another valid email in formsFiller.yaml

**Note:** test_signInWithValidCreds - Sign-in with valid credentials is using email: signInSignUp@gmail.com and requires it to be a new account with everything empty as it looks for message "Looks pretty empty, huh?" for positive test. So if you change the value please do it with a new account with everything empty.
