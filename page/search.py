# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/11 17:11
import yaml
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Search(BasePage):

    def search(self, name):
        self._params['name'] = name

        self.steps('../page/search.yaml')

    def add(self, name):
        self._params['name'] = name
        self.steps('../page/search.yaml')




    def is_choose(self, name):
        self._params['name'] = name
        return self.steps('../page/search.yaml')

    def reset(self, name):
        self._params['name'] = name
        self.steps('../page/search.yaml')





