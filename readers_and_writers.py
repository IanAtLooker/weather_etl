import urllib2
import datetime

###		READER FUNCTION$ BECAUSE WHY NOT

def fileReader(fileName):
	f = open(fileName, 'r')
	tempVariable = f.read().splitlines()[0]
	f.close()
	return tempVariable

def fileWriter(fileName, stringToWrite):
	f = open(fileName, 'w')
	f.write(str(stringToWrite))
	f.close()
	print "Write to " + fileName + " complete at " + str(datetime.datetime.utcnow())

def connectionReader(connString):
	f = urllib2.urlopen(connString)
	results = f.read()
	f.close()
	return results
