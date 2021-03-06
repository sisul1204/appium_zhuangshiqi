# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/12 10:29
import logging

import allure
from selenium.webdriver.common.by import By


def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args,**kwargs):
        _black_list = [
            (By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]'),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),

        ]
        _max_num = 3
        _error_num = 0

        from page.base_page import BasePage
        instance: BasePage = args[0]
        try:
            logging.info('run '+ func.__name__ + '\n args: \n' + repr(args[1:])+ '\n' + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
            instance.screenshot('tmp.png')
            with open('tmp.png','rb') as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            logging.error('element not found, handle black list')
            instance._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1

            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return wrapper(*args, **kwargs)

            raise e
    return wrapper


