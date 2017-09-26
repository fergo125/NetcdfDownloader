import os
import csv
import argparse

def main():
	parser = argparse.ArgumentParser(description='csv columns file')
	parser.add_argument("-d1","--directory1",type=str)
	parser.add_argument("-d2","--directory2",type=str)
	parser.add_argument("-do","--directoryoutput",type=str)
	dir1 = os.path.abspath(parser.directory1)
	dir2 = os.path.abspath(parser.directory1)
	dir_output = os.path(parser.directoryoutput)
	for filename in os.listdir(dir1):
		if filename.endswith(".csv"):
			csv_file1 = filename,
			csv_file2 = os.path.join(dir2,filename)
			csv_file_output = os.path.join(directoryoutput,filename)
			merge_files(csv_file1,csv_file2,csv_file_output)

def merge_files(csv_file1,csv_file2,csv_file_output):
	csv1 = csv.DictReader(csv_file1)
	csv2 = csv.DictReader(csv_file2)
	field_names=[]
	field_names.append(csv1.fieldnames)
	field_names.append(csv2.fieldnames)
	csv_out = csv.DictWriter(csv_file_output,field_names)
	csv_out.writeheader()
	print(field_names)
	for row1,row2 in csv1,csv2:
		row_out = dict()
		for k,e in row2:
			row_out[k] = e
		for k,e in row1:
			row_out[k] = e
		csv_out.writerow(row_out)
