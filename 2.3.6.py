from selenium import webdriver
from time import sleep
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name('btn-primary').click()
    browser.switch_to.window(browser.window_handles[1])
    x  = browser.find_element_by_id('input_value').text
    rez = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_id('answer').send_keys(rez)
    browser.find_element_by_class_name('btn-primary').click()
finally:
    sleep(15)
    browser.quit()
