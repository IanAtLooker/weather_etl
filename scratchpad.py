import readers_and_writers
import getters_and_setters
import cleaner_uppers

###		Rename functions because of reasons
fileReader = readers_and_writers.fileReader
fileWriter = readers_and_writers.fileWriter

updateStations = getters_and_setters.updateStations
getConditions = getters_and_setters.getConditions
observationCleaner = cleaner_uppers.observationCleaner
nullStringer = cleaner_uppers.nullStringer


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
	

def updateConditions(api_key, state, city):

	statonResults = getStations(api_key, state, city)['location']['nearby_weather_stations']
	airportStations = statonResults['airport']['station']
	personalStations = statonResults['pws']['station']

	airportUpdate = ''
	personalUpdate = ''
	stationUpdate = ''

		 # WRITE INSERT STATEMENT FOR AIRPORT STATION DATA
	for airport in airportStations:
		airportUpdate += """INSERT INTO stations (wu_id, city, state, country, lat, lon) VALUES ('%s', '%s', '%s', '%s', %f, %f);""" %(
			airport['icao'], airport['city'], airport['state'], airport['country'], float(airport['lat']), float(airport['lon']))
		airportUpdate += ' \n'

		# WRITE INSERT STATEMENT FOR PERSONAL STATION DATA
	for station in personalStations:
		personalUpdate += """INSERT INTO stations (wu_id, city, state, country, lat, lon, neighborhood, distance_mi, distance_km) VALUES ('%s', '%s', '%s', '%s', %f, %f, '%s', %i, %i);""" %(
				station['id'], station['city'], station['state'], station['country'], float(station['lat']), float(station['lon']),
				station['neighborhood'], int(station['distance_mi']), int(station['distance_km']))
		personalUpdate += ' \n'

	stationUpdate += airportUpdate + personalUpdate
	return stationUpdate



# THIS WILL BE A FUNCTION

conditionResults = getConditions(weatherKey1, 'KCASANTA360')

conditionInsert = ""
conditionValues = ""

conditionInsert += "INSERT INTO conditions (wu_station_id"
conditionValues += "VALUES ('KCASANTA360'"

for key in conditionResults['current_observation']:
	obs = observationCleaner(conditionResults['current_observation'][key])

	if key == "weather":
		conditionInsert += ", weather"
		conditionValues += ", '%s'" %(obs)
	elif key == "windchill_f":
		conditionInsert += ", windchill"
		conditionValues += nullStringer(obs, is_int=True)
	elif key == "pressure_in":
		conditionInsert += ", pressure"
		conditionValues += nullStringer(obs, is_float=True)
	elif key == "solarradiation":
		conditionInsert += ", solarradiation"
		conditionValues += ", '%s'" %(obs)
	elif key == "dewpoint_f":
		conditionInsert += ", dewpoint"
		conditionValues += nullStringer(obs, is_int=True)
	elif key == "wind_speed":
		conditionInsert += ", wind_speed"
		conditionValues += nullStringer(obs, is_float=True)
	elif key == "feelslike_f":
		conditionInsert += ", feels_like"
		conditionValues += nullStringer(obs, is_float=True)
	elif key == "precip_today_in":
		conditionInsert += ", precipitation_today"
		conditionValues += nullStringer(obs, is_float=True)
	elif key == "precip_1hr_in":
		conditionInsert += ", precipitation_hour"
		conditionValues += nullStringer(obs, is_float=True)
	elif key == "nowcast":
		conditionInsert += ", nowcast"
		conditionValues += ", '%s'" %(obs)
	elif key == "temp_f":
		conditionInsert += ", temperature"
		conditionValues += nullStringer(obs, is_float=True)
	elif key == "pressure_trend":
		conditionInsert += ", pressure_trend"
		conditionValues += ", '%s'" %(obs)
	elif key == "visibility_mi":
		conditionInsert += ", visibility"
		conditionValues += nullStringer(obs, is_float=True)
	elif key == "wind_dir":
		conditionInsert += ", wind_direction"
		conditionValues += ", '%s'" %(obs)
	elif key == "wind_degrees":
		conditionInsert += ", wind_degrees"
		conditionValues += nullStringer(obs, is_int=True)
	elif key == "precip_1hr_in":
		conditionInsert += ", precipitation_hour"
		conditionValues += nullStringer(obs, is_float=True)
	elif key == "wind_gust_mph":
		conditionInsert += ", wind_gust"
		conditionValues += nullStringer(obs, is_float=True)
	elif key == "UV":
		conditionInsert += ", UV"
		conditionValues += nullStringer(obs, is_int=True)
	elif key == "observation_epoch":
		conditionInsert += ", observation_epoch"
		conditionValues += nullStringer(obs, is_int=True)
	elif key == "relative_humidity":
		conditionInsert += ", relative_humidity"
		conditionValues += nullStringer(obs, is_float=True)

conditionInsert += ")"
conditionValues += ");"

conditionInsert += " " + conditionValues

print conditionInsert





