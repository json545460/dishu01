# import requests
# import time
# # # dev2
# LIST_URL   = "https://api2.editorup.com/api/v1/resource/templates"
# DETAIL_URL = "https://api2.editorup.com/api/v1/resource/templates/{id}"
#
# # dev
# # LIST_URL   = "https://api.editorup.com/api/v1/resource/templates"
# # DETAIL_URL = "https://api.editorup.com/api/v1/resource/templates/{id}"
#
# # 线上
# # LIST_URL   = "https://api.aitubiao.com/api/v1/resource/templates"
# # DETAIL_URL = "https://api.aitubiao.com/api/v1/resource/templates/{id}"
#
#
# headers = {
#     "Accept": "application/json, text/plain, */*",
#     # dev2
#     "Origin": "https://dev2.editorup.com",
#     "Referer": "https://dev2.editorup.com/",
#
#     # dev
#     # "Origin": "https://dev.editorup.com",
#     # "Referer": "https://dev.editorup.com/",
#
#     # # 线上
#     # "Origin": "https://app.editorup.com",
#     # "Referer": "https://app.editorup.com/",
#
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }
#
# limit = 100        # 每页条数
# delay = 0.15      # 请求详情的间隔
# page  = 1
# total = 1
# templates = []    # 所有模板
#
# # ① 拉取模板列表（自动翻页）
# while (page - 1) * limit < total:
#     params = {
#         "sortBy": "default",
#         "page"  : page,
#         "limit" : limit,
#         "tags"  : ""
#     }
#     r = requests.get(LIST_URL, params=params, headers=headers)
#     r.raise_for_status()
#     j = r.json()
#     if j["code"] != 0:
#         raise RuntimeError(f"列表接口错误：{j}")
#
#     batch = j["data"]["list"]
#     total  = j["data"]["total"]
#
#     print(f"📥 第 {page} 页：{len(batch)} 条（累计 {len(templates)+len(batch)}/{total}）")
#     templates.extend(batch)
#     page += 1
#
# print(f"\n✅ 列表拉取完毕，共 {len(templates)} 个模板\n")
#
# # ② 检测每个模板
# has_empty   = []   # [(id,title)]
# no_empty    = []   # [(id,title)]
#
# print("🔍 开始检测每个模板页面 orders 是否为空 ...\n")
#
# for idx, tpl in enumerate(templates, 1):
#     tpl_id    = tpl["id"]
#     tpl_title = tpl["title"]
#
#     detail = requests.get(DETAIL_URL.format(id=tpl_id), headers=headers).json()
#     if detail["code"] != 0:
#         print(f"{idx:>3}/{len(templates)} ❌ 获取失败：{tpl_title}")
#         continue
#
#     pages  = detail["data"]["data"].get("pages", {})
#     empty_flag = False
#     for page_id, page_data in pages.items():
#         if not page_data.get("orders"):          # 发现空 orders
#             empty_flag = True
#             print(f"{idx:>3}/{len(templates)} ⚠️  检测不通过   - 《{tpl_title}》 page_id={page_id}")
#             has_empty.append((tpl_id, tpl_title))
#             break
#
#     if not empty_flag:
#         print(f"{idx:>3}/{len(templates)} ✅  检测通过     - 《{tpl_title}》")
#         no_empty.append((tpl_id, tpl_title))
#
#     time.sleep(delay)
#
# # ③ 汇总
# print("\n==================  汇  总  ==================")
# print(f"模板总数               : {len(templates)}")
# print(f"存在空 page orders 模板 : {len(has_empty)}")
# print(f"无空 page orders 模板   : {len(no_empty)}")
#
# if has_empty:
#     print("\n📋 详细（空 orders）：")
#     for tid, tname in has_empty:
#         print(f"  - {tname}  (模板id: {tid})")
#
# # if no_empty:
# #     print("\n📋 详细（无空 orders）：")
# #     for tid, tname in no_empty:
# #         print(f"  - {tname}  (模板id: {tid})")
# #
# # print("\n✅ 检测完成！")








import requests
import time

# dev
LIST_URL   = "https://api.editorup.com/api/v1/resource/templates"
DETAIL_URL = "https://api.editorup.com/api/v1/resource/templates/{id}"

# 线上
# LIST_URL   = "https://api.aitubiao.com/api/v1/resource/templates"
# DETAIL_URL = "https://api.aitubiao.com/api/v1/resource/templates/{id}"


headers = {
    "Accept": "application/json, text/plain, */*",

    # dev
    "Origin": "https://dev.editorup.com",
    "Referer": "https://dev.editorup.com/",

    # 线上
    # "Origin": "https://app.aitubiao.com",
    # "Referer": "https://app.aitubiao.com/",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

limit = 100        # 每页条数
delay = 0.15      # 请求详情的间隔
page  = 1
total = 1
templates = []    # 所有模板

# ① 拉取模板列表（自动翻页）
while (page - 1) * limit < total:
    params = {
        "sortBy": "default",
        "page"  : page,
        "limit" : limit,
        "tags"  : ""
    }
    r = requests.get(LIST_URL, params=params, headers=headers)
    r.raise_for_status()
    j = r.json()
    if j["code"] != 0:
        raise RuntimeError(f"列表接口错误：{j}")

    batch = j["data"]["list"]
    total  = j["data"]["total"]

    print(f"📥 第 {page} 页：{len(batch)} 条（累计 {len(templates)+len(batch)}/{total}）")
    templates.extend(batch)
    page += 1

print(f"\n✅ 列表拉取完毕，共 {len(templates)} 个模板\n")

# ② 检测每个模板
has_empty   = []   # [(id,title)]
no_empty    = []   # [(id,title)]

print("🔍 开始检测每个模板页面 orders 是否为空 ...\n")

for idx, tpl in enumerate(templates, 1):
    tpl_id    = tpl["id"]
    tpl_title = tpl["title"]

    detail = requests.get(DETAIL_URL.format(id=tpl_id), headers=headers).json()
    if detail["code"] != 0:
        print(f"{idx:>3}/{len(templates)} ❌ 获取失败：{tpl_title}")
        continue

    pages  = detail["data"]["data"].get("pages", {})
    empty_flag = False
    for page_id, page_data in pages.items():
        if not page_data.get("orders"):          # 发现空 orders
            empty_flag = True
            print(f"{idx:>3}/{len(templates)} ⚠️  检测不通过   - 《{tpl_title}》 page_id={page_id}")
            has_empty.append((tpl_id, tpl_title))
            break

    if not empty_flag:
        print(f"{idx:>3}/{len(templates)} ✅  检测通过     - 《{tpl_title}》")
        no_empty.append((tpl_id, tpl_title))

    time.sleep(delay)

# ③ 汇总
print("\n==================  汇  总  ==================")
print(f"模板总数               : {len(templates)}")
print(f"存在空 page orders 模板 : {len(has_empty)}")
print(f"无空 page orders 模板   : {len(no_empty)}")

if has_empty:
    print("\n📋 详细（空 orders）：")
    for tid, tname in has_empty:
        print(f"  - {tname}  (模板id: {tid})")

