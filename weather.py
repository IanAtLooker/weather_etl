import readers_and_writers
import getters_and_setters

###		Rename functions because of reasons
fileReader = readers_and_writers.fileReader
fileWriter = readers_and_writers.fileWriter

updateStations = getters_and_setters.updateStations
updateConditions = getters_and_setters.updateConditions


###		Get Wunderground API keys (some day this'll be smarter about cycling through mutliple keys maybe)

weatherKey0 = fileReader('.wukey0')
weatherKey1 = fileReader('.wukey1')


###		Grab they db credentials

pgHostName = fileReader('.weatherhost')
pgWord = fileReader('.pgwrd')



###		Write station data

def stationFileWriter(api_key, state, city):
	stations = updateStations(api_key, state, city)
	fileWriter('station_insert.txt', stations)

def conditionFileWriter(api_key, station_id):
	conditions = updateConditions(api_key, station_id)
	fileWriter('condition_insert.txt', conditions)

# scStations = getters_and_setters.updateStations(weatherKey1, 'ca', 'santa_cruz')
# readers_and_writers.fileWriter('station_insert.txt', scStations)

conditionFileWriter(weatherKey1, 'KCASANTA360')