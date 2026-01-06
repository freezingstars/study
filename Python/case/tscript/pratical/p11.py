import time
import requests
from bs4 import BeautifulSoup

with open("movie_titles.txt", "w", encoding="utf-8") as f:
    for i in range(0, 250, 25):
        url = f"https://movie.douban.com/top250?start={i}"
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        time.sleep(1)

        soup = BeautifulSoup(response.text, "lxml")
        movie_divs = soup.find_all("div", class_="hd")

        for div in movie_divs:
            titles = div.find_all("span", class_="title")
            if len(titles) == 2:
                trans_name = titles[0].get_text(strip=True)
                origin_name = titles[1].get_text(strip=True).replace("\xa0", "")
                line = f"{trans_name}"
            else:
                line = titles[0].get_text(strip=True)
            f.write(line + "\n")
