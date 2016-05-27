##########
#
# title: updates.py
# author: Dan Clegg
#
##########
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

PW = "somePassword"
USERNAME = "someUser"

### Login
try:
    browser = webdriver.Firefox()
    browser.get("https://qip.byu.edu/qip")
    login = browser.find_element_by_id("login")
    pw = browser.find_element_by_id("password")
    login.send_keys(USERNAME)
    pw.send_keys(PASSWORD)
    login.submit()
    element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'My View')]")))
except:
    e = sys.exc_info()[0]
    print( "Error: %s" % e )


try:
    slfk
except:
    e = sys.exc_info()[0]
    print( "Error: %s" % e )
