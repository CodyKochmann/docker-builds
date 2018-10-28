FROM codykochmann/centos-patched
RUN yum install -y epel-release 
RUN yum install -y syslog-ng
RUN yum remove -y epel-release
ENTRYPOINT /usr/bin/taskset -a -c 0 /sbin/syslog-ng --no-caps --foreground
