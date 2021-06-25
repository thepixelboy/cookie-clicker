from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
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

    if time.time() > timeout:
        current_money = int("".join(driver.find_element_by_id("money").text.split(",")))
        access = driver.find_elements_by_css_selector("#store b")
        upgrades = [
            {"id": f"buy{i.text.split('-')[0].strip()}", "price": int("".join(i.text.split("-")[1].strip().split(",")))}
            for i in access[:-1]
        ]

        for item in upgrades[::-1]:
            if item["price"] < current_money:
                buy = driver.find_element_by_id(item["id"])
                buy.click()
                break

        timeout = time.time() + 5

    if time.time() > game_time:
        break

cookies_per_second = driver.find_element_by_id("cps").text
print(f"Cookies per second: {cookies_per_second}")
