FROM python
RUN /bin/bash
#RUN apt update
RUN cd /root \
	&& git clone https://github.com/Lao-Liu233/FZYZ_JK_Grades.git \
	&& cd /root/FZYZ_JK_Grades \
	&& pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
#nohup bash /root/FZYZ_JK_Grades/runserver.sh
 
