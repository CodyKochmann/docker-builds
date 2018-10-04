FROM codykochmann/py3
USER root
RUN yum install -y epel-release
RUN yum install -y chromium-headless chromedriver
RUN yum remove -y epel-release
USER py3
RUN /home/py3/py3/bin/pip install --isolated --no-cache-dir selenium
ENTRYPOINT /home/py3/py3/bin/python
