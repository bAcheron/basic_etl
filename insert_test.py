import logging
import sys
import datetime
from DatabaseManager import NewDatabaseManager
import csv

current_date = datetime.datetime.today().strftime('%Y%m%d')
log_name='logs\\'+current_date +'_test_etl.log'


test_db = NewDatabaseManager('DatabaseName','Examples',log_name)

file_list = test_db.select_data("""
		SELECT 
			f.File_Location
			,f.File_type
			,f.File_Name
			,table_name
			,e.Extract_File_Location
		FROM [Examples].[dbo].[Meta_Raw_File_Extracts] e
		Join [dbo].[Meta_Raw_Files] f
		  on e.file_type = f.file_type
		  and e.file_provider = f.file_provider
		  where is_loaded = 0""")
for file in file_list:
	with open(file[0],'r') as f:
		reader = csv.reader(f)
		columns = next(reader)
		query =  open(file[4],'r')
		query = query.read()
		for row in reader:
			test_db.insert_sql_data(query,row)
