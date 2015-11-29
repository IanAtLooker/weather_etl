#!/bin/bash          

i="0"

while true; do

# Destination db business
PGHOST = `cat .weatherhost`
# PGDATABASE = weather
PGUSER = wunderground
PGPORT = 5432
PGPASSWORD = `cat .pgwrd`

i=$[$i+1]
echo $i

rm station_insert.txt
echo "station_insert.txt removed on `date -u`"
 
python weather.py
# eventually this should just call a function and pass the file in


while read line; do 
	PGHOST=$PGHOST PGUSER=$PGUSER PGPORT=$PGPORT PGPASSWORD=$PGPASSWORD \
	/usr/bin/psql -c "$line;"
    echo $line
done < station_insert.txt

echo "Sleeping on `date -u`"

sleep 43200 

done

# psql -U wunderground -h fwd-us.cn1001q2lzdp.us-east-1.rds.amazonaws.com