import requests

def login(account: str, password: str) -> dict:

    # 保存 token 的开关
    # save_to_file = True
    save_to_file = False

    url = "https://api.editorup.com/api/v1/auth/credential/login"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "account": account,
        "passwd": password
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # 抛出请求异常

        response_json = response.json()
        status_code = response.status_code

        if status_code == 201 and response_json.get("code") == 0:
            jwt_data = response_json.get("data", {}).get("jwt", {})
            token = jwt_data.get("token")
            refresh_token = jwt_data.get("refreshToken")

            if token:
                print("✅ 登录成功", "状态码:", status_code)
                print("返回内容:", response_json)

                if save_to_file:
                    with open("token.txt", "w") as f:
                        f.write(token)
                    print("✅ token 已保存到 token.txt")

                return {
                    "status_code": status_code,
                    "token": token,
                    "refreshToken": refresh_token
                }
            else:
                print("⚠️ 登录成功但未返回 token", "状态码:", status_code)
                return {"status_code": status_code}
        else:
            print("❌ 登录失败:", response_json, "状态码:", status_code)
            return {"status_code": status_code}
    except requests.exceptions.RequestException as e:
        print("❌ 请求出错:", str(e))
        return {"status_code": -1, "error": str(e)}

if __name__ == "__main__":
    result = login("18888888888", "asd123456")
    if "token" in result:
        print("token:", result["token"])
