#coding=utf-8
from public.page_object import Page


class change_pw(Page):


    #打开更改密码网页
    def open_change_pw(self):
        self.dr.open_url("http://test2.www.makex.cc/personal/password")

    #旧密码输入
    def input_old(self, old_pw):
        self.dr.clear_keys("id->old_password")
        self.dr.send_keys("id->old_password", old_pw)

    #新密码输入
    def input_new(self, new_pw):
        self.dr.clear_keys("id->new_password")
        self.dr.send_keys("id->new_password", new_pw)

    #重复新密码
    def input_verify(self, verify):
        self.dr.clear_keys("id->new_password")
        self.dr.send_keys("id->new_password", verify)

    #点击保存
    def submit_save(self):
        self.dr.click("xpath->/html/body/div[1]/div[2]/div[1]/div/div/div/form/div[5]/button")

    #点击取消
    def change_cancel(self):
        self.dr.click("/html/body/div[1]/div[2]/div[1]/div/div/div/form/div[6]/a")







