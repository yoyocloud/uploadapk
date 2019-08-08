#coding=utf-8
from flask import Flask,render_template,request
import requests
from backup import deal_data

#先创建一个服务对象
app=Flask(__name__)

#路由分发,定义根路径的作用
@app.route("/")
def index():
    return render_template("demo.html")

#定义上传的这个接口就是把文件上传
@app.route("/upload")
def upload():
    # #获取到前端输入的文件名称
    # file=request.args["bfile"]
    #调用deal_data函数把上传文件的服务器地址拿到可路径
    res=deal_data(url="http://127.0.0.1:4434/")
    #拼接
    return res

#4434的是旭东给我的存文件的服务器地址，这个接口返回一个响应状态码
#5000的这个是我自己的服务器地址，将来会部署到一个环境上

#联动这两个的就是上传服务器的功能需要一个URL就把旭东的传进去，
#然后自己的是和前端交互的一个服务

if __name__ == '__main__':
    app.run(debug=True)

