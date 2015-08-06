import xml.etree.ElementTree as ET

class UrlMaker:
	def __init__(self,filename):
		self.filename = filename
	def createUrl(self):
		url = ''
		querys = dict()
		alldata = ET.parse(self.filename)
		for dataset in alldata.iter():
			values = dict()
			if(dataset.tag == 'dataset'):
				for element in dataset.iter():
					if(element.tag == 'name'):
						values[element.tag]= element.text
					if(element.tag == 'daysAhead'):
						values[element.tag] = element.text
					if element.tag == 'source':
						url =element.get('link')
						for var in element.iter():
							if(var.tag != 'source'):
								text= '' 
								if(var.tag in values):
									values[var.tag].append(var.text)
								else:
									l = list()
									l.append(var.text)
									values[var.tag]=l
				querys[url]=values
		print(querys) 
		return querys

