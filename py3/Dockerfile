FROM codykochmann/centos-patched
RUN yum -y install yum-utils
RUN yum -y groupinstall development
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y install python36u
RUN useradd -ms /bin/bash py3
USER py3
RUN python3.6 -m venv /home/py3/py3
RUN /home/py3/py3/bin/pip install -U pip
RUN echo 'source /home/py3/py3/bin/activate' > /home/py3/.bashrc
WORKDIR /home/py3
ENTRYPOINT /bin/bash
