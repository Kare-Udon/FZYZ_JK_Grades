# coding: utf-8

import sys
import io
import urllib.request
import http.cookiejar
from django.http import HttpResponse
import json
import requests


def send(request):
    # 从前端获取数据
    request.encoding = 'utf-8'
    user = request.GET.get('user')
    passwd = request.GET.get('passwd')
    subject = request.GET.get('subject')

    ## 获取Authorization
    # 登录时需要POST的数据
    data = {'loginName': user, 'password': passwd}
    # 定义认证
    Autho = 'Bearer'
    # 设置请求头
    headers_autho = {
        'Client-Value':     '22',
        'Connection':       'keep-alive',
        'Authorization':    Autho,
        'Content-Type':     'application/json',
        'Host':             'api.fclassroom.com',
        'User-agent':       'User-Agent: ji ke tong xue/4.1.4 (iPhone; iOS 13.3.1; Scale/2.00)'
    }
    # 登录时表单提交到的地址（用开发者工具可以看到）
    url_login = 'https://api.fclassroom.com/pf-account-family/api/account/student/old/login'
    # 设置cookie容器
    cookie = http.cookiejar.CookieJar()
    # 发送POST请求
    response = requests.post(url=url_login,
                             headers=headers_autho,
                             data=json.dumps(data),
                             cookies=cookie)
    # 保存获取到的含有autho的json
    json_autho = response.json()
    # 转化为字符串
    str_autho = json.dumps(json_autho)
    # 转化为字典
    str_autho_load = json.loads(str_autho)
    # 读取json中的json（套娃有意思么（
    data_autho = str_autho_load['data']
    data_autho_str = json.dumps(data_autho)
    data_autho_load = json.loads(data_autho_str)
    Autho_pre = data_autho_load['accessToken']
    Autho = 'Bearer ' + Autho_pre

    ## 获取studentId
    # studentId获取地址
    url_studentId = 'https://api.fclassroom.com/pf-account-family/api/account/student/info/all'
    # 构建成绩查询头
    headers_studentId = headers_autho.copy()
    headers_studentId['Authorization'] = Autho
    # 构造访问请求
    response = requests.get(url=url_studentId,
                            headers=headers_studentId,
                            cookies=cookie)
    # 获取studentId
    json_studentId = response.json()
    str_studentId = json.dumps(json_studentId)
    str_studentId_load = json.loads(str_studentId)
    data_studnetId = str_studentId_load['data']
    data_studnetId_str = json.dumps(data_studnetId)
    data_studnetId_load = json.loads(data_studnetId_str)
    studentId = data_studnetId_load['id']

    ## 获取含某科目全部的成绩json
    # 科目id： examSubjectValue=
    # 数学1；语文2；英语3；物理4；化学5；生物6；政治7；历史8；地理9；信息技术10；理综11；文综12。
    # 成绩查询地址构建
    school_id = '2246'  # 可拓展项
    url_score = (f'https://api.fclassroom.com/ud-api-student/api/v1/exam/list'
                 '?examSubjectValue={subject}'
                 '&offset=1'
                 '&pageSize=999'
                 '&schoolId={school_id}'
                 '&studentId={studentId}')
    # 构建成绩查询头
    headers_score = headers_studentId
    # 构造访问请求
    response = requests.get(url=url_score,
                            headers=headers_score,
                            cookies=cookie)
    # 保存成绩json
    json_score = response.json()
    # 格式化json
    str_score = json.dumps(json_score,
                           ensure_ascii=False,
                           sort_keys=True,
                           indent=2)
    # 暂时直接输出json
    return HttpResponse(str_score)


# '''
#     ##获取成绩json
#     #成绩查询地址
#     url_score = 'https://api.fclassroom.com/ud-family/api/report/student/exam/detail?schoolId=2246&gradeId=9320&subjectBaseId=5&clzssId=102301&studentId=1814919&examId=735115&paperId=814772&clientValue=22'
#     #构建成绩查询头
#     headers_score = {
#         'Client-Value': '22' ,
#         'Connection': 'keep-alive',
#         'Authorization' : Autho ,
#         'Content-Type': 'application/json',
#         'Host': 'api.fclassroom.com',
#         'User-agent': 'User-Agent: ji ke tong xue/4.1.4 (iPhone; iOS 13.3.1; Scale/2.00)'
#      }
#     #构造访问请求
#     response = requests.get(url=url_score, headers=headers_score, cookies=cookie)
#     #保存成绩json
#     json_score = response.json()
#     #确保输出为中文
#     str_score = json.dumps(json_score, ensure_ascii=False)

#     ##返回成绩数据（暂为为处理的json）
#     return HttpResponse(str_score)
# '''