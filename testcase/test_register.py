
from public.cases_format import MyTest
from pages.register import Register
import unittest


class Register1(MyTest):

    def test_register_001(self):
        register = Register(self.dr)
        register.open_login()
        register.click_new_register_button()
        register.input_num("18626909902")
        register.input_pw("123456")
        register.input_verify_pw("123456")
        register.click_register_button()
        self.assertEqual("注册成功，欢迎你加入MakeX！", self.dr.get_text("xpath->"))


if __name__ == '__main__':
    unittest.main()