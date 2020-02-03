# DATABASE HW1
# John Ostermueller and Gavin Glenn
# 2/3/20

# Fortune_500_HQ

from helpers import *
from readDB import *

# num_records = 4110
# record_size = 71

#RANK,NAME,CITY,STATE,ZIP,EMPLOYEES                                     
rank_field_size = 20
name_field_size = 60
city_field_size = 20
state_field_size = 20
zip_field_size = 20
employees_field_size = 20

record_line_size = rank_field_size+name_field_size+city_field_size+state_field_size+zip_field_size+employees_field_size+1
num_fields = 6 


config=""
data=""
overflow=""

Database_open = False
# REQUIRED FUNCTIONS:
# ////////////////////////

# converts input .csv into triplet of files:
# Fortune_500_HQ.config: contains the number of records in the data file, describes the names, sizes of the fields in order
# Fortune_500_HQ.data: contains the data records, one per line, with fixed size fields
# Fortune_500_HQ.overflow: initially empty
def create_database():
	print("create_database")

	global config, data, overflow

	# Input File
	csv_name = input("Input the name of a .csv file (e.g. input): ") + str(".csv")

	# Get Data for files
	read_data = open(str(csv_name), "r")
	entries = 0
	record_size = 0
	for line in read_data:
		entries+=1
		if len(line) > record_size:
			record_size = len(line)
	read_data.close()
	
	num_records = entries-1

	#print("Record Size: " + str(record_size))
	print("Record Line Size: " + str(record_line_size))
	print("Num Records: " + str(num_records))

	# Create Config
	config = open(str(csv_name[:-4])+".config", "w")
	config.write("num_records " + str(num_records) + "\n")
	config.write("record_size " + str(record_size) + "\n")
	config.close()

	# # Create Data
	# read_data = open(str(csv_name), "r") #input .csv file
	# data = open(str(csv_name[:-4])+".data", "w") #new .data file
	# for line in read_data:
	# 	# A note to mention is that when reading the from the data the actual line length
	# 	# will be one more than the displayed line length to accomodate for \n character
	# 	new_line = lineset(line, record_size)
	# 	data.write(new_line)
	# data.close()
	# read_data.close()

	# Create Data
	read_data = open(str(csv_name), "r") #input .csv file
	data = open(str(csv_name[:-4])+".data", "w") #new .data file
	
	for line in read_data:
		# A note to mention is that when reading the from the data the actual line length
		# will be one more than the displayed line length to accomodate for \n character

		line = line.rstrip(" ")
		fields = line.split(",")
		#print(fields)

		if fields[0] == "RANK":
			continue

		#original order: RANK,NAME,CITY,STATE,ZIP,EMPLOYEES                                 
		#new order: NAME,RANK,CITY,STATE,ZIP,EMPLOYEES                                 
		new_line = fix_length(fields[1], name_field_size) # Name    
		new_line = new_line+fix_length(fields[0], rank_field_size) # Rank
		new_line = new_line+fix_length(fields[2], city_field_size) # City
		new_line = new_line+fix_length(fields[3], state_field_size) # State
		new_line = new_line+fix_length(fields[4], zip_field_size) # Zip
		new_line = new_line+fix_length(fields[5], employees_field_size) # Employees

		new_line = str(new_line) + "\n"
		#new_line = lineset(line, record_size)
		data.write(new_line)
	data.close()
	read_data.close()

	# Create Overflow
	overflow = open(str(csv_name[:-4])+".overflow", "w")
	overflow.close()

# opens input database.
# if another database is already open, the user is prompted to close that database first.
def open_database():
	print("open_batabase")

	global Database_open, config, data, overflow

	if Database_open == True:
		print("Another database is already open, please close that database first.")
		return
	
	Database_open = True
	print("Input prefix for datafiles:")

	db_name = input("Input the name of a .csv file (e.g. input): ")
	config = open(str(db_name)+".config", "w+")
	data = open(str(db_name)+".data", "w")
	overflow = open(str(db_name)+".overflow", "w+")

# closes current database files.
def close_database():
	print("close_database")

	global Database_open, config, data, overflow

	if Database_open == False:
		print("The database is not open.")
		return

	config.close()
	data.close()
	overflow.close()

############NOT IMPLEMENTED############
# finds record via primary key with seeks and binary search.
# displays name (from the config file) and the value (from the data file record)
def display_record():
	print("display_record")
	# if Database_open == False:
	# 	print("Please open the database first.")
	# 	return

	print(binary_search())

############NOT IMPLEMENTED############
# finds input record (using same process as displayRecord), then displays contents and allows updates in a specified field.
# the primary key is not allowed to be updated.
def update_record():
	print("update_record")
	# if Database_open == False:
	# 	print("Please open the database first.")
	# 	return

############NOT IMPLEMENTED############
# generates a "human readable" text file which displays the first ten records sorted by primary key
def create_report():
	print("create_report")
	# if Database_open == False:
	# 	print("Please open the database first.")
	# 	return
	merge()
	f = open("report.txt","w")
	for i in range(0, 10):
		#print first ten records nicely formatted
		print()

############NOT IMPLEMENTED############
def add_record():
	print("add_record")
	# if Database_open == False:
	# 	print("Please open the database first.")
	# 	return

############NOT IMPLEMENTED############
def delete_record():
	print("delete_record")
	# if Database_open == False:
	# 	print("Please open the database first.")
	# 	return

# OTHER FUNCTIONS
# ////////////////////////

############NOT IMPLEMENTED############
# # finds and returns a record given the primary key (name)
# def binary_search():
# 	print("findRecord")
# 	global data, num_records, record_line_size
# 	key = input("Input primary key (name) to search by (case insensitive):")
# 	key = upper(key)
# 	low = get_record(0)
# 	high = get_record(num_records-1)
# 	record = "requested record NOT_FOUND"
# 	Found = False
# 	while not Found and high>=low:
# 		middle = (low+high)//2
# 		record = get_record(data, int(middle+1))
# 		middleidnum = record[0:5]
# 		if int(middleidnum)== int(num_id):
# 			Found=True
# 		elif int(middleidnum)< int(num_id):
# 			low = middle+1
# 		else: 
# 			high = middle-1
	
# 	if(Found == True):
# 		return record
# 	else:
# 		return record

# finds and returns a record given the primary key (name)
def binary_search():
	print("findRecord")
	global data, num_records, record_line_size
	key = input("Input primary key (name) to search by (case insensitive):")
	key = str(key).upper()
	low = 0
	high = num_records-1
	record = "requested record NOT_FOUND"
	while low <= high:
		mid = (low+high)//2
		mid_record = get_record(data, mid)
		mid_key = get_key(mid_record)
		if mid_key == key: 
			return mid_record
		elif mid_key > key:
			low = mid+1
		else:
			high = mid-1
	return record

############NOT IMPLEMENTED############
def get_record(f, record_num):
	print("get_record")
	f = open("Fortune_500_HQ.data", "r")
	# print(f.readline())
	record = "requested record NOT_FOUND"
	global num_records
	global record_line_size
	
	if record_num>=0 and record_num<= num_records:
		f.seek(0,0)
		f.seek(((record_num) * record_line_size)) #offset from the beginning of the file
		record = f.readline()
		# print(record)
	f.close()
	return record

# returns key (name) from given record
def get_key(record):
	print("get_key")
	return(record[:name_field_size].rstrip(" "))

############NOT IMPLEMENTED############
# moves all elements in overflow to their appropriate locatoin in .data
def merge():
	print("merge")

# displays list of 8 required functions.
# executes a given function based on user input.
def menu():
	print("Input the appropriate number to execute a function:\n1. Create Database\n2. Open Database\n3. Close Database\n4. Display Record\n5. Update Record\n6. Create Report\n7. Add Record\n8. Delete Record\n9. Quit\n")
	user_input = input()
	# print(user_input)
	if user_input == "1":
		create_database()
	elif user_input == "2":
		open_database()
	elif user_input == "3":
		close_database()
	elif user_input == "4":
		display_record()
	elif user_input == "5":
		update_record()
	elif user_input == "6":
		create_report()
	elif user_input == "7":
		add_record()
	elif user_input == "8":
		delete_record()
	elif user_input == "9":
		close_database()
		exit()
	elif user_input == "0":
		print(get_record(data, 0))
		exit()

while True:
	menu()
