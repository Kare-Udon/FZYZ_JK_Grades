# FZYZ_JK_Grades

## 项目介绍

用于查询 FZYZ 官网成绩和 APP“JK同学” 内成绩的 API 及前端网站。

## 部署教程

### 部署开发/测试环境

运行环境：`Python3`

安装依赖库：

```shell
pip3 install -U -r requirements.txt
```

开启测试Server ：
```shell
python3 manage.py runserver 0.0.0.0:8000
```

### 部署生产环境

[参见 runoob](https://www.runoob.com/django/django-nginx-uwsgi.html)

## API参数

### `fzyz/`
|键       |值     |
|-        |-      |
|'user'   |用户名 |
|'passwd' |密码   |
|'exam'   |考试id |

*注：学科id对照表如下：*


|考试（高中） |id|
|-            |- |
|总评         |3704|
|总评         |3703|

### `JK/`

|键         |值     |
|-          |-      |
|'user'     |用户名 |
|'passwd'   |密码   |
|'subject'  |学科id |

*注：学科id对照表如下：*

|学科|id|
|-   |- |
|数学|1 |
|语文|2 |
|英语|3 |
|物理|4 |
|化学|5 |
|生物|6 |
|政治|7 |
|历史|8 |
|地理|9 |
|信息|10|
|理综|11|
|文综|12|

## 已知问题

- [ ] FZYZ官网查询返回的是未经解析的HTML；
- [ ] 需要打开新的页面；
- [ ] 跨域问题。

## TO DO LIST

- [x] 补全FZYZ官网查询科目/考试
- [x] 补全JK查询科目/考试
- [x] 构建能用的前端
- [x] 构建美丽的前端
- [x] 将代码部署服务器

## 我们需要？

1.  能构建Ajax前端的人（需要jQery等JS基础）

2.  能设计美丽前端的人（需要框架基础）

3.  能补全API查询范围的人（希望高一/高二有兴趣的同学能提供开发所需要的数据）

4.  发现任何问题后开issue反馈的人

5.  有兴趣提交任何代码的人