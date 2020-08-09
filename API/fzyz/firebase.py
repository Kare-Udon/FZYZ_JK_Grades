import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.http import HttpResponse

env_dist = os.environ

cred = credentials.Certificate(env_dist.get('FIREBASE'))
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_fzyz_():
    fzyz_ref = db.collection(u'fzyz')
    fzyz_docs = fzyz_ref.stream()
    return fzyz_docs

def get_jk_():
    jk_ref = db.collection(u'jk')
    jk_docs = jk_ref.stream()
    return jk_docs

def add_fzyz_(ident_code,data):
    fzyz_ref = db.collection(u'fzyz').document(u'{}'.format(ident_code))
    fzyz_ref.set(data)

def add_jk_(ident_code,data):
    jk_ref = db.collection(u'jk').document(u'{}'.format(ident_code))
    jk_ref.set(data)

def send(request):
    request.encoding = 'utf-8'
    fzyz_username = request.GET.get('fzyz_user')
    fzyz_passwd = request.GET.get('fzyz_passwd')
    jk_username = request.GET.get('jk_user')
    jk_passwd = request.GET.get('jk_passwd')
    ident_code = request.GET.get('ident_code')

    fzyz_data = {}
    jk_data = {}
    fzyz_data['username'] = fzyz_username
    fzyz_data['passwd'] = fzyz_passwd
    jk_data['username'] = jk_username
    jk_data['passwd'] = jk_passwd

    add_fzyz_(ident_code,fzyz_data)
    add_jk_(ident_code,jk_data)

    response = HttpResponse()
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "500000"
    response["Access-Control-Allow-Headers"] = "*"
    return response