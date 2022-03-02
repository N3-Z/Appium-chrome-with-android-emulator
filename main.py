from appium import webdriver
import time

desire_caps = {}

desire_caps['platformName'] = 'Android'
desire_caps['deviceName'] = 'emulator-5554'
desire_caps['appPackage'] = 'com.android.chrome'
desire_caps['appActivity'] = 'com.google.android.apps.chrome.Main'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_caps)

driver.find_element_by_id('com.android.chrome:id/terms_accept').click()
time.sleep(1)
driver.find_element_by_id('com.android.chrome:id/negative_button').click()
time.sleep(1)


driver.find_element_by_id('com.android.chrome:id/search_box_text').click()
time.sleep(1)
driver.find_element_by_id('com.android.chrome:id/url_bar').click()
time.sleep(1)
driver.find_element_by_id('com.android.chrome:id/url_bar').send_keys("https://otaku-it.blogspot.com/")
time.sleep(1)
driver.find_element_by_id('com.android.chrome:id/line_2').click()
