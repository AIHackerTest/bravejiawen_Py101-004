'''
定时查询天气，指定城市
'''
import requests
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

key = 'ohqszln8seprvdc5'

def get_weather(city,*args):
    result = requests.get(
        'https://api.seniverse.com/v3/weather/now.json',
        params={
            'key': key,
            'location':city,
            'language': 'zh-cn'
        }, timeout=1
    )
    if result.json().get('results') is not None:
        weather = result.json().get('results')[0]['now']['text']
        temperature = result.json().get('results')[0]['now']['temperature']
        return (weather,temperature)
    else:
        return False

def select_city(se1):
    '''用于接受查询输入，通使用if判断内容返回结果'''
    print('现在的时间是：')
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    for se in se1:
        #se = input('>')
        we = get_weather(se)
        if we:
            print(se + '现在的天气是：' + str(we[0]) + ',气温'+ str(we[1]) + '度')
        else:
            print('%s 城市信息不存在' % se)
    #exit('程序结束')

scheduler = BlockingScheduler()
#scheduler.add_job(select_city,'date',run_date='2017-08-27 11:45:00',args=[['杭州','长沙','北京']]) #固定时间查询
scheduler.add_job(select_city,'interval',seconds=30,start_date='2017-08-28 14:00:00',
                  end_date = '2017-08-28 14:08:00',args=[['杭州','长沙','北京']])#固定间隔时间查询
scheduler.start()

# select_city()
