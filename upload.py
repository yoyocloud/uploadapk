#coding=utf-8
from flask import Flask,render_template,request
import requests

#先创建一个服务对象
app=Flask(__name__)

#这个就是一个上传的接口的功能
def deal_data(url,file_path=None,filename=None):
    '''
    :param file_path: 文件存放的绝对路径
    :param filename: 文件的名称
    :return:
    '''
    # url=""#自己想要请求的接口地址也就是存文件的服务器地址
    res=requests.get(url)
    return res

#路由分发,定义根路径的作用
@app.route("/")
def index():
    return render_template("demo.html")

#定义上传的这个接口就是把文件上传
@app.route("/upload")
def upload():
    # file=request.args["bfile"]
    res=deal_data("http://127.0.0.1:4434/")#旭东给我的地址
    return res.text

#4434的是旭东给我的存文件的服务器地址，这个接口返回一个响应状态码
#5000的这个是我自己的服务器地址，将来会部署到一个环境上

#联动这两个的就是上传服务器的功能需要一个URL就把旭东的传进去，
#然后自己的是和前端交互的一个服务

if __name__ == '__main__':
    app.run(debug=True)

