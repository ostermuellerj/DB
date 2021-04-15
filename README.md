# Single-file database with overflow.

This simple database utilizes a memory-concious overflow buffer for adding entries. The database is sorted while the buffer is not. When the buffer grows larger than four records, the entries in the buffer are sorted with the rest of the records. No more than a few records are ever held in memory at the same time.

Below is a list of menu operations:
1. **Create new database**: Prompts the user for the name of a .csv file (e.g., "Fortune_500_HQ") to convert into a triplet of files: 
   * Fortune_500_HQ.config: contains the number of records in the data file, describes the names and sizes of the fields.
   * Fortune_500_HQ.data: contains the data records, one per line, with fixed size fields.
   * Fortune_500_HQ.overflow: initially empty, will be used to hold overflow records.
2. **Open database**: Promts user for an existing database to open.
3. **Close database**: The current database is closed.
4. **Display record**: Prompts user for key, then finds the record using binary search. The record is displayed with its key and value.
5. **Update record**: Record is found as above, then values of the record are inputted to be updated. The primary key of a record cannot be updated.
6. **Create report**: Creates a human-readable .txt file which displays the first ten records sorted in order by primary key.
7. **Add record**: Adds a record to the overflow file. If the overflow is full, the records in the buffer are sorted into the main set of records before adding.
8. **Delete record**: Deletes a record from the database. Deleted records are marked as "missing", and missing records are removed during re-sorting.
