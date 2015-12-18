# Torfka
####Tor 2 Kafka for the dark web

Requirements
- Apache Zookeeper
- Apache Kafka
- TorBrowser

Run dependecies:
```
$ cd kafka.X.X.X
$ bin/zookeeper-server-start.sh config/zookeeper.properties
$ bin/kafka-server-start.sh config/server.properties
```
Run Torfka:
```
$ python /path/to/torkfa.py
$ bin/kafka-console-consumer.sh --zookeeper  localhost:2181 --topic Dark-web
```
