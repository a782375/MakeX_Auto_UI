#coding=utf-8

import unittest
from public.base_page import basepage
from Config import global_parameter
from public.log import Log

class MyTest(unittest.TestCase):
    """
    The base class is for all testcases.
    """

    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.dr = basepage(global_parameter.browser)
        self.dr.max_window()

    def tearDown(self):
        # self.dr.quit()
        self.logger.info('###############################  End  ###############################')


