
'''
CLI版天气通需要完成的功能有：
输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用h或help）；
输入指令，推出程序的交互（一般使用quit或exit）;
输入指令，获取历史查询信息，城市-天气
在退出程序之前，打印查询过的所有城市。
核心功能：输入城市名，返回该城市的天气数据。
'''
import requests
import json
import sys


KEY = 'fjsbr3wepbuprsk0'  # API location
API = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言


def fetchWeather(location):
    result = requests.get(API, params={
        'key': KEY,
        'location': location,# 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
        'language': LANGUAGE,
        'unit': UNIT
    }
    )
    if result.json().get('results') is not None:
        weather = result.json().get('results')[0]['now']['text']
        temperature = result.json().get('results')[0]['now']['temperature']
        time = result.json().get('results')[0]['last_update']
        return weather, temperature, time
    else:
        return False


def helpdef(userinput):
    print("""
        输入城市名，查询该城市的天气数据；
        输入help，打印帮助文档；
        输入history,打印查询过的所有城市天气；
        输入quit，退出程序交互.
        """)


def histdef(location):
    print(historylist)


historylist = []
while True:
    userinput = input("请输入指令或要查询的城市名：")
    if fetchWeather(userinput) is not False:
        weather, temperature, time = fetchWeather(userinput)
        historylist.append(userinput)
        # print(" %s 的天气状况为： %s" %(location,weather_dict[location]))
        print("{}的天气为{}，温度为{}摄氏度".format(userinput, weather, temperature))
        print("更新时间：%s" % time[:-6])

    elif userinput == "help":
        helpdef(userinput)

    elif userinput == "quit":
        break

    elif userinput == "history":
        histdef(userinput)

    else:
        print("对不起，您输入的城市不存在")
