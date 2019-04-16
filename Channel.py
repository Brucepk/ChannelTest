import os
from appium import webdriver
from time import sleep
import unittest
from HTMLTestRunnerCN import HTMLTestRunner
from QQemail import sendMail
from kaoyan import mainFun
import logging
import logging.config


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
        config_file = open(r'./logger.conf', encoding='utf-8')
        logging.config.fileConfig(config_file)
        cls.logger = logging.getLogger('infoLogger')

    def test_channel(self):
        try:
            app_paths = r'F:\app'
            pnames = os.listdir(app_paths)
            for pname in pnames:
                install_path = str(app_paths + '\\' + pname)
                self.driver.install_app(install_path)
                self.logger.info('app安装成功')
                # mainFun()          # 验证主流程
                sleep(1)
                self.driver.remove_app('com.tal.kaoyan')
                self.logger.info('app卸载成功')
            self.logger.info('安装卸载功能验证成功')
        except:
            self.logger.error('验证失败')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ChannelTest("test_channel"))
    fp = open('report.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title="测试报告", description='测试用例执行结果')
    runner.run(suite)
    fp.close()
    sendMail(r'./report.html')




