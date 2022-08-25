from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

for i in range(5):
    driver = webdriver.Chrome('./chromedriver')
    url = 'https://google.com'
    driver.get(url)

    driver.find_element(By.CSS_SELECTOR, '.gLFyf.gsfi').send_keys('만결숭이의 세상')
    driver.find_element(By.CSS_SELECTOR, '.gLFyf.gsfi').send_keys(Keys.ENTER)

    driver.find_element(By.CSS_SELECTOR, '.LC20lb').click()

    driver.quit()

'''
driver.find_element(By.CSS_SELECTOR, '.t_menu_guestbook.last').click()

driver.find_element(By.CSS_SELECTOR, '.name').send_keys('만결이')
driver.find_element(By.CSS_SELECTOR, '.password').send_keys('2848')
driver.find_element(By.CSS_SELECTOR, '.comment').send_keys('셀레니움 테스트 중입니다.')
driver.find_element(By.CSS_SELECTOR, '.submit').click()
'''

