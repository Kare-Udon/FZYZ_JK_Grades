import sys 
from django.http import HttpResponse
import requests
from .fzyz_exam import fzyz_exam
from .fzyz_grades import fzyz_grades
from .jk import jk

sys.stdout.reconfigure(encoding='utf-8')

def response_(item):
    response = HttpResponse(item)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "500000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def send(request):
    # 从前端获取数据
    request.encoding = 'utf-8'
    username = request.GET.get('user')
    passwd = request.GET.get('passwd')
    user_code = request.GET.get('user_code')
    fzyz_or_jk = request.GET.get('fzyz_or_jk')
    # 1 == 查询 fzyz_exam; 2 == 查询 fzyz_grades; 3 == 查询 jk。
    using_code = request.GET.get('using_code')
    exam_id = request.GET.get('exam_id')
    para_academic_Year = request.GET.get('para_academic_Year')
    para_KEY = request.GET.get('para_KEY')

    if using_code == '0':

        if fzyz_or_jk == '1':
            # 查询 fzyz_exam
            exam_js = fzyz_exam(username, passwd, para_academic_Year, para_KEY)
            response_(exam_js)

        if fzyz_or_jk == '2':
            # 查询 fzyz_grades
            table = fzyz_grades(username, passwd, exam_id)
            response_(table)

        if fzyz_or_jk == '3':
            # 查询 jk
            html_back = jk(username,passwd,exam_id)
            response_(html_back)

    if using_code == '1':
        print(user_code)