import os
import argparse
from datetime import datetime as dt
from datetime import timedelta
import json
import logging
from pprint import pprint
from getfile import get_file
from motu_lib import motu_api,utils_cas,utils_log

def file_downloader_procesor(datasets):	
	for d in datasets:
		time_period = calculate_time_period(int(d['days_ahead']))
		del d['days_ahead']
		if d["method"] == "motu":
			d["params"]["date_max"] = time_period[1]
			d["params"]["date_min"] = time_period[0]
			download_muto( d["params"])  
		if d["method"] == "https":
			d["params"]["time_start"] = time_period[1]
			d["params"]["time_end"] = time_period[0]
			get_file(d["source"],d["file_output"],d["params"])  

def download_muto(params_dict):
	params_object = objectview(params_dict)
	params_object.auth_mode = motu_api.AUTHENTICATION_MODE_CAS
	params_object.proxy_server = None
	params_object.proxy_user = None
	params_object.proxy_pwd = None
	params_object.block_size = 65536
	params_object.socket_timeout = None
	params_object.user_agent = None
	params_object.extraction_output = False
	params_object.outputWritten = None
	params_object.console_mode = None
	params_object.describe = None
	params_object.sync= None
	params_object.log_level = utils_log.TRACE_LEVEL
	params_object.size = None
	motu_api.execute_request(params_object)

class objectview(object):
    def __init__(self, d):
        self.__dict__ = d

def calculate_time_period(days):
	daysahead = timedelta(days=days)
	start = dt.today()
	end = start + daysahead
	return start.strftime("%Y-%m-%d %I:%M:%S"), end.strftime("%Y-%m-%d %I:%M:%S")


def main():
	parser = argparse.ArgumentParser(description='Data downloader for forecast')
	parser.add_argument("-d","--datasets",type=str)
	args = parser.parse_args()
	print(args.datasets)
	with open(os.path.normpath(args.datasets)) as datasets_file:
		datasets = json.loads(datasets_file.read())
		file_downloader_procesor(datasets)

if __name__ == "__main__":
	main()