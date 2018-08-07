from public.page_object import Page


class Register(Page):

    # 打开注册页
    def open_login(self):
        self.dr.open_url("http://test2.www.makex.cc/login")
        return self

    # 点击注册新账号按钮
    def click_new_register_button(self):
        self.dr.click("xpath->//div[@class='pull-right']/a")
        return self


    # 区号选择
    def area_zone(self, code):
        self.dr.click("xpath->//*[@class='btn btn-default dropdown-toggle btn-lg']/button")
        if code == "86":
            self.dr.click("xpath->//div[@class='input-group-btn open']/div[@class='dropdown-menu']/ul/li[1]/a")
        elif code == "852":
            self.dr.click("xpath->//div[@class='input-group-btn open']/div[@class='dropdown-menu']/ul/li[2]/a")
        elif code == "853":
            self.dr.click("xpath->//div[@class='input-group-btn open']/div[@class='dropdown-menu']/ul/li[3]/a")
        elif code == "886":
            self.dr.click("xpath->//div[@class='input-group-btn open']/div[@class='dropdown-menu']/ul/li[4]/a")
        return self


    # 输入手机号
    def input_num(self, num):
        self.dr.clear_keys("id->phone_num")
        self.dr.send_keys("id->phone_num", num)
        return self

    # 输入密码
    def input_pw(self, password):
        self.dr.clear_keys("id->password")
        self.dr.send_keys("id->password", password)
        return self


    # 输入确认密码
    def input_verify_pw(self, verify_pw):
        self.dr.clear_keys("id->verify_password")
        self.dr.send_keys("id->verify_password", verify_pw)
        return self

    # 点击注册按钮
    def click_register_button(self):
        self.dr.click("xpath->//button[contains(text(),'注册')]")
        return self

    # 定位断言注册成功toast信息
    def toast_message(self):
        self.dr.get_element("xpath->")
        return self
