from selenium import webdriver
from selenium.webdriver.chrome.service import Service
n=Service('C:/my data/chromedriver_win32/chromedriver.exe')
options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=options,service=n)
driver.get('https://www.wscubetech.com/')
driver.find_element_by_xpath("""/html/body/section[1]/div/div/div[1]/div/div/a""").click()