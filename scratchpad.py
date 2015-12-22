import readers_and_writers
import getters_and_setters
import cleaner_uppers

###		Rename functions because of reasons
fileReader = readers_and_writers.fileReader
fileWriter = readers_and_writers.fileWriter

updateStations = getters_and_setters.updateStations
updateConditions = getters_and_setters.updateConditions
getConditions = getters_and_setters.getConditions
getStations = getters_and_setters.getStations
observationCleaner = cleaner_uppers.observationCleaner
nullStringer = cleaner_uppers.nullStringer


###		Get Wunderground API keys (some day this'll be smarter about cycling through mutliple keys maybe)

weatherKey0 = fileReader('.wukey0')
weatherKey1 = fileReader('.wukey1')


###		Grab they db credentials

pgHostName = fileReader('.weatherhost')
pgWord = fileReader('.pgwrd')



# def getStationIDs(api_key, state, city):
ids = []
statonResults = getStations(weatherKey1, 'ca', 'santa_cruz')['location']['nearby_weather_stations']

for airport in statonResults['airport']['station']:
	ids.append(airport['icao'])

for station in statonResults['pws']['station']:
	ids.append(station['id'])

print ids

print updateConditions(weatherKey1, ids[1])