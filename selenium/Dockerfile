FROM codykochmann/py3
USER root
RUN yum install -y epel-release
RUN yum install -y chromium-headless chromedriver
RUN yum remove -y epel-release
USER py3
RUN /etc/py3/bin/pip install --isolated --no-cache-dir selenium
ENTRYPOINT /etc/py3/bin/python
