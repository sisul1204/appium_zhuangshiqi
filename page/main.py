# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/11 17:06
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.market import Market


class Main(BasePage):

    def goto_market(self)-> Market:
        self.find(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()

        return Market(self._driver)

