##########
#
# title: updates.py
# author: Dan Clegg
#
##########
import argparse
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

PW = "somePassword"
USERNAME = "someUser"
parser = argparse.ArgumentParser()
parser.parse_args()

numSubnetFolders = 0

browser = webdriver.Firefox()

def Login():
    try:
        browser.get("https://qip.byu.edu/qip")
        login = browser.find_element_by_id("login")
        WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID,"password")))
        pwField = browser.find_element_by_id("password")
        login.send_keys(USERNAME)
        pwField.send_keys(PASSWORD)
        login.submit()
        element = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'My View')]")))
    except:
        e = sys.exc_info()[2]
        print( "Error: %s" % e )

def Logout():
    try:
        WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'Logout')]")))
        LogoutLink = browser.find_element_by_xpath("//div[contains(text(),'Logout')]")
        #LLDiv = LogoutLink.findElement(By.xpath(".."))
        #LLDiv.sendKeys(Keys.Enter)
        LogoutLink.sendKeys(Keys.Enter)
    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )


Login()

### Open Tree menu
try:
    myView = browser.find_element_by_xpath("//div[contains(text(),'My View')]")
    myView.click()
    myViewLinkArr = myView.find_elements_by_xpath("//div[contains(text(),'My View')]")
    myViewLinkArr[0].click()
    #browser.switchTo().defaultContent()

    iframe = browser.find_elements_by_tag_name('iframe')[0]
    browser.switch_to_frame(iframe)

    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'Personal View')]")))
    personalViewPlus = browser.find_element_by_id("Bs_Tree_0_e_myviewLabel0_openClose")
    personalViewPlus.click()

    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'Default View')]")))
    defaultViewPlus = browser.find_element_by_id("Bs_Tree_0_e_myView2_openClose")
    defaultViewPlus.click()

    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID,"Bs_Tree_0_e_ipv4SubnetLabel0_openClose")))
    ipv4SubnetsPlus = browser.find_element_by_id("Bs_Tree_0_e_ipv4SubnetLabel0_openClose")
    ipv4SubnetsPlus.click()

    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID,"Bs_Tree_0_e_Folder0_openClose")))
    folders = browser.find_element_by_id("Bs_Tree_0_e_ipv4SubnetLabel0_children")

    foldersChildren = folders.find_elements_by_xpath("//img[@src='/images/addrAlloc/plus3.gif']")
    numSubnetFolders = len(foldersChildren)

    try:
        for x in range(0,numSubnetFolders-1):
            plusImgId = "Bs_Tree_0_e_Folder" + str(x) + "_openClose"
            img = browser.find_element_by_id(plusImgId)
            browser.execute_script("arguments[0].click();",img)
    except Exception:
        pass

    folders = browser.find_element_by_id("Bs_Tree_0_e_ipv4SubnetLabel0_children")
    subnets = folders.find_elements_by_xpath("//span")
    #subnetDict = {}
    #for s in subnets:
    #    if (s.text.find("10.") > 0):
    #        subnetDict[s.text].append(s)
    subnet = subnets.find_elements_by_xpath("//*[contains(text(),'V635')]")
    print subnet

except:
    e = sys.exc_info()[0]
    #print( "Error: %s" % e )
    raise e

#print numSubnetFolders
#Logout()
