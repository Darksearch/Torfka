import urllib2
import httplib
from torfka import Torfka

# Testing success Codes
if __name__ == '__main__':
	torf = Torfka(9050, 'localhost')
	success = 0
	failure = 0
	onionList = 'onions.txt'
	with open(onionList) as onionList:
		content = onionList.readlines()

	for url in content:
	    try:
	        connection = urllib2.urlopen(url)
	        print ('%s,%s') % (str(url.rstrip()), str(connection.getcode()))
	        connection.close()
	        if connection.getcode() == 200:
	        	success += 1
	    except:
	        print ('%s,%s') % (str(url.rstrip()),'404')
	        failure += 1
		fileOut = open("output.csv", "a")
		fileOut.write(msg + '\n')

	fileOut.close()
	print ('Successes: %d, Failures: %d' % (success,failure))
	torf.reset()
