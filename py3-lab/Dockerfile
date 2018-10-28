FROM codykochmann/py3
USER root
RUN yum install -y epel-release
RUN yum install -y groff nano multitail htop atop python-devel ufw perf python-perf fish autossh nmap tcpdump lsof net-tools git mercurial gcc vim-enhanced openssl openssh openssh-server iproute sshfs strace which wireshark iftop golang gcc gcc-c++ kernel-devel make which
USER py3
RUN mkdir -p /home/py3/.config/fish
RUN bash -c 'echo "source /home/py3/py3/bin/activate.fish 2>/dev/null" > /home/py3/.config/fish/config.fish'
RUN /etc/py3/bin/pip install --no-cache-dir --isolated awscli boto3 generators battle_tested ipython queued better_exceptions requests objgraph iactor graphdb numpy scipy pycallgraph elasticsearch pika ipdb cffi pylint yapf radon
ENTRYPOINT /usr/bin/fish
