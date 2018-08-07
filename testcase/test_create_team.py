#coding=utf-8

import time
from selenium import webdriver
from public.cases_format import MyTest
from pages.login_page import login_page
from pages.create_team import create_team



class create_team1(MyTest):


    def test_create1(self):
        login2 = login_page(self.dr)
        login2.open_login()
        login2.input_num("18626909902")
        login2.input_pw("123456")
        login2.click_submit()
        login3 = create_team(self.dr)
        login3.create_round(999, "D:\A222.png", "北京")

    #
    # def test_create2(self):
    #     login2 = login_page(self.dr)
    #     login2.open_login()
    #     login2.input_num("18565792419")
    #     login2.input_pw("interesting")
    #     login2.click_submit()
    #     login3 = create_team(self.dr)
    #     login3.create_round2(999, "D:\A222.png", "法国")





