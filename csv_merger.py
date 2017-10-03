import os
import csv
import argparse
import datetime
def main():
	parser = argparse.ArgumentParser(description='csv columns file')
	parser.add_argument("-d1","--directory1", type=str)
	parser.add_argument("-d2","--directory2", type=str)
	parser.add_argument("-do","--directoryoutput", type=str)
	args = parser.parse_args()
	dir1 = os.path.abspath(args.directory1)
	dir2 = os.path.abspath(args.directory2)
	dir_output = os.path.abspath(args.directoryoutput)
	for filename in os.listdir(dir1):
		if filename.endswith(".csv"):
			csv_file1 = os.path.join(dir1,filename)
			csv_file2 = os.path.join(dir2,filename)
			csv_file_output = os.path.join(dir_output,filename)
			merge_files(csv_file1,csv_file2,csv_file_output)

def merge_files(csv_file1,csv_file2,csv_file_output):
	csv_out_file = open(csv_file_output,"w")
	csvfile1 = open(csv_file1,"r")
	csvfile2 = open(csv_file2,"r")
	csv1 = csv.DictReader(csvfile1)
	csv2 = csv.DictReader(csvfile2)
	field_names= []
	fields = []
	field_names.append("time")
	fields +=csv1.fieldnames
	fields.remove("time")
	fields +=csv2.fieldnames
	fields.remove("time")
	field_names += fields
	csv_out = csv.DictWriter(csv_out_file,fieldnames=field_names,lineterminator='\n')
	csv_out.writeheader()
	rows1 = delete_entries(csv1)
	rows2 = delete_entries(csv2)
	for row1,row2 in zip(rows1,rows2):
		row_out = dict()
		for k,i in row2.items():
			row_out[k] = i
		for k,i in row1.items():
			row_out[k] = i
		csv_out.writerow(row_out)

def delete_entries(rows):
	result = []
	for row in rows:
		if datetime.datetime.strptime(row["time"],"%Y-%m-%d %H:%M:%S").hour % 6 == 0:
			row["time"] += " Z"
			result.append(row)
	return result

if __name__ == "__main__":
	main()