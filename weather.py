import readers_and_writers
import getters_and_setters


###		Get Wunderground API keys (some day this'll be smarter about cycling through mutliple keys maybe)

weatherKey0 = readers_and_writers.fileReader('.wukey0')
weatherKey1 = readers_and_writers.fileReader('.wukey1')


###		Grab they db credentials

pgHostName = readers_and_writers.fileReader('.weatherhost')
pgWord = readers_and_writers.fileReader('.pgwrd')



###		Write station data

def stationFileWriter(api_key, state, city):
	stations = getters_and_setters.updateStations(api_key, state, city)
	readers_and_writers.fileWriter('station_insert.txt', stations)


# scStations = getters_and_setters.updateStations(weatherKey1, 'ca', 'santa_cruz')
# readers_and_writers.fileWriter('station_insert.txt', scStations)