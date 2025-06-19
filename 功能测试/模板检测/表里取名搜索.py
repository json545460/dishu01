import requests
import openpyxl
import time

# ========== 配置 ==========
EXCEL_PATH = r"D:\install\python-put\dishu_atb\功能测试\模板检测\moban.xlsx"
ONLY_FIRST_N = None                 # 设为数字可只处理前 N 个
# DETAIL_URL  = "https://api.editorup.com/api/v1/resource/templates/{}"
# SEARCH_URL  = "https://api.editorup.com/api/v1/resource/templates"

DETAIL_URL = "https://api.aitubiao.com/api/v1/resource/templates/{}"
SEARCH_URL = "https://api.aitubiao.com/api/v1/resource/templates"

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    # "Origin": "https://dev.editorup.com",
    # "Referer": "https://dev.editorup.com/",

    "Origin": "https://app.aitubiao.com",
    "Referer": "https://app.aitubiao.com/",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# ========== 读取 Excel 模板名称 ==========
def read_template_names(path, limit=ONLY_FIRST_N):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    names = []

    for row in sheet.iter_rows(min_row=2, max_col=1, values_only=True):
        if row[0]:
            names.append(str(row[0]).strip())
        if limit and len(names) >= limit:
            break
    return names

# ========== 搜索模板ID ==========
def search_template_by_name(name):
    params = {
        "keyword": name,
        "tags": "",
        "sortBy": "default",
        "priceStrategy": "all",
        "style": "all",
        "page": 1,
        "limit": 10
    }
    r = requests.get(SEARCH_URL, params=params, headers=HEADERS)
    j = r.json()
    if j.get("code") == 0 and j["data"]["list"]:
        return j["data"]["list"][0]["id"]         # 返回第一个结果的 ID
    return None

# ========== 获取模板详情 ==========
def get_template_detail(template_id):
    r = requests.get(DETAIL_URL.format(template_id), headers=HEADERS)
    return r.json()

# ========== 主程序 ==========
if __name__ == "__main__":
    names = read_template_names(EXCEL_PATH)
    not_found = []                       # 用于收集没找到的模板名

    print(f"读取模板名称 {len(names)} 个：\n")
    for i, name in enumerate(names, 1):
        print(f"🔍 [{i}] 搜索模板名称：{name}")
        tpl_id = search_template_by_name(name)

        if tpl_id:
            print(f"    ✅ 模板ID：{tpl_id}")
            detail = get_template_detail(tpl_id)
            if detail["code"] == 0:
                print("    📦 模板数据：")
                print(detail["data"])
            else:
                print(f"    ❌ 获取详情失败：{detail}")
        else:
            print("    ❌ 未找到匹配模板")
            not_found.append(name)       # 记录缺失

        print("-" * 50)
        time.sleep(0.2)                  # 轻量限速，避免刷接口

    # ========== 汇总报告 ==========
    print("\n======================== 汇总 ========================\n")
    if not_found:
        print(f"❗️共 {len(not_found)} 个模板未找到：")
        for idx, n in enumerate(not_found, 1):
            print(f"{idx}. {n}")
    else:
        print("🎉 所有模板均已成功匹配！")


