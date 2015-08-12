#!/bin/bash
echo "Instalando NetcdfAutoDownloader"
if [ -d /opt/NetcdfAutoDownloader];then 
	echo "Hay una instalacion existente"
else
	cp -fr ../NetcdfAutoDownloader /opt
	if [-z "${NETCDFAUTODOWNLOADERHOME+x}"]; then 
		echo "export NETCDFAUTODOWNLOADERHOME=/opt/NetcdfAutoDownloader" >>  ~/.bashrc
		echo "Variable de ambiente creada"
	fi
	touch tempCronScript
	echo "01 01 * * * ${NETCDFAUTODOWNLOADERHOME}/runDownloader.sh"	>> tempCronScript
	crontab tempCronScript
	rm -f tempCronScript
fi
