# Torfka
Torfka allows you to scrape the Dark Web using Tor, then publish to a local Kafka thread. 

##Requirements
- Apache Zookeeper
- Apache Kafka
- Tor
- Kafka-python
- Socksipy

##Running Torfka
You can run Torka with Docker, using the Tor service. Or stand-alone, using the TorBrowser App

####With Docker
1. After you build and run the Docker container, start the required services in /home

  ```
  $ bin/zookeeper-server-start.sh config/zookeeper.properties
  $ bin/kafka-server-start.sh config/server.properties
  $ sudo service tor start
  ```
2. Next you'll need to make sure torfka object has the correct paramenters in torfka.py, 

  ```
  Torfka(9050, <IP OF PRODUCER>)
  ```

3. Finally, run the script and follow your topic
  ```
  $ python Torfka/torfka.py
  # Consume new messages
  $ bin/kafka-console-consumer.sh --zookeeper  <IP OF PRODUCER>:2181 --topic Dark-web --from-beginning
  ```
####Without Docker using Tor Browser
Same steps, except:

- You do not need to run 'sudo service tor start', instead, open your TorBrowser.
 
- In torfka.py, you need to change the socket to 9150 instead of 9050:
  ```
  Torfka(9150, <IP OF PRODUCER>)
  ```
