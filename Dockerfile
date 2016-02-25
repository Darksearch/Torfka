FROM ubuntu:14.04
RUN apt-get update && apt-get install -y \
	python \
	build-essential \
	python-dev \
	python-pip \
	git \
	wget \
	default-jre \
	zookeeperd \
	tor \
	python-socksipy

# Kafka installation
RUN \
  pip install kafka-python 
WORKDIR /home
RUN \
  wget "http://apache.arvixe.com/kafka/0.9.0.0/kafka_2.11-0.9.0.0.tgz" -O kafka.tgz && \
  tar -xvzf kafka.tgz --strip 1 && \
  rm kafka.tgz && \
  git clone https://github.com/vlall/torfka
