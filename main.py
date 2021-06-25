from selenium import webdriver
import time

chrome_driver_path = "/Users/ruben/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
game_time = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()
