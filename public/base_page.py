# coding=utf-8
"""
Create on 2018-5-24
@Author:Junjie Peng
Project: BasePage为封装所有页面公有的方法，
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import win32con
import win32gui
import time
from public.log import Log

success = "SUCCESS"
fail = "FAIL"
logger = Log()

class basepage(object):

    def __init__(self, browser='firefox'):
        """

        功能：浏览器初始化
        """
        t = time.time()
        if browser == 'firefox':
            dr = webdriver.Firefox()
        elif browser == 'chrome':
            dr = webdriver.Chrome()
        elif browser == 'IE':
            dr = webdriver.Ie()

        try:
            self.driver = dr
            self.print_log("{0} Open a new browser : {1}, Spend {2} seconds. " .format(success, browser, time.time()-t))

        except Exception:

            raise NameError('Cannot found {0} browser'.format(browser))

    def print_log(self, msg):
        logger.info(msg)

    def element_wait(self, css):
        """

         功能：等待一个元素显示
         用法：driver.element_wait("id->kw")
        """
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        messages = 'Element: {0} not found .'.format(css)

        if by == 'id':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, value)), messages)
        elif by == 'name':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, value)), messages)
        elif by == 'class':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, value)), messages)
        elif by == 'tag':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, value)), messages)
        elif by == 'link_text':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, value)), messages)
        elif by == 'partial_link_text':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)), messages)
        elif by == 'css':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)), messages)
        elif by == 'xpath':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, value)), messages)
        else:
            raise NameError("Please enter the correct elements")

    def element_clickable(self, css):
        """

         功能：等待一个元素可点击
         用法：driver.element_wait("id->kw")
        """
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        messages = 'Element: {0} not found .'.format(css)
        if by == 'id':
            button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, value)), messages)
        elif by == 'name':
            button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, value)), messages)
        elif by == 'class':
            button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, value)), messages)
        elif by == 'tag':
            button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, value)), messages)
        elif by == 'link_text':
            button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, value)), messages)
        elif by == 'partial_link_text':
            button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, value)), messages)
        elif by == 'css':
            button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, value)), messages)
        elif by == 'xpath':
            button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, value)), messages)
        else:
            raise NameError("Please enter the correct elements")
        return button

    def get_element(self, css):
        """

        功能：获取一个元素
        用法：driver.get_element("id->kw")
        """
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "tag":
            element = self.driver.find_element_by_tag_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "partial_link_text":
            element = self.driver.find_element_by_partial_link_text(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        else:
            raise NameError("Please enter the correct elements")
        return element

    def open_url(self, url):
        """
        功能：打开URL网址
        用法：driver.open_url("www.baidu.com")
        """
        t = time.time()
        try:
            self.driver.get(url)
            self.print_log("{0} Open url: {1}, Spend {2} seconds. " .format(success, url, time.time()-t))
        except Exception:
            raise ValueError("{0} Open url: {1}, Spend {2} seconds. " .format(fail, url, time.time()-t))

    def max_window(self):
        """
        功能：最大化窗口
        用法：driver.max_window()
        """
        t = time.time()
        self.driver.maximize_window()
        self.print_log("{0} Set browser window maximized, Spend {1} seconds".format(success, time.time() - t))

    def set_window(self, width, height):
        """
        功能：设置窗口宽和高
        用法：driver.set_window(wide, high)
        """
        t = time.time()
        self.driver.set_window_size(width, height)
        self.print_log("{0} Set browser window wide {1}, height {2}, Spend {3} seconds".format(success,
                                                                                               width, height,
                                                                                               time.time() - t))

    def send_keys(self, css, text):
        """
        功能：定位到元素之后输入文本
        用法：driver.send_keys("id->kw","selenium")
        """
        t = time.time()
        try:
            self.element_wait(css)
            element = self.get_element(css)
            element.send_keys(text)
            self.print_log("{0} Sent element: {1}, content: {2}, Spend {3} seconds".format(success,
                                                                                           css, text, time.time() - t))
        except Exception:
            self.print_log("{0} Sent element: {1}, content: {2}, Spend {3} seconds".format(fail,
                                                                                           css, text, time.time() - t))
            raise

    def clear_keys(self, css):
        """
        功能：清除元素空间里面的文本
        用法：driver.clear_keys("id->kw")
        """
        t = time.time()
        try:
            self.element_wait(css)
            element = self.get_element(css)
            element.clear()
            self.print_log("{0} Clearing content of element: {1}, Spend {2} seconds".format(success, css,
                                                                                            time.time() - t))
        except Exception:
            self.print_log("{0} Clearing content of element: {1}, Spend {2} seconds".format(fail, css,
                                                                                            time.time() - t))
            raise

    def click(self, css):
        """
        功能：定位到某元素后左键单击
        用法：driver.click("id->kw")
        """
        t = time.time()
        try:
            self.element_wait(css)
            element = self.get_element(css)
            element.click()
            self.print_log("{0} Click element: {1}, Spend {2} seconds".format(success, css, time.time() - t))
        except Exception:
            self.print_log("{0} Click element: {1}, Spend {2} seconds".format(fail, css, time.time() - t))
            raise

    def clickable(self, css):
        t = time.time()
        try:
            element = self.element_clickable(css)
            element.click()
            self.print_log("{0} Click element: {1}, Spend {2} seconds".format(success, css, time.time() - t))
        except Exception:
            self.print_log("{0} Click element: {1}, Spend {2} seconds".format(fail, css, time.time() - t))
            raise

    def right_click(self, css):
        """
        功能：定位到某元素后右键单击
        用法：driver.right_click("id->kw")
        """
        t = time.time()
        try:
            self.element_wait(css)
            element = self.get_element(css)
            ActionChains(self.driver).context_click(element).perform()
            self.print_log("{0} Right click element: {1}, Spend {2} seconds".format(success, css, time.time() - t))
        except Exception:
            self.print_log("{0} Right click element: {1}, Spend {2} seconds".format(fail, css, time.time() - t))
            raise

    def double_click(self, css):
        """
        功能：定位到某元素后左键双击
        用法：driver.double_click("id->kw")
        """
        t = time.time()
        try:
            self.element_wait(css)
            element = self.get_element(css)
            ActionChains(self.driver).double_click(element).perform()
            self.print_log("{0} Double click element: {1}, Spend {2} seconds".format(success, css, time.time() - t))
        except Exception:
            self.print_log("{0} Double click element: {1}, Spend {2} seconds".format(fail, css, time.time() - t))
            raise

    def move_to_element(self, css):
        """
        功能：鼠标悬停在一个元素上
        用法：driver.move_to_element("id->kw")
        """
        t = time.time()
        try:
            self.element_wait(css)
            element = self.get_element(css)
            ActionChains(self.driver).move_to_element(element).perform()
            self.print_log("{0} Move to element: {1}, Spend {2} seconds".format(success, css, time.time() - t))
        except Exception:
            self.print_log("{0} Move to element: {1}, Spend {2} seconds".format(fail, css, time.time() - t))
            raise

    def click_link_text(self, text):
        """
        功能：点击链接本文
        用法：driver.click_link_text("贴吧")
        """
        t = time.time()
        try:
            self.driver.find_element_by_link_text(text).click()
            self.print_log("{0} Click link text element: {1}, Spend {2} seconds".format(success, text,
                                                                                           time.time() - t))
        except Exception:
            self.print_log("{0} Click link text element: {1}, Spend {2} seconds".format(fail, text,
                                                                                           time.time() - t))
            raise

    def close_window(self):
        """
        功能：关闭当前浏览器窗口
        用法：driver.close_window()
        """
        t = time.time()
        self.driver.close()
        self.print_log("{0} Close current window, Spend {1} seconds".format(success, time.time() - t))

    def quit(self):
        """
        功能：关闭浏览器
        用法：driver.quit_browser()
        """
        t = time.time()
        self.driver.quit()
        self.print_log("{0} Close all windows and quit the driver, Spend {1} seconds".format(success,
                                                                                                time.time() - t))

    def submit(self, css):
        """
        功能：提交某元素
        用法：driver.submit("id->kw")
        """
        t = time.time()
        try:
            self.element_wait(css)
            element = self.get_element(css)
            element.submit()
            self.print_log("{0} Submit element: {1}, Spend {2} seconds".format(success, css, time.time() - t))
        except Exception:
            self.print_log("{0} Submit element: {1}, Spend {2} seconds".format(fail, css, time.time() - t))
            raise

    def f5(self):
        """
        功能：刷新当前窗口页面
        用法：driver.f5()
        """
        t = time.time()
        self.driver.refresh()
        self.print_log("{0} Refresh current page, Spend {1} seconds".format(success, time.time() - t))

    def get_attribute(self, css, attribute):
        """
        功能：获取元素属性的值
        用法：driver.get_attribute("id->su","href")
        """
        t = time.time()
        try:
            element = self.get_element(css)
            attr = element.get_attribute(attribute)
            self.print_log("{0} Get attribute element: {1}, attribute: {2}, Spend {3} seconds".format(success, css,
                                                                                                      attribute,
                                                                                                      time.time() - t))
            return attr
        except Exception:
            self.print_log("{0} Get attribute element: {1}, attribute: {2}, Spend {3} seconds".format(fail, css,
                                                                                                      attribute,
                                                                                                      time.time() - t))
            raise

    def get_text(self, css):
        """
        功能：获取元素的文本
        用法：driver.get_text("id->kw")
        """
        t = time.time()
        try:
            self.element_wait(css)
            text = self.get_element(css).text
            self.print_log("{0} Get text element, element: {1}, text: {2}, Spend {3} seconds".format(success, css, text,
                                                                                          time.time() - t))
            return text
        except Exception:
            self.print_log("{0} Get text element, element: {1}, Spend {2} seconds".format(fail, css, time.time() - t))
            raise

    def get_title(self):
        """
        功能：获取页面标题
        用法：driver.get_title()
        """
        t = time.time()
        tit = self.driver.title
        self.print_log("{0} Get title for current page, Spend {1} seconds".format(success, time.time() - t))
        return tit

    def get_url(self):
        """
        功能：获取当前页面的url
        用法：driver.get_url()
        """
        t = time.time()
        url = self.driver.current_url
        self.print_log("{0} Get url for current page, Spend {1} seconds".format(success, time.time() - t))
        return url

    def wait(self, secs):
        """
        功能：隐性等待
        用法：driver.wait(5)
        """
        t = time.time()
        self.driver.implicitly_wait(secs)
        self.print_log("{0} Set wait all elements to display in {1} seconds , Spend {2} seconds".format(success, secs, time.time() - t))

    def alert_accept(self):
        """
        功能：弹窗确定
        用法：driver.alert_accept()
        """
        t = time.time()
        self.driver.switch_to.alert.accept()
        self.print_log("{0} Accept warning window , Spend {1} seconds".format(success, time.time() - t))

    def alert_dismiss(self):
        """
        功能：弹窗取消
        用法：driver.alert_dismiss()
        """
        t = time.time()
        self.driver.switch_to.alert.dismiss()
        self.print_log("{0} Dismiss warning window , Spend {1} seconds".format(success, time.time() - t))

    def open_new_window(self, css):
        """
        功能：点击元素打开新窗口，并切换句柄至新窗口
        用法：driver.open_new_window("id->kw")
        """
        t = time.time()
        try:
            original_handle = self.driver.current_window_handle
            element = self.get_element(css)
            element.click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_handle:
                    self.driver.switch_to.window(handle)
            self.print_log("{0} Click element: {1} open new window and switch into, Spend {2} seconds".format(success, css, time.time() - t))
        except Exception:
            self.print_log("{0} Click element: {1} open new window and switch into, Spend {2} seconds".format(fail, css, time.time() - t))
            raise

    def get_screen_shot(self, file_path):
        """
        功能：获取当前窗口截图，并保存至指定路径
        用法：driver.get_screenshot("c:/test.png")
        """
        t = time.time()
        try:
            self.driver.get_screenshot_as_file(file_path)
            self.print_log(
                "{0} Get current window screenshot, path: {1} Spend {2} seconds".format(success, file_path,
                                                                                                   time.time() - t))
        except Exception:
            self.print_log(
                "{0} Get current window screenshot, path: {1} Spend {2} seconds".format(fail, file_path,
                                                                                        time.time() - t))
            raise

    def upload_picture(self, pic_path):
        """
        功能：上传图片
        用法：driver.upload_picture("c:/test.png")
        """
        t = time.time()
        try:
            dialog = win32gui.FindWindow("#32770", u"文件上传")  # 对话框
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
            Edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)
            button = win32gui.FindWindowEx(ComboBox, 0, "Button", None)  # 确定按钮Button
            win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, pic_path)  # 往输入框输入绝对地址
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
            self.print_log("{0} Upload picture, path: {1} Spend {2} seconds".format(success, pic_path,
                                                                                        time.time() - t))
        except Exception:
            self.print_log("{0} Upload picture, path: {1} Spend {2} seconds".format(fail, pic_path,
                                                                                    time.time() - t))
            raise

    def js_click(self, css):
        """
        功能：使用javascript点击元素
        用法：driver.js_click('#buttonid')
        """
        t1 = time.time()
        js_str = "$('{0}').click()".format(css)
        try:
            self.driver.execute_script(js_str)
            self.print_log("{0} Use javascript click element: {1}, Spend {2} seconds".format(success, js_str, time.time()-t1))
        except Exception:
            self.print_log("{0} Unable to use javascript click element: {1}, Spend {2} seconds".format(fail,
                js_str, time.time() - t1))
            raise

    def scroll(self):
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
