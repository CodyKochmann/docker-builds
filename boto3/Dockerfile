FROM codykochmann/py3
USER root
RUN yum install -y groff
USER py3
RUN /home/py3/py3/bin/pip install boto3
ENTRYPOINT /home/py3/py3/bin/python
