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

import os
import requests
def create_waterfall(url,loading_time=4):
    driver = UC.Chrome(use_subprocess=True)
    driver.get(url)
    time.sleep(loading_time)
    images = driver.find_elements(By.CSS_SELECTOR, "img") 
    image_sizes = {}
    for i in range(len(images)):
        image_url = images[i].get_attribute("src")
        try:
            file_name = f"images/image.png"
            with open(file_name, "wb") as src:
                response = requests.get(image_url)
                src.write(response.content)
                # src.write(images[i].screenshot_as_png)
                size = round(os.path.getsize(file_name)/1024)
                image_sizes[size] = image_url
                os.remove(file_name)
        except:
            pass
    try:
        pass
        os.remove("images/image.png")
    except:
        pass
    return [sorted(image_sizes.items(), reverse=True),f"image count: {len(image_sizes)}"]