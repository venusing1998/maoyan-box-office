import os
import time

import requests


def get_html():
    """获取网页源代码

    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
        "X-Requested-With": "XMLHttpRequest",
    }
    url = "https://box.maoyan.com/promovie/api/box/second.json"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result
    except requests.ConnectionError as e:
        print(e)


def get_data(json):
    """获取数据

    """
    data = json.get("data")
    if data:
        list = data.get("list")
        if list:
            for item in list:
                contents = {}
                # 场均上座率
                contents["avgSeatView"] = item.get("avgSeatView")
                # 场均人次
                contents["avgShowView"] = item.get("avgShowView")
                # 平均票价
                contents["avgViewBox"] = item.get("avgViewBox")
                # 票房
                contents["boxInfo"] = item.get("boxInfo")
                # 票房占比
                contents["boxRate"] = item.get("boxRate")
                # 电影名称
                contents["movieName"] = item.get("movieName")
                # 上映天数
                contents["releaseInfo"] = item.get("releaseInfo")
                # 排片场次
                contents["showInfo"] = item.get("showInfo")
                # 排片占比
                contents["showRate"] = item.get("showRate")
                # 总票房
                contents["sumBoxInfo"] = item.get("sumBoxInfo")
                yield contents


def main():
    while True:
        json = get_html()
        results = get_data(json)
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")
        print(json.get("data")["updateInfo"])
        print("今日总票房: {0}{1}".format(
            json.get("data")["totalBox"], json.get("data")["totalBoxUnit"]
        ))
        print("-" * 155)
        print("电影名称\t综合票房（万）\t票房占比\t场均上座率\t场均人次\t平均票价\t排片场次\t排片占比\t累积总票房\t上映天数")
        print("-" * 155)
        for result in results:
            print(
                result["movieName"][:7].ljust(8), "\t",
                result["boxInfo"][:8].rjust(8), "\t",
                result["boxRate"][:8].rjust(8), "\t",
                result["avgSeatView"][:8].rjust(8), "\t",
                result["avgShowView"][:8].rjust(8), "\t",
                result["avgViewBox"][:8].rjust(8), "\t",
                result["showInfo"][:8].rjust(8), "\t",
                result["showRate"][:8].rjust(8), "\t",
                result["sumBoxInfo"][:8].rjust(8), "\t",
                result["releaseInfo"][:8],
                "\n", sep=""
            )
        time.sleep(5)


if __name__ == "__main__":
    main()
