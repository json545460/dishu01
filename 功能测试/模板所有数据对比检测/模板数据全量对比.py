# import os, json, requests
# from glob import glob
#
# DETAIL_URL = "https://api.editorup.com/api/v1/resource/templates/{id}"
# headers = {
#     "Accept": "application/json, text/plain, */*",
#     "Origin": "https://app.editorup.com",
#     "Referer": "https://app.editorup.com/",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }
#
# # 📁 本地 JSON 文件目录
# LOCAL_JSON_DIR = "./mobanData_20250611_111058"
# # LOCAL_JSON_DIR = "./mobanData_20250611_120422"
#
# IGNORED_KEYS = {
#     "/data/dimension",
#     "/data/height",
#     "/data/width",
#     "/data/updatedAt",
#     "/msg"
# }
#
# PRINT_KEYS = [
#     "/data/title",
#     "/data/priceStrategy",
#     "/data/snapshot",
#     "/data/tags",
#     "/data/author",
#     "/data/data/pages",
#     "/data/data/orders"
# ]
#
# def load_json(path):
#     with open(path, encoding="utf-8") as f:
#         return json.load(f)
#
# def get_by_path(data, path):
#     keys = path.strip("/").split("/")
#     for k in keys:
#         if isinstance(data, dict):
#             data = data.get(k)
#         else:
#             return None
#     return data
#
# def find_differences(local, remote, prefix=""):
#     diffs = []
#     if isinstance(local, dict) and isinstance(remote, dict):
#         keys = set(local.keys()) | set(remote.keys())
#         for k in keys:
#             path = f"{prefix}/{k}"
#             if path in IGNORED_KEYS:
#                 continue
#             lv = local.get(k)
#             rv = remote.get(k)
#             diffs.extend(find_differences(lv, rv, path))
#     elif isinstance(local, list) and isinstance(remote, list):
#         if local != remote:
#             diffs.append((prefix, local, remote))
#     else:
#         if local != remote:
#             diffs.append((prefix, local, remote))
#     return diffs
#
# def print_field(data, path):
#     val = get_by_path(data, path)
#     print(f"     • {path} : {repr(val)}")
#
# # ❗目录检查
# if not os.path.isdir(LOCAL_JSON_DIR):
#     print(f"❌ 错误：目录不存在 - {LOCAL_JSON_DIR}")
#     exit(1)
#
# files = glob(os.path.join(LOCAL_JSON_DIR, "*.json"))
# if not files:
#     print(f"❌ 错误：目录中未找到任何 JSON 文件 - {LOCAL_JSON_DIR}")
#     exit(1)
#
# # 🔍 开始对比
# print(f"\n📂 待对比文件数：{len(files)}\n")
#
# pass_cnt, fail_cnt = 0, 0
# fail_detail = []
#
# for idx, filepath in enumerate(files, 1):
#     local_json = load_json(filepath)
#     tpl_id = get_by_path(local_json, "/data/id")
#     title = get_by_path(local_json, "/data/title")
#     try:
#         r = requests.get(DETAIL_URL.format(id=tpl_id), headers=headers, timeout=10)
#         r.raise_for_status()
#         remote_json = r.json()
#     except Exception as e:
#         print(f"{idx:>3}/{len(files)} ❌ 请求失败 - ID:{tpl_id} - {e}")
#         fail_cnt += 1
#         continue
#
#     diffs = find_differences(local_json, remote_json)
#
#     if diffs:
#         fail_cnt += 1
#         print(f"{idx:>3}/{len(files)} ❌ 不通过 - ID:{tpl_id}")
#         for path, local_val, remote_val in diffs[:10]:
#             print(f"     • {path}")
#             print(f"         本地值 : {repr(local_val)}")
#             print(f"         线上值 : {repr(remote_val)}")
#         if len(diffs) > 10:
#             print(f"     … 其余 {len(diffs)-10} 条差异省略")
#         fail_detail.append({
#             "id": tpl_id,
#             "title": title,
#             "diffs": diffs[:10]
#         })
#     else:
#         pass_cnt += 1
#         print(f"{idx:>3}/{len(files)} ✅ 通过   - ID:{tpl_id}")
#         for path in PRINT_KEYS:
#             print_field(local_json, path)
#
# # ✅ 汇总
# print("\n================  汇  总  ================ ")
# print(f"总模板数   : {len(files)}")
# print(f"通过数量   : {pass_cnt}")
# print(f"不通过数量 : {fail_cnt}")
#
# if fail_detail:
#     print("\n🚨 不通过模板详情：")
#     for item in fail_detail:
#         tpl_id = item['id']
#         print(f"\n❌ 模板标题: {item['title']}")
#         print(f"   模板 ID : {tpl_id}")
#         for path, lv, rv in item["diffs"]:
#             field = path.strip("/").split("/")[-1]
#             page_id, element_id = extract_ids_from_path(path)
#             prefix = f"[模板ID:{tpl_id}]"
#             if page_id:
#                 prefix += f" [页面ID:{page_id}]"
#             if element_id:
#                 prefix += f" [素材ID:{element_id}]"
#             print(f"  {prefix} 差异字段: {path}")
#             print(f"  {prefix} {field} : 本地数据 {repr(lv)} ≠ 接口返回 {repr(rv)}")
#






import os, json, requests
from glob import glob

DETAIL_URL = "https://api.editorup.com/api/v1/resource/templates/{id}"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://app.editorup.com",
    "Referer": "https://app.editorup.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# 📁 本地 JSON 文件目录
LOCAL_JSON_DIR = "./mobanData_20250612_101229"


IGNORED_KEYS = {
    "/data/dimension",
    "/data/height",
    "/data/width",
    "/data/updatedAt",
    "/msg"
}

PRINT_KEYS = [
    "/data/title",
    "/data/priceStrategy",
    "/data/snapshot",
    "/data/tags",
    "/data/author",
    "/data/data/pages",
    "/data/data/orders"
]

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def get_by_path(data, path):
    keys = path.strip("/").split("/")
    for k in keys:
        if isinstance(data, dict):
            data = data.get(k)
        else:
            return None
    return data

def find_differences(local, remote, prefix=""):
    diffs = []
    if isinstance(local, dict) and isinstance(remote, dict):
        keys = set(local.keys()) | set(remote.keys())
        for k in keys:
            path = f"{prefix}/{k}"
            if path in IGNORED_KEYS:
                continue
            lv = local.get(k)
            rv = remote.get(k)
            diffs.extend(find_differences(lv, rv, path))
    elif isinstance(local, list) and isinstance(remote, list):
        if local != remote:
            diffs.append((prefix, local, remote))
    else:
        if local != remote:
            diffs.append((prefix, local, remote))
    return diffs

def print_field(data, path):
    val = get_by_path(data, path)
    print(f"     • {path} : {repr(val)}")

def extract_ids_from_path(path):
    # path: "/data/data/pages/{pageId}/elements/{elementId}/..."
    parts = path.strip("/").split("/")
    page_id = None
    element_id = None
    try:
        if "pages" in parts:
            idx = parts.index("pages")
            page_id = parts[idx + 1]
        if "elements" in parts:
            idx = parts.index("elements")
            element_id = parts[idx + 1]
    except IndexError:
        pass
    return page_id, element_id

# ❗目录检查
if not os.path.isdir(LOCAL_JSON_DIR):
    print(f"❌ 错误：目录不存在 - {LOCAL_JSON_DIR}")
    exit(1)

files = glob(os.path.join(LOCAL_JSON_DIR, "*.json"))
if not files:
    print(f"❌ 错误：目录中未找到任何 JSON 文件 - {LOCAL_JSON_DIR}")
    exit(1)

# 🔍 开始对比
print(f"\n📂 待对比文件数：{len(files)}\n")

pass_cnt, fail_cnt = 0, 0
fail_detail = []

for idx, filepath in enumerate(files, 1):
    local_json = load_json(filepath)
    tpl_id = get_by_path(local_json, "/data/id")
    title = get_by_path(local_json, "/data/title")
    try:
        r = requests.get(DETAIL_URL.format(id=tpl_id), headers=headers, timeout=10)
        r.raise_for_status()
        remote_json = r.json()
    except Exception as e:
        print(f"{idx:>3}/{len(files)} ❌ 请求失败 - ID:{tpl_id} - {e}")
        fail_cnt += 1
        continue

    diffs = find_differences(local_json, remote_json)

    if diffs:
        fail_cnt += 1
        print(f"{idx:>3}/{len(files)} ❌ 不通过 - ID:{tpl_id}")
        for path, local_val, remote_val in diffs[:10]:
            page_id, element_id = extract_ids_from_path(path)
            prefix = f"[模板ID:{tpl_id}]"
            if page_id:
                prefix += f" [页面ID:{page_id}]"
            if element_id:
                prefix += f" [素材ID:{element_id}]"
            field = path.strip("/").split("/")[-1]
            print(f"  {prefix} 差异字段: {path}")
            print(f"  {prefix} {field} : 本地数据 {repr(local_val)} ≠ 接口返回 {repr(remote_val)}")
        if len(diffs) > 10:
            print(f"     … 其余 {len(diffs)-10} 条差异省略")
        fail_detail.append({
            "id": tpl_id,
            "title": title,
            "diffs": diffs[:10]
        })
    else:
        pass_cnt += 1
        print(f"{idx:>3}/{len(files)} ✅ 通过   - ID:{tpl_id}")
        for path in PRINT_KEYS:
            print_field(local_json, path)

# ✅ 汇总
print("\n================  汇  总  ================ ")
print(f"总模板数   : {len(files)}")
print(f"通过数量   : {pass_cnt}")
print(f"不通过数量 : {fail_cnt}")

if fail_detail:
    print("\n🚨 不通过模板详情：")
    for item in fail_detail:
        tpl_id = item['id']
        print(f"\n❌ 模板标题: {item['title']}")
        print(f"  模板 ID: {tpl_id}")
        for path, lv, rv in item["diffs"]:
            page_id, element_id = extract_ids_from_path(path)
            prefix = f"[模板ID:{tpl_id}]"
            if page_id:
                prefix += f" [页面ID:{page_id}]"
            if element_id:
                prefix += f" [素材ID:{element_id}]"
            field = path.strip("/").split("/")[-1]
            print(f"  ID 定位: {prefix}")
            print(f"  差异位置: {path}")
            print(f"  差异数据: 本地数据 {repr(lv)} ≠ 接口返回 {repr(rv)}")


