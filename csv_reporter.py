import os
import requests as r
import csv
import argparse
import os

def main():
	parser = argparse.ArgumentParser(description='Update process for csvs')
	parser.add_argument('-f','--files',  type=str)
	parser.add_argument('-e','--endpoint',  type=str)
	args = parser.parse_args()
	with open(os.path.abspath(args.files)) as csv_files:
		reader = csv.DictReader(csv_files)
		for row in reader:
			print("Reporting:",row['csv_file'])
			r.post(args.endpoint,json=row)

if __name__ == "__main__":
	main()