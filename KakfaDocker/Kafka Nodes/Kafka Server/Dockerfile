FROM ubuntu

# Install dependencies
RUN apt-get update && apt-get install -y software-properties-common wget vim
RUN apt-get update && apt-get install -y python3.4 python3-pip 
RUN apt-get update -y && apt-get upgrade -y
#   JAVA
RUN add-apt-repository ppa:webupd8team/java
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections
RUN apt update && apt install -y oracle-java8-installer
RUN apt install -y oracle-java8-set-default
#   Zookeeper
RUN apt-get install -y zookeeperd

# Download Kafka
RUN mkdir kafka
RUN cd kafka
ADD http://www-eu.apache.org/dist/kafka/1.0.1/kafka_2.12-1.0.1.tgz .

# Next, create a directory for Kafka installation:
RUN mkdir /opt/Kafka

# Copy downloaded to here
RUN tar -xvf kafka_2.12-1.0.1.tgz -C /opt/Kafka/

# Start the Kafka server
# RUN cd /opt/Kafka
# RUN sh /opt/Kafka/kafka_2.12-1.0.1/bin/kafka-server-start.sh /opt/Kafka/kafka_2.12-1.0.1/config/server.properties

