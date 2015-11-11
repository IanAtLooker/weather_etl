#!/bin/bash          

i="0"

while true; do

sleep 600 

i=$[$i+1]

rm weather.json  /usr/local/var/postgres/weather.csv
 
python weather.py > weather.json

ruby to_csv.rb >> weather.csv
 
cp ~/weather.csv /usr/local/var/postgres

echo $i

done

