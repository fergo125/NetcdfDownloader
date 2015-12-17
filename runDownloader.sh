#! /bin/bash
echo "corriendo downloader"
sh /opt/NetcdfDownloader/scripts/scriptCopernicus.sh
echo "datos descargados"
python3 /opt/NetcdfDownloader/scripts/Downloader.py
echo "datos descargados"
kill $(ps aux | grep 'java' | awk '{print $2}')
idv /opt/NetcdfDownloader/Plantillas/Display3x3.xidv &
exit 0
 
