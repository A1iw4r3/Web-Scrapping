from selenium import webdriver 
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.youtube.com')
search=driver.find_element("""<input id="search" autocapitalize="none" autocomplete="off" autocorrect="off" name="search_query" tabindex="0" type="text" spellcheck="false" placeholder="Search" aria-label="Search" control-id="ControlID-1" role="combobox" aria-haspopup="false" aria-autocomplete="list" dir="ltr" class="ytd-searchbox" style="outline: none;">""")
search.send_keys('wscubetech')