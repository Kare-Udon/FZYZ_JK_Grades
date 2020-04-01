FROM python

MAINTAINER Lao_Liu

RUN /bin/bash
RUN cd /root \
	&& apt update \
	&& apt -y install git \
	&& git clone https://github.com/Lao-Liu233/FZYZ_JK_Grades.git \
	&& cd /root/FZYZ_JK_Grades \
	&& pip3 install -r requirements.txt
#	&& pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
#nohup bash /root/FZYZ_JK_Grades/runserver.sh
