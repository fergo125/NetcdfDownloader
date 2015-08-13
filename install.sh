#!/bin/bash
echo "Instalando NetcdfDownloader"
if [ -d /opt/NetcdfDownloader ];then 
	echo "Hay una instalacion existente"
	rm -fr /opt/NetcdfDownloader
fi
cp -rf ../NetcdfDownloader /opt
mkdir /opt/NetcdfDownloader/data
chmod 777 /opt/NetcdfDownloader/data 
if [ -z "$NETCDFDOWNLOADERHOME"]; then 
	echo "export NETCDFDOWNLOADERHOME=/opt/NetcdfDownloader" >>  /home/miocimar/.bashrc
	export NETCDFDOWNLOADERHOME=/opt/NetcdfDownloader
	echo "Variable de ambiente creada"
fi
touch tempCronScript
echo "01 00 * * * ${NETCDFDOWNLOADERHOME}/runDownloader.sh"	>> tempCronScript
crontab tempCronScript
rm -f tempCronScript
echo "Instalacion completada satisfactoriamente"
