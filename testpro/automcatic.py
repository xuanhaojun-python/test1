
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='D:\\selenium.txt')

driver.get("https://www.baidu.com/")

driver.find_element_by_xpath('//input[@id=“kw”]').send_keys('12132')

driver.find_element_by_xpath('//input[@id="su"]').click()

time.sleep(2)

driver.quit()


