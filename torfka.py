import socks
import socket
import urllib2
from kafka import SimpleProducer, KafkaClient
import threading


class Torfka(object):
    """
    Make sure that Zookeeper, Kafka, and Tor are all running.
    """

    def __init__(self, torSocket, hostIP):
        self.torSocket = torSocket
        self.hostIP = hostIP
        self.start()

    def create_connection(self, address, timeout=None, source_address=None):
        sock = socks.socksocket()
        sock.connect(address)
        return sock

    def start(self):
        socks.setdefaultproxy(
                                socks.PROXY_TYPE_SOCKS5,
                                "127.0.0.1",
                                self.torSocket
        )
        socket.socket = socks.socksocket
        #  We need to monkey patch the create connection function
        socket.create_connection = self.create_connection

    def reset(self):
        socks.setdefaultproxy()

    def produce(self, topic, message):
        #  Tor messes with the kafka stream. Reset changes.
        self.reset()
        kafka = KafkaClient('%s:9092' % self.hostIP)
        producer = SimpleProducer(kafka)
        producer.send_messages(topic, message)

    def onion_feed(self, site):
        onionfeed = urllib2.urlopen(site).read()
        #  Scrape here.
        return onionfeed


if __name__ == '__main__':
    """
    Use Socket 9150 for Tor Browser, 9050 for Tor Service
    The Following example uses Tor in your container to
    push darkweb messages to a local broker.
    """
    torf = Torfka(9050, 'localhost')
    #  Hidden Wiki
    msg = torf.onion_feed(
            'http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page'
    )
    torf.produce('Dark-web', msg)
    print msg
