# ---------------------------------------------------------------------------------------------------------带相似模板名检测

# import requests
# import time
# import logging
# import json
# from collections import Counter
# from datetime import datetime
# from difflib import SequenceMatcher
# import os
# from tqdm import tqdm
#
# # ========== 配置 ==========
# LIST_URL = "https://api.aitubiao.com/api/v1/resource/templates"
# HEADERS = {
#     "Accept": "application/json, text/plain, */*",
#     "Origin": "https://app.aitubiao.com",
#     "Referer": "https://app.aitubiao.com/",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }
#
# # 日志配置
# LOG_DIR = "logs"
# if not os.path.exists(LOG_DIR):
#     os.makedirs(LOG_DIR)
# log_file = os.path.join(LOG_DIR, f"template_duplicate_check_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler(log_file, encoding='utf-8'),
#         logging.StreamHandler()
#     ]
# )
#
#
# # ========== 获取模板列表 ==========
# def get_templates():
#     all_templates = []
#     page = 1
#     page_size = 100
#     max_retries = 3
#     retry_delay = 1
#
#     while True:
#         params = {
#             "tags": "",
#             "sortBy": "default",
#             "priceStrategy": "all",
#             "style": "all",
#             "page": page,
#             "limit": page_size
#         }
#
#         for retry in range(max_retries):
#             try:
#                 r = requests.get(LIST_URL, params=params, headers=HEADERS)
#                 j = r.json()
#                 if j.get("code") == 0 and j["data"]["list"]:
#                     all_templates.extend(j["data"]["list"])
#                     if len(j["data"]["list"]) < page_size:
#                         return all_templates
#                     page += 1
#                     time.sleep(0.2)
#                     break
#                 else:
#                     logging.error(f"API返回错误: {j.get('message', '未知错误')}")
#                     return all_templates
#             except Exception as e:
#                 if retry < max_retries - 1:
#                     logging.warning(f"第{retry + 1}次请求失败，{retry_delay}秒后重试: {e}")
#                     time.sleep(retry_delay)
#                 else:
#                     logging.error(f"获取模板数据失败: {e}")
#                     return all_templates
#
#
# # ========== 检查重名 ==========
# def check_duplicates(templates):
#     names = [t["title"] for t in templates]
#     counter = Counter(names)
#     duplicates = {name: count for name, count in counter.items() if count > 1}
#     return duplicates
#
#
# # ========== 检查相似名称 ==========
# def check_similar_names(templates, similarity_threshold=0.8):
#     similar_pairs = []
#     names = [t["title"] for t in templates]
#
#     for i in range(len(names)):
#         for j in range(i + 1, len(names)):
#             similarity = SequenceMatcher(None, names[i], names[j]).ratio()
#             if similarity >= similarity_threshold:
#                 similar_pairs.append((names[i], names[j], similarity))
#
#     return similar_pairs
#
#
# # ========== 统计分类 ==========
# def analyze_categories(templates):
#     categories = Counter()
#     for template in templates:
#         for tag in template.get("tags", []):
#             categories[tag] += 1
#     return categories
#
#
# # ========== 导出结果 ==========
# def export_results(templates, duplicates, similar_pairs, categories):
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#
#     # 导出JSON
#     result = {
#         "total_templates": len(templates),
#         "duplicates": duplicates,
#         "similar_pairs": similar_pairs,
#         "categories": dict(categories)
#     }
#
#     with open(f"template_analysis_{timestamp}.json", "w", encoding="utf-8") as f:
#         json.dump(result, f, ensure_ascii=False, indent=2)
#
#     # 导出CSV
#     with open(f"template_list_{timestamp}.csv", "w", encoding="utf-8") as f:
#         f.write("标题,标签,创建时间\n")
#         for template in templates:
#             tags = ",".join(template.get("tags", []))
#             f.write(f"{template['title']},{tags},{template.get('createdAt', '')}\n")
#
#
# # ========== 主程序 ==========
# if __name__ == "__main__":
#     try:
#         logging.info("开始获取模板数据...")
#         templates = get_templates()
#         logging.info(f"共获取到 {len(templates)} 个模板")
#
#         # 检查重名
#         duplicates = check_duplicates(templates)
#         if duplicates:
#             logging.warning("发现重复的模板名：")
#             for name, count in duplicates.items():
#                 logging.warning(f"{name}: {count}次")
#         else:
#             logging.info("✅ 没有发现重复的模板名")
#
#         # 检查相似名称
#         similar_pairs = check_similar_names(templates)
#         if similar_pairs:
#             logging.warning("发现相似的模板名：")
#             for name1, name2, similarity in similar_pairs:
#                 logging.warning(f"{name1} 与 {name2} 相似度: {similarity:.2f}")
#
#         # 统计分类
#         categories = analyze_categories(templates)
#         logging.info("模板分类统计：")
#         for category, count in categories.most_common():
#             logging.info(f"{category}: {count}个")
#
#         # 导出结果
#         export_results(templates, duplicates, similar_pairs, categories)
#         logging.info("分析结果已导出到文件")
#
#     except Exception as e:
#         logging.error(f"程序执行失败: {e}", exc_info=True)






import requests
import time
from collections import Counter

# ========== 配置 ==========
LIST_URL = "https://api.aitubiao.com/api/v1/resource/templates"
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://app.aitubiao.com",
    "Referer": "https://app.aitubiao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# ========== 获取模板列表 ==========
def get_templates():
    all_templates = []
    page = 1
    page_size = 100
    while True:
        params = {
            "tags": "",
            "sortBy": "default",
            "priceStrategy": "all",
            "style": "all",
            "page": page,
            "limit": page_size
        }
        try:
            r = requests.get(LIST_URL, params=params, headers=HEADERS)
            j = r.json()
            if j.get("code") == 0 and j["data"]["list"]:
                all_templates.extend(j["data"]["list"])
                if len(j["data"]["list"]) < page_size:
                    break  # 最后一页
                page += 1
                time.sleep(0.2)  # 轻微限速，防止被封
            else:
                break
        except Exception as e:
            print(f"获取模板数据时发生错误: {e}")
            break
    return all_templates

# ========== 检查重名 ==========
def check_duplicates(templates):
    names = [t["title"] for t in templates]
    counter = Counter(names)
    duplicates = {name: count for name, count in counter.items() if count > 1}
    return duplicates

# ========== 主程序（带错误处理） ==========
if __name__ == "__main__":
    try:
        templates = get_templates()
        print(f"共获取到 {len(templates)} 个模板")
        duplicates = check_duplicates(templates)
        if duplicates:
            print("发现重复的模板名：")
            for name, count in duplicates.items():
                print(f"{name}: {count}次")
        else:
            print("✅ 没有发现重复的模板名")
    except Exception as e:
        print(f"程序执行失败: {e}")

