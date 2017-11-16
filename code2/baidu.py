#coding=utf-8
import time
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("www.baidu.com")
time.sleep(5)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.quit()