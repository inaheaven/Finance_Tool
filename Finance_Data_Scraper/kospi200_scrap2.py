# coding=utf-8

from urllib.request import urlopen
import pandas as pd
import matplotlib.pyplot as plt
import json

if __name__ == "__main__":
    key = [1010000]
    # https://ecos.bok.or.kr/jsp/openapi/OpenApiController.jsp?t=guideServiceDtl&apiCode=OA-1040&menuGroup=MENU000004
    # 여기서 주소 만들면 쉽다.

    # 통계 목록표 뽑기
    url = "http://ecos.bok.or.kr/api/StatisticItemList/" + key + "/json/kr/1/2000/028Y015/"
    result = urlopen(url)
    html = result.read()
    data = json.loads(html)
    data = data["StatisticItemList"]

    name = pd.DataFrame(data["row"])

    # 일자별로는 제공하지 않음
    url = "http://ecos.bok.or.kr/api/StatisticSearch/" + key + "/json/kr/1/1000/028Y015/MM/198001/201805/1080000/?/?"
    result = urlopen(url)
    html = result.read()
    data = json.loads(html)
    data = data["StatisticSearch"]

    data = pd.DataFrame(data["row"])

    data["DATA_VALUE"] = data["DATA_VALUE"].astype(float)

    plt.plot(data["TIME"], data["DATA_VALUE"])

    data_out = data[["DATA_VALUE", "TIME"]]
    data_out.to_csv("KOSPI_200401_201805.csv")
