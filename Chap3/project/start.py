from flask import render_template,request,url_for,Flask
import w2_api

app = Flask(__name__)

history = []

@app.route('/weather')
@app.route('/weather/<name>')
def hello(name = None,city = None,weather = None,help=None):
    searchword = request.args.get('city','')
    weather1 = w2_api.getWeather()
    weather2 = weather1.get_weather(searchword)
    if weather2:
        history.append(weather2)
        return render_template('query.html', name='阿炳,欢迎使用天气查询', city=searchword,weather=weather2)  # 模板文件必须放在模板文件夹里
    elif request.args.get('history') == 'history':
        return render_template('query.html', name='阿炳,欢迎使用天气查询',history=history)  # 模板文件必须放在模板文件夹里
    elif request.args.get('help') == 'help':
        return render_template('query.html', name='阿炳,欢迎使用天气查询',help=weather1.help())  # 模板文件必须放在模板文件夹里

    return render_template('query.html', name='阿炳,欢迎使用天气查询')

app.run(debug=True)