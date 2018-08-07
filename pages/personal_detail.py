#coding=utf-8
from public.page_object import Page

class personal_detail(Page):


    # 打开修改个人信息页
    def open_login(self):
        self.dr.open_url("http://test2.www.makex.cc/personal/edit")

    # 上传头像
    def upload_portrait(self, pic_path):
        self.dr.click("xpath->//a[@class = 'btn btn-default btn-upload']")
        self.dr.upload_picture(pic_path)

    #输入姓名
    def input_name(self, name):
        self.dr.clear_keys("id->name")
        self.dr.send_keys("id->name", name)

    #证件类型选择
    def id_type(self, type):
        self.dr.click("xpath->//div[@class = 'has-line']/div[3]/div[1]/div/button")
        if type == "身份证":
            self.dr.click("xpath->//div[@class = has-line]/div[3]/div[1]/div/ul/li[1]/a")
        elif type == "护照":
            self.dr.click("xpath->//div[@class = has-line]/div[3]/div[1]/div/ul/li[2]/a")
        elif type == "回乡证":
            self.dr.click("xpath->//div[@class = has-line]/div[3]/div[1]/div/ul/li[3]/a")
        elif type == "台胞证":
            self.dr.click("xpath->//div[@class = has-line]/div[3]/div[1]/div/ul/li[4]/a")

    #输入证件号码
    def id_num(self, num):
        self.dr.clear_keys("id->id_num")
        self.dr.send_keys("id->id_num", num)

    #选择年份
    def year_choose(self, year):
        year = int(year)
        self.dr.click("xpath->//div[@class = 'has-line']/div[4]/div[1]/div[1]/div/div[1]/button")
        self.dr.click("xpath->//div[@class = 'input-group-btn open']/ul/li[%d]/a" % (year-1948))

    #选择月份
    def month_choose(self, month):
        month1 = int(month)
        self.dr.click("xpath->//div[@class = 'has-line']/div[4]/div[1]/div[2]/div/div[1]/button")
        self.dr.click("xpath->//div[@class = 'input-group-btn open']/ul/li[%d]/a" % month1)

    #选择日期
    def day_choose(self, day):
        day1 = int(day)
        self.dr.click("xpath->//div[@class = 'has-line']/div[4]/div[1]/div[3]/div/div[1]/button")
        self.dr.click("xpath->//div[@class = 'input-group-btn open']/ul/li[%d]/a" % day1)

    #选择性别
    def gender_choose(self, gender):
        if gender == "male":
            self.dr.click("id->gender-male")
        if gender == "female":
            self.dr.click("id->gender-female")

    #提交
    def submit(self):
        self.dr.click("xpath->/html/body/div[1]/div[2]/div[1]/div/div/div/form/div[2]/div[2]/div[4]/button")

    #取消
    def cancel(self):
        self.dr.click("xpath->/html/body/div[1]/div[2]/div[1]/div/div/div/form/div[2]/div[2]/div[5]/a")





