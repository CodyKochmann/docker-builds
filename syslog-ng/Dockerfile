FROM codykochmann/centos-patched
RUN yum install -y epel-release 
RUN yum install -y syslog-ng
RUN yum remove -y epel-release
ENTRYPOINT /sbin/syslog-ng --no-caps --foreground
