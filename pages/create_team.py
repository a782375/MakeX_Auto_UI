#coding=utf-8
from public.page_object import Page
import time



class create_team(Page):



    # 打开创建战队页
    def open_create_team(self):
        self.dr.open_url("http://test2.www.makex.cc/team/create")


    # 上传战队Logo
    def upload_logo(self, pic_path):
        # self.dr.clickable("xpath->//div[@class = 'part-edit-mt']/div[1]/a")
        self.dr.click("xpath->/html/body/div[1]/div[2]/div[1]/div[2]/form/div/div/div/div[1]/a/i")  # 点击更新战队logo
        time.sleep(2)
        self.dr.click("xpath->//div[@class = 'col-xs-7 col-sm-7']")  # 点击选择图片
        self.dr.upload_picture(pic_path)  # 选择文件上传
        time.sleep(1)
        self.dr.click("xpath->//div[@class = 'col-xs-5 col-sm-5']/button")  # 点击完成

    # 选择国家
    def country_choose(self, country):
        self.dr.click("xpath->//button[@class= 'btn btn-default dropdown-toggle country-toggle']")
        self.dr.click("link_text->%s" % country)


    # 选择省份
    def province_choose(self, province):
        self.dr.click("id->area_id")
        self.dr.click("xpath->//div[@class = 'bs-chinese-region flat dropdown open']/div/div/ul/li[1]/a")
        self.dr.click("partial_link_text->%s" % province)

    # 选择城市
    def city_choose(self, city):
        self.dr.click("xpath->//div[@class = 'bs-chinese-region flat dropdown open']/div/div/ul/li[2]/a")
        self.dr.click("partial_link_text->%s" % city)

    # 输入战队名称
    def input_name(self, name):
        self.dr.clear_keys("id->name")
        self.dr.send_keys("id->name", name)

    # 输入战队口号
    def input_slogan(self, slogan):
        self.dr.clear_keys("id->slogan")
        self.dr.send_keys("id->slogan", slogan)

    # 输入俱乐部
    def input_club(self, club):
        self.dr.clear_keys("id->club")
        self.dr.send_keys("id->club", club)

    # 输入战队介绍
    def input_intro(self, intro):
        self.dr.clear_keys("id->intro")
        self.dr.send_keys("id->intro", intro)

    # 点击创建
    def team_submit(self):
        self.dr.click("xpath->//div[@class = 'part-edit-mt']/div[@class = 'form-group form-group-lg']/button")

    # 点击取消
    def team_cancel(self):
        self.dr.click("xpath->//div[@class = 'part-edit-mt']/div[8]/a")

    # 点击+
    def plus(self):
        self.dr.click("xpath->//div[@class = 'teams-list-title hidden-xs']/a/i")




    # 选择页面循环次数
    def create_round(self, num, pic_path, province, city = None):
        """
        :param num: 生成的战队数量
        :param pic_path: 战队logo图片路径
        :param province: 生成的省份
        :return:
        """
        for i in range(1, num+1):
            self.dr.click("xpath->//ul[@class = 'nav navbar-nav navbar-right']/li[7]/a/span")  # 点击个人中心
            self.dr.wait(15)
            time.sleep(1)
            self.plus()  # 点击+
            time.sleep(2)
            self.upload_logo(pic_path)  # 上传战队logo
            time.sleep(1)
            self.province_choose(province)  # 选择省份
            if city is None:   # 根据需要选择城市
                pass
            else:
                self.city_choose(city)
            self.input_name(u"%s测试战队50%d" % (province, i))  # 输入战队名称
            self.input_slogan("11111")  # 输入口号
            self.input_intro("22222")  # 输入战队介绍
            self.team_submit()  # 创建战队
            assert self.dr.get_text("xpath->//div[@class = 'toast-wrap toast-success']") == "战队创建成功！"
            self.dr.element_wait("xpath->/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/a")
            time.sleep(1)


    def create_round2(self, num, pic_path, country):
        """
        :param num: 生成的战队数量
        :param pic_path: 战队logo图片路径
        :param province: 生成的省份
        :return:
        """
        for i in range(1, num+1):
            self.dr.click("xpath->//ul[@class = 'nav navbar-nav navbar-right']/li[7]/a/span")  # 点击个人中心
            self.dr.wait(15)
            time.sleep(1)
            self.plus()  # 点击+
            time.sleep(2)
            self.upload_logo(pic_path)  # 上传战队logo
            time.sleep(1)
            self.country_choose(country)
            self.input_name(u"%s测试战队538%d" % (country, i))  # 输入战队名称
            self.input_slogan("11111")  # 输入口号
            self.input_intro("123456")  # 输入战队介绍
            self.dr.scroll()
            self.team_submit()  # 创建战队
            assert self.dr.get_text("xpath->//div[@class = 'toast-wrap toast-success']") == "战队创建成功！"
            self.dr.element_wait("xpath->/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/a")
            time.sleep(1)










