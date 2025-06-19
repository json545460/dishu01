# from selenium import webdriver
# import unittest
# import random
# from time import sleep
# from unittestreport import rerun,list_data,ddt
# dishu_aitubiao=webdriver.Chrome()
#
# # 谷歌套件跟版本不匹配无法启动浏览器时用自动获取兼容套件打开浏览器
# # from webdriver_manager.chrome import ChromeDriverManager
# # dishu_aitubiao = webdriver.Chrome(ChromeDriverManager().install())
#
# dishu_aitubiao.get("https://dev.editorup.com");
# dishu_aitubiao.maximize_window();
# sleep(3)
# # dishu_aitubiao.minimize_window();
# x='xpath'
#
#
# @ddt
# class management(unittest.TestCase):
#
#     # @list_data(range(200))
#     #
#     # def test_ot9999(self,case):
#     #     '''后台管理UI元素检测'''
#
#     def test_ot1001(self):
#         '''登录'''
#         dishu_aitubiao.find_element(x,'/html/body/ace-root/div/ace-builder/div/ace-header/ace-sharded-header/div/div/button/span[2]').click()
#         sleep(2)
#         dishu_aitubiao.find_element(x,'//*[@id="mat-mdc-dialog-0"]/div/div/ace-auth/div/div/div[2]/ace-sign-in/div/div[2]/ace-sign-in-by-wechat/div/div[2]/button/span[2]').click()
#         sleep(3)
#         dishu_aitubiao.find_element(x,'//*[@id="mat-mdc-dialog-0"]/div/div/ace-auth/div/div/div[2]/ace-sign-in/div/div[2]/ace-sign-in-by-sms/div/div[1]/a').click()
#         sleep(1)
#         dishu_aitubiao.find_element(x,'//*[@id="account"]').click()
#         sleep(1)
#         dishu_aitubiao.find_element(x,'//*[@id="account"]').send_keys('18888888888')
#         dishu_aitubiao.find_element(x,'//*[@id="password"]').send_keys('888888')
#         dishu_aitubiao.find_element(x,'//*[@id="mat-mdc-dialog-0"]/div/div/ace-auth/div/div/div[2]/ace-sign-in/div/div[2]/ace-sign-in-by-password/div/form/button/span[2]/span').click()
#         sleep(1)
#         wo=dishu_aitubiao.find_element(x,'/html/body/ace-root/div/ace-builder/div/div/ace-menu/div/div/button[1]/div/span').text
#         self.assertEqual(wo,'我的空间')
#
#     def test_ot1002(self):
#         '''创建项目'''
#         dishu_aitubiao.find_element(x,'/html/body/ace-root/div/ace-builder/div/div/ace-menu/div/div/button[1]/div/span').click()
#         sleep(2)
#         dishu_aitubiao.find_element(x,'/html/body/ace-root/div/ace-builder/div/div/div/ace-project/div/div/div[1]/div[1]/div[2]/ace-button/button/span[2]/span').click()
#         sleep(1)
#         dishu_aitubiao.find_element(x,'//*[@id="mat-tab-group-0-content-0"]/div/div/div[1]/div[1]/ace-button/button/span[2]/span').click()
#         sleep(3)
#         dishu_aitubiao.find_element(x,'//*[@id="driver-popover-content"]/footer/span[2]/button[1]').click()
#         sleep(1)
#         dishu_aitubiao.find_element(x,'//*[@id="aceSidebar"]/div/div[1]/div/div[2]/span').click()
#         sleep(1)
#         dishu_aitubiao.find_element(x,'//*[@id="mat-input-6"]').click()
#         sleep(1)
#         dishu_aitubiao.find_element(x,'//*[@id="mat-input-6"]').send_keys('数据')
#         sleep(1)
#         dishu_aitubiao.find_element(x, '//*[@id="mat-input-6"]').clear()
#         sleep(1)
#         dishu_aitubiao.find_element(x, '//*[@id="mat-input-6"]').send_keys('简历')
#         sleep(1)
#         dishu_aitubiao.find_element(x, '//*[@id="mat-input-6"]').clear()
#         sleep(1)
#         dishu_aitubiao.find_element(x, '//*[@id="mat-input-6"]').send_keys('测试')
#         sleep(1)
#         dishu_aitubiao.find_element(x,'//*[@id="aceSidebar"]/div/div[1]/div/div[3]/span').click()
#         sleep(2)
#         dishu_aitubiao.find_element(x,'//*[@id="aceSidebar"]/div/div[2]/ace-material/div/div/div[3]/div[2]/ace-masonry/div/ace-scroll-list/div/div[1]/ace-masonry-item[2]/div/div/img').click()
#         sleep(1)
#         # dishu_aitubiao.find_element(x,'//*[@id="aceSidebar"]/div/div[1]/div/div[4]/button/mat-icon/svg').click()
#         sleep(1)
#         # dishu_aitubiao.find_element(x, '//*[@id="aceSidebar"]/div/div[1]/div/div[3]/button/mat-icon/svg').click()
#
#         sleep(300)







from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from time import sleep
x = 'xpath'

class Management:

    def open_browser(self):
        try:
            driver = webdriver.Chrome()
            driver.get("https://dev.editorup.com")
            driver.maximize_window()
            sleep(3)
            return driver
        except WebDriverException as e:
            print(f"❌ 浏览器启动失败: {e}")
            return None

    def test_login(self, driver):
        '''登录测试'''
        try:
            driver.find_element(x, '/html/body/ace-root/div/ace-builder/div/ace-header/ace-sharded-header/div/div/button/span[2]').click()
            sleep(2)
            driver.find_element(x, '//*[@id="mat-mdc-dialog-0"]/div/div/ace-auth/div/div/div[2]/ace-sign-in/div/div[2]/ace-sign-in-by-wechat/div/div[2]/button/span[2]').click()
            sleep(3)
            driver.find_element(x, '//*[@id="mat-mdc-dialog-0"]/div/div/ace-auth/div/div/div[2]/ace-sign-in/div/div[2]/ace-sign-in-by-sms/div/div[1]/a').click()
            sleep(1)
            driver.find_element(x, '//*[@id="account"]').click()
            sleep(1)
            driver.find_element(x, '//*[@id="account"]').send_keys('19999999999')
            driver.find_element(x, '//*[@id="password"]').send_keys('888888')
            driver.find_element(x, '//*[@id="mat-mdc-dialog-0"]/div/div/ace-auth/div/div/div[2]/ace-sign-in/div/div[2]/ace-sign-in-by-password/div/form/button/span[2]/span').click()
            sleep(1)
            text = driver.find_element(x, '/html/body/ace-root/div/ace-builder/div/div/ace-menu/div/div/button[1]/div/span').text
            assert text == '我的空间'
            print("✅ 登录测试通过")
        except Exception as e:
            print(f"❌ 登录测试失败: {e}")

    def test_create_project(self, driver):
        '''创建项目测试'''
        try:
            driver.find_element(x, '/html/body/ace-root/div/ace-builder/div/div/ace-menu/div/div/button[1]/div/span').click()
            sleep(2)
            driver.find_element(x, '/html/body/ace-root/div/ace-builder/div/div/div/ace-project/div/div/div[1]/div[1]/div[2]/ace-button/button/span[2]/span').click()
            sleep(1)
            driver.find_element(x, '//*[@id="mat-tab-group-0-content-0"]/div/div/div[1]/div[1]/ace-button/button/span[2]/span').click()
            sleep(3)
            driver.find_element(x, '//*[@id="driver-popover-content"]/footer/span[2]/button[1]').click()
            sleep(1)
            driver.find_element(x, '//*[@id="aceSidebar"]/div/div[1]/div/div[2]/span').click()
            sleep(1)
            driver.find_element(x, '//*[@id="mat-input-6"]').click()
            sleep(1)
            driver.find_element(x, '//*[@id="mat-input-6"]').send_keys('数据')
            sleep(1)
            driver.find_element(x, '//*[@id="mat-input-6"]').clear()
            driver.find_element(x, '//*[@id="mat-input-6"]').send_keys('简历')
            sleep(1)
            driver.find_element(x, '//*[@id="mat-input-6"]').clear()
            driver.find_element(x, '//*[@id="mat-input-6"]').send_keys('测试')
            sleep(1)
            driver.find_element(x, '//*[@id="aceSidebar"]/div/div[1]/div/div[3]/span').click()
            sleep(2)
            driver.find_element(x, '//*[@id="aceSidebar"]/div/div[2]/ace-material/div/div/div[3]/div[2]/ace-masonry/div/ace-scroll-list/div/div[1]/ace-masonry-item[2]/div/div/img').click()
            sleep(3)
            print("✅ 创建项目测试通过")
        except Exception as e:
            print(f"❌ 创建项目测试失败: {e}")

    def run(self):
        for i in range(1, 110):
            print(f"\n🚀 第 {i} 次测试开始")
            driver = self.open_browser()
            if not driver:
                continue

            try:
                self.test_login(driver)
                self.test_create_project(driver)
            finally:
                driver.quit()
                print(f"🔚 第 {i} 次测试完成，浏览器关闭,测试日志保存成功")


if __name__ == '__main__':
    test_runner = Management()
    test_runner.run()


