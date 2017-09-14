import os
import sys
import requests
import requests.exceptions


def get_file(url, download_params, output_file):
	with open(os.path.abspath(output_file), 'wb') as f:
		f.truncate()
		response = requests.get(url, params=download_params,stream=True)
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
		else:
			print('Error descargando archivo ',  output_file)
		
