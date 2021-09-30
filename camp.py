# Dependency
from selenium import webdriver
import time

# Config
# Change PATH if you wanna use the other webdriver.
PATH = './Webdriver/chromedriver'
driver = webdriver.Chrome(PATH)

driver.set_window_position(1000, 0)
driver.get('https://m.icamping.app/store/gbl141')
# print(driver.title)
time.sleep(5)
driver.execute_script('window.scrollTo(0, 1200);')
date = driver.find_element_by_class_name('cal-day-number').get_attribute('innerHTML')
# time.sleep(5)
# print('OK')
print(date)

# driver.quit()
