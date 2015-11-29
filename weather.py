import readers_and_writers
import getters_and_setters


###		Get Wunderground API keys (some day this'll be smarter about cycling through mutliple keys maybe)

weatherKey0 = readers_and_writers.fileReader('.wukey0')
weatherKey1 = readers_and_writers.fileReader('.wukey1')


###		Grab they db credentials

pgHostName = readers_and_writers.fileReader('.weatherhost')
pgWord = readers_and_writers.fileReader('.pgwrd')

# Still doing this stuff in python instead of shell so we can do fancier stuff later


###		Get station data

scStations = getters_and_setters.updateStations(weatherKey1, 'ca', 'santa_cruz')
readers_and_writers.fileWriter('station_insert.txt', scStations)


###		Make it still do what it orginally did for now

orignalThing = getters_and_setters.getConditions(weatherKey1, 'ca', 'santa_cruz')
# print  orignalThing