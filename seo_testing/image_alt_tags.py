from selenium.webdriver.common.keys import Keys

from pprint import pprint
import time
# for selections
from selenium.webdriver.common.by import By

import undetected_chromedriver as UC


driver = UC.Chrome(use_subprocess=True)

driver.get("https://www.starman.agency/")
time.sleep(4)

images = driver.find_elements(By.CSS_SELECTOR, "img")

image_db = {}

count = 1
for image in images: 
    try:
        image_url ="https://"+ image.get_attribute("src").split("://")[1]
        image_class =image.get_attribute("class")
        image_alt = image.get_attribute("alt")
        if len(image_alt) <= 3:
            image_db[count] = {image_class:image_url}
            count += 1
    except:
        pass
pprint(image_db)

