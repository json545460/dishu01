# --------------------------------------------------------------------------------------------------------------Ai贝值修改

import psycopg2
import redis
import re

# PostgreSQL 配置
conn_info = {
    'host': 'gate.editorup.com',
    'port': 55432,
    'user': 'lmj#pg-for-test',
    'password': 'test2025',
    'dbname': 'core'
}

# Redis 配置
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0

# 是否手动输入用户 ID, True 为手动输入
dishu_user_id = False
# dishu_user_id = True

def detect_user_type(user_input):
    if re.match(r'^\d{11}$', user_input):  # 手机号
        return 'phone'
    elif re.match(r'^[^@]+@[^@]+\.[^@]+$', user_input):  # 邮箱
        return 'email'
    else:  # 用户名
        return 'name'

def choose_user_id_from_list(rows):
    print("🔍 搜索到多个匹配用户，选择一个：")
    for idx, row in enumerate(rows):
        print(f"{idx + 1}: 用户 ID = {row[0]}")
    while True:
        choice = input(f"输入要使用的序号（1~{len(rows)}）：").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(rows):
            return rows[int(choice) - 1][0]
        else:
            print("❌ 无效选择，请重新输入。")

def main():
    try:
        conn = psycopg2.connect(**conn_info)
        cursor = conn.cursor()
        print("✅ 已连接 PostgreSQL")

        if dishu_user_id:
            user_id = input("输入用户 ID：").strip()
            if not user_id:
                print("❌ 用户 ID 不能为空")
                return
        else:
            identity = input("✏️ 输入手机号、邮箱或用户名（默认手机号 18888888888）: ").strip()
            if not identity:
                identity = '18888888888'

            user_type = detect_user_type(identity)
            cursor.execute(f'SELECT "id" FROM studio."user" WHERE {user_type} = %s;', (identity,))
            rows = cursor.fetchall()
            if not rows:
                print("❌ 未查到用户")
                return
            if len(rows) == 1:
                user_id = rows[0][0]
            else:
                user_id = choose_user_id_from_list(rows)

            print(f'📌 用户 ID: {user_id}')

        # 查询 shellLeft
        cursor.execute('SELECT "shellLeft" FROM studio.user_profile WHERE "userId" = %s;', (user_id,))
        shell_row = cursor.fetchone()
        if shell_row is not None:
            print(f'💎 当前 shellLeft: {shell_row[0]}')
        else:
            print("⚠️ 未查到 shellLeft")
            return

        # Redis 处理 - 必须成功连接Redis，否则不能修改
        try:
            r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
            # 测试Redis连接
            r.ping()
            redis_key = f"user:profile:{user_id}"
            
            if r.exists(redis_key):
                print(f"🔍 发现Redis缓存：{redis_key}")
                print("💡 提示：RDS缓存可能会影响修改操作的成功性")
                confirm_clear = input(f"是否清除 Redis 缓存？(y/n，默认 y)：").strip().lower()
                if confirm_clear == 'n':
                    print("⚠️ 警告：不清除缓存可能导致修改失败")
                    confirm_continue = input("是否继续修改？(y/n，默认 n)：").strip().lower()
                    if confirm_continue != 'y':
                        print("👋 取消修改")
                        return  # 退出
                    else:
                        print("🚀 继续修改（不清除缓存）")
                else:
                    deleted = r.delete(redis_key)
                    if deleted:
                        print(f"🧹 已清除 Redis 缓存：{redis_key}")
                    else:
                        print(f"❌ 清除失败，Redis 键不存在：{redis_key}")
                        print("❌ 缓存清除失败，无法进行修改操作")
                        return  # 退出
            else:
                print(f"✅ Redis 中未找到缓存键：{redis_key}，无需清除")
        except Exception as re:
            print(f"❌ Redis 连接失败：{re}")
            print("❌ Redis连接失败，无法进行修改操作")
            print("💡 提示：修改数据库中的AI贝积分没有意义，因为缓存会影响实际效果")
            return  # 退出

        # 修改 shellLeft
        # 修改 shellLeft
        raw_input = input("❓ 是否修改 shellLeft？(y/n，默认 n，或直接输入新值)：").strip().lower()
        if raw_input == '' or raw_input == 'n':
            print("👋 取消修改")
            return
        elif raw_input == 'y':
            while True:
                new_value = input("✏️ 输入新的 shellLeft 值（整数）：").strip().lower()
                if new_value == '' or new_value == 'n':
                    print("👋 取消修改")
                    return
                elif new_value.isdigit():
                    new_value_int = int(new_value)
                    break
                else:
                    print("❌ 输入无效，必须为整数、n 或直接回车取消")
        elif raw_input.isdigit():
            new_value_int = int(raw_input)
        else:
            print("❌ 输入无效，必须为整数、y 或 n")
            return

        cursor.execute(
            'UPDATE studio.user_profile SET "shellLeft" = %s WHERE "userId" = %s;',
            (new_value_int, user_id)
        )
        conn.commit()
        print(f'✅ shellLeft 已更新为 {new_value_int}')

    except Exception as e:
        print(f"❌ 程序出错：{e}")

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    main()

