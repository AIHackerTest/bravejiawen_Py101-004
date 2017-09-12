
# 内网版天气查询程序

## Flask

### 简介
- web框架
 - web框架用于动态网站，提升代码复用性，减轻开发共通性模块的工作量。（近似理解为把开发网站应用需要的常见功能封装在一起，反复利用。）
- flask的特点
 - 轻量级，简单
 - 拓展性好，可以自定义
- flask参考资源
 - [flask中文文档](http://docs.jinkan.org/docs/flask/index.html)
 - [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### 安装
- 需要安装的
 - flask
 - jinja2
 - Werkzeug
- 安装方式
 - pip install flask （会同时下载依赖的库）

### 最小程序
- Hello world！


```python
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

### 文件结构
- app （程序）
 - templates （html模板）
 - static （css等静态文件）
 - model 
 - weather.py (起始运行的文件）

### jinja2模板
- 模板渲染


```python
render_template('weather.html',name='abing')#html文件名后加各种参数，需赋值
```

- 表达式与变量


```python
# <!-- html代码中可以用下面这样的方式插代码，if与for语句类似，不用：但是需要end -->
{% if name %} # 表达式的结构为 {% foo... %}
    {{ name }} # 使用{{ var }}，相当于print(name)
{% endif %} # if语句结束需使用endif，其他语句也都需结束
```

- 拓展与参考资料
 - [jinja2中文文档--模板](http://docs.jinkan.org/docs/jinja2/templates.html#id2)

## Html+css

### html基础
- html页面内容


```python
<html>
<head>
#页面头部，放页面标题描述等信息，引用静态文件
<title>网页标题</title>
</head>
<body>
# 网页展示的内容部分，一般使用div框架
</body>
</html>
```

- html中常用的标签


```python
 - <h1>标题系列</h1>，从h1到h6
 - <div>框，什么都可以装框里</div>
 - <br/>换行
 - <form>表格<input>输入框<button>按钮</button></form>
 - <a>超链接</a>
 - <img>图片
 - <ul><li>列表</li></ul>
```

### css使用

- html中导入css文件


```python
<link type='text/css' rel='stylesheet' herf='/static/style.css'>
```

- css文件内容


```python
.class {#css中的类，使用.name的方式，属性都放{}里
    font:20px;#属性:值;的方式，一定要；
}
```
