#coding=utf-8
from flask import Flask,request,render_template
import os

app=Flask(__name__)

# 允许上传的文件类型为apk
ALLOWED_EXTENSIONS = set(["apk","docx"])

#这个函数的作用是判断上传的文件是否是apk
def allowed_file(filename):

    # return '.' in filename and \
    #        filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS
    file_list=filename.rsplit(".",1)
    # if file_list[1] in ALLOWED_EXTENSIONS:
    if '.' in filename and \
            filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS:
        return {"encode":1,"content":filename}
    else:
        return {"encode":0,"content":"请检查文件后缀，后缀必须为.apk"}

@app.route("/")
def index():
    return render_template("demo.html")

@app.route("/upload",methods=['GET','POST'])
def deal_data(url):
    # 获取到前端输入的文件名称
    # 这块前端还会给我传文件的大小之类的一些参数那就需要获取这些值然后做判断
    file = request.args["bfile"]
    file_name=allowed_file(file)
    try:
        # return {"encode":200,"file_url":url+file_name}
       if file_name["encode"]==1:
           return {"code":200,"file_url":url + file}
       elif file_name["encode"]==0:
            return {"code":201,"msg":"文件上传失败"}
    except Exception as e:
        raise e


if __name__ == '__main__':
    app.run(debug=True,port=4434)