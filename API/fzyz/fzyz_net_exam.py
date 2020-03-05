# coding: utf-8

import sys
import io
import urllib.request
import http.cookiejar
from django.http import HttpResponse
import json
import requests

# 改变标准输出的默认编码
#sys.stdout.reconfigure(encoding='utf-8')


def send(request):
    # 从前端获取数据
    request.encoding = 'utf-8'
    user = request.GET.get('user')
    passwd = request.GET.get('passwd')
    para_academic_Year = request.GET.get('para_academic_Year')
    para_KEY = request.GET.get('para_KEY')

    # 获取登陆Cookies
    # 登录时需要POST的数据
    data = {
        'staffCode':    user,
        'password':     passwd,
        'loginRole':    '2',
    }
    # 将数据转化为bytes格式
    post_data = urllib.parse.urlencode(data).encode('utf-8')
    # 设置请求头
    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    # 登录时表单提交到的地址（用开发者工具可以看到）
    login_url = 'http://fzyz.net/sys/login.shtml'
    # 构造登录请求
    req = urllib.request.Request(login_url, headers={}, data=post_data)
    # 构造cookie
    cookie = http.cookiejar.CookieJar()
    # 由cookie构造opener
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cookie))
    # 发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
    resp = opener.open(req)

    # 获取考试详情json
    # 考试详情查询界面
    exam_url = (f'http://fzyz.net/education/score/score/getstuExamsByAcademicYearTermYears.shtml'
                f'?para.academic_Year={para_academic_Year}'
                f'&para.KEY={para_KEY}')
    # 获取json
    req = urllib.request.Request(exam_url,
                                 headers=headers)
    resp = opener.open(req)
    exam_js = resp.read().decode('gbk')
#    exam_js = json.dumps(json.loads(exam_js))

    exam_js = '{"data":' + exam_js + "}"

    # 返回json
    response = HttpResponse(exam_js)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
