import requests

class getWeather:
    def get_weather(self,city):
        result = requests.get(
            'https://api.seniverse.com/v3/weather/now.json',
            params={
                'key': 'ohqszln8seprvdc5',
                'location':city,
                'language': 'zh-cn'
            }, timeout=10
        )
        result_get = result.json().get('results')
        if result_get is not None:
            weather = result_get[0]['now']['text']
            temperature = result_get[0]['now']['temperature']
            #last_update = result.json().get('results')[0]['last_update']
            return (city + '此刻的天气是：' + str(weather) + ',气温' + str(temperature) + '度。')
        else:
            return False

    def help(self):
        return ('''欢迎使用天气查询：\n
            输入城市名称后点击查询按钮，即可看到对应天气。\n
            城市名称支持中文和拼音。\n
            点击帮助获取帮助信息。\n
            点击历史获取历史查询信息。\n
            ''')
