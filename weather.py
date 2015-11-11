import urllib2
import json

f = urllib2.urlopen('http://api.wunderground.com/api/1003f9ff33c9e5f5/conditions/q/CA/Santa_Cruz.json')

json_string = f.read()
print  json_string
f.close()
