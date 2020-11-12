# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/12 8:19
from page.app import App


class TestSearch:

    def setup(self):
        self.search = App().start().main().goto_market().goto_search()


    def test_search(self):
        self.search.search('京东')
        assert self.search.is_choose('京东')