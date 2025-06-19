import requests
import openpyxl

# ========== 配置 ==========
EXCEL_PATH = r"D:\install\python-put\dishu_atb\功能测试\模板检测\moban.xlsx"
SEARCH_URL = "https://api.editorup.com/api/v1/resource/templates"

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://dev.editorup.com",
    "Referer": "https://dev.editorup.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def search_template_ids(name):
    params = {
        "keyword": name,
        "tags": "",
        "sortBy": "default",
        "priceStrategy": "all",
        "style": "all",
        "page": 1,
        "limit": 100
    }
    r = requests.get(SEARCH_URL, params=params, headers=HEADERS)
    j = r.json()
    if j.get("code") == 0:
        return [(item["id"], item["title"]) for item in j["data"]["list"]]
    return []

# ========== 主程序 ==========
if __name__ == "__main__":
    wb = openpyxl.load_workbook(EXCEL_PATH)
    sheet = wb.active
    rows = list(sheet.iter_rows(min_row=2, values_only=True))

    failed = []

    for i, row in enumerate(rows, start=1):
        name = str(row[0]).strip()
        results = search_template_ids(name)

        print(f"[{i}] Excel模板名：{name}")

        if results:
            print("    🔍 搜索结果：")
            for tpl_id, title in results:
                print(f"       - 模板名：{title}（ID: {tpl_id}）")

            matched = any(name in title or title in name for _, title in results)
            if matched:
                print("    ✅ 匹配成功")
            else:
                print("    ❌ 匹配失败")
                failed.append(name)
        else:
            print("    ❌ 未搜索到任何模板")
            failed.append(name)

        print("-" * 60)

    print("\n====== 匹配失败汇总 ======")
    print(f"❌ 匹配失败数：{len(failed)}")
    if failed:
        for name in failed:
            print(f"❗ 未匹配模板名：{name}")



