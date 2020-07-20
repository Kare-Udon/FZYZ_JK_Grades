# coding: utf-8

import sys
from bs4 import BeautifulSoup
from urllib.request import Request, build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import CookieJar
from django.http import HttpResponse

# 改变标准输出的默认编码
sys.stdout.reconfigure(encoding='utf-8')


def send(request):
    
    # 从前端获取数据
    request.encoding = 'utf-8'
    user = request.GET.get('user')
    passwd = request.GET.get('passwd')
    exam = request.GET.get('para_academic_Year')

    # 获取登陆Cookies
    # 登录时需要POST的数据
    data = {
        'staffCode': user,
        'password' : passwd,
        'loginRole': '2',
    }
    # 将数据转化为bytes格式
    post_data = urlencode(data).encode('utf-8')
    # 设置请求头
    headers = {
        'User-agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    # 登录时表单提交到的地址（用开发者工具可以看到）
    login_url = 'http://fzyz.net/sys/login.shtml'
    # 构造登录请求
    req = Request(login_url, headers={}, data=post_data)
    # 构造cookie
    cookie = CookieJar()
    # 由cookie构造opener
    opener = build_opener(HTTPCookieProcessor(cookie))
    # 发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
    opener.open(req)

    # 查询成绩
    # 成绩查询页面
    url_score = 'http://fzyz.net/doone-edu/family/familyinfo/loadStuRScoreAction.shtml'
    # 查询成绩所POST的数据
    data_score = {
        'academic_Year': '2019-2020',
        'termYear'     : '1',
        'exam_Id'      : exam,
        'myscoreconfig': '0',
    }
    post_data_score = urlencode(data_score).encode('utf-8')
    # 构造访问请求（此时opener内存有上面POST后已认证的Cookies）
    req = Request(url_score, headers=headers, data=post_data_score)
    resp = opener.open(req)
    get_html = resp.read().decode('gbk')

    # 分析数据
    # '''
    #     Soup = BeautifulSoup(get_html,'html.parser')
    #     title = Soup.title
    #     grade = Soup.find_all(name='td',attrs={"class":"zi12"})#按照字典的形式给attrs参数赋值
    #     grade_str = str(grade)
    #     grade_html = '<table>' + grade_str + '</table>'
    #     print(grade_html)
    # '''

    # 解析获取HTML，截取所需部分
    soup = BeautifulSoup(get_html, "html.parser")
    #    [s.extract() for s in soup()]
    table = soup.find("table", attrs={"cellspacing": "1"})
    #    table = soup.select('table[cellspacing="1"]')

    #    print(table)
    # 解析表格为json
    #    data_list = []
    #    for i in range(3, 10):
    #        tr = table[i]
    #        for j in range(0, 2):
    #            tds = tr.find_all("td")
    #            text = tds[j].contents
    #            text = str(text)
    #            a_list = re.findall(r'[\u4e00-\u9fa5]|\d+\.?\d*|[A,B,C,D]', text)
    #            a_list = "".join(a_list)
    #            data_list.append(a_list)
    #        print(data_list)

    response = HttpResponse(table)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "500000"
    response["Access-Control-Allow-Headers"] = "*"
    return response