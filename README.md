# FZYZ_JK_Grades

![](https://img.shields.io/badge/language-python-blue.svg) ![](https://img.shields.io/github/issues/Lao-Liu233/FZYZ_JK_Grades) ![](https://img.shields.io/github/stars/Lao-Liu233/FZYZ_JK_Grades) ![](https://img.shields.io/github/v/release/Lao-Liu233/FZYZ_JK_Grades) ![](https://img.shields.io/github/license/Lao-Liu233/FZYZ_JK_Grades)

## 项目介绍

用于查询 FZYZ 官网成绩和 APP “ JK 同学 ” 内成绩的 API 及前端网站。

![](https://cdn.jsdelivr.net/gh/Lao-Liu233/blog_imgs/fzyz_jk_grades/guide.png)

## Demo

### Demo 站点

[Lao_Liu搭建的查询站点](https://grade.laoliu.eu.org)

### Demo API

https://api2.laoliu.eu.org

https://api.laoliu.eu.org:4438

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

#### 使用 Docker 部署

详见 [Docker Hub](https://hub.docker.com/r/laoliu233/fzyz_jk_grades_api) 。

#### 部署基于 Uwsgi 的 API 服务

`nohup bash ./runserver.sh &`

默认端口为 8000 。

## API参数

### `fzyz_net_exam`
|键       |值     |
|-        |-      |
|'user'   |用户名 |
|'passwd' |密码   |
|'para_academic_Year'|查询年份 |
|'para_KEY'|查询学期 |

*注：*年份格式：年份1-年份2，（如 2019-2020）

*查询学期对照表如下：*


| 考试（高中） | id   |
| ------------ | ---- |
| 第一学期     | 1    |
| 第二学期     | 2    |

### `fzyz_net/`
|键       |值     |
|-        |-      |
|'user'   |用户名 |
|'passwd' |密码   |
|'exam'   |考试id |

*注：学科id对照表如下：*


|考试（高中） |id|
|-            |- |
|总评         |3704|
|卷面         |3703|

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

- FZYZ 官网查询中，查询卷面成绩时无法显示等第。

> 据分析此问题来源于 FZYZ 官网，由于较难修复暂时挂起。

## TO DO LIST

- 继续美化 UI；
- 修复任何被发现的 BUG；
- 在KubeSail上搭建稳定后端；
- 将网站推广。

## 我们需要？

2.  能设计美丽前端的人（需要框架基础）
4.  发现任何问题后开 issue 反馈的人
5.  有兴趣提交任何代码的人

## 特别感谢

### 开发人员

[@Lao_Liu](https://github.com/Lao-Liu233)

- 代码开发
- UI 设计
- API 设计
- Debugger

[@yihanwu1024]( https://github.com/yihanwu1024)

- UI 设计
- Debugger

[@zhangshifen38](https://github.com/zhangshifen38)

- Debugger

[@jerryc05](https://github.com/jerryc05)

- 技术顾问
- 代码开发
- Debugger

[@Googleplex](https://github.com/y-young)

- 技术顾问

感谢 [@mnihyc](https://github.com/mnihyc) 提供的 Demo API服务器！

### 借物表

Django https://www.djangoproject.com/

jQuery https://jquery.com/

Bootstrap https://getbootstrap.com/

Material Design for Bootstrap https://mdbootstrap.com/

Cloudflare CDN https://www.cloudflare.com/

jsDelivr CDN https://www.jsdelivr.com/

Kubusail https://kubesail.com/

......