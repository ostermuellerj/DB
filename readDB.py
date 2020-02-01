import random
num_records = 4110
record_size = 71

def main():
	f = open('input.txt', 'r')
		
	print("\n\n\n")

	Record = get_record(f, 3)
	print("\n\nCall-->get_record(3)","\n\nOutput:",Record, "\n\n")
	
	Record = get_record(f, 9)
	print("Call-->get_record(9)","\n\nOutput:",Record, "\n\n")
	
	
	Record = get_record(f, 99999)
	print("Call-->get_record(99999)","\n\nOutput:",Record, "\n\n")
	
	
	Record = binary_search(f, 4)
	print("Call-->binary_search(4)","\n\nOutput:",Record, "\n\n")
	
	Record = binary_search(f, 12)
	print("Call-->binary_search(12)","\n\nOutput:",Record, "\n\n")
	
	f.close()

# Get record number n-th (from 1 to 4360)
def get_record(f, recordNum):
	#record = "We only have 9 records, requested record NOT_FOUND"
	record = "requested record NOT_FOUND"
	global num_records
	global record_size
	
	if recordNum>=1 and recordNum<= num_records:
		f.seek(0,0)
		f.seek(((recordNum) * record_size)) #offset from the beginning of the file
		record = f.readline()
		
	return record

# Binary Search by record id
def binary_search(f, num_id):
	global num_records,record_size
	low=0
	high=num_records-1
	#record = "We only have 9 records, requested record NOT_FOUND"
	record = "requested record NOT_FOUND"
	Found = False
	
	while not Found and high>=low and num_id<num_records:
		middle = (low+high)/2
		record = get_record(f, int(middle+1))
		middleidnum = record[0:5]
		if int(middleidnum)== int(num_id):
			Found=True
		elif int(middleidnum)< int(num_id):
			low = middle+1
		else: 
			high = middle-1
	
	if(Found == True):
		return record
	else:
		return record
	
main()	