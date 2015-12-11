import readers_and_writers
import getters_and_setters

###		Rename functions because of reasons
fileReader = readers_and_writers.fileReader
fileWriter = readers_and_writers.fileWriter

updateStations = getters_and_setters.updateStations
getConditions = getters_and_setters.getConditions
observationCleaner = getters_and_setters.observationCleaner
nullStringer = getters_and_setters.nullStringer


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
		# conditionValues += ", %i" %(int(obs))

		if obs == "NULL":
			conditionValues += ", NULL"
		else:
			conditionValues += ", %i" %(int(obs))

	elif key == "pressure_in":
		conditionInsert += ", pressure"
		conditionValues += ", %f" %(float(obs))
	elif key == "solarradiation":
		conditionInsert += ", solarradiation"
		conditionValues += ", '%s'" %(obs)
	elif key == "dewpoint_f":
		conditionInsert += ", dewpoint"
		conditionValues += ", %i" %(int(obs))
	elif key == "wind_speed":
		conditionInsert += ", wind_speed"
		conditionValues += ", %f" %(float(obs))
	elif key == "feelslike_f":
		conditionInsert += ", feels_like"
		conditionValues += ", %f" %(float(obs))
	elif key == "precip_today_in":
		conditionInsert += ", precipitation_today"
		conditionValues += ", %f" %(float(obs))
	elif key == "precip_1hr_in":
		print "precip_1hr_in", obs
		print "conditionResults['current_observation'][key]", conditionResults['current_observation'][key]
		conditionInsert += ", precipitation_hour"
		conditionValues = nullStringer(obs, conditionValues, is_float=True)
		# conditionValues += ", %f" %(float(obs))
		print "conditionValues", conditionValues
	elif key == "nowcast":
		conditionInsert += ", nowcast"
		conditionValues += ", '%s'" %(obs)
	elif key == "temp_f":
		conditionInsert += ", temperature"
		conditionValues += ", %f" %(float(obs))
	elif key == "pressure_trend":
		conditionInsert += ", pressure_trend"
		conditionValues += ", '%s'" %(obs)
	elif key == "visibility_mi":
		conditionInsert += ", visibility"
		conditionValues += ", %f" %(float(obs))
	elif key == "wind_dir":
		conditionInsert += ", wind_direction"
		conditionValues += ", '%s'" %(obs)
	elif key == "wind_degrees":
		conditionInsert += ", wind_degrees"
		conditionValues += ", %i" %(int(obs))
	elif key == "precip_1hr_in":
		conditionInsert += ", precipitation_hour"
		conditionValues += ", %f" %(float(obs))
	elif key == "wind_gust_mph":
		print "wind_gust_mph", obs, type(obs)
		print "conditionResults['current_observation'][key]", conditionResults['current_observation'][key]
		conditionInsert += ", wind_gust"
		conditionValues += ", %f" %(float(obs))
	elif key == "UV":
		conditionInsert += ", UV"
		conditionValues += ", %i" %(int(obs))
	elif key == "observation_epoch":
		conditionInsert += ", observation_epoch"
		conditionValues += ", %i" %(int(obs))
	elif key == "relative_humidity":
		conditionInsert += ", relative_humidity"
		conditionValues += ", %f" %(float(obs[:-1])/100)

conditionInsert += ")"
conditionValues += ");"

conditionInsert += " " + conditionValues

print conditionInsert








