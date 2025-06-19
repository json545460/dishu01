import requests
import openpyxl
import time

# ========== 配置 ==========
EXCEL_PATH   = r"D:\install\python-put\dishu_atb\功能测试\模板检测\moban.xlsx"
ONLY_FIRST_N = None
DETAIL_URL   = "https://api.editorup.com/api/v1/resource/templates/{}"
SEARCH_URL   = "https://api.editorup.com/api/v1/resource/templates"

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://dev.editorup.com",
    "Referer": "https://dev.editorup.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Excel 第 14 列 → priceStrategy 映射
PRICE_MAP = {
    "会员": "paid",
    "免费": "free"
}

# ========== 读取 Excel ==========
def read_template_rows(path, limit=ONLY_FIRST_N):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    rows = []
    for excel_row in sheet.iter_rows(min_row=2, values_only=True):
        name = str(excel_row[0]).strip() if excel_row[0] else ""
        expect_flag = str(excel_row[13]).strip() if len(excel_row) >= 14 and excel_row[13] else ""
        if name:
            rows.append({"name": name, "expect_flag": expect_flag})
        if limit and len(rows) >= limit:
            break
    return rows

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
    j = requests.get(SEARCH_URL, params=params, headers=HEADERS).json()
    if j.get("code") == 0 and j["data"]["list"]:
        return j["data"]["list"][0]["id"]
    return None

# ========== 获取模板详情 ==========
def get_template_detail(template_id):
    return requests.get(DETAIL_URL.format(template_id), headers=HEADERS).json()

# ========== 主程序 ==========
if __name__ == "__main__":
    rows        = read_template_rows(EXCEL_PATH)
    successes   = []
    failures    = []

    print(f"读取模板名称 {len(rows)} 个：\n")
    print("序号 | 模板名                          | Excel | API实际 | 比对结果")
    print("-" * 70)

    for idx, row in enumerate(rows, 1):
        name         = row["name"]
        expect_flag  = row["expect_flag"]
        expect_value = PRICE_MAP.get(expect_flag, "").lower()  # 'paid' / 'free' / ''
        display_exp  = expect_flag or "（空）"

        tpl_id = search_template_by_name(name)

        if not tpl_id:
            result = "未找到模板"
            print(f"{idx:<4}| {name:<30}| {display_exp:<8}| —       | {result}")
            failures.append({
                "name": name, "expect": display_exp, "actual": "—", "reason": "not_found"
            })
            time.sleep(0.2)
            continue

        detail = get_template_detail(tpl_id)
        if detail["code"] != 0:
            result = "详情错误"
            print(f"{idx:<4}| {name:<30}| {display_exp:<8}| —       | {result}")
            failures.append({
                "name": name, "expect": display_exp, "actual": "—", "reason": "detail_error"
            })
            time.sleep(0.2)
            continue

        actual_value  = detail["data"].get("priceStrategy", "").lower()
        display_act   = actual_value or "（空）"

        if expect_value and actual_value != expect_value:
            result = "异常"
            failures.append({
                "name": name, "expect": display_exp, "actual": display_act, "reason": "price_mismatch"
            })
        else:
            result = "OK"
            successes.append(name)

        print(f"{idx:<4}| {name:<30}| {display_exp:<8}| {display_act:<7}| {result}")
        time.sleep(0.2)

    # ========== 汇总 ==========
    total   = len(rows)
    success = len(successes)
    fail    = len(failures)

    print("\n======================== 汇总 ========================\n")
    print(f"总数：{total} | ✅ 成功：{success} | ❌ 失败：{fail}\n")

    if failures:
        print("❌ 失败详情：")
        for i, f in enumerate(failures, 1):
            print(f"{i}. {f['name']} | 表: {f['expect']} | 实际: {f['actual']} | 原因: {f['reason']}")
    else:
        print("🎉 全部模板通过校验！")


