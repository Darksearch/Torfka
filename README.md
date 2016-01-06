# Torfka
Torfka allows you to scrape the Dark Web using Tor, then publish to a Kafka thread. 

##Dependencies
- Apache Zookeeper
- Apache Kafka
- Tor
- Kafka-python
- Socksipy

##Running Torfka
You can run Torfka with the provided Dockerfile, or stand-alone. 

####With Docker
1. After you build and run the Docker container, start the required services in /home

  ```
  $ bin/zookeeper-server-start.sh config/zookeeper.properties
  $ bin/kafka-server-start.sh config/server.properties
  $ sudo service tor start
  ```
2. Next, make sure your torfka object has the correct paramenters in torfka.py, 

  ```
  Torfka(9050, <IP OF PRODUCER>)
  ```

3. Finally, run the script and follow your topic
  ```
  $ python Torfka/torfka.py
  $ bin/kafka-console-consumer.sh --zookeeper  <IP OF PRODUCER>:2181 --topic Dark-web --from-beginning
  ```

####Without Docker using TorBrowser
Same steps, except:

1. You do not need to run 'sudo service tor start', instead, open your TorBrowser.
 
2. In torfka.py, you need to change the socket to 9150 instead of 9050:
  ```
  Torfka(9150, <IP OF PRODUCER>)
  ```
  
####Troubleshooting Errors

- Insufficient Kafka memory Error- specify heap size

  ```
  $ export KAFKA_HEAP_OPTS="-Xmx1G -Xms1G"
  $ export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"  
  ```
