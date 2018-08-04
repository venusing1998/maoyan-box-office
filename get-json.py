import json
import os

import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "dist")


def get_html():
    """获取网页源代码

    """
    url = "https://box.maoyan.com/promovie/api/box/second.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = json.dumps(response.json(), indent=4, ensure_ascii=False)
            return result
    except requests.ConnectionError:
        print(e)


def write_into_file(result):
    """写入文件

    """
    if not os.path.exists(DIST_DIR):
        os.makedirs(DIST_DIR)
    with open("dist/result.json", "w", encoding="utf-8") as f:
        f.write(result)


def main():
    """主函数

    """
    result = get_html()
    write_into_file(result)


if __name__ == "__main__":
    main()