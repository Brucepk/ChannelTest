from appium import webdriver
import random
from time import sleep


def mainFun():
    cap = {}
    cap['platformName'] = 'Android'
    cap['platformVersion'] = '4.4.2'
    cap['appPackage'] = 'com.tal.kaoyan'
    cap['appActivity'] = '.ui.activity.SplashActivity'
    cap['deviceName'] = '127.0.0.1:62001'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
    driver.implicitly_wait(10)

    # 版本更新提示判断,弹窗，就点击取消按钮
    try:
        driver.find_element_by_id('android:id/button2').click()  # 点击版本更新的取消按钮
    except:
        pass

    # 跳过广告页,判断是否有此按钮，有的话则点击跳过安妮
    try:
        # 用xpath定位跳过按钮
        driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()  # 点击跳过按钮
    except:
        pass

    driver.find_element_by_xpath('//android.widget.TextView[@text="注册"]').click()   # 点击注册按钮

    # ------注册流程---------
    # 添加头像
    driver.find_element_by_xpath('//android.widget.ImageView[@resource-id="com.tal.kaoyan:id/activity_register_userheader"]').click()
    images = driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
    images[1].click()
    sleep(0.5)
    driver.find_element_by_id('com.tal.kaoyan:id/save').click()   # 点击保存按钮

    sleep(0.5)
    text_random = random.randint(111, 9999)   # 生成随机数字，用作随机登录名和邮箱
    driver.find_element_by_xpath('//android.widget.EditText[@text="用户名"]').send_keys('brucepk{}'.format(text_random))   # 输入用户名
    sleep(0.5)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys('pkpkpkpk123456')  # 输入密码
    sleep(0.5)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys('98998645fssf56{}@qq.com'.format(text_random))  # 输入邮箱
    sleep(0.5)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()

    # -----完善资料------
    driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
    # 随机选择城市
    city_id = driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')
    city_num = random.randint(0, len(city_id)-1)
    city_id[city_num].click()
    sleep(0.5)

    # 随机选择大学，避免不在一屏内，向上滑动一屏
    # 获取屏幕分辨率
    def get_size():
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return x, y


    x = int(get_size()[0])
    y = int(get_size()[1])


    # 定义向上滑动
    def swipeUp():
        driver.swipe(x*0.5, y*0.9, x*0.5, y*0.2)


    swipeUp()     # 向上滑动一屏
    uni_id = driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')
    uni_num = random.randint(0, len(uni_id)-1)
    uni_id[uni_num].click()
    sleep(0.5)
    # 选择目标院校
    driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()

    # 重复上个步骤，选择目标院校
    sleep(0.5)
    city_id2 = driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')  # 随机选择城市
    city_num2 = random.randint(0, len(city_id2)-1)
    city_id2[city_num2].click()
    # 随机选择大学
    swipeUp()     # 向上滑动一屏
    uni_id2 = driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')
    uni_num2 = random.randint(0, len(uni_id2)-1)
    uni_id2[uni_num2].click()

    # 选择目标专业
    driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()


    # 随机选择专业，哲学的分类和其他不一样，需要做区分
    sleep(0.5)
    majors = driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')
    maj_num = random.randint(0, len(majors)-1)
    if majors[maj_num].text == '哲学':
        majors[maj_num].click()
        sleep(0.5)
        # 选择细分专业
        major2 = driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')
        maj_num2 = random.randint(0, len(major2)-1)
        major2[maj_num2].click()
        sleep(0.5)

    else:
        majors[maj_num].click()
        sleep(0.5)

        # 选择细分专业
        major2 = driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')
        maj_num2 = random.randint(0, len(major2) - 1)
        major2[maj_num2].click()
        sleep(0.5)

        # 随机选择科目
        major_item = driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')
        item_num = random.randint(0, len(major_item) - 1)
        major_item[item_num].click()
        sleep(0.5)


    # 点击进入考研帮按钮
    driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()






