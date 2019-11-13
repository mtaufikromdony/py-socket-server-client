FROM million12/ssh

RUN yum -y update && \
 yum -y install epel-release && \
 yum -y install openssh-server python36 python36-pip && \
 mkdir -p /var/run/sshd ; chmod -rx /var/run/sshd && \
 pip3 install tailer && \
 sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config && \
 sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
 sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config

ADD socket-client.py /
ADD init.sh /config/init/init.sh
EXPOSE 22
CMD ["/bin/sh", "./config/init/init.sh"]