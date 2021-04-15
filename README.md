# Single-file database with overflow.

This simple database utilizes a memory-concious overflow buffer for adding entries. The database is sorted while the buffer is not. When the buffer grows larger than four records, the entries in the buffer are sorted with the rest of the records. No more than a few records are ever held in memory at the same time.

Below is a list of menu operations:
1. Create new database: Prompts the user for the name of a .csv file (e.g., "Fortune_500_HQ". Reads and converts the .csv file into a triplet of files: Fortune_500_HQ.config, Fortune_500_HQ.data, Fortune_500_HQ.overflow. 
   * Fortune_500_HQ.config: contains the number of records in the data file, describes the names, sizes of the fields in order, anything else you want. The first field is assumed to be the key.
   * Fortune_500_HQ.data: contains the data records, one per line, with fixed size fields. You may use any separator you want (or no separator). There should be no blank records.
   * Fortune_500_HQ.overflow: initially empty
2. Open database
3. Close database
4. Display record
5. Update record
6. Create report
7. Add record
8. Delete record
9. Quit
