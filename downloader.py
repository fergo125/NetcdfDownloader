import os
import argparse
from datetime import datetime as dt
from datetime import timedelta
import json
import logging
import logging.config
from pprint import pprint
from getfile import get_file
from motu_lib import motu_api,utils_cas,utils_log

LOG_CFG_FILE = 'motu_lib/etc/log.ini'
log=None

def file_downloader_procesor(datasets):	
	for d in datasets:
		if "days_offset" in d:
			time_period = calculate_time_period(int(d['days_ahead']), int(d['days_offset']) )
		else:
			time_period = calculate_time_period(int(d['days_ahead']))
		del d['days_ahead']
		if d["method"] == "motu":
			d["params"]["date_max"] = time_period[1]
			d["params"]["date_min"] = time_period[0]
			download_muto( d["params"])  
		if d["method"] == "http":
			d["params"]["time_end"] = time_period[1]
			d["params"]["time_start"] = time_period[0]
			get_file(d["source"],d["params"],d["file_output"])  

def download_muto(params_dict):
	logging.addLevelName(utils_log.TRACE_LEVEL, 'TRACE')
	print(os.path.abspath(LOG_CFG_FILE))
	logging.config.fileConfig(os.path.abspath(LOG_CFG_FILE)) 
	log = logging.getLogger("motu-client-python")
	logging.getLogger().setLevel(logging.INFO)
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
	params_object.log_level = None
	params_object.size = None
	motu_api.execute_request(params_object)

class objectview(object):
    def __init__(self, d):
        self.__dict__ = d

def calculate_time_period(days,offset=0):
	daysahead = timedelta(days=days)
	start = dt.today() + offset
	end = start + daysahead
	return start.strftime("%Y-%m-%d %I:%M:%S"), end.strftime("%Y-%m-%d %I:%M:%S")
def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

def main():
	parser = argparse.ArgumentParser(description='Data downloader for forecast')
	parser.add_argument("-d","--datasets",type=str)
	args = parser.parse_args()
	print(args.datasets)
	with open(os.path.normpath(args.datasets)) as datasets_file:
		datasets = json_loads_byteified(datasets_file.read())
		file_downloader_procesor(datasets)

if __name__ == "__main__":
	main()

