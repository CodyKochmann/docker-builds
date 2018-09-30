FROM codykochmann/py3
USER root
RUN yum install -y groff
USER py3
RUN /home/py3/py3/bin/pip install awscli
ENTRYPOINT /home/py3/py3/bin/aws
