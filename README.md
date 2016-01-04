# Torfka
####Tor 2 Kafka for the dark web

Requirements
- Apache Zookeeper
- Apache Kafka
- Tor
- Kafka-python
- Socksipy

Running Torfka:
```
# Go to Kafka folder.
$ bin/zookeeper-server-start.sh config/zookeeper.properties
$ bin/kafka-server-start.sh config/server.properties

# Run Tor
$ service tor start
$ python /path/to/torkfa.py

# Consume new messages
$ bin/kafka-console-consumer.sh --zookeeper  localhost:2181 --topic Dark-web
```
*Note:* If running Tor Browser, please change the port to 9150 in torfka.py to get it to work. 