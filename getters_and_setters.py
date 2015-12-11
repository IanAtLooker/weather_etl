import json
import readers_and_writers


##		GET YOUNG DATAUMS

def getStations(api_key, state, city):
	url = 'http://api.wunderground.com/api/' + api_key + '/geolookup/q/' + state + '/' + city + '.json'
	weatherJson = readers_and_writers.connectionReader(url)
	parsedJson = json.loads(weatherJson)
	return parsedJson


def getConditions(api_key, station_id, is_airport=False):
	if is_airport:
		url = 'http://api.wunderground.com/api/' + api_key + '/conditions/q/' + station_id + '.json'
	else:
		url = 'http://api.wunderground.com/api/' + api_key + '/conditions/q/pws:' + station_id + '.json'
	weatherJson = readers_and_writers.connectionReader(url)
	parsedJson = json.loads(weatherJson)
	return parsedJson

def updateStations(api_key, state, city):

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

def observationCleaner(observation):
	if observation in ("NA", "-9999", "-999", "-9999.00", "-999.00"):
		obs = "NULL"
	else:
		obs = observation
	return	obs

def nullStringer(observation, valueString, is_int=False, is_float=False):
	outputString = str(valueString)
	if observation == "NULL":
		outputString += ", NULL"
	else:
		if is_float:
			outputString += ", %f" %(float(obs))
		elif is_int:
			outputString += ", %i" %(int(obs))
	return outputString


