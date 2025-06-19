import requests, json, os, time, re
from datetime import datetime

LIST_URL   = "https://api.editorup.com/api/v1/resource/templates"
DETAIL_URL = "https://api.editorup.com/api/v1/resource/templates/{id}"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://app.editorup.com",
    "Referer": "https://app.editorup.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

limit, delay = 100, 0.15
page, total  = 1, 1
templates    = []

SAVE_COUNT = "5"   # 设置为 "all" 表示全部保存；设置为整数如 10 表示只保存前 10 个

# 拉取模板列表
while (page - 1) * limit < total:
    r = requests.get(LIST_URL,
                     params={"sortBy":"default","page":page,"limit":limit,"tags":""},
                     headers=headers)
    j = r.json();  r.raise_for_status()
    if j["code"]: raise RuntimeError(j)
    templates += j["data"]["list"]
    total = j["data"]["total"]; page += 1

print(f"共 {len(templates)} 个模板")

# 限制保存数量
if SAVE_COUNT != "all":
    try:
        SAVE_COUNT = int(SAVE_COUNT)
        templates = templates[:SAVE_COUNT]
        print(f"⚠️  只保存前 {SAVE_COUNT} 个模板")
    except:
        raise ValueError("SAVE_COUNT 必须是整数或 'all'")

# 创建带时间戳的输出目录
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
out_dir = f"mobanData_{timestamp}"
os.makedirs(out_dir, exist_ok=True)

# 清理文件名
def safe_name(text):
    return re.sub(r"[^\w\-\.一-龥]", "_", text)[:80]

# 保存模板
for i, tpl in enumerate(templates, 1):
    tpl_id, title = tpl["id"], tpl["title"]
    try:
        d = requests.get(DETAIL_URL.format(id=tpl_id), headers=headers).json()
        fname = f"{tpl_id}_{safe_name(title)}.json"
        with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, separators=(",", ":"))
        print(f"{i:>4}/{len(templates)} ✔ 写入 {fname}")
    except Exception as e:
        print(f"{i:>4}/{len(templates)} ✖ 失败 ({tpl_id}): {e}")
    time.sleep(delay)

print(f"\n✅ 完成！模板详情保存在： ./{out_dir}/")
