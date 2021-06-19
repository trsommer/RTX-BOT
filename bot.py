from logging import log
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options

import random
import time
import webbrowser
import os
import sys
import threading
import config
import requests

def sleepNatural(rangeStart, rangeEnd):
    time.sleep(random.uniform(rangeStart, rangeEnd))

def printout(message):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S:%MS", t)
    print(current_time + ": " + message)

def sendNotification(message, url):
    payload = {
    "app_key": config.appKey,
    "app_secret": config.appSecret,
    "target_type": "app",
    "content": message,
    "content_type": "url",
    "content_extra": url
    }

    r = requests.post("https://api.pushed.co/1/push", data=payload)

def checkRTX(rtxModel):

    lastURL = ""

    delayTimes =[0.05, 0.1]

    execution_path = os.getcwd()
    driver = webdriver.Chrome(executable_path=binary_path)
    driver.get("https://discord.com/channels/758137923203235911/758140899124445230")
    ac = ActionChains(driver)

    login = None

    sleepNatural(2, 5)

    #login --------------------------------------

    try:
        emailField = driver.find_element_by_name("email")
        pwField = driver.find_element_by_name("password")

        emailField.send_keys(config.email)
        pwField.send_keys(config.password)

        sleepNatural(0.5, 1)

        button = driver.find_element_by_css_selector('[type="submit"]')

        unloaded = 0
        while unloaded == 0:
            try:
                ac.move_to_element(button).click().perform()
                unloaded = 1
            except:
                sleepNatural(0.1, 0.3)
                printout("login button failed")
    except:
        printout(f"login failed for thread rtx{rtxModel}")
        return

    printout(f"login success in thread rtx{rtxModel}")

    #loading --------------------------------------


    try:
        channels = driver.find_elements_by_css_selector('[aria-label="rules (text channel)"]')

        while len(channels) == 0:
            try:
                channels = driver.find_elements_by_css_selector('[aria-label="rules (text channel)"]')
            except:
                sleepNatural(2,3)
    except:
        sleepNatural(12, 15)
        printout("failed2")

    #navigating --------------------------------------

    driver.execute_script(f"""document.querySelector("[aria-label='{rtxModel}-europe (announcement channel)']").click()""")


    sleepNatural(2,5)

    #searching --------------------------------------

    printout(f"thread {rtxModel} checking for new drops")


    while 1 != 0:
        startTime = time.time()
        lastElements = driver.find_elements_by_xpath(f"//div[@aria-label='Messages in {rtxModel}-europe']/div[last()-1]/div/div/a")
        
        if len(lastElements) == 0:
            sleepNatural(delayTimes[0], delayTimes[1])
            continue
        
        newURl = lastElements[0].get_attribute("href")

        if(lastURL == ""):
            lastURL = newURl
            sleepNatural(delayTimes[0], delayTimes[1])

        if(newURl == lastURL):
            sleepNatural(delayTimes[0], delayTimes[1])
            continue

        urls = config.urls

        i = len(urls) - 1

        while i >= 0:
            if(urls[i] in newURl):
                webbrowser.open(newURl, new=1)
                endTime = time.time()
                printout(f"thread rtx{rtxModel} found new link: " + newURl)
                print(endTime-startTime)
                if(config.enableNotifications == 1):
                    sendNotification(f"thread rtx{rtxModel} found new link", newURl)
                lastURL = newURl
            i = i - 1


for rtxCard in config.rtxCards:
    thread = threading.Thread(target=checkRTX, args=(rtxCard,))
    thread.start()