from selenium import webdriver
import math
from time import sleep

link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 100);")
    x  = browser.find_element_by_id('input_value').text
    rez = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_id('answer').send_keys(rez)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn-primary').click()
finally:
    sleep(30)
    browser.quit()
