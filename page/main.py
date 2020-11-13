# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/11 17:06
import yaml
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.market import Market


class Main(BasePage):

    def goto_market(self)-> Market:

        # self.find(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
        self.steps('../page/main.yaml')
        # with open('../page/main.yaml', encoding='utf-8') as f:
        #     steps = yaml.safe_load(f)
        # for step in steps:
        #     element = None
        #     if 'by' in step.keys():
        #         element = self.find(step['by'], step['locator'])
        #     if 'action' in step.keys():
        #         action = step['action']
        #         if 'click' == action:
        #             element.click()
        #         if 'send' == action:
        #             value = step['value']
        #             print(f'send{value}')

        return Market(self._driver)

