import sys
import os
# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# import unittest
# from unittestreport import TestRunner
# # 交互
# import tkinter as tk
# from tkinter import messagebox
# import sys
# root = tk.Tk()
# root.withdraw()
# response = messagebox.askokcancel("确认", "脚本加载完成，开始执行【镝数】自动化测试！")
# if response == True:
#     print("开始执行镝数自动化测试！")
# else:
#     print("取消执行镝数自动化测试！")
#     sys.exit()
#
# # 1，创建一个测试套件
# suite = unittest.TestSuite()
# # 2，创建一个用例加载器
# loader = unittest.TestLoader()
# from dishu_atb.APIautomation import dishu_api
# # 3，加载用例
# suite.addTest(loader.loadTestsFromModule(dishu_api))
#
# print("镝数自动化执行的用例数量:",suite.countTestCases())
# # with open('result.txt','w',encoding='utf-8') as f:
# #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
# #     runner.run(suite)
#
# runner = TestRunner(suite,
#                     filename="report.html",
#                     title='镝数项目管理测试报告数据看板',
#                     tester='李明进',
#                     desc="镝数项目测试生成的报告",
#                     templates=2
#                     )
# runner.run(thread_count=1)
#
# # 交互
# l_email = tk.Tk()
# l_email.withdraw()
# root.title("Confirmation Dialog")
# root.attributes("-topmost", True)
# label = tk.Label(root, text="Are you sure you want to continue?")
# label.pack(padx=10, pady=10)
# response = messagebox.askokcancel("确认", "自动化测试已完成，是否需要邮件发送【测试报告】？")
# if response == True:
#     print("发送测试报告代码执行中...")
# else:
#     print("已取消发送测试报告！")
#     sys.exit()
#
# # 发送邮件的方法
# try:
#     all1=['564491544@qq.com','934842487@qq.com']
#     a='564491544@qq.com'
#     runner.send_email(
#         host='smtp.gmail.com',
#         port=465,
#         user="mingjin.li520@gmail.com",
#         password='clqruvbvqlyxcpaw',
#         to_addrs = all1
#     )
# except:
#     print('\033[7;31m邮件发送失败\033[0m')
# else:
#     print('\033[7;32m邮件发送成功\033[0m')
#


import unittest
from unittestreport import TestRunner
import sys

# ✅ 控制是否手动确认开始测试
f_t = True  # True = 控制台询问，False = 直接开始

# === ① 启动确认 ===
if f_t:
    answer = input("❓ 脚本加载完成，是否开始执行【爱图表】自动化测试？(Y/n): ").strip().lower()
    if answer not in ["", "y", "yes"]:
        print("取消执行爱图表自动化测试！")
        sys.exit()
    print("开始执行爱图表自动化测试！")
else:
    print("自动化脚本已启动（跳过手动确认）")

# === ② 加载测试用例 ===
suite = unittest.TestSuite()
loader = unittest.TestLoader()
from dishu_atb.APIautomation import atb_api
suite.addTest(loader.loadTestsFromModule(atb_api))
print("爱图表自动化执行的用例数量:", suite.countTestCases())

# === ③ 执行测试 ===
# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 在脚本所在目录下创建reports文件夹
reports_dir = os.path.join(current_dir, 'reports')
if not os.path.exists(reports_dir):
    os.makedirs(reports_dir)
# 设置报告文件路径
report_path = os.path.join(reports_dir, 'report.html')

runner = TestRunner(
    suite,
    filename=report_path,
    title='"爱图表"APi测试报告',
    tester='李明进',
    desc="爱图表项目测试生成的报告",
    templates=2
)
runner.run(thread_count=1)
print(f"测试报告已经生成，报告路径为: {report_path}")

# === ④ 控制台确认是否发送邮件 ===
answer = input("❓ 自动化测试已完成，是否发送【测试报告】到指定邮箱？(Y/n): ").strip().lower()
if answer not in ["", "y", "yes"]:
    print("已取消发送测试报告！")
    sys.exit()
print("开始发送测试报告...")

# === ⑤ 执行邮件发送逻辑 ===

try:
    recipients = ['564491544@qq.com', 'huangwenjun@dyclub.org']
    # recipients = ['564491544@qq.com']
    runner.send_email(
        host='smtp.gmail.com',
        port=465,
        user="mingjin.li520@gmail.com",
        # password='clqruvbvqlyxcpaw',
        password='dxedrpydrxywevmb',
        to_addrs=recipients
    )

except Exception as e:
    print('\033[7;31m邮件发送失败\033[0m')
    print("错误信息：", e)
else:
    print('\033[7;32m邮件发送成功\033[0m')

