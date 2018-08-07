#coding=utf-8

from public.page_object import Page

class login_page(Page):


    #打开登录页
    def open_login(self):
        self.dr.open_url("http://test2.www.makex.cc/login")
    #输入手机号
    def input_num(self, num):
        self.dr.clear_keys("id->phone_num")
        self.dr.send_keys("id->phone_num", num)
    #清空手机号
    def input_clear(self):
        self.dr.clear_keys("id->phone_num")
    #清空密码
    def pw_clear(self):
        self.dr.clear_keys("id->password")
    #输入密码
    def input_pw(self, pw):
        self.dr.clear_keys("id->password")
        self.dr.send_keys("id->password", pw)
    #点击登录
    def click_submit(self):
        self.dr.click("xpath->//button[@class = 'btn btn-primary btn-block btn-lg']")
    #手机号为空时tip内容提示
    def phone_tip(self):
        return self.dr.get_text("xpath->//form[@id='login']/div[1]/div[2]/ul/li")
    #密码为空时tip内容提示
    def pw_tip(self):
        return self.dr.get_text("xpath->//div[@class = 'help-block with-errors text-right']/ul/li")
    #区号选择
    def area_zone(self, code):
        self.dr.click("xpath->//button[@class = 'btn btn-default dropdown-toggle btn-lg']")
        if code == "86":
            self.dr.click("xpath->//div[@class = 'input-group-btn open']/ul/li[1]/a")
        elif code == "852":
            self.dr.click("xpath->//div[@class = 'input-group-btn open']/ul/li[2]/a")
        elif code == "853":
            self.dr.click("xpath->//div[@class = 'input-group-btn open']/ul/li[3]/a")
        elif code == "886":
            self.dr.click("xpath->//div[@class = 'input-group-btn open']/ul/li[4]/a")














