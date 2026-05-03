from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time



options = Options()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options)

driver.get("https://www.youtube.com")

#Wait for the search box to be present
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.NAME, "search_query")))

#Find the search box and type a query
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Best 400cc motorcycles")
search_box.send_keys(Keys.RETURN)

#Wait for the search results to load
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer")))

#click the first video result
first_video = driver.find_element(By.CSS_SELECTOR, "ytd-video-renderer #video-title")
first_video.click()

#Wait for the video page to load
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.ytd-video-primary-info-renderer")))

#watch the video for desired time
time.sleep(60)
#Close the browser
driver.quit()