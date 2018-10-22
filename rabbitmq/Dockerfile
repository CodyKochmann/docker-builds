FROM rabbitmq:3-management
MAINTAINER kochmanncody@gmail.com
COPY ./rabbitmq.config /etc/rabbitmq/rabbitmq.config
EXPOSE 5672
EXPOSE 15672
HEALTHCHECK CMD python -c 'import urllib2;assert urllib2.urlopen("http://127.0.0.1:5672").read(), "could not read from port 5672";assert urllib2.urlopen("http://127.0.0.1:15672").read(), "could not read from port 15672";exit(0)'
#TODO: add healthcheck for high file descriptor and no swap

#docker run -d --restart always 
#-e RABBITMQ_ERLANG_COOKIE='<random-data>'
#-v /var/rabbit:/var/lib/rabbitmq 
#--hostname rabbit --name rabbit 
#--cpus 1 --cpuset-cpus 3 --cpu-shares 1000 --memory 64m 
#-v /root/rabbit.conf:/etc/rabbitmq/rabbitmq.config 
#-p 5672:5672 -p 15672:15672 rabbitmq:3-management
