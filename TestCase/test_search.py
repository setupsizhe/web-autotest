#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from page.webpage import WebPage, sleep
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage
from selenium.webdriver.support import expected_conditions as EC



@allure.feature("GIS测试演示")
class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def login(self, drivers):
        search = SearchPage(drivers)
        search.get_url(ini.url)

    @allure.story("成功用例")
    def test_001(self,drivers):
        search = SearchPage(drivers)
        """登录系统"""
        search.inputuername("csw")
        search.inputpassword("Csw672996")
        search.click_search()
        sleep(5)
        check="事故预防及应急管理智能化平台"
        assert search.text1() == check

    @allure.story("失败用例")
    def test_002(self,drivers):
        search = SearchPage(drivers)
        check="事故预防及应急管理智能化平台"
        assert search.text1() != check
if __name__ == '__main__':
    pytest.main(['TestCase/test_search.py'])
