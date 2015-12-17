#!/bin/bash
echo "Instalando NetcdfDownloader"
if [ -d /opt/NetcdfDownloader ];then 
	echo "Hay una instalacion existente"
	rm -fr /opt/NetcdfDownloader
fi
cp -rf ../NetcdfDownloader /opt
mkdir /opt/NetcdfDownloader/data
chmod 777 /opt/NetcdfDownloader/data 
chmod 777 /opt/NetcdfDownloader/scripts/Downloader.py
chmod 777 /opt/NetcdfDownloader/scripts/scriptCopernicus.sh
if [ -z "$NETCDFDOWNLOADERHOME"]; then 
	echo "export NETCDFDOWNLOADERHOME=/opt/NetcdfDownloader" >>  /home/miocimar/.bashrc
	export NETCDFDOWNLOADERHOME=/opt/NetcdfDownloader
	echo "Variable de ambiente creada"
fi

touch tempCronScript
touch /opt/NetcdfDownloader/log
chmod 777 /opt/NetcdfDownloader/log
echo "00 3 * * * sh ${NETCDFDOWNLOADERHOME}/runDownloader.sh &> log">> tempCronScript
crontab tempCronScript
rm -fr "$NETCDFDOWNLOADERHOME"/.git
rm -fr "$NETCDFDOWNLOADERHOME"/.gitignore
rm -f tempCronScript
cp ncdfdownloader /usr/bin
echo "Instalacion completada satisfactoriamente"
