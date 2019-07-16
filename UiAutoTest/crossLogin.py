from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_argument('disable-infobars')
driver = webdriver.Chrome(options=opts)
driver.get('https://mail.163.com/')
driver.implicitly_wait(20)
driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])
driver.find_element_by_xpath('//input[@data-loginname="loginEmail"]').send_keys('fallinlove_lq')
driver.find_element_by_xpath('//input[@name="password"]').send_keys('lovelove123..')
driver.find_element_by_css_selector('#dologin').click()
driver.quit()