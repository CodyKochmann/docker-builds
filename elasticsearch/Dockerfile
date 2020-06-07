FROM docker.elastic.co/elasticsearch/elasticsearch:7.7.1
MAINTAINER kochmanncody@gmail.com
ENV node.name=$HOSTNAME
ENV discovery.zen.ping_timeout=300s
HEALTHCHECK CMD curl -o - 127.0.0.1:9200
ENV ES_JAVA_OPTS="-XX:MaxGCPauseMillis=100 -Xlog:gc: -XX:MinRAMPercentage=10.0 -XX:CMSInitiatingOccupancyFraction=20 -Xmx2048m -Xms64m -XX:+PrintFlagsFinal -XX:+ClassUnloading -XX:-UsePSAdaptiveSurvivorSizePolicy -XX:+UseStringDeduplication -XX:-UseGCOverheadLimit  -XX:-UseSerialGC -XX:-UseConcMarkSweepGC -XX:-UseG1GC -XX:-UseParallelGC -XX:+UnlockExperimentalVMOptions -XX:+UseZGC -XX:-UseThreadPriorities -XX:+UseDynamicNumberOfGCThreads -XX:HeapSizePerGCThread=5452595 -XX:-UseBiasedLocking -XX:-MaxFDLimit -XX:MaxRAMFraction=2 -XX:MaxRAMPercentage=50.0 -XX:+BackgroundCompilation -XX:CICompilerCount=2 -XX:-PrintCompilation -XX:InlineSmallCode=256M -XX:MaxInlineSize=256M -XX:+DisableExplicitGC"
RUN rm -f config/jvm.options && touch config/jvm.options
