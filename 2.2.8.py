from selenium import webdriver
from time import sleep
from os import path

link = 'http://suninjuly.github.io/file_input.html'
file_path = path.join(path.abspath(path.dirname(__file__)), 'file.txt')
print(file_path)  

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name('firstname').send_keys('t')
    browser.find_element_by_name('lastname').send_keys('t')
    browser.find_element_by_name('email').send_keys('t')
    browser.find_element_by_name('file').send_keys(file_path)
    browser.find_element_by_class_name('btn-primary').click()
finally:
    sleep(15)
    browser.quit()
