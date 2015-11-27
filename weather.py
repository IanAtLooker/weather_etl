import urllib2
import json
# import psycopg2		don't yet have this part done
import weather_readers


###		Get Wunderground API keys (some day this'll be smarter about cycling through mutliple keys maybe)

weatherKey0 = weather_readers.fileReader('.wukey0')
weatherKey1 = weather_readers.fileReader('.wukey1')

###		Grab they db credentials

pgHostName = weather_readers.fileReader('.weatherhost')
pgWord = weather_readers.fileReader('.pgwrd')


###		Get Stations

def getStations(api_key, state, city):
	url = 'http://api.wunderground.com/api/' + api_key + '/geolookup/q/' + state + '/' + city + '.json'
	weatherJson = weather_readers.connectionReader(url)
	parsedJson = json.loads(weatherJson)
	return parsedJson

thingTest = getStations(weatherKey1, 'ca', 'santa_cruz')
print thingTest['location']['nearby_weather_stations']['airport']['station'][0].keys()
print thingTest['location']['nearby_weather_stations']['pws']['station'][0].keys()


###		Make young connection string

conString = ''



	# TO DO
# connection business
# pull stations in santa cruz
# make sure they're in the db
# if not, upload to stations table
# pull current observations for each station ID
# load the estimates into the current observations table







# PSYCOPG2 EXAMPLES

# # Connect to an existing database
# >>> conn = psycopg2.connect("dbname=test user=postgres")

# # Open a cursor to perform database operations
# >>> cur = conn.cursor()

# # Execute a command: this creates a new table
# >>> cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# # Pass data to fill a query placeholders and let Psycopg perform
# # the correct conversion (no more SQL injections!)
# >>> cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
# ...      (100, "abc'def"))

# # Query the database and obtain data as Python objects
# >>> cur.execute("SELECT * FROM test;")
# >>> cur.fetchone()
# (1, 100, "abc'def")

# # Make the changes to the database persistent
# >>> conn.commit()

# # Close communication with the database
# >>> cur.close()
# >>> conn.close()

