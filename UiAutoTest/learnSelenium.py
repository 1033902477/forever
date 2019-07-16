from selenium import webdriver
import unittest,time

opt = webdriver.ChromeOptions()
opt.add_argument('disable-infobars')
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(5)
# driver.get('https://mail.163.com/')
driver.get('https://www.caasdata.com/')
# frame = driver.find_elements_by_tag_name('iframe')[0]
# driver.switch_to.frame(frame)
# driver.find_element_by_xpath('//*[@name="email"]').send_keys('123')
# # //*[@id="auto-id-1548320022443"]
token = {'domain':'.caasdata.com','expiry':'2019-02-16T15:47:51.000Z','httpOnly':'False','name':'token','path':'/',
         'secure':'False','value':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5kYXRhLmNhYXNkYXRhLmNvbS9hdXRoIiwiaWF0IjoxNTQ3NjUzNjcxLCJleHAiOjE1NTAyNDU2NzEsIm5iZiI6MTU0NzY1MzY3MSwianRpIjoialJTSTAwM1BySUhLNTJkMCIsInN1YiI6IjQ4OTg4IiwiTG9naW5Ub2tlbiI6IloweHl1NUhjTTJZVWQifQ.EpzoxWHklOtya8eaW8Ta4dd6E6NNREMdZGk9J4el1Rc'}
driver.add_cookie(token)
time.sleep(2)
driver.refresh()
time.sleep(1)
driver.get('https://products.caasdata.com/kol_list/kol_list')
# time.sleep(2)
# driver.find_element_by_link_text('卡思商业版').click()
time.sleep(2)
driver.quit()
