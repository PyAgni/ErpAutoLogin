#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pytesseract import image_to_string
from urllib.request import urlretrieve
from PIL import Image
from io import BytesIO
import sys,time


user = input('''Enter your Roll No in the format
BE/10xxx/1x :
''')
passwd = input('Enter your password : ')
browser = webdriver.Firefox()
browser.get('http://erp.bitmesra.ac.in')
user_name = browser.find_element_by_id('txt_username')
user_name.send_keys(user)
pwd = browser.find_element_by_id('txt_password')
pwd.send_keys(passwd)
time.sleep(2)
captcha = browser.find_element_by_xpath('//*[@id="frmDefault"]/div[3]/div/div[4]/div[1]/div[2]/img')
src = captcha.get_attribute('src')

location = captcha.location
size = captcha.size
png = browser.get_screenshot_as_png()

im = Image.open(BytesIO(png))
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

im = im.crop((left, top, right, bottom))
im.save('screenshot.png')

cp_txt = image_to_string(Image.open('screenshot.png'))

captcha_box = browser.find_element_by_id('txtcaptcha')
captcha_box.send_keys(cp_txt)

time.sleep(1)
login = browser.find_element_by_id('btnSubmit')
login.click()
