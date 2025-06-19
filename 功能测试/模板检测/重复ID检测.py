import requests

# dev接口地址
LIST_URL = "https://api.editorup.com/api/v1/resource/templates"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://dev.editorup.com",
    "Referer": "https://dev.editorup.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

limit = 100
page = 1
total = 1
templates = []
id_set = set()
duplicate_ids = set()

# 拉取模板列表（自动翻页）
while (page - 1) * limit < total:
    params = {
        "sortBy": "default",
        "page": page,
        "limit": limit,
        "tags": ""
    }
    r = requests.get(LIST_URL, params=params, headers=headers)
    r.raise_for_status()
    j = r.json()
    if j["code"] != 0:
        raise RuntimeError(f"列表接口错误：{j}")

    batch = j["data"]["list"]
    total = j["data"]["total"]

    print(f"📥 第 {page} 页：{len(batch)} 条（累计 {len(templates) + len(batch)}/{total}）")

    # 检查重复 ID
    for tpl in batch:
        if tpl["id"] in id_set:
            duplicate_ids.add(tpl["id"])
        else:
            id_set.add(tpl["id"])
        templates.append(tpl)

    page += 1

print(f"\n✅ 列表拉取完毕，共 {len(templates)} 个模板")

# 打印模板ID和名称
# print("\n模板ID\t\t                模板名称")
# for tpl in templates:
#     print(f"{tpl['id']}\t{tpl['title']}")

# 打印重复 ID（如果有）
if duplicate_ids:
    print(f"\n⚠️ 发现重复的模板ID，共 {len(duplicate_ids)} 个：")
    for dup_id in duplicate_ids:
        print(f"- {dup_id}")
else:
    print("\n✅ 没有发现重复的模板ID")
