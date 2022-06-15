#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from selenium.webdriver.support import expected_conditions as EC

search = Element('search')

class SearchPage(WebPage):
    """搜索类"""
    def inputuername(self,content):
        "登录"
        self.input_text(search["账号"],txt=content)
        sleep()
    def inputpassword(self,content):
        self.input_text(search["密码"],txt=content)
        sleep()

    def click_search(self):
        self.is_click(search['登录'])
    def text1(self):
        re=self.element_text(search["title"])
        re1=self.element_text(search["title1"])
        return re,re1
if __name__ == '__main__':
    pass
