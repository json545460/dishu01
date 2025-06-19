import requests
import openpyxl
import time

# ========== 配置 ==========
EXCEL_PATH = r"D:\install\python-put\dishu_atb\功能测试\模板检测\moban.xlsx"
ONLY_FIRST_N = None
DETAIL_URL = "https://api.editorup.com/api/v1/resource/templates/{}"
SEARCH_URL = "https://api.editorup.com/api/v1/resource/templates"

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://dev.editorup.com",
    "Referer": "https://dev.editorup.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# ========== 工具函数 ==========
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
        for item in j["data"]["list"]:
            if item["title"].strip() == name.strip():
                return item["id"]
    return None

def get_template_detail(template_id):
    r = requests.get(DETAIL_URL.format(template_id), headers=HEADERS)
    return r.json()

# ========== 主程序 ==========
if __name__ == "__main__":
    wb = openpyxl.load_workbook(EXCEL_PATH)
    sheet = wb.active

    passed = []
    failed = []

    rows = list(sheet.iter_rows(min_row=2, values_only=True))
    if ONLY_FIRST_N:
        rows = rows[:ONLY_FIRST_N]

    print(f"共读取 {len(rows)} 个模板进行检测：\n")

    for i, row in enumerate(rows, start=1):
        name = str(row[0]).strip()
        excel_tag = str(row[3]).strip() if row[3] else ""
        tpl_id = search_template_by_name(name)

        print(f"[{i}] 模板名称：{name}")

        if tpl_id:
            print(f"    ✅ 模板ID：{tpl_id}")
            detail = get_template_detail(tpl_id)
            if detail["code"] == 0:
                api_tag = str(detail["data"].get("dimension", "")).strip()

                print(f"    📄 Excel标签（第4列）：{excel_tag}")
                print(f"    🌐 接口标签（dimension字段）：{api_tag}")

                if api_tag == excel_tag:
                    print(f"    ✅ 标签对比成功")
                    passed.append(name)
                else:
                    print(f"    ❌ 标签不一致")
                    failed.append({"name": name, "id": tpl_id, "excel": excel_tag, "api": api_tag})
            else:
                print(f"    ❌ 获取详情失败：{detail}")
                failed.append({"name": name, "id": tpl_id, "error": "详情接口失败"})
        else:
            print(f"    ❌ 未找到匹配模板")
            failed.append({"name": name, "id": None, "error": "未搜索到"})
        print("-" * 60)
        time.sleep(0.2)

    print("\n================== ✅ 检测结果汇总 ==================\n")
    print(f"✔ 匹配成功：{len(passed)} 个")
    print(f"❌ 匹配失败：{len(failed)} 个\n")

    if failed:
        for f in failed:
            print(f"❗ 模板名称：{f['name']}")
            print(f"   🆔 模板ID：{f['id']}")
            if "error" in f:
                print(f"   ⛔ 错误原因：{f['error']}")
            else:
                print(f"   📄 Excel标签：{f['excel']}")
                print(f"   🌐 接口标签：{f['api']}")
            print("-" * 40)
    else:
        print("🎉 所有模板标签均成功匹配！")

