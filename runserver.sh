#!/bin/bash 
uwsgi --master --http 0.0.0.0:8000 --chdir /root/FZYZ_JK_Grades/API/ --module fzyz.wsgi