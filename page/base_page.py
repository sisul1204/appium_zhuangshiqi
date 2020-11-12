# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/11 10:53
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.wrapper import handle_black


class BasePage:


    def __init__(self, driver:WebDriver=None):
        self._driver = driver


    def finds(self, locator, value:str=None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value:str=None):
        element: WebElement

        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)

        return element




