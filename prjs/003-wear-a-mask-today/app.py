# coding: utf-8
import requests


pm25_in_key = "XXXXXXXXXXXXXXXXXXXX"
server_chan_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def get_aqi(city):
    url = "http://www.pm25.in/api/querys/aqi_details.json?city={city}&token={token}".format(city=city, token=pm25_in_key)
    ret = requests.get(url)
    aqi = 0
    for aqi_data in ret.json():
        aqi = aqi_data["aqi"]
        if aqi_data["station_code"] == "1011A":     # 奥体中心
            break
        elif aqi_data["station_code"] is None:      # 均值，一般最后出现
            break
    return aqi


def send_msg(title, desc):
    url = "https://sc.ftqq.com/{}.send".format(server_chan_key)
    data = {
        "text": title,
        "desp": desc,
    }
    requests.post(url, data)


def main():
    aqi = get_aqi("北京")
    if aqi > 100:
        send_msg("今天要戴口罩", "AQI：{}".format(aqi))
    else:
        send_msg("今天不用戴口罩", "AQI：{}".format(aqi))


if __name__ == '__main__':
    main()
