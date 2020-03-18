from selenium import webdriver
import os
import argparse
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def argument_parse():
    parser = argparse.ArgumentParser(description='Download Folder!')
    parser.add_argument("location", type=str, nargs='+')
    args = parser.parse_args()
    location = args.location
    return location


def read_file():
    data = open(file='data.txt')
    return data.readlines()


def wait(browser):
    delay = 10  # seconds
    try:
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'pdfViewer')))
    except TimeoutException as e:
        print(e)


def selenium():
    directory = argument_parse()[0]
    if not os.path.isdir(directory):
        os.mkdir(directory)
    lines = read_file()
    for line in lines:
        print('Started working on {}'.format(line))
        options = webdriver.ChromeOptions()
        path = os.path.abspath(os.getcwd()) + '\\{}'.format(directory)
        pref = {"download.default_directory": path}
        options.add_experimental_option("prefs", pref)
        browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        browser.get(url='https://app.box.com/file/635632167612')
        username = browser.find_element_by_id("login-email")
        username.send_keys("ksantana3@gmail.com")

        browser.find_element_by_id("login-submit").click()
        password = browser.find_element_by_id("password-login")
        password.send_keys("Password123!@#")
        browser.find_element_by_id("login-submit-password").click()
        browser.find_element_by_xpath(xpath='//*[@id="app"]/div[5]/span/div/span/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)
        browser.close()
        print('Downloaded {} Successfully!'.format(line))


if __name__ == '__main__':
    print('==============================Project Start===================================')
    selenium()
    print('==============================Project End=====================================')
