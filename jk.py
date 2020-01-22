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
    headers = {
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
    response = requests.post(url=login_url, headers=headers, data=json.dumps(data), cookies=cookie)
    # 保存获取到的含有autho的json
    print(response.json())

'''
    #获取成绩json
    url_score = 'https://api.fclassroom.com/ud-family/api/report/student/exam/detail?schoolId=2246&gradeId=9320&subjectBaseId=5&clzssId=102301&studentId=1814919&examId=735115&paperId=814772&clientValue=22'
    post_data_score = urllib.parse.urlencode(data_score).encode('utf-8')
    #构造访问请求
    req = urllib.request.Request(url_score, headers = headers, data = post_data_score)
    resp = opener.open(req)
    get_html = resp.read().decode('gbk')
'''