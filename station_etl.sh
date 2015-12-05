#!/bin/bash          

i="0"

while true; do

# Destination db business
PGHOST=`cat .weatherhost`
# PGDATABASE = weather
PGUSER=wunderground
PGPORT=5432
PGPASSWORD=`cat .pgwrd`
# APIKEY=`cat .wukey1`

i=$[$i+1]
echo $i

rm station_insert.txt
echo "station_insert.txt removed on `date -u`"
 
# python weather.py
# eventually this should just call a function and pass the file in

python -c "from weather import *; stationFileWriter(weatherKey0, 'ca', 'santa_cruz')"

# For now, just truncate the table and re-populate
PGHOST=$PGHOST PGUSER=$PGUSER PGPORT=$PGPORT PGPASSWORD=$PGPASSWORD \
	/usr/bin/psql -c "TRUNCATE TABLE stations;"
echo "stations truncated on `date -u`"

while read line; do 
	PGHOST=$PGHOST PGUSER=$PGUSER PGPORT=$PGPORT PGPASSWORD=$PGPASSWORD \
	/usr/bin/psql -c "$line;"
done < station_insert.txt

echo "Sleeping on `date -u`"

sleep 43200 

done