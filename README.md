# FZYZ_JK_Grades

## 项目介绍

用于查询FZYZ官网成绩及APP“JK同学”内成绩的API及前端网站（制作中）。

## 部署教程

### 部署开发/测试环境

需要安装的库：

Python3,pip3 ： 略；

`pip3 install Django beautifulsoup4 requests  ` 

开启测试Server ：

`python3 manage.py runserver 0.0.0.0:8000`

### 部署生产环境

[参见runoob](https://www.runoob.com/django/django-nginx-uwsgi.html)

## API参数

### fzyz/

用户名 ： 'user':'username',

密码 ： 'passwd':'password'

考试id ： 'exam':'exam_Id'

### JK/

用户名 ： 'user':'username',

密码 ： 'passwd':'password'

## 已知问题

前端仅支持FZYZ官网查询功能，且查询API时需跳转其他地址；

FZYZ官网仅能查询高三年级第一学期期末考卷面成绩，且返回的是未经解析的HTML；

JK仅能查询高三年级第一学期期末考化学学科卷面成绩，且返回的是未经解析的JSON。

## TO DO LIST

- [ ] 补全FZYZ官网查询科目/考试
- [ ] 补全JK查询科目/考试
- [ ] 构建能用的前端
- [ ] 构建美丽的前端
- [ ] 将代码部署服务器

## 我们需要？

能构建Ajax前端的人（需要jQery等JS基础）；

能设计美丽前端的人（需要框架基础）；

能补全API查询范围的人（JK查询范围扩大Lao_Liu还在制作中）;

发现任何问题后开issue反馈的人；

有兴趣提交任何代码的人。