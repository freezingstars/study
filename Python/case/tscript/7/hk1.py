import time
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0'
}

for start_num in range(0, 250, 25):
    # 3.1 拼接分页URL，发送GET请求
    url = f"https://movie.douban.com/top250?start={start_num}&filter="
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # 非200状态码抛出异常
        time.sleep(1)  # 延时防反爬
    except requests.exceptions.RequestException as e:
        print(f"第{start_num//25 + 1}页请求失败：{e}")
        continue
    print(f"第{start_num // 25 + 1}页响应状态码：", response.status_code)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.find_all("span", attrs={"class": "title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)
