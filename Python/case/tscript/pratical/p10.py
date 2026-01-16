import requests
import json
import urllib3

# 禁用 SSL 警告（可选）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_github_user(username: str):
    url = f"https://api.github.com/users/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/vnd.github+json"
    }

    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()  # 自动抛出错误状态码异常
        data = response.json()

        # 规范输出
        print("=== GitHub 用户信息 ===")
        print(f"登录名: {data.get('login')}")
        print(f"昵称: {data.get('name')}")
        print(f"个人主页: {data.get('html_url')}")
        print(f"公司: {data.get('company')}")
        print(f"所在地: {data.get('location')}")
        print(f"公开仓库数: {data.get('public_repos')}")
        print(f"粉丝: {data.get('followers')}")
        print(f"关注: {data.get('following')}")
        print("======================")

        # 如果需要完整 JSON 输出（格式化）
        print("\n--- 完整 JSON 数据 ---")
        print(json.dumps(data, indent=4, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        print("请求失败:", e)


if __name__ == "__main__":
    get_github_user("freezingstars")   # 替换成你的 GitHub 用户名
