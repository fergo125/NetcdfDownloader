import shutil
import requests
import requests.exceptions
import time
import sys
from datetime import date, timedelta
import xml.etree.ElementTree as ET
import urlCreator


#Recordatorio para Fernando: Aun falta ver como se itera en el diccionario para 
#poder ejecutar todas las consultas a los webservices, ademas hay que ver porque 
#no está funcionando bien la descarga de datos, al parecer hay algo con la descarga
#de archivos que no está funcionando bien.

f = 'dataCatExample.xml'
urlMaker = urlCreator.UrlMaker(f)
dataRequest = urlMaker.createUrl() 


for p,a in dataRequest.items():
		filename = a['name'] + ".nc"
		del a['name']
		daysAhead = timedelta(days=int(a['daysAhead']))
		del a['daysAhead']
		print(p)
		print(a)
		datatimeStart = date.today()
		datatimeEnd= datatimeStart + daysAhead
		
		timeStart = str(datatimeStart.year) +'-' + str(datatimeStart.month) + '-'+ str(datatimeStart.day) +'T'+'00\x3A00\x3A00'
		timeEnd = str(datatimeEnd.year) +'-' + str(datatimeEnd.month) + '-'+ str(datatimeEnd.day) +'T'+'00\x3A00\x3A00'
		
		print(timeStart)
		print(timeEnd)
		
		a['time_start']= timeStart
		a['time_end']= timeEnd
		
		filepath = './data/' +filename
		with open(filepath, 'wb') as f:
			f.truncate()
			print ("Downloading " + filename)
			response = requests.get(p, params=a,stream=True)
			print('status code',response.status_code)
			if(response.status_code == 200):
				total_length = response.headers.get('content-length')
				if total_length is None: # no content length header
					f.write(response.content)
				else:
					dl = 0
					total_length = int(total_length)
					for data in response.iter_content():
						dl += len(data)
						f.write(data)
						done = int(50 * dl / total_length)
						sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)))
						sys.stdout.flush()
				print('File succesfully downloaded: ', filename)
			else:
				print('Error downloading file: ',  filename)
		
