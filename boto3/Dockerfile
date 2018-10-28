FROM codykochmann/py3
USER root
RUN yum install -y groff
USER py3
RUN /etc/py3/bin/pip install --no-cache-dir boto3
RUN chmod -Rv go-rwx /etc/py3
ENTRYPOINT /etc/py3/bin/python
