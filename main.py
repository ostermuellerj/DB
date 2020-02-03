from helpers import *
# DATABASE HW1
# John Ostermueller and Gavin Glenn
# 2/3/20

# REQUIRED FUNCTIONS:
# ////////////////////////

# converts input .csv into triplet of files:
# Fortune_500_HQ.config: contains the number of records in the data file, describes the names, sizes of the fields in order
# Fortune_500_HQ.data: contains the data records, one per line, with fixed size fields
# Fortune_500_HQ.overflow: initially empty

def create_database():
	print("create_database")
	#Input File
	csv_name = input("Input the name of a .csv file (e.g. input): ") + str(".csv")

	#Get Data for files
	read_data = open(str(csv_name), "r")
	entries = 0
	record_size = 0
	for line in read_data:
		entries+=1
		if len(line) > record_size:
			record_size = len(line)
	read_data.close()
	
	num_records = entries

	print("Record Size: " + str(record_size))
	print("Num Records: " + str(num_records))

	#Create Config
	config = open(str(csv_name[:-4])+".config", "w")
	config.close()

	#Create Data
	read_data = open(str(csv_name), "r")
	data = open(str(csv_name[:-4])+".data", "w")
	for line in read_data:
		#A note to mention is that when reading the from the data the actual line length
		# will be one more than the displayed line length to accomodate for \n character
		new_line = lineset(line, record_size)
		data.write(new_line)
	data.close()
	read_data.close()


	#Create Overflow
	overflow = open(str(csv_name[:-4])+".overflow", "w")
	overflow.close()


# opens input database.
# if another database is already open, the user is prompted to close that database first.
def open_batabase():
	print("open_batabase")
	print("Input prefix for datafiles:")

# closes current database files.
def close_database():
	print("close_database")

# finds record via primary key with seeks and binary search.
# displays name (from the config file) and the value (from the data file record)
def display_record():
	print("display_record")

# finds input record (using same process as displayRecord), then displays contents and allows updates in a specified field.
# the primary key is not allowed to be updated.
def update_record():
	print("update_record")

# generates a "human readable" text file which displays the first ten records sorted by primary key
def create_report():
	print("create_report")

def add_record():
	print("add_record")

def delete_record():
	print("delete_record")

# OTHER FUNCTIONS
# ////////////////////////

# finds and returns a record given the primary key
def find_record():
	print("findRecord")

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
		exit()
menu()