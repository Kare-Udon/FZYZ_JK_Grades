import sys 
from django.http import HttpResponse
import requests
from .fzyz_exam import fzyz_exam
from .fzyz_grades import fzyz_grades
from .jk import jk

def send(request):
    # 从前端获取数据
    request.encoding = 'utf-8'
    username = request.GET.get('user')
    passwd = request.GET.get('passwd')
    ident_code = request.GET.get('ident_code')
    fzyz_or_jk = request.GET.get('fzyz_or_jk')
    # 1 == 查询 fzyz_exam; 2 == 查询 fzyz_grades; 3 == 查询 jk。
    exam_or_grades = request.GET.get('exam_or_grades')
    using_code = request.GET.get('using_code')
    exam_id = request.GET.get('exam_id')
    para_academic_Year = request.GET.get('para_academic_Year')
    para_KEY = request.GET.get('para_KEY')
    subject = request.GET.getlist('subject')

    if using_code == '0':

        if exam_or_grades == '0':

            if fzyz_or_jk == '1':
                # 查询 fzyz_grades
                final = fzyz_grades(username, passwd, exam_id)

            if fzyz_or_jk == '2':
                # 查询 jk
                final = jk(username,passwd,subject)

        if exam_or_grades == '1':
            final = fzyz_exam(username, passwd, para_academic_Year, para_KEY)

    if using_code == '1':
        print(ident_code)

    response = HttpResponse(final)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "500000"
    response["Access-Control-Allow-Headers"] = "*"
    return response