""" Testing for python """
# Dependency
import time
from selenium import webdriver

# Config
# Change PATH if you wanna use the other webdriver.
PATH = './Webdriver/chromedriver'

option = webdriver.ChromeOptions()
option.add_argument(r"\home\jessie\.config\google-chrome")
option.add_argument("blink-settings=imagesEnabled=false")

driver = webdriver.Chrome(executable_path=PATH, options=option)


driver.set_window_position(1000, 0)
driver.get('https://m.icamping.app/store/stuff/search-result;store_name=gbl141')
# print(driver.title)
time.sleep(5)
driver.execute_script('window.scrollTo(0, 1200);')
# date = driver.find_element_by_class_name(
#     'cal-day-number').get_attribute('innerHTML')
# time.sleep(5)
print('OK')

# if (date == '26'):
#     print(date)
# else:
#     print('not 26')

driver.quit()
