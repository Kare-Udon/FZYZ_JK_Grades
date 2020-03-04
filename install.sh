#!/bin/bash
cd /root
git clone -b dev https://github.com/Lao-Liu233/FZYZ_JK_Grades.git
cd /root/FZYZ_JK_Grades
pip3 install -r requirements.txt
cd /root/FZYZ_JK_Grades/API
nohup bash /root/FZYZ_JK_Grades/runserver.sh &
