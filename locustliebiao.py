# from locust import HttpUser, TaskSet, task, between, constant_pacing
#
#
# class UserBehavior(TaskSet):
#     headers = {
#         "accept": "application/json, text/plain, */*",
#         "accept-language": "zh",
#         # "referer": "https://dev.editorup.com/",
#         "referer": "https://api.editorup.com/api/v1/version",
#         "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": '"Windows"',
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
#     }
#
#     @task
#     def get_templates(self):
#         params = {
#             "tags": "",
#             "sortBy": "default",
#             "priceStrategy": "all",
#             "style": "all",
#             "page": 1,
#             "limit": 10
#         }
#         self.client.get("/api/v1/resource/templates", headers=self.headers, params=params)
#
# class WebsiteUser(HttpUser):
#     tasks = [UserBehavior]
#     # wait_time = between(1, 2)
#     wait_time = constant_pacing(0.01)
#     # host = "https://api.editorup.com"
#     host = "https://api.editorup.com/api/v1/version"
# # locust -f locustliebiao.py


from locust import HttpUser, TaskSet, task, between, constant_pacing


class UserBehavior(TaskSet):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh",
        # "referer": "https://dev.editorup.com/",
        "referer": "https://api.editorup.com/api/v1/version",
        "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    }

    @task
    def get_templates(self):
        params = {
            "tags": "",
            "sortBy": "default",
            "priceStrategy": "all",
            "style": "all",
            "page": 1,
            "limit": 10
        }
        response = self.client.get("/api/v1/resource/templates", headers=self.headers, params=params)

        # 打印详细返回信息
        print("=== 请求响应详情 ===")
        print(f"状态码: {response.status_code}")
        print(f"请求 URL: {response.url}")
        try:
            print("响应 JSON 数据:")
            print(response.json())
        except Exception as e:
            print("无法解析为 JSON，响应文本如下:")
            print(response.text)
        print("===================")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # wait_time = between(1, 2)
    wait_time = constant_pacing(0.01)
    host = "https://api.editorup.com/api/v1/version"
