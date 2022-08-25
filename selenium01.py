from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('./chromedriver')
url = 'https://google.com'
driver.get(url)

driver.find_element(By.CSS_SELECTOR, '.gLFyf.gsfi').send_keys('파이썬')
driver.find_element(By.CSS_SELECTOR, '.gLFyf.gsfi').send_keys(Keys.ENTER)
