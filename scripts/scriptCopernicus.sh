#!/bin/bash
time=$(date +"%Y%m%d ")
time1=$(date +"%Y-%m-%d ")
time2=$(date +"%Y-%m-%d" -d "120 hours")

#MERCATOR OCEAN
python "/home/miocimar/motu-client-python/motu-client.py" -u fmata -p 1gGjkdDl -m http://atoll.mercator-ocean.fr/mfcglo-mercator-gateway-servlet/Motu -s http://purl.org/myocean/ontology/service/database#GLOBAL_ANALYSIS_FORECAST_PHYS_001_002-TDS -d global-analysis-forecast-phys-001-002-2hourly-t-u-v-ssh -x -100 -X -73.5 -y 0 -Y 18 -t "$time1 00:00:00" -T "$time2 00:00:00" -z 0.494 -Z 0.4942 -v v -v u -v ssh -v temperature -o /home/miocimar/myocean 

cp /home/miocimar/myocean/data.nc /home/miocimar/myocean/global-analysis-forecast-phys-001-002-$time1.nc

exit #  The right and proper method of "exiting" from a script.


