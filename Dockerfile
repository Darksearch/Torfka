FROM ubuntu:14.04
MAINTAINER Vishal Lall "vishal.h.lall@gmail.com"
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
  mkdir ~/Downloads && \
  wget "http://mirror.cc.columbia.edu/pub/software/apache/kafka/0.8.2.1/kafka_2.11-0.8.2.1.tgz" -O ~/Downloads/kafka.tgz && \
  cd ~/Downloads && \
  tar -xvzf ~/Downloads/kafka.tgz --strip 1 
WORKDIR /home
RUN git clone https://github.com/vlall/torfka 
