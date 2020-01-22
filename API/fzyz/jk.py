# coding: utf-8

import sys
import io
import urllib.request
import http.cookiejar
from django.http import HttpResponse
import json
import requests


def send(request):
    #从前端获取数据
    request.encoding='utf-8'
    user= request.GET.get('user')
    passwd = request.GET.get('passwd')
 
    ##获取Authorization
     #登录时需要POST的数据
    data = {
          'loginName' : str(user) ,
          'password' : str(passwd)
    }
    #定义认证
    Autho = 'Bearer'
    #设置请求头
    headers_autho = {
        'Client-Value': '22' ,
        'Connection': 'keep-alive',
        'Authorization' : Autho ,
        'Content-Type': 'application/json',
        'Host': 'api.fclassroom.com',
        'User-agent': 'User-Agent: ji ke tong xue/4.1.4 (iPhone; iOS 13.3.1; Scale/2.00)'
        }
    #登录时表单提交到的地址（用开发者工具可以看到）
    login_url = 'https://api.fclassroom.com/pf-account-family/api/account/student/old/login'
    #设置cookie容器
    cookie = http.cookiejar.CookieJar()
    #发送POST请求
    response = requests.post(url=login_url, headers=headers_autho, data=json.dumps(data), cookies=cookie)
    #保存获取到的含有autho的json
    autho_json = response.json()
    #转化为字符串
    json_str = json.dumps(autho_json)
    #转化为字典
    json_load = json.loads(json_str)
    #读取json中的json（套娃有意思么(
    data = json_load['data']
    data_str = json.dumps(data)
    data_load = json.loads(data_str)
    Autho_pre = data_load['accessToken']
    Autho = 'Bearer ' + Autho_pre

    ##获取成绩json
    #成绩查询地址
    url_score = 'https://api.fclassroom.com/ud-family/api/report/student/exam/detail?schoolId=2246&gradeId=9320&subjectBaseId=5&clzssId=102301&studentId=1814919&examId=735115&paperId=814772&clientValue=22'
    #构建成绩查询头
    headers_score = {
        'Client-Value': '22' ,
        'Connection': 'keep-alive',
        'Authorization' : Autho ,
        'Content-Type': 'application/json',
        'Host': 'api.fclassroom.com',
        'User-agent': 'User-Agent: ji ke tong xue/4.1.4 (iPhone; iOS 13.3.1; Scale/2.00)'
     }
    #构造访问请求
    response = requests.get(url=url_score, headers=headers_score, cookies=cookie)
    #保存成绩json
    score_json = response.json()
    #确保输出为中文
    score_str = json.dumps(score_json, ensure_ascii=False)

    ##返回成绩数据（暂为为处理的json）
    return HttpResponse(score_str)