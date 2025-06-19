import requests
import json
import uuid
from datetime import datetime

# 接口配置
BASE_URL = "https://api.editorup.com"
CREATE_PROJECT_ENDPOINT = "/APIautomation/v1/projects"  # 注意检查端点是否正确
URL = BASE_URL + CREATE_PROJECT_ENDPOINT

# 认证token
AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJjbWFuYnNkNHcwMDAzZTg2b3piaGp3aGxnIiwibmFtZSI6IjE4ODg4ODg4ODg4Iiwicm9sZSI6InZpcCIsImlhdCI6MTc0NzI5MTk3OCwiZXhwIjoxNzQ3Mjk1NTc4fQ.KDh8lb_MeaUR9KbWx5EWZmOeG9aKeK16rhtItL3KecY"

# 请求头
headers = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Referer": "https://dev.editorup.com/",
    "Origin": "https://dev.editorup.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}


def generate_unique_title():
    """生成带时间戳的唯一标题"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"测试项目_{timestamp}"


def test_create_project():
    """测试创建项目接口"""
    try:
        # 创建项目的请求数据（根据成功响应调整）
        payload = {
            "title": generate_unique_title(),
            "width": 960,
            "height": 540,
            "private": True
            # 根据API文档添加其他可选参数
        }

        print("请求数据：")
        print(json.dumps(payload, indent=2, ensure_ascii=False))

        response = requests.post(URL, headers=headers, json=payload)

        # 打印响应信息
        print(f"\n请求URL: {URL}")
        print(f"状态码: {response.status_code}")
        print("响应头:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")

        # 检查状态码
        if response.status_code == 200:
            print("\n项目创建成功！")
            response_data = response.json()
            print("\n响应数据:")
            print(json.dumps(response_data, indent=2, ensure_ascii=False))

            # 验证响应数据结构
            assert response_data.get("code") == 0, "code应为0"
            assert response_data.get("msg") == "ok", "msg应为'ok'"
            assert "data" in response_data, "响应应包含data字段"

            data = response_data["data"]
            required_fields = ["id", "title", "createdAt", "width", "height"]
            for field in required_fields:
                assert field in data, f"data应包含{field}字段"

            print("\n所有断言验证通过！")
            print(f"新项目ID: {data['id']}")
            print(f"创建时间: {data['createdAt']}")
        else:
            print(f"\n请求失败，状态码: {response.status_code}")
            print("错误详情:", response.text)

    except Exception as e:
        print(f"\n发生错误: {str(e)}")


if __name__ == "__main__":
    test_create_project()


