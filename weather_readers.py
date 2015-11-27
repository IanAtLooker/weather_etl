import urllib2
import json
# import psycopg2		don't yet have this part done


###		FUNCTION$ BECAUSE WHY NOT

def fileReader(fileName):
	f = open(fileName, 'r')
	tempVariable = f.read().splitlines()[0]
	f.close()
	return tempVariable

def connectionReader(connString):
	f = urllib2.urlopen(connString)
	results = f.read()
	f.close()
	return results