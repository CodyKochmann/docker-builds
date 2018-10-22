FROM docker.elastic.co/elasticsearch/elasticsearch:6.4.2
MAINTAINER kochmanncody@gmail.com
ENV node.name=$HOSTNAME
ENV discovery.zen.ping_timeout=300s
ENV ES_JAVA_OPTS="-XX:MinRAMPercentage=10.0 -XX:CMSInitiatingOccupancyFraction=20 -Xmx256m -Xms256m -XX:+PrintFlagsFinal -XX:+ClassUnloading -XX:-UsePSAdaptiveSurvivorSizePolicy -XX:+UseStringDeduplication -XX:-UseGCOverheadLimit  -XX:-UseSerialGC -XX:-UseConcMarkSweepGC -XX:-UseG1GC -XX:+UseParallelGC -XX:-UseThreadPriorities -XX:+UseDynamicNumberOfGCThreads -XX:HeapSizePerGCThread=5452595"
HEALTHCHECK CMD curl -o - 127.0.0.1:9200
