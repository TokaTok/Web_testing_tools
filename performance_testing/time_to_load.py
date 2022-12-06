# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for selections
from selenium.webdriver.common.by import By

import undetected_chromedriver as UC

def page_load(url, element):

    driver = UC.Chrome(use_subprocess=True)

    start_time = time.time()
    driver.get(url)

    delay = 20 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
        load_time = time.time() - start_time
        return round(load_time, 2)
    except TimeoutException:
        return "Loading took too much time!"
    
