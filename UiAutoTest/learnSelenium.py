from selenium import webdriver
import unittest,time

class testui(unittest.TestCase):
    def setUp(self):
        opts = webdriver.ChromeOptions()
        opts.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(options=opts)
        #driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://www.baidu.com')

    def testlll(self):
        time.sleep(5)
        driver = self.driver
        filename = '/Users/liuqing/my_project/forever/UiAutoTest/failPicture'
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        driver.get_screenshot_as_file(filename + now + '.jpg')
        print('ok')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
