from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pandas as pd
import time

data_frame = pd.DataFrame(columns=["Name", "Comment"])
url = "https://www.thegioididong.com/dtdd/samsung-galaxy-a7-2018"
driver = webdriver.Chrome("/home/ledinhtuyenbkdn/Downloads/chromedriver")
index = 0

driver.get(url)
# get all rating boxes
for numPageRating in range(0, 5):
    eleRating = driver.find_elements_by_class_name("par")
    nextRatingBtn = None
    titleAttr = "trang 2"
    for i in range(0, len(eleRating)):
        ele = eleRating.pop(0)
        nameEle = ele.find_element_by_css_selector(".rh span").text
        commentEle = ele.find_elements_by_css_selector(".rc i")[5].text
        print(nameEle)
        print(commentEle)
        data_frame.set_value(index,"Name",nameEle)
        data_frame.set_value(index,"Comment",commentEle)
        index = index + 1
        nextRatingBtn = driver.find_elements_by_class_name("pagcomment")[0].find_elements_by_tag_name("a").pop()
    
    print(nextRatingBtn.text)
    print(nextRatingBtn.get_attribute('title')) 
    driver.execute_script("arguments[0].click();", nextRatingBtn)
    time.sleep(2)

data_frame.to_csv("crawl-tgdd.csv")
driver.close()
driver.quit()