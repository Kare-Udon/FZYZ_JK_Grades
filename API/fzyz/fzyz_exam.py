from urllib.request import Request, build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import CookieJar
import json
import re


def fzyz_exam(username, passwd, para_academic_Year, para_KEY):

    # 获取登陆Cookies
    # 登录时需要POST的数据
    data = {
        'staffCode': username,
        'password': passwd,
        'loginRole': '2',
    }
    # 登录时表单提交到的地址（用开发者工具可以看到）
    login_url = 'http://fzyz.net/sys/login.shtml'
    # 将数据转化为bytes格式
    post_data = urlencode(data).encode('utf-8')
    # 构造登录请求
    req = Request(login_url, headers={}, data=post_data)
    # 构造cookie
    cookie = CookieJar()
    # 由cookie构造opener
    opener = build_opener(HTTPCookieProcessor(cookie))
    # 发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
    opener.open(req)

    # 获取考试详情json
    # 考试详情查询界面
    exam_url = (f'http://fzyz.net/education/score/score/'
                f'getstuExamsByAcademicYearTermYears.shtml?'
                f'para.academic_Year={para_academic_Year}&'
                f'para.KEY={para_KEY}')
    # 获取json
    req = Request(exam_url, headers={})
    resp = opener.open(req)
    exam_js = resp.read().decode('gbk')

    # 删除冗余信息，是小屏设备能正常显示。
    exam_js = re.sub(r'(?<=高中部)[0-9\-]+', '', exam_js)
    exam_js = re.sub(r'高中部', "", exam_js)
    exam_js = re.sub(r'第一学期', "", exam_js)
    exam_js = re.sub(r'第二学期', "", exam_js)

    return exam_js
