from django.http import HttpResponse
import requests
from .fzyz_exam import fzyz_exam
from .fzyz_grades import fzyz_grades
from .jk import jk
from .firebase import get_fzyz_ , get_jk_

def send(request):
    # 从前端获取数据
    request.encoding = 'utf-8'
    username = request.GET.get('user')
    passwd = request.GET.get('passwd')
    ident_code = request.GET.get('ident_code')
    fzyz_or_jk = request.GET.get('fzyz_or_jk')
    exam_or_grades = request.GET.get('exam_or_grades')
    using_code = request.GET.get('using_code')
    exam_id = request.GET.get('exam_id')
    para_academic_Year = request.GET.get('para_academic_Year')
    para_KEY = request.GET.get('para_KEY')
    subject = request.GET.getlist('subject')

    if using_code == '0':
        #不使用 ident_code

        if exam_or_grades == '0':

            if fzyz_or_jk == '1':
                # 查询 fzyz_grades
                final = fzyz_grades(username, passwd, exam_id)

            if fzyz_or_jk == '2':
                # 查询 jk
                final = jk(username,passwd,subject)

        if exam_or_grades == '1':
            #查询 fzyz_exam
            final = fzyz_exam(username, passwd, para_academic_Year, para_KEY)

    if using_code == '1':
        #使用 ident_code

        if exam_or_grades == '0':

            if fzyz_or_jk == '1':
                # 查询 fzyz_grades
                data = get_fzyz_()
                for doc in data:
                    if doc.id == ident_code:
                        doc_dict = doc.to_dict()
                        username = doc_dict['username']
                        passwd = doc_dict['passwd']
                        final = fzyz_grades(username, passwd, exam_id)
                    else:
                        pass

            if fzyz_or_jk == '2':
                # 查询 jk
                data = get_jk_()
                for doc in data:
                    if data.id == ident_code:
                        doc_dict = doc.to_dict()
                        username = doc_dict['username']
                        passwd = doc_dict['passwd']
                        final = jk(username,passwd,subject)
                    else:
                        pass

        if exam_or_grades == '1':
            #查询 fzyz_exam
            data = get_fzyz_()
            for doc in data:
                if doc.id == ident_code:
                    doc_dict = doc.to_dict()
                    username = doc_dict['username']
                    passwd = doc_dict['passwd']
                    final = fzyz_exam(username, passwd, para_academic_Year, para_KEY)
                else:
                    pass

    response = HttpResponse(final)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "500000"
    response["Access-Control-Allow-Headers"] = "*"
    return response