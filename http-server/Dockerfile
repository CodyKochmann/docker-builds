FROM codykochmann/centos-patched
MAINTAINER kochmanncody@gmail.com

RUN yum install -y epel-release
RUN yum install -y npm
RUN yum remove -y epel-release
RUN npm install -g http-server

# still working on this portion...
# no permissions for world
# RUN chmod -vR o-rwx /
# read only permissions for group
# RUN chmod -vR g-wx /

RUN useradd --system --home-dir /var/http-server --create-home http-server

WORKDIR /var/http-server

USER http-server

ENTRYPOINT ["http-server", "-c-1"]