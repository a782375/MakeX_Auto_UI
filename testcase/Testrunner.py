# coding=utf-8
import HTMLTestRunner
import unittest
import time
import Config.global_parameter



def run():
    test_dir = './'
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = Config.global_parameter.report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)


if __name__ =='__main__':
    run()