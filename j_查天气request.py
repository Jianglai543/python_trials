# -*- coding: utf-8 -*-
import requests
import threading


def get_it(city_data, num):
    city_forecast = city_data['forecast'][num]
    print(
        city_forecast.get('date'),
        city_forecast.get('high'),
        city_forecast.get('low'),
        city_forecast.get('type')
    )

def get_wheater(city):
    """req = requests.get('http://www.baidu.com')
    print(req)
    req.encoding = 'utf-8'
    content = req.text
    print(content)"""



    if not city:
        return
    try:
        req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    except:
        print('request error!')


    # print(req.text)
    dic_city = req.json()
    # print(dic_city)
    city_data = dic_city.get('data')
    if city_data:
        print(city)
        get_it(city_data, 0)
        get_it(city_data, 1)
        get_it(city_data, 2)
    else:
        print('find info error!')


if __name__ == '__main__':
    thread = []
    cities = ['北京','成都','大连','徐州']
    for i in range(len(cities)):
        t = threading.Thread(target=get_wheater, args=(cities[i],))
        thread.append(t)
    for i in range(len(cities)):
        thread[i].start()
    for i in range(len(cities)):
        thread[i].join()
