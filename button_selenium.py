from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
n=Service('C:/my data/chromedriver_win32/chromedriver.exe')
driver=webdriver.Chrome()
driver.get('https://portals.au.edu.pk/admissions/')
time.sleep(2)
search=driver.find_element("""/html/body/form/div[3]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/input""")
search.send_keys('wscubetech')
time.sleep(60)