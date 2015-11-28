import readers_and_writers
import getters_and_setters


###		Get Wunderground API keys (some day this'll be smarter about cycling through mutliple keys maybe)

weatherKey0 = readers_and_writers.fileReader('.wukey0')
weatherKey1 = readers_and_writers.fileReader('.wukey1')


###		Grab they db credentials

pgHostName = readers_and_writers.fileReader('.weatherhost')
pgWord = readers_and_writers.fileReader('.pgwrd')


###		Get station data

testPrint = getters_and_setters.updateStations(weatherKey1, 'ca', 'santa_cruz')
print 'testPrint:', '\n', testPrint




###		Make it still do what it orginally did

orignalThing = getters_and_setters.getConditions(weatherKey1, 'ca', 'santa_cruz')
# print  orignalThing


	# TO DO
# connection business
# pull stations in santa cruz
# loop through and build the insert string
# clear DB and use the new ones (later make sure they're in the db and upload if not)
# pull current observations for each station ID (probably needs a new query)
# load the estimates into the current observations table