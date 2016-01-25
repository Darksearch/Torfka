import urllib2
from torfka import Torfka
import requests
from time import gmtime, strftime
from urllib2 import Request, urlopen, URLError


def working(site):
    req = urllib2.Request(site)
    try:
        urllib2.urlopen(req)
        print('%s, 200') % site
        return True

    except Exception:
        print('%s, 404') % site
        return False


def main():
    torf = Torfka(9150, 'localhost')

    with open('onionlinks.txt') as sites:
        for onion in sites:
            #  Remove CHOMP.
            onion = onion.rstrip()
            if working(onion):

                #  Write to HTML
                domain = onion.split('://')[1]
                domain = domain.split('.onion')[0]
                domain = str(domain + '.html')
                content = urllib2.urlopen(onion).read()
                Html_file = open('data/%s' % (domain), "w")
                Html_file.write(content)
                #  Log
                clock = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                logContent = (
                    '%s, %s, %s, %d\n' % (
                                        str(clock),
                                        str(onion),
                                        domain,
                                        len(content)
                                    )
                )
                print logContent
                with open("logs/scrape.log", "a") as log:
                    log.write(logContent)
                urllib2.urlopen(onion).close()
                Html_file.close()
    sites.close()
    torf.reset()


main()
