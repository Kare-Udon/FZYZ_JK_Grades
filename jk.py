import sys
import io
import urllib.request
import http.cookiejar
from django.http import HttpResponse
import json

def send(request):
    request.encoding='utf-8'
        user= request.GET.get('user')
        passwd = request.GET.get('passwd')
         #登录时需要POST的数据
        data = json.dumps({
          'loginName' : str(user) ,
          'password' : str(passwd)
        }, sort_keys=True, indent=4) 

        post_data = urllib.parse.urlencode(data).encode('utf-8')

        #设置请求头
        headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        #登录时表单提交到的地址（用开发者工具可以看到）
        login_url = 'http://fzyz.net/sys/login.shtml'
        #构造登录请求
        req = urllib.request.Request(login_url, headers = headers, data = post_data)
        #构造cookie
        cookie = http.cookiejar.CookieJar()
        #由cookie构造opener
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        #发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
        resp = opener.open(req)
        #登录后才能访问的网页
        url_score = 'http://fzyz.net/doone-edu/family/familyinfo/loadStuRScoreAction.shtml'

        #查询成绩所POST的数据
        data_score = { 
                                        'academic_Year': '2019-2020',
                                        'termYear': '1',
                                        'exam_Id': '3703',
                                        'myscoreconfig': '0',
                                        }
        post_data_score = urllib.parse.urlencode(data_score).encode('utf-8')
        #构造访问请求
        req = urllib.request.Request(url_score, headers = headers, data = post_data_score)
        resp = opener.open(req)
        get_html = resp.read().decode('gbk')
'''