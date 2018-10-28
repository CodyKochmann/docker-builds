FROM codykochmann/centos-patched
RUN yum -y install yum-utils
RUN yum -y groupinstall development
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y install python36u

RUN mkdir -p --mode 700 /etc/py3
RUN mkdir --mode 700 /src

RUN useradd -ms /bin/bash py3
RUN chown -Rv py3 /etc/py3
RUN chown -Rv py3 /src

USER py3
RUN python3.6 -m venv --copies /etc/py3
RUN echo 'source /etc/py3/bin/activate' >> /home/py3/.bashrc

USER root
RUN echo 'source /etc/py3/bin/activate' >> /root/.bashrc

USER py3
RUN /etc/py3/bin/pip install --upgrade --isolated --no-cache-dir pip
RUN chmod -Rv go-rwx /etc/py3 

WORKDIR /src

ENTRYPOINT /bin/bash
