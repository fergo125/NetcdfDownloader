import os
import csv
import argparse

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
	field_names +=csv1.fieldnames
	# temp_fields = csv2.fieldnames
	# temp_fields.remove("time")
	# field_names += temp_fields
	field_names += csv2.fieldnames

	print(field_names)
	csv_out = csv.DictWriter(csv_out_file,fieldnames=field_names,lineterminator='\n')
	csv_out.writeheader()
	print(field_names)
	for row1,row2 in zip(csv1,csv2):
		row_out = dict()
		for k,i in row2.items():
			row_out[k] = i
		for k,i in row1.items():
			row_out[k] = i
		print(row_out)
		csv_out.writerow(row_out)
if __name__ == "__main__":
	main()