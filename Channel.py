import os
from appium import webdriver
from time import sleep
import unittest
from HTMLTestRunnerCN import HTMLTestRunner
from QQemail import sendMail


class ChannelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        caps = {}
        caps['platformVersion'] = '5.1.1'
        caps['platformName'] = 'Android'
        caps['deviceName'] = '127.0.0.1:62001'
        caps['appPackage'] = 'com.android.contacts'
        caps['appActivity'] = 'com.android.contacts.activities.PeopleActivity'
        caps['noReset'] = True
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        cls.driver.implicitly_wait(10)

    def test_channel(self):
        app_paths = r'D:\app'
        pnames = os.listdir(app_paths)
        for pname in pnames:
            install_path = str(app_paths + '\\' + pname)
            print(install_path)
            self.driver.install_app(install_path)
            print('安装完成，准备卸载')
            sleep(1)
            self.driver.remove_app('com.tal.kaoyan')
            print('卸载完成')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ChannelTest("test_channel"))
    fp = open('report.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title="测试报告", description='测试用例执行结果')
    runner.run(suite)
    fp.close()
    sendMail(r'D:\PycharmProjects\report.html')




