import socks
import socket
import urllib2
from kafka import SimpleProducer, KafkaClient
import threading

# Make sure that Zookeeper, Kafka, and Tor are all running. 

class Torfka:

	def __init__(self, n =120, torSocket = 9150):	
		# Loop printing to the Kafka producer every n seconds
		threading.Timer(n, main).start()
		self.start()

	def create_connection(self, address, timeout=None, source_address=None):
	    sock = socks.socksocket()
	    sock.connect(address)
	    return sock

	def start(self):
		# Socket is 9150, 9050 was the old one. Troubleshoot this using netstat
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
		socket.socket = socks.socksocket
		# We need to monkey patch the create connection function
		socket.create_connection = self.create_connection

	def reset(self):
		socks.setdefaultproxy()

	def produce(self, topic, message):
		# Tor messes with the kafka stream, so lets reset some changes we've made. 
		self.reset()
		kafka = KafkaClient('localhost:9092')
		producer = SimpleProducer(kafka)
		producer.send_messages(topic, message)

	def onion_feed(self, site):
		onionfeed = urllib2.urlopen(site).read()
		# Scrape here. 
		return onionfeed

def main():
	torf = Torfka(120)
	msg = torf.onion_feed()
	torf.produce('Dark-web', msg)
	print msg
main()
