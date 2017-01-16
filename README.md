
Pre conditions:

Ubuntu 14 or 16 (Ubuntu 16.04.1)

Python 2.7.x (Python 2.7.12)
sudo apt-get install python]

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

python2 testSignInWithEmailForm.py

