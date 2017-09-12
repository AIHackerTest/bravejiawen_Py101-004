#字典
'''
CLI版天气通需要完成的功能有：
输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用h或help）；
输入指令，推出程序的交互（一般使用quit或exit）;
输入指令，获取历史查询信息，城市-天气
在退出程序之前，打印查询过的所有城市。
核心功能：输入城市名，返回该城市的天气数据。
'''

weather_dict = {}
# 3.0由列表更改为字典后，历史查询输出更美观，没有单引号
history_dic = {}

with open('weather_info.txt', 'r', encoding="utf-8") as f:
    weather_dict = {city.strip():weath.strip() for city,weath in (line.split(',') for line in f)}

def helpdef(userinput):
    print("""
        输入城市名，返回该城市的天气数据；
        输入help，打印帮助文档；
        输入history,打印查询过的所有城市；
        输入quit，退出程序交互.
        """)
# 2.0输出格式不对，为 [['北京'，'晴'],['上海'，'小雨']]，希望去掉列表格式和单引号
# 未实现
def histdef(userinput):
    for userinput in history_dic:
        print(userinput, history_dic[userinput])


while True:
    key = input("请输入指令或要查询的城市名：")
    if key in dict(weather_dict):
        history_dic[key] = weather_dict[key]
        # print(" %s 的天气状况为： %s" %(key,weather_dict[key]))
        print(" {} 的天气状况为： {}".format(key, weather_dict[key]))

    elif key == "help":
        helpdef(key)

    elif key == "quit":
        break

    elif key == "history":
        histdef(key)

    else:
        print("对不起，您输入的城市不存在")
