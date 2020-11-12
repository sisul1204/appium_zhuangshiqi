# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/11 17:08
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.search import Search


class Market(BasePage):

    def goto_search(self):
        # self.find(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]').click()
        return Search(self._driver)

